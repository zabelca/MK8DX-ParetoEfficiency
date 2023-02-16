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

# Image Files (pre-loaded)
mushroom_mkc_path = r"images/179px-MK8_Mario_Kart_Stadium_Course_Icon.png"
mushroom_wp_path = r"images/179px-MK8_Water_Park_Course_Icon.png"
mushroom_ssc_path = r"images/179px-MK8_Sweet_Sweet_Canyon_Course_Icon.png"
mushroom_tr_path = r"images/179px-MK8_Thwomp_Ruins_Course_Icon.png"
flower_mc_path = r"images/179px-MK8_Mario_Circuit_Course_Icon.png"
flower_th_path = r"images/179px-MK8_Toad_Harbor_Course_Icon.png"
flower_tm_path = r"images/179px-MK8_Twisted_Mansion_Course_Icon.png"
flower_sgf_path = r"images/179px-MK8_Shy_Guy_Falls_Course_Icon.png"
star_sa_path = r"images/179px-MK8_Sunshine_Airport_Course_Icon.png"
star_ds_path = r"images/179px-MK8_Dolphin_Shoals_Course_Icon.png"
star_electro_path = r"images/179px-MK8_Electrodrome_Course_Icon.png"
star_mw_path = r"images/179px-MK8_Mount_Wario_Course_Icon.png"
speical_cc_path = r"images/179px-MK8_Cloudtop_Cruise_Course_Icon.png"
speical_bdd_path = r"images/179px-MK8_Bone-Dry_Dunes_Course_Icon.png"
speical_bc_path = r"images/179px-MK8_Bowser's_Castle_Course_Icon.png"
speical_rr_path = r"images/179px-MK8_Rainbow_Road_Course_Icon.png"
shell_mmm_path = r"images/179px-MK8_Wii_Moo_Moo_Meadows_Course_Icon.png"
shell_GBA_mc_path = r"images/179px-MK8_GBA_Mario_Circuit_Course_Icon.png"
shell_ccb_path = r"images/179px-MK8_DS_Cheep_Cheep_Beach_Course_Icon.png"
shell_tt_path = r"images/179px-MK8_N64_Toad's_Turnpike_Course_Icon.png"
banana_ddd_path = r"images/179px-MK8_GCN_Dry_Dry_Desert_Course_Icon.png"
banana_dp3_path = r"images/179px-MK8_SNES_Donut_Plains_3_Course_Icon.png"
banana_rr_path = r"images/179px-MK8_N64_Royal_Raceway_Course_Icon.png"
banana_dkj_path = r"images/179px-MK8_3DS_DK_Jungle_Course_Icon.png"
leaf_ws_path = r"images/179px-MK8_DS_Wario_Stadium_Course_Icon.png"
leaf_sl_path = r"images/179px-MK8_GCN_Sherbet_Land_Course_Icon.png"
leaf_mp_path = r"images/179px-MK8_3DS_Music_Park_Course_Icon.png"
leaf_yv_path = r"images/179px-MK8_N64_Yoshi_Valley_Course_Icon.png"
lightning_ttc_path = r"images/179px-MK8_DS_Tick-Tock_Clock_Course_Icon.png"
lightning_pps_path = r"images/179px-MK8_3DS_Piranha_Plant_Slide_Course_Icon.png"
lightning_gv_path = r"images/179px-MK8_Wii_Grumble_Volcano_Course_Icon.png"
lightning_n64_rr_path = r"images/179px-MK8_N64_Rainbow_Road_Course_Icon.png"
egg_yc_path = r"images/179px-MK8_GCN_Yoshi_Circuit_Course_Icon.png"
egg_ea_path = r"images/179px-MK8_Excitebike_Arena_Course_Icon.png"
egg_dd_path = r"images/179px-MK8_Dragon_Driftway_Course_Icon.png"
egg_mc_path = r"images/179px-MK8_Mute_City_Course_Icon.png"
triforce_wgm_path = r"images/179px-MK8_Wii_Wario's_Gold_Mine_Course_Icon.png"
triforce_snes_rr_path = r"images/179px-MK8_SNES_Rainbow_Road_Course_Icon.png"
triforce_iio_path = r"images/179px-MK8_Ice_Ice_Outpost_Course_Icon.png"
triforce_hc_path = r"images/179px-MK8_Hyrule_Circuit_Course_Icon.png"
crossing_bp_path = r"images/179px-MK8_GCN_Baby_Park_Course_Icon.png"
crossing_cl_path = r"images/179px-MK8_GBA_Cheese_Land_Course_Icon.png"
crossing_ww_path = r"images/179px-MK8_Wild_Woods_Course_Icon.png"
crossing_ac_path = r"images/179px-MK8_Animal_Crossing_Course_Icon.png"
bell_neb_path = r"images/179px-MK8_3DS_Neo_Bowser_City_Course_Icon.png"
bell_gba_rr_path = r"images/179px-MK8_GBA_Ribbon_Road_Course_Icon.png"
bell_sbs_path = r"images/179px-MK8_Super_Bell_Subway_Course_Icon.png"
bell_bb_path = r"images/179px-MK8_Big_Blue_Course_Icon.png"

