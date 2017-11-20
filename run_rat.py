
import os
import time
from geo_generator import make_geometry
from myPhotonTracking import plot_output

import subprocess


def run_rat(theta_i=45, substance="air", tube_included=True, angular_size=10., laser_offset=0., show=False, run=False, x_min=-100., x_max=100., y_min=-100., y_max=100.,):

    make_geometry(theta_i=theta_i, substance=substance, tube_included=tube_included, angular_size=angular_size, laser_offset=laser_offset)

    str = "cd ~/Desktop/RAT_files/error_analysis\n"
    str += "cp error_analysis.geo ~/Desktop/RAT/rat-pac/data/error_analysis\n"
    os.system(str)

    str_2 = "cd ~/Desktop/RAT_files/error_analysis\n"
    str_2 += "rat photon_gun.mac"
    os.system(str_2)

    plot_output(theta_i=theta_i, laser_offset=laser_offset, show_position=False, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, substance=substance, show=show)
