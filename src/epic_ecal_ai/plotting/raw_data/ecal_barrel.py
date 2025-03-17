# Plotting code for the ECAL barrel

import matplotlib.pyplot as plt
import os
import awkward as ak
import uproot
import numpy as np

def ecalBarrelPlot_v1(events=None, particle=None, outdir=None, return_plot=False):
    """
    Plots hits from the ECAL barrel using EcalBarrelImagingRecHits

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

    # Load the ECAL Barrel Imaging Hits positions into awkward arrays
    x_all = events[
        "EcalBarrelImagingRecHits/EcalBarrelImagingRecHits.position.x"
    ].array(library="ak")
    y_all = events[
        "EcalBarrelImagingRecHits/EcalBarrelImagingRecHits.position.y"
    ].array(library="ak")
    z_all = events[
        "EcalBarrelImagingRecHits/EcalBarrelImagingRecHits.position.z"
    ].array(library="ak")

    # Flatten the arrays
    x_all_flat = ak.to_numpy(ak.flatten(x_all))
    y_all_flat = ak.to_numpy(ak.flatten(y_all))
    z_all_flat = ak.to_numpy(ak.flatten(z_all))

    # Create a figure
    fig, axs = plt.subplots(1, 3, figsize=(18, 5), dpi=200)

    # XY projection
    axs[0].hist2d(x_all_flat, y_all_flat, bins=100, cmap="rainbow", cmin=0.1)
    axs[0].set_xlabel("X")
    axs[0].set_ylabel("Y")
    axs[0].set_title("ECAL Imaging RecHits: XY")

    # XZ projection
    axs[1].hist2d(x_all_flat, z_all_flat, bins=100, cmap="rainbow", cmin=0.1)
    axs[1].set_xlabel("X")
    axs[1].set_ylabel("Z")
    axs[1].set_title("ECAL Imaging RecHits: XZ")

    # YZ projection
    axs[2].hist2d(y_all_flat, z_all_flat, bins=100, cmap="rainbow", cmin=0.1)
    axs[2].set_xlabel("Y")
    axs[2].set_ylabel("Z")
    axs[2].set_title("ECAL Imaging RecHits: YZ")

    plt.tight_layout()

    if outdir is not None:
        particle_savename = particle if particle is not None else ""
        outdir = outdir + "/ecal-barrel"
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        plt.savefig(f"{outdir}/{particle_savename}_ecalBarrelPlot_v1.png")

    if return_plot:
        return fig, axs


def ecalBarrelPlot_v2(events=None, particle=None, outdir=None, return_plot=False):
    """
    Creates a 2x4 grid of subplots (8 events) showing the ECAL barrel imaging rec hits in the XY plane.
    Args:
        events: Uproot TTree containing branches
        particle: Optional particle name (used for saving file name).
        outdir: Output directory in which to save the plot.
        return_plot: If True, returns the matplotlib figure and axes.
    """
    
    # Check the type of events (for compatibility)
    assert (
        type(events) == uproot.models.TTree.Model_TTree_v20
    ), f"Incompatible `uproot` input type: {type(events)}"
    
    # Load ECAL Barrel Imaging RecHits positions and energies as awkward arrays.
    x_all = events["EcalBarrelImagingRecHits/EcalBarrelImagingRecHits.position.x"].array(library="ak")
    y_all = events["EcalBarrelImagingRecHits/EcalBarrelImagingRecHits.position.y"].array(library="ak")
    energy_all = events["EcalBarrelImagingRecHits/EcalBarrelImagingRecHits.energy"].array(library="ak")
    
    # Load MCParticles arrays for kinematics
    gen_status_all = events["MCParticles/MCParticles.generatorStatus"].array(library="ak")
    mom_x_all = events["MCParticles/MCParticles.momentum.x"].array(library="ak")
    mom_y_all = events["MCParticles/MCParticles.momentum.y"].array(library="ak")
    mom_z_all = events["MCParticles/MCParticles.momentum.z"].array(library="ak")
    
    # Determine the number of events to plot (up to 8)
    num_events = min(8, len(x_all))
    
    # Compute overall energy min and max for consistent color scaling
    energy_all_flat = ak.to_numpy(ak.flatten(energy_all))
    energy_min = np.min(energy_all_flat[:num_events])
    energy_max = np.max(energy_all_flat[:num_events])

    # Create a 2x4 grid of subplots
    fig, axs = plt.subplots(2, 4, figsize=(16, 8), dpi=200)
    axs = axs.flatten()  # easier to index in a 1D loop
    
    for i in range(num_events):
        # Get this event's hit positions and energies, converting to numpy arrays.
        x_event = ak.to_numpy(x_all[i])
        y_event = ak.to_numpy(y_all[i])
        energy_event = ak.to_numpy(energy_all[i])
        
        # Plot the hit positions as markers, colored by energy.
        sc = axs[i].scatter(x_event, y_event, c=energy_event, cmap="rainbow",
                            vmin=energy_min, vmax=energy_max, marker='o', s=25)
        
        axs[i].grid(True)
        axs[i].set_xlabel("X")
        axs[i].set_ylabel("Y")
        axs[i].set_xlim(-800,800)
        axs[i].set_ylim(-800,800)
        axs[i].set_title(f"Event {i}")
        
        # For this event, extract MCParticles that have generatorStatus==1
        gen_status = gen_status_all[i]
        mask = gen_status == 1
        # Initialize default label values
        p_val, theta_deg, phi_deg = None, None, None
        if ak.sum(mask) > 0:
            # Select the first valid particle
            mom_x = ak.to_numpy(mom_x_all[i][mask])[0]
            mom_y = ak.to_numpy(mom_y_all[i][mask])[0]
            mom_z = ak.to_numpy(mom_z_all[i][mask])[0]
            p_val = np.sqrt(mom_x**2 + mom_y**2 + mom_z**2)
            # To avoid division by zero
            if p_val > 0:
                theta_rad = np.arccos(mom_z / p_val)
                theta_deg = np.degrees(theta_rad)
            else:
                theta_deg = 0.0
            phi_deg = np.degrees(np.arctan2(mom_y, mom_x))
            label_text = f"P = {p_val:.2f} GeV\nθ = {theta_deg:.2f}°\nφ = {phi_deg:.2f}°"
        else:
            label_text = "P = N/A\nθ = N/A\nφ = N/A"
        
        # Annotate the subplot in the top left with the kinematic info using a rounded bbox.
        axs[i].text(0.05, 0.95, label_text, transform=axs[i].transAxes,
                    fontsize=9, verticalalignment='top',
                    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))
    
    # Remove unused subplots if fewer than 8 events (if any)
    for j in range(num_events, 8):
        fig.delaxes(axs[j])
    
    plt.tight_layout()
    
    # Optionally save the figure
    if outdir is not None:
        particle_savename = particle if particle is not None else ""
        out_path = os.path.join(outdir, "ecal-barrel")
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        save_path = os.path.join(out_path, f"{particle_savename}_ecalBarrelPlot_v2.png")
        plt.savefig(save_path)
    
    if return_plot:
        return fig, axs