#Track Maps
mushroom_mkc_map = r"images/120px-MK8_Mario_Kart_Stadium_Map.png"
mushroom_wp_map = r"images/120px-MK8_Water_Park_Map.png"
mushroom_ssc_map = r"images/120px-MK8_Sweet_Sweet_Canyon_Map.png"
mushroom_tr_map = r"images/120px-MK8_Thwomp_Ruins_Map.png"
flower_mc_map = r"images/120px-MK8_"
flower_th_map = r"images/120px-MK8_"
flower_tm_map = r"images/120px-MK8_"
flower_sgf_map = r"images/120px-MK8_"
star_sa_map = r"images/120px-MK8_"
star_ds_map = r"images/120px-MK8_"
star_electro_map = r"images/120px-MK8_"
star_mw_map = r"images/120px-MK8_"
speical_cc_map = r"images/120px-MK8_"
speical_bdd_map = r"images/120px-MK8_"
speical_bc_map = r"images/120px-MK8_"
speical_rr_map = r"images/120px-MK8_"
shell_mmm_map = r"images/120px-MK8_"
shell_GBA_mc_map = r"images/120px-MK8_"
shell_ccb_map = r"images/120px-MK8_"
shell_tt_map = r"images/120px-MK8_"
banana_ddd_map = r"images/120px-MK8_"
banana_dp3_map = r"images/120px-MK8_"
banana_rr_map = r"images/120px-MK8_"
banana_dkj_map = r"images/120px-MK8_"
leaf_ws_map = r"images/120px-MK8_"
leaf_sl_map = r"images/120px-MK8_"
leaf_mp_map = r"images/120px-MK8_"
leaf_yv_map = r"images/120px-MK8_"
lightning_ttc_map = r"images/120px-MK8_"
lightning_pps_map = r"images/120px-MK8_"
lightning_gv_map = r"images/120px-MK8_"
lightning_n64_rr_map = r"images/120px-MK8_"
egg_yc_map = r"images/120px-MK8_"
egg_ea_map = r"images/120px-MK8_"
egg_dd_map = r"images/120px-MK8_"
egg_mc_map = r"images/120px-MK8_"
triforce_wgm_map = r"images/120px-MK8_"
triforce_snes_rr_map = r"images/120px-MK8_"
triforce_iio_map = r"images/120px-MK8_"
triforce_hc_map = r"images/120px-MK8_"
crossing_bp_map = r"images/120px-MK8_"
crossing_cl_map = r"images/120px-MK8_"
crossing_ww_map = r"images/120px-MK8_"
crossing_ac_map = r"images/120px-MK8_"
bell_neb_map = r"images/120px-MK8_"
bell_gba_rr_map = r"images/120px-MK8_"
bell_sbs_map = r"images/120px-MK8_"
bell_bb_map = r"images/120px-MK8_"

