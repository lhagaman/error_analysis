from myPhotonTracking import plot_output

# plots output degrees from specular angle with no misalignments
# axes are positioned such that if you look at the front of the PMT from the direction of incoming photons,
# right is right and up is up

plot_output(45, 0., show_position=True, x_min=-1., x_max=1.)


