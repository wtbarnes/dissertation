"""
Helper functions for formatting plots
"""
from matplotlib.ticker import NullFormatter, NullLocator


def remove_ticks_and_spines(ax):
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.xaxis.set_major_locator(NullLocator())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_locator(NullLocator())
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
