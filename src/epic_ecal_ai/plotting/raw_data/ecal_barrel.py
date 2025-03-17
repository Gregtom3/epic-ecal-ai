# Plotting code for the ECAL barrel

import matplotlib.pyplot as plt
import os
import awkward as ak
import uproot


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

    if particle is not None:
        fig.suptitle(f"{particle.capitalize()} ECAL Barrel Imaging RecHits",y=1.05,fontsize=20)

    if outdir is not None:
        particle_savename = particle if particle is not None else ""
        outdir = outdir + "/ecal-barrel"
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        plt.savefig(f"{outdir}/{particle_savename}_ecalBarrelPlot_v1.png")

    if return_plot:
        return fig, axs
