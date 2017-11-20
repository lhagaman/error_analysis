
import os
from geo_generator import make_geometry
from myPhotonTracking import plot_output

theta_i = 45.
laser_offset = 0.2  # number of inches that the center of PMT/cell/sample are to the right of the laser beam

angular_size = 20.

make_geometry(theta_i=theta_i, substance="air", tube_included=True, angular_size=angular_size, laser_offset=laser_offset)

os.system("cd ~/Desktop/RAT_files/error_analysis\n"
          + "cp error_analysis.geo ~/Desktop/RAT/rat-pac/data/error_analysis\n"
          + "rat photon_gun.mac")

plot_output(theta_i=theta_i, laser_offset=laser_offset)
