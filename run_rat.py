
import os
from geo_generator import make_geometry
from myPhotonTracking import plot_output


def run_rat(name="", num_photons=50000, theta_i=45, substance="air", wavelength=405., sample_x=0., sample_y=0.,
            cell_x=0., cell_y=0.,  laser_distance=5., tube_included=True, angular_size=10., laser_offset=0.,
            show=False, run=False, x_min=-100., x_max=100., y_min=-100., y_max=100.,):

    if run:

        make_geometry(theta_i=theta_i, substance=substance, sample_x=sample_x, sample_y=sample_y,
                      cell_x=cell_x, cell_y=cell_y, laser_offset=laser_offset, tube_included=tube_included, angular_size=angular_size)

        mac_file_name = "./photon_gun.mac"

        mac_str  = "/glg4debug/glg4param omit_muon_processes  1.0\n"
        mac_str += "/glg4debug/glg4param omit_hadronic_processes  1.0\n"
        mac_str += "/rat/db/set DETECTOR geo_file \"error_analysis/error_analysis.geo\"\n"
        mac_str += "/run/initialize\n"
        mac_str += "/rat/proc count\n"
        mac_str += "/rat/procset update 1000\n"
        mac_str += "/rat/proclast outroot\n"
        mac_str += "/tracking/storeTrajectory 1\n"
        mac_str += "/generator/add combo gun2:point\n"

        # energy = h*c/wavelength, use planck's constant in MeV
        energy = str(4.135668e-21 * 2.998e8 / (wavelength * 1e-9))
        mac_str += "/generator/vtx/set opticalphoton  0  1  0 0.25 " + energy + " " + energy + "\n"

        dist_y = str(laser_distance * -25.4)
        dist_x = str(laser_offset * 25.4)
        mac_str += "/generator/pos/set " + dist_x + " " + dist_y + " 0\n"
        mac_str += "/run/beamOn " + str(num_photons) + "\n"

        mac_file = open(mac_file_name, 'w+')
        mac_file.write(mac_str)
        mac_file.close()

        str_1 = "cd ~/Desktop/error_analysis\n"
        str_1 += "cp error_analysis.geo ~/Desktop/install_rat/rat_stuff/rat-pac/data/error_analysis\n"
        os.system(str_1)

        str_2 = "cd ~/Desktop/error_analysis\n"
        str_2 += "rat photon_gun.mac"
        os.system(str_2)

    plot_output(name=name, wavelength=wavelength, theta_i=theta_i, laser_offset=laser_offset,
                sample_x=sample_x, sample_y=sample_y, cell_x=cell_x, cell_y=cell_y, show_position=False,
                x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, substance=substance, show=show)
