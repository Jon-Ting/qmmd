import os
import shutil
from os.path import exists

import pandas as pd
from qmmd.qmcalc.tabulate import writeToExcel


def test_writeToExcel(tmp_path):
    # Create mock Gaussian output files
    molecule_name = "example_mol"
    molecule_dir = tmp_path / molecule_name
    molecule_dir.mkdir()
    
    out_file = molecule_dir / f"{molecule_name}.out"
    out_file.write_text("""
 Entering Gaussian System, Link 0=g16
 %mem=4000mb
 %chk=example_mol.chk
 ----------------------------------------------------------------------
 # m062x/6-311+g(d,p) opt=calcfc freq scrf=(cpcm,solvent=water) int(grid=ultrafine)
 ----------------------------------------------------------------------
 
 example_mol
 
 0 1
 ...
  1 imaginary frequencies (negative Signs)
  Sum of electronic and zero-point Energies=          -100.1
  Sum of electronic and thermal Enthalpies=           -100.3
  Sum of electronic and thermal Free Energies=        -100.4
 
 1\\1\\GINC-GADI\\SP\\RM062X\\6-311+G(D,P)\\C\\USER\\05-Jul-2023\\0\\\\# opt=calcfc freq 6-311+g(d,p) scrf=(cpcm,solvent=water) m062x int(grid=ultrafine)\\\\example_mol\\\\0,1\\\\C,0,0,0\\\\HF=-100.2\\\\NI=1\\\\zero-point Energies=-100.1\\\\thermal Enthalpies=-100.3\\\\thermal Free Energies=-100.4\\\\@
 """)
    
    writeToExcel(str(tmp_path), verbose=True)
    excel_file = tmp_path / "Energies.xlsx"
    assert exists(excel_file)
    df = pd.read_excel(excel_file, sheet_name='Sheet1', header=1)
    assert df.iloc[0]['Z (Hartree)'] == -100.1
    assert df.iloc[0]['E (Hartree)'] == -100.2
    assert df.iloc[0]['H (Hartree)'] == -100.3
    assert df.iloc[0]['G (Hartree)'] == -100.4
    assert df.iloc[0]['NImag'] == 1
