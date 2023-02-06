#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import seaborn as sns
import itertools as it
import tkinter as tk
import webbrowser as wb
import customtkinter as ctk
from PIL import ImageTk, Image

from sklearn.cluster import KMeans

sns.set_context('talk')

import os

# Image Files
img_files = {
    'Mario Kart Stadium': r'mario_kart_stadium.png',
    'Water Park': 'water_park.png',
    'Sweet Sweet Canyon': 'sweet_sweet_canyon.png',
    'Thwomp Ruins': 'thwomp_ruins.png'
}
"""
    'Mario Circuit':
    'Toad Harbor':
    'Twisted Mansion':
    'Shy Guy Falls':
    'Sunshine Airport':
    'Dolphin Shoals':
    'Electrodrome':
    'Mount Wario':
    'Cloudtop Cruise':
    'Bone-Dry Dunes':
    'Bowser\'s Castle':
    'Rainbow Road':
    'Wii Moo Moo Meadows':
    'GBA Mario Circuit':
    'DS Cheep Cheep Beach':
    'N64 Toad\'s Turnpike':
    'GCN Dry Dry Desert':
    'SNES Donut Plains 3':
    'N64 Royal Raceway':
    '3DS DK Jungle':
    'DS Wario Stadium':
    'GCN Sherbet Land':
    '3DS Music Park':
    'N64 Yoshi Valley':
    'DS Tick-Tock Clock':
    '3DS Piranha Plant Slide':
    'Wii Grumble Volcano':
    'N64 Rainbow Road':
    'GCN Yoshi Circuit':
    'Excitebike Arena':
    'Dragon Driftway':
    'Mute City':
    'Wii Wario\'s Gold Mine':
    'SNES Rainbow Road':
    'Ice Ice Outpost':
    'Hyrule Circuit':
    'GCN Baby Park':
    'GBA Cheese Land':
    'Wild Woods':
    'Animal Crossing':
    '3DS Neo Bowser City':
    'GBA Ribbon Road':
    'Super Bell Subway':
    'Big Blue':
}
"""

# originally from https://github.com/woodnathan/MarioKart8-Stats, added DLC and fixed a few typos
bodies = pd.read_csv('bodies.csv')
chars = pd.read_csv('characters.csv')
gliders = pd.read_csv('gliders.csv')
tires = pd.read_csv('tires.csv')
tracks = pd.read_csv('MK8DX-World-Record-Data.csv')

# use only stock (non-DLC) characters / karts / tires
chars = chars.loc[chars['DLC']==0]
bodies = bodies.loc[bodies['DLC']==0]
tires = tires.loc[tires['DLC']==0]
gliders = gliders.loc[gliders['DLC']==0]

stat_cols = bodies.columns[2:-1]
main_cols = ['Weight','Speed','Acceleration','Handling','Traction']
track_cols = ['Track', 'Character', 'Vehicle', 'Tires', 'Glider', 'Tilt']

# lots of characters/karts/tires are exactly the same. here we just want one from each stat type
chars_unique = chars.drop_duplicates(subset=stat_cols).set_index('Character')[stat_cols].sort_values('Weight')
bodies_unique = bodies.drop_duplicates(subset=stat_cols).set_index('Body')[stat_cols].sort_values('Acceleration')
tires_unique = tires.drop_duplicates(subset=stat_cols).set_index('Tire')[stat_cols].sort_values('Speed')

n_uniq_chars = len(chars_unique)
n_uniq_bodies = len(bodies_unique)
n_uniq_tires = len(tires_unique)

# add a column indicating which category each character/kart/tire is in
chars['char_class'] = KMeans(n_uniq_chars, n_init=10, random_state=0).fit_predict(chars[stat_cols])
bodies['body_class'] = KMeans(n_uniq_bodies, n_init=10).fit_predict(bodies[stat_cols])
tires['tire_class'] = KMeans(n_uniq_tires, n_init=10).fit_predict(tires[stat_cols])

# change the character class labels so that they correspond to weight order
char_class_dict = dict(zip([3, 0, 5, 4, 2, 6, 1], [0, 1, 2, 3, 4, 5, 6]))
chars['char_class'] = chars['char_class'].apply(lambda c: char_class_dict[c])

# only two types of gliders, one of which is pretty clearly just better
glider_best = gliders.loc[gliders['Glider']=='Flower']

# plot a heatmap of the stats for each component class
def hmap_char_class():
    fig, ax = plt.subplots(1,1, figsize=(8,5))

    sns.heatmap(chars_unique[main_cols], annot=True, ax=ax, linewidth=1, fmt='.3g')
    
    fig.tight_layout()

    plt.show()

