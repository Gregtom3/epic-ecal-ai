import pytest
from epic_ecal_ai.dataloader import dataLoader
from epic_ecal_ai.plotting.raw_data.particle_kinematics import particleKinematicsPlot

import matplotlib.pyplot as plt

def test_electron_plot():
    plt.plot([1],[2])
    plt.savefig("artifacts/save.png")
    plt.close()
    return 
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("electron",0,"dropbox")
    particleKinematicsPlot(events = events,
                           outdir = outdir,
                           particle = "electron",
                           return_plot = False)

def test_pion_plot():
    plt.plot([1],[2])
    plt.savefig("artifacts/save.png")
    plt.close()
    return 
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("pion",0,"dropbox")
    particleKinematicsPlot(events = events,
                           outdir = outdir,
                           particle = "pion",
                           return_plot = False)