# Plotting code for particle kinematics
# (2,3) subplots with (px, py, pz, P, theta, phi)

import matplotlib.pyplot as plt
import numpy as np
import os
import awkward as ak
import uproot


def particleKinematicsPlot(events=None, particle=None, outdir=None, return_plot=False):
    """
    Plots particle kinematics from a given uproot TTree.

    Args:
        events: Uproot TTree.
        particle: Name of the particle to plot.
        outdir: Output directory for plots.
        return_plot: Flag to return axes
    """

    # Assert tree type
    assert (
        type(events) == uproot.models.TTree.Model_TTree_v20
    ), f"Incompatible `uproot` input type: {type(events)}"

    # Assert particle is either 'electron' or 'pion' or 'None'
    assert particle in ["electron", "pion", None], f"Unknown particle type {particle}"

    # Load the arrays from the MCParticles branch.
    gen_status = events["MCParticles/MCParticles.generatorStatus"].array(library="ak")
    mom_x = events["MCParticles/MCParticles.momentum.x"].array(library="ak")
    mom_y = events["MCParticles/MCParticles.momentum.y"].array(library="ak")
    mom_z = events["MCParticles/MCParticles.momentum.z"].array(library="ak")

    # Filter particles where generatorStatus==1 for each event
    mask = gen_status == 1
    mom_x_sel = mom_x[mask]
    mom_y_sel = mom_y[mask]
    mom_z_sel = mom_z[mask]

    # Flatten the jagged arrays into a single 1D array
    mom_x_flat = ak.to_numpy(ak.flatten(mom_x_sel))
    mom_y_flat = ak.to_numpy(ak.flatten(mom_y_sel))
    mom_z_flat = ak.to_numpy(ak.flatten(mom_z_sel))

    # Compute the total momentum for each selected particle:
    p_total = np.sqrt(mom_x_flat**2 + mom_y_flat**2 + mom_z_flat**2)

    # Calculate the angles in radians first
    theta_rad = np.arccos(mom_z_flat / p_total)
    phi_rad = np.arctan2(mom_y_flat, mom_x_flat)

    # Convert the angles to degrees
    theta = np.degrees(theta_rad)
    phi = np.degrees(phi_rad)

    fig, axs = plt.subplots(2, 3, figsize=(8, 6), dpi=150)

    axs[0, 0].hist(mom_x_flat, bins=50, color="red", edgecolor="black")
    axs[0, 0].set_xlabel("$P_{X}$ [GeV]", fontsize=15)

    axs[0, 1].hist(mom_y_flat, bins=50, color="red", edgecolor="black")
    axs[0, 1].set_xlabel("$P_{Y}$ [GeV]", fontsize=15)

    axs[0, 2].hist(mom_z_flat, bins=50, color="red", edgecolor="black")
    axs[0, 2].set_xlabel("$P_{Z}$ [GeV]", fontsize=15)

    axs[1, 0].hist(p_total, bins=50, range=(0,10), color="red", edgecolor="black")
    axs[1, 0].set_xlabel("$P$ [GeV]", fontsize=15)

    axs[1, 1].hist(theta, bins=50, color="red", edgecolor="black")
    axs[1, 1].set_xlabel("$\\theta$ [deg]", fontsize=15)

    axs[1, 2].hist(phi, bins=50, color="red", edgecolor="black")
    axs[1, 2].set_xlabel("$\phi$ [deg]", fontsize=15)

    if particle is not None:
        fig.suptitle(f"{particle.capitalize()} kinematics",y=1.05, fontsize=20)

    plt.tight_layout()



    if outdir is not None:
        particle_savename = particle if particle is not None else ""
        outdir = outdir + "/particle-kinematics"
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        plt.savefig(f"{outdir}/{particle_savename}_kinematics.png")

    if return_plot:
        return fig, axs