# Image Files Dict.
img_files = {
    'Mario Kart Stadium': mushroom_mkc_path,
    'Water Park': mushroom_wp_path,
    'Sweet Sweet Canyon': mushroom_ssc_path,
    'Thwomp Ruins': mushroom_tr_path,
    'Mario Circuit': flower_mc_path,
    'Toad Harbor': flower_th_path,
    'Twisted Mansion': flower_tm_path,
    'Shy Guy Falls': flower_sgf_path,
    'Sunshine Airport': star_sa_path,
    'Dolphin Shoals': star_ds_path,
    'Electrodrome': star_electro_path,
    'Mount Wario': star_mw_path,
    'Cloudtop Cruise': speical_cc_path,
    'Bone-Dry Dunes': speical_bdd_path,
    'Bowser\'s Castle': speical_bc_path,
    'Rainbow Road': speical_rr_path,
    'Wii Moo Moo Meadows': shell_mmm_path,
    'GBA Mario Circuit': shell_GBA_mc_path,
    'DS Cheep Cheep Beach': shell_ccb_path,
    'N64 Toad\'s Turnpike':shell_tt_path,
    'GCN Dry Dry Desert': banana_ddd_path,
    'SNES Donut Plains 3': banana_dp3_path,
    'N64 Royal Raceway': banana_rr_path,
    '3DS DK Jungle': banana_dkj_path,
    'DS Wario Stadium': leaf_ws_path,
    'GCN Sherbet Land': leaf_sl_path,
    '3DS Music Park': leaf_mp_path,
    'N64 Yoshi Valley': leaf_yv_path,
    'DS Tick-Tock Clock': lightning_ttc_path,
    '3DS Piranha Plant Slide': lightning_pps_path,
    'Wii Grumble Volcano': lightning_gv_path,
    'N64 Rainbow Road': lightning_n64_rr_path,
    'GCN Yoshi Circuit': egg_yc_path,
    'Excitebike Arena': egg_ea_path,
    'Dragon Driftway': egg_dd_path,
    'Mute City': egg_mc_path,
    'Wii Wario\'s Gold Mine': triforce_wgm_path,
    'SNES Rainbow Road': triforce_snes_rr_path,
    'Ice Ice Outpost': triforce_iio_path,
    'Hyrule Circuit': triforce_hc_path,
    'GCN Baby Park': crossing_bp_path,
    'GBA Cheese Land': crossing_cl_path,
    'Wild Woods': crossing_ww_path,
    'Animal Crossing': crossing_ac_path,
    '3DS Neo Bowser City': bell_neb_path,
    'GBA Ribbon Road': bell_gba_rr_path,
    'Super Bell Subway': bell_sbs_path,
    'Big Blue': bell_bb_path
}

# Track Map image files
track_maps = {
    'Mario Kart Stadium': mushroom_mkc_map,
    'Water Park': mushroom_wp_map,
    'Sweet Sweet Canyon': mushroom_ssc_map,
    'Thwomp Ruins': mushroom_tr_map,
    'Mario Circuit': flower_mc_map,
    'Toad Harbor': flower_th_map,
    'Twisted Mansion': flower_tm_map,
    'Shy Guy Falls': flower_sgf_map,
    'Sunshine Airport': star_sa_map,
    'Dolphin Shoals': star_ds_map,
    'Electrodrome': star_electro_map,
    'Mount Wario': star_mw_map,
    'Cloudtop Cruise': speical_cc_map,
    'Bone-Dry Dunes': speical_bdd_map,
    'Bowser\'s Castle': speical_bc_map,
    'Rainbow Road': speical_rr_map,
    'Wii Moo Moo Meadows': shell_mmm_map,
    'GBA Mario Circuit': shell_GBA_mc_map,
    'DS Cheep Cheep Beach': shell_ccb_map,
    'N64 Toad\'s Turnpike':shell_tt_map,
    'GCN Dry Dry Desert': banana_ddd_map,
    'SNES Donut Plains 3': banana_dp3_map,
    'N64 Royal Raceway': banana_rr_map,
    '3DS DK Jungle': banana_dkj_map,
    'DS Wario Stadium': leaf_ws_map,
    'GCN Sherbet Land': leaf_sl_map,
    '3DS Music Park': leaf_mp_map,
    'N64 Yoshi Valley': leaf_yv_map,
    'DS Tick-Tock Clock': lightning_ttc_map,
    '3DS Piranha Plant Slide': lightning_pps_map,
    'Wii Grumble Volcano': lightning_gv_map,
    'N64 Rainbow Road': lightning_n64_rr_map,
    'GCN Yoshi Circuit': egg_yc_map,
    'Excitebike Arena': egg_ea_map,
    'Dragon Driftway': egg_dd_map,
    'Mute City': egg_mc_map,
    'Wii Wario\'s Gold Mine': triforce_wgm_map,
    'SNES Rainbow Road': triforce_snes_rr_map,
    'Ice Ice Outpost': triforce_iio_map,
    'Hyrule Circuit': triforce_hc_map,
    'GCN Baby Park': crossing_bp_map,
    'GBA Cheese Land': crossing_cl_map,
    'Wild Woods': crossing_ww_map,
    'Animal Crossing': crossing_ac_map,
    '3DS Neo Bowser City': bell_neb_map,
    'GBA Ribbon Road': bell_gba_rr_map,
    'Super Bell Subway': bell_sbs_map,
    'Big Blue': bell_bb_map
}

