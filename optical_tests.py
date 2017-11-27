from run_rat import run_rat
import matplotlib.pyplot as plt

run = True  # if False, uses previous simulation in output.root

theta_i = 45.
laser_offset = 1. / 25.4  # number of inches that the center of PMT/cell/sample are to the right of the laser beam
substance_list = ["air", "water", "mineral_oil"]

x_min = -3.
x_max = 3.

y_min = -1.
y_max = 1.

angular_size = 20.

"""
for i in range(len(substance_list)):
    run_rat(theta_i=theta_i, substance=substance_list[i], tube_included=True, angular_size=angular_size,
            laser_offset=laser_offset, show=False, run=run, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
"""

run_rat(theta_i=theta_i, substance="my_xe", tube_included=True, angular_size=angular_size,
            laser_offset=laser_offset, show=False, run=run, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

plt.show()
