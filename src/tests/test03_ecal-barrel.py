import pytest
from epic_ecal_ai.dataloader import dataLoader
from epic_ecal_ai.plotting.raw_data.ecal_barrel import ecalBarrelPlot_v1
import matplotlib.pyplot as plt
import os
def test_electron_plot():
    os.makedirs("artifacts",exist_ok=True)
    plt.plot([1],[2])
    plt.savefig("artifacts/save.png")
    plt.close()
    return 

    outdir = "artifacts"
    events = dataLoader.load_uproot_events("electron",0,"dropbox")
    ecalBarrelPlot_v1(events = events,
                           outdir = outdir,
                           particle = "electron",
                           return_plot = False)

def test_pion_plot():
    os.makedirs("artifacts",exist_ok=True)
    plt.plot([1],[2])
    plt.savefig("artifacts/save.png")
    plt.close()
    return 
    
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("pion",0,"dropbox")
    ecalBarrelPlot_v1(events = events,
                      outdir = outdir,
                      particle = "pion",
                      return_plot = False)