# originally from https://github.com/woodnathan/MarioKart8-Stats, added DLC and fixed a few typos
bodies = pd.read_csv('bodies.csv')
chars = pd.read_csv('characters.csv')
gliders = pd.read_csv('gliders.csv')
tires = pd.read_csv('tires.csv')
tracks = pd.read_csv('MK8DX-World-Record-Data.csv')
"""
# use only stock (non-DLC) characters / karts / tires
chars = chars.loc[chars['DLC']==0]
bodies = bodies.loc[bodies['DLC']==0]
tires = tires.loc[tires['DLC']==0]
gliders = gliders.loc[gliders['DLC']==0]
"""
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
# for Non-DLC Stats:
#char_class_dict = dict(zip([3, 0, 5, 4, 2, 6, 1], [0, 1, 2, 3, 4, 5, 6]))
# for DLC Stats:
char_class_dict = dict(zip([0, 3, 2, 7, 8, 4, 1, 6, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8]))
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

images = []
def display_tracks(key):
    button_array = []
    #track_list = tracks[tracks.Cup == key]
    track_list = tracks.loc[tracks['Cup'] == key]
    track_list = track_list["Track"]
    for x in track_list:
        track_img = ImageTk.PhotoImage(file=img_files[x])
        images.append(track_img)
        my_button = tk.Button(root, image=track_img, borderwidth=0, command=lambda x=x: track_details(x))
        button_array.append(my_button)

    for i, button in enumerate(button_array):
        button.grid(row=3, column=i)

def track_details(key):
    # Track detail window
    detail = tk.Tk()
    detail.title("Track Details")
    detail.geometry("1280x720")

    # locate the details for the track
    #track_list = tracks.loc[tracks['Track'] == key]

    # display track map
    #print(track_maps[key])
    img = ImageTk.PhotoImage(file=track_maps[key])
    label = tk.Label(detail, image=img, width=120, height=120, borderwidth=0)
    label.pack()
    #print(key)


# Main window
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
mushroom_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_MushroomCup.png"))
button7 = tk.Button(root, image=mushroom_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Mushroom"))
button7.grid(row=1, column=0, ipady=10, pady=10, padx=5)

flower_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_FlowerCup.png"))
button8 = tk.Button(root, image=flower_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Flower"))
button8.grid(row=1, column=1, ipady=10, pady=10, padx=5)

star_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Star_Cup_Emblem.png"))
button9 = tk.Button(root, image=star_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Star"))
button9.grid(row=1, column=2, ipady=10, pady=10, padx=5)

special_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Special_Cup_Emblem.png"))
button10 = tk.Button(root, image=special_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Speical"))
button10.grid(row=1, column=3, ipady=10, pady=10, padx=5)

egg_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Egg_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button11 = tk.Button(root, image=egg_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Egg"))
button11.grid(row=1, column=4, ipady=10, pady=10, padx=5)

crossing_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Crossing_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button12 = tk.Button(root, image=crossing_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Crossing"))
button12.grid(row=1, column=5, ipady=10, pady=10, padx=5)

shell_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Shell_Cup_Emblem.png"))
button13 = tk.Button(root, image=shell_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Shell"))
button13.grid(row=2, column=0, ipady=10, pady=10, padx=5)

banana_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Banana_Cup_Emblem.png"))
button14 = tk.Button(root, image=banana_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Banana"))
button14.grid(row=2, column=1, ipady=10, pady=10, padx=5)

leaf_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Leaf_Cup_Emblem.png"))
button15 = tk.Button(root, image=leaf_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Leaf"))
button15.grid(row=2, column=2, ipady=10, pady=10, padx=5)

lightning_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Lightning_Cup_Emblem.png"))
button16 = tk.Button(root, image=lightning_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Lightning"))
button16.grid(row=2, column=3, ipady=10, pady=10, padx=5)

triforce_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Triforce_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button17 = tk.Button(root, image=triforce_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Triforce"))
button17.grid(row=2, column=4, ipady=10, pady=10, padx=5)

bell_cup_icon = ImageTk.PhotoImage(Image.open(r"images/MK8_Bell_Cup_Emblem.png").resize((128,128), Image.Resampling.BICUBIC))
button18 = tk.Button(root, image=bell_cup_icon, width=128, height=128, borderwidth=0, command=lambda: display_tracks("Bell"))
button18.grid(row=2, column=5, ipady=10, pady=10, padx=5)

root.mainloop()
