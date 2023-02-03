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

from sklearn.cluster import KMeans

sns.set_context('talk')


# originally from https://github.com/woodnathan/MarioKart8-Stats, added DLC and fixed a few typos
bodies = pd.read_csv('bodies.csv')
chars = pd.read_csv('characters.csv')
gliders = pd.read_csv('gliders.csv')
tires = pd.read_csv('tires.csv')

# use only stock (non-DLC) characters / karts / tires
chars = chars.loc[chars['DLC']==0]
bodies = bodies.loc[bodies['DLC']==0]
tires = tires.loc[tires['DLC']==0]
gliders = gliders.loc[gliders['DLC']==0]

stat_cols = bodies.columns[2:-1]
main_cols = ['Weight','Speed','Acceleration','Handling','Traction']

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


root = tk.Tk()
root.title("Pareto Efficiency Stats")
root.geometry("200x250")
root.protocol("WM_DELETE_WINDOW", root.quit)

button1 = tk.Button(root, text="Charater Classes (by weight)", command=hmap_char_class)
button1.pack()

button2 = tk.Button(root, text="Body/Tire Stats", command=hmap_part_class)
button2.pack()

button3 = tk.Button(root, text="Pareto Frontier", command=pareto_frontier)
button3.pack()

button4 = tk.Button(root, text="Interactive Graph", command=interactive_graph)
button4.pack()

button5 = tk.Button(root, text="Combos", command=combos)
button5.pack()

button6 = tk.Button(root, text="All Classes", command=categories)
button6.pack()

root.mainloop()
