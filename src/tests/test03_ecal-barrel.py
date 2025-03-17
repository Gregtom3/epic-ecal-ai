import pytest
from epic_ecal_ai.dataloader import dataLoader
from epic_ecal_ai.plotting.raw_data.ecal_barrel import ecalBarrelPlot_v1, ecalBarrelPlot_v2

def test_electron_plot_v1():
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("electron",0,"dropbox")
    ecalBarrelPlot_v1(events = events,
                      outdir = outdir,
                      particle = "electron",
                      return_plot = False)
    
def test_electron_plot_v2():
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("electron",0,"dropbox")
    ecalBarrelPlot_v2(events = events,
                      outdir = outdir,
                      particle = "electron",
                      return_plot = False)

def test_pion_plot_v1():
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("pion",0,"dropbox")
    ecalBarrelPlot_v1(events = events,
                      outdir = outdir,
                      particle = "pion",
                      return_plot = False)
    
def test_pion_plot_v2():
    outdir = "artifacts"
    events = dataLoader.load_uproot_events("pion",0,"dropbox")
    ecalBarrelPlot_v2(events = events,
                      outdir = outdir,
                      particle = "pion",
                      return_plot = False)