# plot a heatmap of the stats for each component class
def hmap_part_class():
    fig, axes = plt.subplots(2,1, figsize=(8,10))

    tables = [bodies_unique, tires_unique]

    for ax, table in zip(axes, tables):
        sns.heatmap(table[main_cols], annot=True, ax=ax, linewidth=1, fmt='.3g')
            
    fig.tight_layout()

    plt.show()

def check(char_name, body_type, tire_type):
    # find the stats for each element of the configuration
    character = chars.loc[chars['Character']==char_name]
    kart = bodies.loc[bodies['Body']==body_type]
    wheels = tires.loc[tires['Tire']==tire_type]

    # the total stats for the configuration are just the sum of the components
    stats = pd.concat([character[stat_cols], kart[stat_cols], wheels[stat_cols], glider_best[stat_cols]]).sum()
                                
    # index the row by the configuration (character, kart, tire)
    index = pd.MultiIndex.from_tuples([(char_name, body_type, tire_type)], names=['Character', 'Body', 'Tire'])
                                            
    df = pd.DataFrame(stats).transpose()
    df.index = index
    return df

# returns True if the row is at the pareto frontier for variables xlabel and ylabel
def is_pareto_front(row, xlabel, ylabel):
        
    x = row[xlabel]
    y = row[ylabel]
                
    # look for points with the same y value but larger x value
    is_max_x = config_base.loc[config_base[ylabel]==y].max()[xlabel] <= x
    # look for points with the same x value but larger y value
    is_max_y = config_base.loc[config_base[xlabel]==x].max()[ylabel] <= y
    # look for points that are larger in both x and y
    is_double = len(config_base.loc[(config_base[xlabel]>x) & (config_base[ylabel]>y)])==0
                                            
    return is_max_x and is_max_y and is_double

# generate list of tuples for every possible configuration
config_all = it.product(chars_unique.index, bodies_unique.index, tires_unique.index)

# generate a dataframe with stats for each unique configuration
frames = []
#config_base = pd.DataFrame()
for (c,b,t) in config_all:
    this_config = check(c,b,t)
    frames.append(this_config)
    #config_base = config_base.append(this_config)
config_base = pd.concat(frames)

# array of True/False indicating whether the corresponding row is on the pareto frontier
is_pareto = config_base.apply(lambda row: is_pareto_front(row, 'Speed', 'Acceleration'), axis=1)

# just the configurations that are on the pareto frontier
config_pareto = config_base.loc[is_pareto].sort_values('Speed')

def pareto_frontier():
    # plot all the configurations
    fig, ax = plt.subplots(1,1, figsize=(8,5))
    sns.regplot(x='Speed', y='Acceleration', data=config_base, fit_reg=False, ax=ax)
            
    # plot the pareto frontier
    plt.plot(config_pareto['Speed'], config_pareto['Acceleration'], '--', label='Pareto frontier', alpha=0.5)

    plt.xlim([0.75,6]);
    plt.legend(loc='best');

    plt.show()

def interactive_graph():
    wb.open_new_tab('bokeh_plot.html')

def combos():
    # number of possible combinations
    print('Possible combinations    : ',len(list(it.product(chars.index, bodies.index, tires.index, gliders.index))))

    # number of combinations with different statistics
    print('Unique stat combinations : ',len(config_base.drop_duplicates(subset=stat_cols)))

    # number of optimal combinations (considering only speed and acceleration)
    print('Optimal combinations     : ',len(config_pareto))

    print(config_base.loc[is_pareto][['Speed','Acceleration']].sort_values('Speed'))

    fig, ax = plt.subplots(1,1, figsize=(8,7))
    sns.heatmap(config_pareto[main_cols].sort_values('Speed'), annot=True, ax=ax, linewidth=1, fmt='.3g');

def categories():
    # print out the various components, grouped by category
    tables = [chars, bodies, tires]
    keys = ['char_class', 'body_class', 'tire_class']
    columns = ['Character', 'Body', 'Tire']

    for table, key, col in zip(tables, keys, columns):
        print(col + ' Classes')
        print('*****************')
        for class_ in table[key].unique():
            class_list = table.loc[table[key]==class_][col].values
            print(', '.join(class_list))
                                            
        print()


def hide_buttons():
    button7.grid_forget()
    button8.grid_forget()
    button9.grid_forget()
    button10.grid_forget()
    button11.grid_forget()
    button12.grid_forget()
    button13.grid_forget()
    button14.grid_forget()
    button15.grid_forget()
    button16.grid_forget()
    button17.grid_forget()
    button18.grid_forget()

