import uproot
from epic_ecal_ai.dataloader import dropboxLoader
import re


def load_uproot_events(particle: str, index: int, source: str) -> uproot.TBranch:
    """
    Loads an uproot TBranch from a given file.

    Args:
        particle: The particle to load.
        index: The index of the file to load.
        source: The source of the file. (ex: dropbox)

    Returns:
        Uproot 'events' branch from file
    """

    if source == "dropbox":
        filename = dropboxLoader.load_dropbox_filename(particle, index)
    else:
        raise ValueError(f"Unknown source: {source}")

    # Open uproot file
    f = uproot.open(filename)

    # Assert 'f' contains the correct keys
    pattern = re.compile(r"events*")
    assert any(
        pattern.search(item) for item in f.keys()
    ), f"Error: `events` branch not in file {filename}"

    # Load events TTree
    events = f["events"]

    return events
