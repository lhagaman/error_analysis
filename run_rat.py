
import os
from geo_generator import make_geometry
from myPhotonTracking import plot_output

theta_i = 67.8

make_geometry(theta_i=theta_i, substance="air", tube_included=True, angular_size=20.)

os.system("cd ~/Desktop/RAT_files/error_analysis\n"
          + "cp error_analysis.geo ~/Desktop/RAT/rat-pac/data/error_analysis\n"
          + "rat photon_gun.mac")

plot_output(theta_i=theta_i)
