from run_rat import run_rat
import matplotlib.pyplot as plt
import numpy as np

run = True  # if False, uses previous simulation in output.root

# laser offset in inches
# sample offsets in inches

theta_i = 45.
laser_offset = 1. / 25.4  # number of inches that the center of PMT/cell/sample are to the right of the laser beam
substance_list = ["air", "water", "mineral_oil", "my_xe"]

x_min = -15.
x_max = 15.

y_min = -1.
y_max = 1.

angular_size = 20.


# calculating the sample offset from the angle
dist = 14.  # distance from center of sample to fulcrum in inches
angle = 1.  # angle of error in degrees
direction = -45.  # direction of angular change in degrees (0 is x-axis, 90 is y-axis)
sample_x = dist * np.pi / 180. * angle * np.cos(np.pi / 180. * direction)
sample_y = dist * np.pi / 180. * angle * np.sin(np.pi / 180. * direction)

"""
for i in range(len(substance_list)):
    run_rat(theta_i=theta_i, substance=substance_list[i], tube_included=True, angular_size=angular_size,
            laser_offset=0., show=False, run=run, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
"""

run_rat(theta_i=theta_i, substance="air", tube_included=True, angular_size=angular_size,
            laser_offset=0., sample_x=sample_x, sample_y=sample_y, show=False, run=run,
        x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

"""
run_rat(theta_i=theta_i, substance="water", tube_included=True, angular_size=angular_size,
            laser_offset=laser_offset, show=False, run=run, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

run_rat(theta_i=theta_i, substance="my_xe", tube_included=True, angular_size=angular_size,
            laser_offset=laser_offset, show=False, run=run, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
"""

plt.show()
