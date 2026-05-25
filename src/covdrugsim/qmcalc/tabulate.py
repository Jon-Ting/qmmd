import re
from os import listdir
from os.path import isdir
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from xlsxwriter.workbook import Workbook


def sortNatural(targetList: List[str]) -> List[str]:
    """
    Sort a given list in a more natural way (e.g., 'abc2' before 'abc10').

    Parameters
    ----------
    targetList : List[str]
        List of strings to be sorted.

    Returns
    -------
    List[str]
        Naturally sorted list.
    """
    tryConvertNumeric = lambda text: float(text) if text.isdigit() else text
    alphanum = lambda key: [
        tryConvertNumeric(c) for c in re.split(r"([-+]?[0-9]*\.?[0-9]*)", key)
    ]
    targetList.sort(key=alphanum)
    return targetList


def replaceMultiple(str1: str, strsToReplace: List[str], str2: str) -> str:
    """
    Replace multiple strings in str1 by str2.

    Parameters
    ----------
    str1 : str
        Target string.
    strsToReplace : List[str]
        List of strings to be replaced.
    str2 : str
        Replacement string.

    Returns
    -------
    str
        Updated string.
    """
    for strToReplace in strsToReplace:
        if strToReplace in str1:
            str1 = str1.replace(strToReplace, str2)
    return str1


def findVal(lineList: List[str], targetStr: List[str]) -> Union[float, str]:
    """
    Find the values of interest from Gaussian output files.

    Parameters
    ----------
    lineList : List[str]
        List of lines from the Gaussian output file (reversed).
    targetStr : List[str]
        List of target strings to search for.

    Returns
    -------
    Union[float, str]
        Found value, either as a float (for energies) or a string.

    Raises
    ------
    Exception
        If the target string is not found in the line list.
    """
    val, isEnergy, isMethod = (
        None,
        "Energies" in targetStr[0] or "Enthalpies" in targetStr[0],
        "%chk" in targetStr[0],
    )
    for string in targetStr:
        for j, line in enumerate(lineList):
            if string in line:
                if isMethod:
                    # Method is typically on the line starting with '#' which is a few lines after %chk
                    # In reversed list, it's a few lines before %chk
                    try:
                        valueInc = lineList[j - 2]
                        val = valueInc.split(" ")[2]
                        break
                    except (IndexError, ValueError):
                        continue
                else:
                    valueInc = line.split(string)[-1].strip()
                    # If it's an archive entry, it might have backslashes
                    if "\\" in valueInc:
                        valueInc = valueInc.split("\\")[0]
                    
                    if isEnergy:
                        try:
                            val = float(valueInc.split("=")[-1].strip().replace(" ", ""))
                            break
                        except ValueError:
                            continue
                    else:
                        # Non-energy values (like NImag)
                        raw_val = valueInc.split("=")[-1].strip()
                        if not raw_val:
                            # Try previous line if it was a multi-line archive entry
                            try:
                                raw_val = lineList[j - 1].split("\\")[0].split("=")[-1].strip()
                            except (IndexError, ValueError):
                                pass
                        
                        try:
                            val = float(raw_val.replace(" ", ""))
                            break
                        except ValueError:
                            # Might be a string value
                            val = raw_val
                            if val:
                                break
                            continue
    if val is None:
        raise Exception("Target string {0} not found!".format(targetStr))
    return val


def writeToExcel(inputDirPath: str, verbose: bool = False) -> Workbook:
    """
    Tabulate the quantities of interest from Gaussian .out files to an Excel document.

    Parameters
    ----------
    inputDirPath : str
        Path to the directory containing Gaussian output files.
    verbose : bool, optional
        Whether to display details of the process.

    Returns
    -------
    Workbook
        The xlsxwriter Workbook object.
    """
    groups = [f for f in listdir(inputDirPath) if isdir("{0}/{1}".format(inputDirPath, f))]

    if verbose:
        print(
            "\n# Tabulating values of interest from Gaussian .out files to an Excel sheet..."
        )
        print("\n# Input directory:\n", inputDirPath, "\n\n# Groups:\n", groups, "\n")

    methodList, nameList, moleculeList, conformerList, NImagList, ZList, EList, HList, GList = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )
    varFillList = [methodList, NImagList, ZList, EList, HList, GList]
    keywordList = (
        ["%chk"],
        ["NI", "Im"],
        ["zero-point Energies"],
        ["HF"],
        ["thermal Enthalpies"],
        ["thermal Free Energies"],
    )
    for name in groups:
        moleculeDir = "{0}/{1}".format(inputDirPath, name)
        print("Molecule:", name)
        try:
            with open("{0}/{1}.out".format(moleculeDir, name), "r") as f:
                lineList = f.readlines()
                lineList.reverse()
                for i, varList in enumerate(varFillList):
                    val = findVal(lineList, keywordList[i])
                    varList.append(val)
                nameList.append(name)
                moleculeList.append(
                    replaceMultiple(
                        name.split("c")[0].replace("_", ""), ["TR", "TSS", "TP"], ""
                    )
                )
                conformerList.append("c" + name.split("c")[-1])
        except FileNotFoundError:
            print("{0}/{1}.out not found!".format(moleculeDir, name))
            continue
    data = {
        "Method": methodList,
        "Name": nameList,
        "Molecule": moleculeList,
        "Conformer": conformerList,
        "NImag": NImagList,
        "Z (Hartree)": ZList,
        "E (Hartree)": EList,
        "H (Hartree)": HList,
        "G (Hartree)": GList,
    }
    df = pd.DataFrame(data)
    nameList = sortNatural(nameList)
    sortedDF = df.set_index("Name").reindex(nameList).reset_index()
    print("# Sorted data frame:\n", sortedDF)

    print("# Writing to Excel sheet...")
    writer = pd.ExcelWriter("{0}/Energies.xlsx".format(inputDirPath), engine="xlsxwriter")
    sortedDF.to_excel(writer, startrow=1, sheet_name="Sheet1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]
    for i, col in enumerate(sortedDF.columns):
        column_len = sortedDF[col].astype(str).str.len().max()
        column_len = max(column_len, len(col)) + 2
        worksheet.set_column(i, i, column_len)
    writer.close()
    return workbook


if __name__ == "__main__":
    inputDirPath = "/mnt/c/Users/ASUS/Documents/covdrugsim/src/covdrugsim/data/exampleXYZs"  # To be modified!
    workbook = writeToExcel(inputDirPath, verbose=True)
