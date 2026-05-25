from importlib.resources import files
from os import mkdir
from os.path import isdir
from shutil import copytree


def getExampleChargePath():
    """Get path to chargesExample.txt.

    Returns
    -------
    str
        Path to file.
    """
    return str(files('qmmd.data').joinpath('chargesExample.txt'))


def getExampleEnergyLevellerInputPath():
    """Get path to energyLevellerExample.inp.

    Returns
    -------
    str
        Path to file.
    """
    return str(files('qmmd.data').joinpath('energyLevellerExample.inp'))


def genExampleXYZs(targetDirPath):
    """
    Generates example xyz files at specified directory path.
    """
    if not isdir(targetDirPath):
        mkdir(targetDirPath)
    exampleXYZsPath = str(files('qmmd.data').joinpath('exampleXYZs'))
    copytree(exampleXYZsPath, targetDirPath, dirs_exist_ok=True)

