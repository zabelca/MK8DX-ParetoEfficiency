#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools as it

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
fig, ax = plt.subplots(1,1, figsize=(8,5))

sns.heatmap(chars_unique[main_cols], annot=True, ax=ax, linewidth=1, fmt='.3g')
    
fig.tight_layout()

# plot a heatmap of the stats for each component class
fig, axes = plt.subplots(2,1, figsize=(8,10))

tables = [bodies_unique, tires_unique]

for ax, table in zip(axes, tables):
        sns.heatmap(table[main_cols], annot=True, ax=ax, linewidth=1, fmt='.3g')
            
fig.tight_layout()

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

# array of True/False indicating whether the corresponding row is on the pareto frontier
is_pareto = config_base.apply(lambda row: is_pareto_front(row, 'Speed', 'Acceleration'), axis=1)

# just the configurations that are on the pareto frontier
config_pareto = config_base.loc[is_pareto].sort_values('Speed')

# plot all the configurations
fig, ax = plt.subplots(1,1, figsize=(8,5))
sns.regplot(x='Speed', y='Acceleration', data=config_base, fit_reg=False, ax=ax)
            
# plot the pareto frontier
plt.plot(config_pareto['Speed'], config_pareto['Acceleration'], '--', label='Pareto frontier', alpha=0.5)

plt.xlim([0.75,6]);
plt.legend(loc='best');

plt.show()

# number of possible combinations
print('Possible combinations    : ',len(list(it.product(chars.index, bodies.index, tires.index, gliders.index))))

# number of combinations with different statistics
print('Unique stat combinations : ',len(config_base.drop_duplicates(subset=stat_cols)))

# number of optimal combinations (considering only speed and acceleration)
print('Optimal combinations     : ',len(config_pareto))

print(config_base.loc[is_pareto][['Speed','Acceleration']].sort_values('Speed'))

fig, ax = plt.subplots(1,1, figsize=(8,7))
sns.heatmap(config_pareto[main_cols].sort_values('Speed'), annot=True, ax=ax, linewidth=1, fmt='.3g');

# note: needs modifications from https://github.com/josherick/bokeh/tree/2715_add_callbacks_to_groups to work
from bokeh.io import output_notebook, show
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool, CustomJS
from bokeh.models.widgets import CheckboxButtonGroup

from bokeh.models.widgets import Dropdown
from bokeh.io import output_file, show
from bokeh.layouts import column

output_notebook()
output_file('bokeh_plot.html')

def rgb_to_hex(rgb_tuple):
    tuple_255 = tuple([int(255*c) for c in rgb_tuple])
    hex_str = '#%02x%02x%02x' % tuple_255
    return hex_str

# make the color palette for plotting
palette = sns.color_palette("Set1", n_colors=n_uniq_chars)
pal_hex = [rgb_to_hex(color) for color in palette]

# collect all the data from each df (chars, bodies, tires)
bokeh_data = config_base.join(chars.set_index('Character')['char_class'])\
.join(bodies.set_index('Body')['body_class'])\
.join(tires.set_index('Tire')['tire_class'])

# store all the original data in this ColumnDataSource
source_all = ColumnDataSource(
    data = dict(
        x=config_base['Speed'],
        y=config_base['Acceleration'],
        character=config_base.index.get_level_values('Character'),
        kart=config_base.index.get_level_values('Body'),
        tire=config_base.index.get_level_values('Tire'),
        char_class=bokeh_data.char_class,
        color=[pal_hex[i] for i in bokeh_data['char_class']]
    )
)

# store just what is currently being shown in the plot in this CDS
source_plot = ColumnDataSource(
    data = dict(
        x=config_base['Speed'],
        y=config_base['Acceleration'],
        character=config_base.index.get_level_values('Character'),
        kart=config_base.index.get_level_values('Body'),
        tire=config_base.index.get_level_values('Tire'),
        char_class=bokeh_data.char_class,
        color=[pal_hex[i] for i in bokeh_data['char_class']]
    )
)

hover = HoverTool()
hover.tooltips = [
    ("Character", "@character"),
    ("Kart", "@kart"),
    ("Tires", "@tire")
]

# some javascript to update the plot based on which characters are selected
callback = CustomJS(args=dict(s_all=source_all, s_plot=source_plot), code="""
        var data = s_all.get('data');
        var show_class = cb_obj.get('active')
        x = data['x']
        y = data['y']
        char_class = data['char_class']

        var d2 = s_plot.get('data');
        d2['x'] = []
        d2['y'] = []
        d2['character'] = []
        d2['kart'] = []
        d2['tire'] = []
        d2['char_class'] = []
        d2['color'] = []

        var colors = '#e41a1c,#377eb7,#4dae4a,#994ea1,#ff8100,#fdfb32,#a7572b,#f481bd,#999999'.split(',');

        for (i = 0; i < x.length; i++) {
            if(show_class.indexOf(char_class[i]) != -1)
                {
                    d2['x'].push(data['x'][i])
                    d2['y'].push(data['y'][i])
                    d2['character'].push(data['character'][i])
                    d2['kart'].push(data['kart'][i])
                    d2['tire'].push(data['tire'][i])
                    d2['char_class'].push(data['char_class'][i])
                    d2['color'].push(colors[data['char_class'][i]])
                }
        }

        s_plot.trigger('change');

        for (i = 0; i < speed.length; i++) {
            if(blockedTile.indexOf("118") != -1)
                {
                    // element found
                }
            y[i] = Math.pow(x[i], f)
        }
        source.trigger('change');
    """)

# make checkboxes for each character class
#checkbox_group = CheckboxButtonGroup(
#    labels=list(config_base.index.get_level_values('Character').unique()), 
#    active=list(range(n_uniq_chars)),
#    js_event_callbacks={'change': callback})
#*********************************************************************

checkbox_group = CheckboxButtonGroup(
    labels=list(config_base.index.get_level_values('Character').unique()),
    active=list(range(n_uniq_chars)),
    js_event_callbacks={'change': [CustomJS(args=dict(s_all=source_all, s_plot=source_plot), code="""
        var new_data = source.data;
        new_data['weights'] = [];
        new_data['speeds'] = [];
        new_data['accelerations'] = [];
        new_data['handlings'] = [];
        new_data['tractions'] = [];

        var active = cb_obj.active;
        for (var i = 0; i < active.length; i++) {
            var char = active[i];
            new_data['weights'].push(chars_weights[char]);
            new_data['speeds'].push(chars_speeds[char]);
            new_data['accelerations'].push(chars_accelerations[char]);
            new_data['handlings'].push(chars_handlings[char]);
            new_data['tractions'].push(chars_tractions[char]);
        }
        source.change.emit();
    """)]})



TOOLS = [hover]

p = figure(width=600, height=600, y_range=(0.8,6), x_range=(0.8, 6), tools=TOOLS)

p.circle('x', 'y', size=8, source=source_plot, fill_color='color', line_color='#000000')

# janky way to do custom legend: plot 1 point for each color, then cover with white circle
for char, color in zip(chars_unique.index.values, pal_hex):
    p.circle(1.5, 1.5, size=8, line_color='#000000', fill_color=color)
p.circle(1.5, 1.5, size=10, fill_color='#FFFFFF', line_color='#FFFFFF')

p.xaxis.axis_label = 'Speed'
p.yaxis.axis_label = 'Acceleration'


show(column(checkbox_group,p)) # show the results


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