def show_buttons():
    button7.grid(row=1, column=0, ipady=10, pady=10, padx=5)
    button8.grid(row=1, column=1, ipady=10, pady=10, padx=5)
    button9.grid(row=1, column=2, ipady=10, pady=10, padx=5)
    button10.grid(row=1, column=3, ipady=10, pady=10, padx=5)
    button11.grid(row=1, column=4, ipady=10, pady=10, padx=5)
    button12.grid(row=1, column=5, ipady=10, pady=10, padx=5)
    button13.grid(row=2, column=0, ipady=10, pady=10, padx=5)
    button14.grid(row=2, column=1, ipady=10, pady=10, padx=5)
    button15.grid(row=2, column=2, ipady=10, pady=10, padx=5)
    button16.grid(row=2, column=3, ipady=10, pady=10, padx=5)
    button17.grid(row=2, column=4, ipady=10, pady=10, padx=5)
    button18.grid(row=2, column=5, ipady=10, pady=10, padx=5)

import time
def display_tracks(key):
    button_array = []
    track_list = tracks[tracks.Cup == key]
    track_list = track_list["Track"]
    for x in track_list:
        my_img = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/Tracks/" + img_files[x]))
        my_button = tk.Button(root, image=my_img)
        button_array.append(my_button)

    for i, button in enumerate(button_array):
        button.grid(row=3, column=i)


root = tk.Tk()
root.title("Pareto Efficiency Stats")
root.geometry("1366x768")
root.protocol("WM_DELETE_WINDOW", root.quit)

button1 = ctk.CTkButton(master=root, text="Character Classes (by weight)", width=190, height=40, command=hmap_char_class)
button1.grid(row=0, column=0, ipady=10, pady=10, padx=5)

button2 = ctk.CTkButton(master=root, text="Body/Tire Stats", width=190, height=40, command=hmap_part_class)
button2.grid(row=0, column=1, ipady=10, pady=10, padx=5)

button3 = ctk.CTkButton(master=root, text="Pareto Frontier", width=190, height=40, command=pareto_frontier)
button3.grid(row=0, column=2, ipady=10, pady=10, padx=5)

button4 = ctk.CTkButton(master=root, text="Interactive Graph", width=190, height=40, command=interactive_graph)
button4.grid(row=0, column=3, ipady=10, pady=10, padx=5)

button5 = ctk.CTkButton(master=root, text="Combos", width=190, height=40, command=combos)
button5.grid(row=0, column=4, ipady=10, pady=10, padx=5)

button6 = ctk.CTkButton(master=root, text="All Classes", width=190, height=40, command=categories)
#button6.pack(pady=5)
button6.grid(row=0, column=5, ipady=10, pady=10, padx=5)

# All cup buttons
mushroom_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_MushroomCup.png"))
button7 = tk.Button(root, image=mushroom_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Mushroom"))
button7.grid(row=1, column=0, ipady=10, pady=10, padx=5)

flower_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_FlowerCup.png"))
button8 = tk.Button(root, image=flower_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Flower"))
button8.grid(row=1, column=1, ipady=10, pady=10, padx=5)

star_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Star_Cup.png"))
button9 = tk.Button(root, image=star_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button9.grid(row=1, column=2, ipady=10, pady=10, padx=5)

special_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Special_Cup.png"))
button10 = tk.Button(root, image=special_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button10.grid(row=1, column=3, ipady=10, pady=10, padx=5)

egg_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Egg_Cup.png").resize((128,128), Image.Resampling.BICUBIC))
button11 = tk.Button(root, image=egg_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button11.grid(row=1, column=4, ipady=10, pady=10, padx=5)

crossing_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Crossing_Cup.png").resize((128,128), Image.Resampling.BICUBIC))
button12 = tk.Button(root, image=crossing_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button12.grid(row=1, column=5, ipady=10, pady=10, padx=5)

shell_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Shell_Cup.png"))
button13 = tk.Button(root, image=shell_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button13.grid(row=2, column=0, ipady=10, pady=10, padx=5)

banana_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Banana_Cup.png"))
button14 = tk.Button(root, image=banana_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button14.grid(row=2, column=1, ipady=10, pady=10, padx=5)

leaf_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Leaf_Cup.png"))
button15 = tk.Button(root, image=leaf_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button15.grid(row=2, column=2, ipady=10, pady=10, padx=5)

lightning_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Lightning_Cup.png"))
button16 = tk.Button(root, image=lightning_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button16.grid(row=2, column=3, ipady=10, pady=10, padx=5)

triforce_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Triforce_Cup.png").resize((128,128), Image.Resampling.BICUBIC))
button17 = tk.Button(root, image=triforce_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button17.grid(row=2, column=4, ipady=10, pady=10, padx=5)

bell_cup_icon = ImageTk.PhotoImage(Image.open(r"/home/zabel/automation/ParetoEfficiency-MarioKart8/code/images/MK8_Bell_Cup.png").resize((128,128), Image.Resampling.BICUBIC))
button18 = tk.Button(root, image=bell_cup_icon, width=128, height=128, borderwidth=0, command=hmap_char_class)
button18.grid(row=2, column=5, ipady=10, pady=10, padx=5)

root.mainloop()
