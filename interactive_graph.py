

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
