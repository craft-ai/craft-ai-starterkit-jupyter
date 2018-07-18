import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)


FONT = {'family': 'sans-serif', 'weight': 'normal', 'size': 16}

rmse_series = lambda s0, s1: np.sqrt(np.mean((np.array(s0)-np.array(s1))**2))

def plot_zone_results(zone, reality, craftai, craftai_std, sklearn, utc_test_index):    
    real = go.Scatter(
            x = utc_test_index,      
            y = reality[zone].values,
            name = 'Reality',
            line=dict(color='hsla(0,0,0%)')
        )

    craft = go.Scatter(
            x = utc_test_index,      
            y = craftai[zone].values,
            name = 'Prediction Craft - RMSE {}'.format(
                int(rmse_series(reality[zone], craftai[zone])*10)/10),
            line=dict(color='#85144B')
        )
    
    craft_std = go.Scatter(
            x = utc_test_index,      
            y = craftai[zone].values,
            name = 'Prediction Craft - STD',
            mode='markers',
            error_y=dict(
                type='data',
                array=craftai_std[zone],
                visible=True,
                color='#85144B'
            ),
            marker=dict(color='#85144B')
        )
    
    dt_sklearn = go.Scatter(
            x = utc_test_index,      
            y = sklearn[zone].values,
            name = 'Prediction Sklearn - RMSE {}'.format(
                int(rmse_series(reality[zone], sklearn[zone])*10)/10)
        )

    layout = {'title': 'Zone {:0>3}'.format(zone),
                      'xaxis': {'title':'Time'},
                      'yaxis': {'title':'#Clients'},
                      'font': dict(size=16)}

    iplot({'data': [real, craft, craft_std, dt_sklearn],
           'layout': layout})


def plot_matshow(matrix, text, categories=None ):
    """
    Plots a graphical representation of a given matrix
    """
    
    FIGSIZE = (10, 10)
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.set_frame_on(False)
    
    if categories :
        cax = ax.matshow(matrix, cmap=plt.cm.get_cmap('viridis', len(categories)))        

        # We must be sure to specify the ticks matching our target names
        step = (max(categories))/len(categories)
        locs = [step*(i + 1/2) for i in range(len(categories))]
        
        cbar = fig.colorbar(cax, ticks=locs, fraction=0.046, pad=0.04)
        cbar.ax.set_yticklabels(['Zone {:0>3}'.format(c) for c in categories])

    else:
        cax = ax.matshow(matrix)

        cbar = fig.colorbar(cax, fraction=0.046, pad=0.04)
        cbar.ax.set_ylabel(text['cbar_label'], rotation=90, fontdict=FONT)

    plt.tick_params(
    axis='x',       
    which='both',   
    bottom=True,      
    top=False,  
    labeltop=False,
    labelbottom=True)
    
    x_tick_labels = text['x_tick_labels']
    y_tick_labels = text['y_tick_labels']
    
    plt.xticks(range(len(x_tick_labels)), x_tick_labels)
    plt.yticks(range(len(y_tick_labels)), y_tick_labels)
    
    plt.title(text['title'], fontdict=FONT, y=1.03)
    plt.xlabel(text['xlabel'], fontdict=FONT)
    plt.ylabel(text['ylabel'], fontdict=FONT)
    
    plt.show()
    
    
def plot_mat_error(reality, df, selected_zones, title='', nb_hours_to_display=24):

    sq_er = (reality.subtract(df))**2
    plot_text = {
        'x_tick_labels': selected_zones,
        'y_tick_labels': sq_er.index[:nb_hours_to_display],
        'title': title,
        'xlabel': 'Zone',
        'ylabel': 'Time',
        'cbar_label': 'Square Error'
    }

    plot_matshow(sq_er[:nb_hours_to_display], plot_text)