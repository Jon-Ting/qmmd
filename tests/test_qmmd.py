from os import listdir
from os.path import exists, isdir, isfile
from shutil import rmtree

import numpy as np
from pytest import approx, fixture, mark

from qmmd.datasets import genExampleXYZs, getExampleEnergyLevellerInputPath, getExampleChargePath
from qmmd.qmcalc.constants import keywordDict
from qmmd.qmcalc.genScripts import genAllScripts
from qmmd.qmcalc.admin import groupFilesIntoDir
from qmmd.qmcalc.tabulate import writeToExcel
from qmmd.qmcalc.unitConv import energyUnitsConversion, eyringEquation, timeUnitsConversion
from qmmd.mdsim import mdAnalyse

targetDirPath = 'tests/exampleXYZs'
exampleXYZname = 'example1'
exampleXYZdirPath = f"{targetDirPath}/{exampleXYZname}"


def test_genExampleXYZs():
    """Unit test for genExampleXYZs()."""
    genExampleXYZs(targetDirPath)
    assert exists(targetDirPath), f"{targetDirPath} not found"
    assert isdir(targetDirPath), f"{targetDirPath} not a directory"
    assert len(listdir(targetDirPath)) == 3, f"Incorrect number of xyz files in {targetDirPath}"


def test_getExampleEnergyLevellerInputPath():
    """Unit test for genExampleEnergyLevellerInputPath()."""
    energyLevellerInputPathAct = getExampleEnergyLevellerInputPath()
    assert isinstance(energyLevellerInputPathAct, str), 'Path not a string'


def test_getExampleChargePath():
    """Unit test for genExampleChargePath()."""
    chargePathAct = getExampleChargePath()
    assert isinstance(chargePathAct, str), 'Path not a string'


def test_groupFilesIntoDir():
    """Unit test for groupFilesIntoDir()."""
    groupFilesIntoDir(targetDirPath)

    assert exists(exampleXYZdirPath), f"{exampleXYZdirPath} not found"
    assert isdir(exampleXYZdirPath), f"{exampleXYZdirPath} not a directory"

    assert exists(f"{exampleXYZdirPath}/{exampleXYZname}.xyz"), f"{exampleXYZname}.xyz not found"
    assert isfile(f"{exampleXYZdirPath}/{exampleXYZname}.xyz"), f"{exampleXYZname}.xyz not a file"

    assert len(listdir(targetDirPath)) == 3, f"Incorrect number of files in {exampleXYZdirPath}"

    if isdir(targetDirPath):
        rmtree(targetDirPath)


def test_genAllScripts():
    """Unit test for genAllScripts()."""
    genExampleXYZs(targetDirPath)
    genAllScripts(targetDirPath, verbose=True)
    assert exists(f"{exampleXYZdirPath}/{exampleXYZname}.xyz"), f"{exampleXYZname}.xyz not found"
    assert isfile(f"{exampleXYZdirPath}/{exampleXYZname}.xyz"), f"{exampleXYZname}.xyz not a file"
    assert exists(f"{exampleXYZdirPath}/{exampleXYZname}.inp"), f"{exampleXYZname}.inp not found"
    assert isfile(f"{exampleXYZdirPath}/{exampleXYZname}.inp"), f"{exampleXYZname}.inp not a file"
    assert exists(f"{exampleXYZdirPath}/{exampleXYZname}.sh"), f"{exampleXYZname}.sh not found"
    assert isfile(f"{exampleXYZdirPath}/{exampleXYZname}.sh"), f"{exampleXYZname}.sh not a file"
    if isdir(targetDirPath):
        rmtree(targetDirPath)


def test_energyUnitsConversion():
    assert energyUnitsConversion(100, None) == approx((100, 418.4))
    assert energyUnitsConversion(None, 418.4) == approx((100, 418.4))


@mark.parametrize("kcal, kj", [(None, None), (100, 418.4)])
def test_energyUnitsConversion_raises(kcal, kj):
    import pytest
    with pytest.raises(ValueError):
        energyUnitsConversion(kcal, kj)


def test_eyringEquation():
    # Example values: T=300, dGbarr=20 kcal/mol
    # k = (kappa*kB*T/h) * exp(-dGbarr_J/(R*T))
    # kappa=1, kB=1.380649e-23, h=6.62607015e-34, R=8.314462618
    # dGbarr_kJ = 20 * 4.184 = 83.68 kJ/mol = 83680 J/mol
    # k = (1 * 1.380649e-23 * 300 / 6.62607015e-34) * exp(-83680 / (8.314462618 * 300))
    # k = (6.25098e12) * exp(-33.548) = 6.25098e12 * 2.693e-15 = 0.0168
    k, dG = eyringEquation(None, 20, 300)
    assert k == approx(0.01683, rel=1e-3)
    assert dG == approx(20)

    k2, dG2 = eyringEquation(0.01683, None, 300)
    assert k2 == approx(0.01683)
    assert dG2 == approx(20, rel=1e-3)


def test_timeUnitsConversion():
    # k = 0.01683
    # t_half = ln(2) / k = 0.693147 / 0.01683 = 41.185
    # RT = 1 / k = 1 / 0.01683 = 59.417
    k, t_half, RT = timeUnitsConversion(0.01683, None, None)
    assert k == approx(0.01683)
    assert t_half == approx(41.185, rel=1e-3)
    assert RT == approx(59.417, rel=1e-3)

    k2, t_half2, RT2 = timeUnitsConversion(None, 41.185, None)
    assert k2 == approx(0.01683, rel=1e-3)
    assert t_half2 == approx(41.185)
    assert RT2 == approx(59.417, rel=1e-3)


def test_sumCharge(tmp_path):
    charge_file = tmp_path / "charges.txt"
    out_file = tmp_path / "totCharge.txt"
    charge_file.write_text("0.1\n-0.2\n0.3\n")
    
    mdAnalyse.sumCharge(str(charge_file), str(out_file), correction=0.002)
    
    # Corrected charges: 0.102, -0.198, 0.302
    # Total: 0.206
    content = out_file.read_text().splitlines()
    assert len(content) == 3
    assert float(content[0]) == approx(0.102)
    assert float(content[1]) == approx(-0.198)
    assert float(content[2]) == approx(0.302)


