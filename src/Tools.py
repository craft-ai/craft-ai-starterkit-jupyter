import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
FONT = {'family': 'sans-serif', 'weight': 'normal', 'size': 16}

rmse_series = lambda s0, s1: np.sqrt(np.mean((np.array(s0)-np.array(s1))**2))

def plot_zone_results(z, index, reality, craft, craft_std, sklearn=pd.Series()):    
  FIGSIZE = (17, 5)
  fig, ax = plt.subplots(figsize=FIGSIZE)

  plt.plot(index, reality[z].values, label="Reality", )

  if not sklearn.empty:
    plt.plot(index, sklearn[z].values, linestyle='dotted',
             label='DT Sklearn - RMSE {:0.3}'\
             .format(rmse_series(reality[z], sklearn[z])))

  plt.plot(index, craft[z].values, linestyle='-.',
           color="#42348B",
           label='craft - RMSE {:0.3}'.format(rmse_series(reality[z], craft[z])))
  ax.fill_between(index,
                  (craft[z] + craft_std[z]).values,
                  (craft[z] - craft_std[z]).values,
                 color='#42348B', alpha=0.1,
                 label="Confidence")

  plt.title(f'Predictions for zone {z}', y=1.25, fontdict=FONT, size=20)
  ax.set_frame_on(False)
  plt.grid(True)
  plt.legend(prop={'size': FONT['size']}, 
             bbox_to_anchor=(0., 1.02, 1., .102), 
             loc='lower left', ncol=2, 
             mode="expand", borderaxespad=0.)
  plt.show()


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