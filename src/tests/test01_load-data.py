import pytest
from epic_ecal_ai.dataloader import dataLoader
from epic_ecal_ai.dataloader import dropboxLoader

def test_dropboxLoader():

    # Test all 'electron' and 'pion' files
    for i in range(len(dropboxLoader.ELECTRON_FILES)):
        assert dropboxLoader.load_dropbox_filename("electron", i) == dropboxLoader.ELECTRON_FILES[i]
    for i in range(len(dropboxLoader.PION_FILES)):
        assert dropboxLoader.load_dropbox_filename("pion", i) == dropboxLoader.PION_FILES[i]

    # Test exception for 'muon' (no file)
    with pytest.raises(ValueError):
        dropboxLoader.load_dropbox_filename("muon", 0)
    
def test_dataloader():

    # Test bad source
    with pytest.raises(ValueError):
        dataLoader.load_uproot_events("electron", 0, "google-drive")

    with pytest.raises(AssertionError):
        dataLoader.load_uproot_events("electron", 1234, "dropbox")

    
