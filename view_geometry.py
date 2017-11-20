from geo_generator import make_geometry
import os

make_geometry(theta_i=45, substance="air", tube_included=True, angular_size=20., laser_offset=10)

os.system("cd ~/Desktop/RAT_files/error_analysis\n" +
          "cp error_analysis.geo ~/Desktop/RAT/rat-pac/data/error_analysis\n" +
          "rat error_analysis.mac")
