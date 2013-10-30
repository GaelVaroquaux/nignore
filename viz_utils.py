import numpy as np

from nipy.labs.viz import plot_map
from nipy.labs.viz_tools import cm


def plot_estimator(niimg, title, report_params=None):
    vmax = np.abs(niimg.get_data()).max()

    if report_params is None:
        report_params = {}

    params = {
        'slicer': 'z',
        'cut_coords': 7,
        'cmap': cm.cold_hot}

    for k in report_params:
        if k.startswith('plot_map'):
            params[k.split('plot_map__')[1]] = report_params[k]

    plot_map(niimg.get_data(),
             affine=niimg.get_affine(),
             vmin=-vmax,
             vmax=vmax,
             title=title,
             **params)