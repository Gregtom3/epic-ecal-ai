# Files are located in Gregory M.'s DukeBox
# !! In the future, we want a more secure, permament way of pulling these larger files !!
ELECTRON_FILES = [
    "https://duke.box.com/shared/static/vyiizlfvwz6tmfupey5hxluc45gkbvr3.root"
]
PION_FILES = [
    "https://duke.box.com/shared/static/zlojdktck99wygbn8bwku778rqty9rir.root"
]


def load_dropbox_filename(particle: str, index: int) -> list:
    """
    Gets a list of filenames from a given version.

    Args:
        particle: The particle to load.
        index: The index of the file to load.

    Returns:
        A filename.
    """

    if particle == "electron":
        assert index <= len(
            ELECTRON_FILES
        ), f"Not enough electron files available for index: {index}"
        return ELECTRON_FILES[index]
    elif particle == "pion":
        assert index <= len(
            PION_FILES
        ), f"Not enough pion files available for index: {index}"
        return PION_FILES[index]
    else:
        raise ValueError(f"Unknown particle: {particle}")
