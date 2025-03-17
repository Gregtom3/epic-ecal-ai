import pytest
from epic-ecal-ai.dataloader import dataloader
from epic-ecal-ai.plotting.raw-data.ecal-barrel import ecalBarrelPlot_v1

def test_electron_plot():
    outdir = "artifacts"
    events = dataloader.load_uproot_events("electron",0,"dropbox")
    ecalBarrelPlot_v1(events = events,
                           outdir = outdir,
                           particle = "electron",
                           return_plot = False)

def test_pion_plot():
    outdir = "artifacts"
    events = dataloader.load_uproot_events("pion",0,"dropbox")
    ecalBarrelPlot_v1(events = events,
                      outdir = outdir,
                      particle = "pion",
                      return_plot = False)