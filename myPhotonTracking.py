import rat
import ROOT
import sys
#import runCheckTools as RCT
import json
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np


def plot_output(theta_i):  #distance in inches

    # Get command line arguments
    cmdArgs = sys.argv

    file_name = '~/Desktop/RAT_files/error_analysis/output.root'

    fileIterator = rat.dsreader(file_name)

    print_all_steps = False
    if print_all_steps:
        for iEntry, anEntry in enumerate(fileIterator):
            print("########################## NEW MC ######################")
            MC = anEntry.GetMC()
            num_tracks = MC.GetMCTrackCount()
            print('num_tracks: ', num_tracks)
            track = MC.GetMCTrack(0)
            starting_momentum = track.GetMCTrackStep(0).GetMomentum()
            for i in range(track.GetMCTrackStepCount()):
                step = track.GetMCTrackStep(i)
                endpoint = step.GetEndpoint()
                volume = step.GetVolume()
                momentum = step.GetMomentum()
                process = step.GetProcess()
                print("######### NEW STEP #########")
                print('endpoint: ', endpoint[0], endpoint[1], endpoint[2])
                print('momentum: ', momentum[0], momentum[1], momentum[2])
                print('volume: ', volume)
                print('process: ', process)

    print_all_momentum_changes = False
    if print_all_momentum_changes:
        for iEntry, anEntry in enumerate(fileIterator):
            MC = anEntry.GetMC()
            num_tracks = MC.GetMCTrackCount()
            track = MC.GetMCTrack(0)
            starting_momentum = track.GetMCTrackStep(0).GetMomentum()
            for i in range(track.GetMCTrackStepCount()):
                step = track.GetMCTrackStep(i)
                endpoint = step.GetEndpoint()
                volume = step.GetVolume()
                momentum = step.GetMomentum()
                process = step.GetProcess()
                if momentum != starting_momentum:
                    print("######### NEW STEP #########")
                    print('endpoint: ', endpoint[0], endpoint[1], endpoint[2])
                    print('momentum: ', momentum[0], momentum[1], momentum[2])
                    print('volume: ', volume)
                    print('process: ', process)

    x = []
    y = []
    z = []
    for iEntry, anEntry in enumerate(fileIterator):
        MC = anEntry.GetMC()
        track = MC.GetMCTrack(0)
        for i in range(track.GetMCTrackStepCount()):
            step = track.GetMCTrackStep(i)
            volume = step.GetVolume()
            volume_string = str(volume)
            endpoint = step.GetEndpoint()
            if volume_string == "coherent_surface":
                x.append(endpoint[0])
                y.append(endpoint[1])
                z.append(endpoint[2])

    """
    plt.figure()
    plt.hist2d(y, z, bins=40, norm=LogNorm())
    plt.xlabel("y")
    plt.ylabel("z")
    plt.colorbar()
    plt.title("position unzeroed")
    """

    r = []
    phi = []  # horizontal, 0 at x = 1, y=0, z=0
    theta = []  # vertical, 0 at z=0
    for i in range(len(x)):
        r.append(np.sqrt(x[i] ** 2 + y[i] ** 2 + z[i] ** 2))
        phi.append(180. / np.pi * np.arctan2(y[i], x[i]))
        theta.append(180. / np.pi * np.arctan2(z[i], np.sqrt(x[i] ** 2 + y[i] ** 2)))

    """
    plt.figure()
    plt.hist2d(phi, theta, bins=40, norm=LogNorm())
    plt.xlabel("phi (horizontal)")
    plt.ylabel("theta (vertical)")
    plt.colorbar()
    plt.title("angular unzeroed")
    """

    phi_specular = 2. * theta_i - 90.
    print(phi_specular)
    phi_zeroed = [phi_ - phi_specular for phi_ in phi]

    plt.figure()
    plt.hist2d(phi_zeroed, theta, bins=40, norm=LogNorm())
    plt.xlabel("Delta phi (horizontal)")
    plt.ylabel("Delta theta (vertical)")
    plt.colorbar()
    plt.title("angular zeroed")

    plt.show()

