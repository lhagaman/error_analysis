import math
import geoShapes as GS
import numpy as np

geoFileName = './error_analysis.geo'


def make_geometry(theta_i, substance="air", tube_included=True, angular_size=20., sample_x=0., sample_y=0.,
                  cell_x=0., cell_y=0., laser_offset=0., angle_collecting_surfaces=True):

    sample_included = True
    tube_caps_included = False
    laser_included = True
    table_included = True
    post_included = False
    center_included = False
    fluid_included = True

    sample_surface_centered = True

    collecting_surface_distance = 5.5

    collecting_surfaces_included = False
    num_collecting_surfaces = 360
    collecting_surface_thickness = 0.01
    collecting_surface_height = 0.5

    two_dimensional_collecting_surfaces = False
    num_x = 36
    num_y = 36

    coherent_surface = True

    tube_radius = 1.
    tube_wall_width = 0.125
    tube_height = 1.8

    sample_radius = 0.5
    sample_thickness = 0.2

    tube_cap_radius = 2.25 / 2
    upper_tube_cap_height = 0.7
    lower_tube_cap_height = 0.9

    laser_radius = 1.4 / 2.
    laser_length = 5.
    dist_from_laser_to_sample = 8.

    dist_from_table_to_sample = 8.

    post_radius = 0.5 / 2.

    masterString = ''

    # Create the world first
    world = GS.boxVolume('world', 400, 400, 400)
    world.mother = ''
    world.invisible = 1
    world.material = "air"
    world.center = {'x':0.,'y':0.,'z':0.}
    masterString = world.writeToString(masterString)

    if tube_included:
        sapphire_tube = GS.tubeVolume("sapphire_tube", tube_radius, tube_height)
        sapphire_tube.colorVect = [0.658954714849, 0.802189023832, 0.994216568893, 0.2]
        sapphire_tube.center = {'x': cell_x, 'y': cell_y, 'z': 0.}
        sapphire_tube.material = 'sapphire'
        masterString = sapphire_tube.writeToString(masterString)

        outer_tube_surface = GS.border("outer_tube_surface", world.name, sapphire_tube.name)
        outer_tube_surface.surface = 'quartz'
        masterString = outer_tube_surface.writeToString(masterString)
        inner_tube_surface = GS.border("inner_tube_surface", sapphire_tube.name, world.name)
        inner_tube_surface.surface = 'quartz'
        masterString = inner_tube_surface.writeToString(masterString)

    if fluid_included:
        # added the 0.001 in order to make the surfaces interactions behave nicer
        fluid = GS.tubeVolume("fluid", tube_radius - tube_wall_width, tube_height)
        fluid.colorVect = [0.4, 0.4, 0.994216568893, 0.2]
        fluid.center = {'x': cell_x, 'y': cell_y, 'z': 0.}
        fluid.material = substance
        fluid.mother = sapphire_tube.name
        masterString = fluid.writeToString(masterString)

        outer_tube_fluid_surface = GS.border("outer_tube_fluid_surface", sapphire_tube.name, fluid.name)
        outer_tube_fluid_surface.surface = 'quartz'
        masterString = outer_tube_fluid_surface.writeToString(masterString)
        inner_tube_fluid_surface = GS.border("inner_tube_fluid_surface", fluid.name, sapphire_tube.name)
        inner_tube_fluid_surface.surface = 'quartz'
        masterString = inner_tube_fluid_surface.writeToString(masterString)

    if sample_included:
        sample = GS.tubeVolume('sample', sample_radius, sample_thickness)
        sample.mother = fluid.name
        sample.colorVect = [0.976892196027, 0.408361008099, 0.504698048762, 0.8]
        if not sample_surface_centered:
            sample.center = {'x': sample_x, 'y': sample_y, 'z': 0}
        else:
            sample.center = {'x': -sample_thickness / 2 * math.sin(theta_i * math.pi / 180) + sample_x - cell_x, 'y': sample_thickness / 2 * math.cos(theta_i * math.pi / 180) + sample_y - cell_y, 'z': 0}
        sample.rotation = [90, theta_i, 0]
        sample.material = 'mirror'
        masterString = sample.writeToString(masterString)

        outer_sample_surface = GS.border("outer_sample_surface", fluid.name, sample.name)
        outer_sample_surface.surface = "mirror"
        masterString = outer_sample_surface.writeToString(masterString)

        inner_sample_surface = GS.border("inner_sample_surface", sample.name, fluid.name)
        inner_sample_surface.surface = "mirror"
        masterString = inner_sample_surface.writeToString(masterString)

    if center_included:
        center = GS.tubeVolume('center', 0.02, 4)
        center.center = {'x': 0, 'y': 0, 'z': 0}
        center.material = 'air'
        center.colorVect = [1, 1, 1, 1]
        masterString = center.writeToString(masterString)

    if collecting_surfaces_included:
        for i in range(num_collecting_surfaces):
            surface_num = i - 180
            phi_start = 360.0 / num_collecting_surfaces * i + theta_i + 90
            phi_delta = 360.0 / num_collecting_surfaces
            current_collecting_surface = GS.tubeVolume('collecting_surface_' + str(surface_num),
                                                       collecting_surface_distance + collecting_surface_thickness,
                                                       collecting_surface_height, collecting_surface_distance, phi_start,
                                                       phi_delta)
            current_collecting_surface.material = 'air'
            current_collecting_surface.center = {'x': 0, 'y': 0, 'z': 0}

            if surface_num == 0:
                current_collecting_surface.colorVect = [1, 1, 1, 1]
            elif surface_num == 45:
                current_collecting_surface.colorVect = [1, 1, 1, 1]
            elif surface_num == -90:
                current_collecting_surface.colorVect = [1, 0, 0, 1]
            elif surface_num == 90:
                current_collecting_surface.colorVect = [0, 0, 1, 1]
            else:
                current_collecting_surface.colorVect = [0.2, 0.5, 0.2, 1]

            masterString = current_collecting_surface.writeToString(masterString)

    if two_dimensional_collecting_surfaces:
        for i in range(-num_x / 2, num_x / 2 + 1):
            for j in range(-num_y / 2, num_y / 2 + 1):

                # phi is horizontal, theta is vertical

                phi_delta = 1. * angular_size / num_x
                theta_delta = 1. * angular_size / num_y

                phi_start = 2. * theta_i + i * phi_delta

                phi = phi_start + phi_delta / 2.
                theta = j * theta_delta

                collecting_surface_height = collecting_surface_distance * \
                                            (np.sin(np.pi / 180. * (j+1) * phi_delta) - np.sin(np.pi / 180. * (j-1) * phi_delta))

                collecting_surface_z = collecting_surface_distance * np.sin(np.pi / 180. * j * phi_delta)

                current_collecting_surface = GS.tubeVolume('collecting_surface_phi_' + str(phi) + '_theta_' + str(theta),
                                                           collecting_surface_distance + collecting_surface_thickness,
                                                           collecting_surface_height, collecting_surface_distance,
                                                           phi_start - 90,
                                                           phi_delta)
                current_collecting_surface.center["z"] = collecting_surface_z

                masterString = current_collecting_surface.writeToString(masterString)

    if coherent_surface:

        height = collecting_surface_distance * 2. * np.sin(np.pi / 180. * angular_size / 2.)

        surface = GS.tubeVolume('coherent_surface', collecting_surface_distance + collecting_surface_thickness, height,
                                collecting_surface_distance, (360. + 2. * theta_i - 90. - angular_size / 2.) % 360.,
                                angular_size)

        """
        surface = GS.sphereVolume('coherent_surface', collecting_surface_distance + collecting_surface_thickness,
                                                   collecting_surface_distance, 90. - angular_size / 2., angular_size,
                                (360. + 2. * theta_i - 90. - angular_size / 2.) % 360., angular_size)
        """
        masterString = surface.writeToString(masterString)

    if angle_collecting_surfaces:
        #height = 0.5
        outer_distance = tube_radius + 0.1
        inner_distance = tube_radius - tube_wall_width - 0.1

        thickness = 0.01
        angular_size_ = 10.

        outer_surface = GS.tubeVolume('outer_angle_surface', outer_distance + thickness, height,
                                outer_distance, (360. - 90. - angular_size_ / 2.) % 360.,
                                angular_size_)
        outer_surface.material = 'pmt_vacuum'
        inner_surface = GS.tubeVolume('inner_angle_surface', inner_distance, height,
                                inner_distance - thickness, (360. - 90. - angular_size_ / 2.) % 360.,
                                angular_size_)
        inner_surface.material = 'pmt_vacuum'
        inner_surface.mother = fluid.name

        masterString = outer_surface.writeToString(masterString)
        masterString = inner_surface.writeToString(masterString)


    if tube_caps_included:
        upper_tube_cap = GS.tubeVolume('upper_tube_cap', tube_cap_radius, upper_tube_cap_height)
        lower_tube_cap = GS.tubeVolume('lower_tube_cap', tube_cap_radius, lower_tube_cap_height)
        upper_tube_cap.center = {'x': 0, 'y': 0, 'z': (tube_height + upper_tube_cap_height) / 2}
        lower_tube_cap.center = {'x': 0, 'y': 0, 'z': -(tube_height + lower_tube_cap_height) / 2}
        upper_tube_cap.material = 'aluminum'
        lower_tube_cap.material = 'aluminum'
        upper_tube_cap.colorVect = [0.2, 0.8, 0.6, 0.2]
        lower_tube_cap.colorVect = [0.2, 0.8, 0.6, 0.2]
        masterString = upper_tube_cap.writeToString(masterString)
        masterString = lower_tube_cap.writeToString(masterString)

    if laser_included:
        laser = GS.tubeVolume('laser', laser_radius, laser_length)
        laser.center = {'x': laser_offset, 'y': -(laser_length / 2. + dist_from_laser_to_sample), 'z': 0}
        laser.rotation = [90, 0, 0]
        laser.material = 'stainless_steel'
        laser.colorVect = [0.5, 0.5, 0, 0.5]
        masterString = laser.writeToString(masterString)

    if table_included:
        table = GS.boxVolume('table', 24, 24, 4)
        table.center = {'x': 0, 'y': 0, 'z': -dist_from_table_to_sample}
        table.material = 'stainless_steel'
        table.colorVect = [0.6, 0.2, 0.6, 1]
        masterString = table.writeToString(masterString)

    if post_included:
        post = GS.tubeVolume('post', post_radius, dist_from_table_to_sample - tube_height / 2 - lower_tube_cap_height)
        post.center = {'x': 0, 'y': 0, 'z': ((-tube_height / 2 - lower_tube_cap_height) + -dist_from_table_to_sample) / 2}
        post.material = 'stainless_steel'
        post.colorVect = [0.4, 0.7, 0.3, 0.5]
        masterString = post.writeToString(masterString)

    geoOutFile = open(geoFileName, 'w+')
    geoOutFile.write(masterString)
    geoOutFile.close()
