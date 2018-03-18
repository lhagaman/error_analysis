from run_rat import run_rat
import matplotlib.pyplot as plt
import numpy as np

#run = True  # if False, uses previous simulation in output.root

# all distances are in inches here, and in millimeters in the plot
# sample offsets in inches

"""
theta_i = 45.
laser_offset = 1. / 25.4  # number of inches that the center of PMT/cell/sample are to the right of the laser beam
substance_list = ["air", "water", "mineral_oil", "my_xe"]

wavelength = 405.

num_photons = 50000

x_min = -15.
x_max = 15.

y_min = -1.
y_max = 1.

"""
"""
# calculating the sample offset from the angle
dist = 14.  # distance from center of sample to fulcrum in inches
angle = 1.  # angle of error in degrees
direction = -45.  # direction of angular change in degrees (0 is x-axis, 90 is y-axis)
sample_x = dist * np.pi / 180. * angle * np.cos(np.pi / 180. * direction)
sample_y = dist * np.pi / 180. * angle * np.sin(np.pi / 180. * direction)
"""

run = True

wavelength = 405.

num_photons = 5000

x_min = -2.
x_max = 2.

y_min = -1.
y_max = 1.

angular_size = 30

theta_i = 45.

sample_x = 0.
sample_y = 0.
cell_x = 0.
cell_y = 0.
laser_offset = 0.

laser_offsets = [i / 25.4 for i in range(3)]

for offset in laser_offsets:

	run_rat(name="laser shifted by " + str(offset * 25.4) + " mm", num_photons=num_photons, wavelength=wavelength, theta_i=theta_i, substance="water",
	        tube_included=True, angular_size=angular_size, laser_offset=offset, sample_x=sample_x, sample_y=sample_y,
	        cell_x=cell_x, cell_y=cell_y, show=False, run=run, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

plt.show()
