from geo_generator import make_geometry
import os

make_geometry(theta_i=45, substance="water", tube_included=True, angular_size=20., laser_offset=0.)

os.system("cd ~/Desktop/error_analysis\n" +
          "cp error_analysis.geo ~/Desktop/install_rat/rat_stuff/rat-pac/data/error_analysis\n" +
          "rat error_analysis.mac")
