# coding=UTF-8

"""
Energy Leveller version 2.0  (2019)
This code is shared under the MIT license Copyright 2019 James Furness.
"""
import os.path
import sys
from typing import Dict, List, Optional, Tuple, Union

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")


class State:
    """
    Holds values for a single state in the energy level diagram.
    """

    name: str = ""
    color: str = ""
    labelColor: str = ""
    linksTo: str = ""
    label: str = ""
    legend: Optional[str] = None
    energy: float = 0.0
    normalisedPosition: float = 0.0
    column: int = 1
    leftPointx: float = 0.0
    leftPointy: float = 0.0
    rightPointx: float = 0.0
    rightPointy: float = 0.0
    labelOffset: Tuple[float, float] = (0.0, 0.0)
    textOffset: Tuple[float, float] = (0.0, 0.0)


class Diagram:
    """
    Holds global values for the diagram and handles drawing through Draw() method.
    """

    statesList: Dict[str, State]
    dashes: List[float] = [6.0, 3.0]  # ink, skip
    outputName: str = ""
    columns: int = 0
    width: float = 0.0
    height: float = 0.0
    energyUnits: str = ""
    do_legend: bool = False
    COLORS: Dict[str, str] = {}

    def __init__(self, width: float, height: float, fontSize: int, outputName: str):
        self.width = width
        self.height = height
        self.outputName = outputName
        self.statesList = {}

        self.fig = plt.figure(figsize=(self.width, self.height))
        self.ax = self.fig.add_subplot(111)

    def AddState(self, state: State) -> None:
        """Add a state to the diagram."""
        state.name = state.name.upper()
        state.color = state.color.upper()
        state.labelColor = state.labelColor.upper()
        state.linksTo = state.linksTo.upper()
        if state.legend is not None:
            self.do_legend = True
        if state.name not in self.statesList:
            self.statesList[state.name] = state
        else:
            print(
                "ERROR: States must have unique names. State "
                + state.name
                + " is already in use!"
            )
            sys.exit("Non unique state names.")

    def DetermineEnergyRange(self) -> List[float]:
        """Determine the range of energies in the diagram."""
        if len(self.statesList) == 0:
            sys.exit("No states in diagram.")
        maxE = -10e20
        minE = 10e20
        for state in self.statesList.values():
            if state.energy > maxE:
                maxE = state.energy
            if state.energy < minE:
                minE = state.energy
        self.axesTop = maxE
        self.axesMin = minE
        self.axesOriginNormalised = 1 + (minE / (maxE - minE))
        return [minE, maxE]

    def MakeLeftRightPoints(self) -> None:
        """Calculate the left and right points for each state."""
        columnWidth = 1.0

        for key, state in self.statesList.items():
            state.leftPointx = (
                state.column * columnWidth + state.column * columnWidth / 2.0
            )
            state.leftPointy = state.energy
            state.rightPointx = state.leftPointx + columnWidth
            state.rightPointy = state.energy

    def Draw(self) -> None:
        """Draw the energy level diagram."""
        self.ax.axhline(0.0, color="gray", linestyle=":")

        #   Draw the states
        for key in self.statesList.keys():
            state = self.statesList[key]
            self.ax.plot(
                [state.leftPointx, state.rightPointx],
                [state.leftPointy, state.rightPointy],
                c=state.color,
                lw=3,
                ls="-",
                label=state.legend,
            )

        #   Draw their labels
        offset_y = self.ax.get_ylim()
        offset = offset_y[1] * 0.01
        for key in self.statesList.keys():
            state = self.statesList[key]
            self.ax.text(
                state.leftPointx + state.labelOffset[0],
                state.leftPointy + state.labelOffset[1] + offset,
                state.label,
                color=state.labelColor,
                verticalalignment="bottom",
            )
            self.ax.text(
                state.leftPointx + state.textOffset[0],
                state.leftPointy + state.textOffset[1] - offset,
                "  " + str(state.energy),
                color=state.labelColor,
                verticalalignment="top",
            )

        #   Draw the dashed lines connecting them
        for key in self.statesList.keys():
            state = self.statesList[key]
            if state.linksTo != "":
                for link in state.linksTo.split(","):
                    link = link.strip()
                    raw = link.split(":")
                    dest = raw[0]
                    if len(raw) > 1:
                        color = raw[1]
                    else:
                        color = "BLACK"
                    if dest in self.statesList:
                        self.ax.plot(
                            [state.rightPointx, self.statesList[dest].leftPointx],
                            [state.rightPointy, self.statesList[dest].leftPointy],
                            c=color,
                            ls="--",
                            lw=1,
                        )
                    else:
                        print("Name: " + dest + " is unknown.")

        self.ax.set_ylabel(str(self.energyUnits), family="sans-serif", fontsize=12)
        self.ax.set_xlabel("Reaction Progress", family="sans-serif", fontsize=12)
        self.ax.set_xticks([])
        self.ax.set_ylim([-3, 26])
        self.ax.set_title(
            r"Energy Profile of $\alpha$-Santonin",
            loc="center",
            family="sans-serif",
            fontsize=12,
        )
        if self.do_legend:
            self.ax.legend()
        self.fig.savefig(self.outputName)


######################################################################################################
#           Input reading block
######################################################################################################


def ReadInput(filename: str) -> Diagram:
    """Read input from a file and return a Diagram object."""
    try:
        inp = open(filename, "r")
    except:
        print("Error opening file. File: " + filename + " may not exist.")
        sys.exit("Could not open Input file.")

    stateBlock = False
    statesList: List[State] = []
    width = 0.0
    height = 0.0
    fontSize = 8
    outName = ""
    energyUnits = ""
    colorsToAdd: Dict[str, str] = {}
    lc = 0
    for line in inp:
        lc += 1
        line = line.strip()
        if len(line) > 0 and line.strip()[0] != "#":
            if stateBlock:
                if line.strip()[0] == "{":
                    print(
                        "Unexpected opening '{' within state block on line "
                        + str(lc)
                        + ".\nPossible forgotten closing '}'."
                    )
                    sys.exit("ERROR: Unexpected { on line " + str(lc))
                if line.strip()[0] == "}":
                    stateBlock = False
                else:
                    raw = line.split("=")
                    if len(raw) != 2 and raw[0].upper().strip() != "LABEL":
                        print(raw[0].strip())
                        print("Ignoring unrecognised line " + str(lc) + ":\n\t" + line)
                    else:
                        raw[0] = raw[0].upper().strip()
                        raw[1] = raw[1].strip()
                        if raw[0] == "NAME":
                            statesList[-1].name = raw[1].upper()
                        elif raw[0] in [
                            "TEXTCOLOR",
                            "TEXTCOLOUR",
                            "TEXT-COLOUR",
                            "TEXT-COLOR",
                            "TEXT COLOUR",
                            "TEXT COLOR",
                        ]:
                            statesList[-1].color = raw[1].upper()
                        elif raw[0] == "LABEL":
                            statesList[-1].label = ""
                            for i in range(1, len(raw)):
                                statesList[-1].label += raw[i]
                                if i < len(raw) - 1:
                                    statesList[-1].label += " = "
                        elif raw[0] == "LABELCOLOR" or raw[0] == "LABELCOLOUR":
                            statesList[-1].labelColor = raw[1]
                        elif raw[0] == "LINKSTO" or raw[0] == "LINKS TO":
                            statesList[-1].linksTo = raw[1].upper()
                        elif raw[0] == "COLUMN":
                            try:
                                statesList[-1].column = int(raw[1]) - 1
                            except ValueError:
                                print(
                                    "ERROR: Could not read integer for column number on line "
                                    + str(lc)
                                    + ":\n\t"
                                    + line
                                )
                        elif raw[0] == "ENERGY":
                            try:
                                statesList[-1].energy = float(raw[-1])
                            except ValueError:
                                print(
                                    "ERROR: Could not read real number for energy on line "
                                    + str(lc)
                                    + ":\n\t"
                                    + line
                                )
                        elif raw[0] in ["LABELOFFSET", "LABEL OFFSET", "LABEL-OFFSET"]:
                            raw[1] = raw[1].split(",")
                            try:
                                tx = float(raw[1][0])
                                ty = float(raw[1][1])
                                statesList[-1].labelOffset = (tx, ty)
                            except:
                                print(
                                    "ERROR: Could not read real number for label offset on line "
                                    + str(lc)
                                    + ":\n\t"
                                    + line
                                )
                        elif raw[0] in ["TEXTOFFSET", "TEXT OFFSET", "TEXT-OFFSET"]:
                            raw[1] = raw[1].split(",")
                            try:
                                tx = float(raw[1][0])
                                ty = float(raw[1][1])
                                statesList[-1].textOffset = (tx, ty)
                            except:
                                print(
                                    "ERROR: Could not read real number for text offset on line "
                                    + str(lc)
                                    + ":\n\t"
                                    + line
                                )
                        elif raw[0] == "LEGEND":
                            statesList[-1].legend = raw[1]
                        else:
                            print(
                                "Ignoring unrecognised line " + str(lc) + ":\n\t" + line
                            )

            elif line.strip()[0] == "{":
                statesList.append(State())
                stateBlock = True  # we have entered a state block

            elif line.strip()[0] == "}":
                print("WARNING: Not expecting closing } on line: " + str(lc))

            else:
                raw = line.split("=")
                if len(raw) != 2:
                    print("Ignoring unrecognised line " + str(lc) + ":\n\t" + line)
                else:
                    raw[0] = raw[0].upper().strip()
                    raw[1] = raw[1].strip().lstrip()
                    if raw[0] == "WIDTH":
                        try:
                            width = float(raw[1])
                        except ValueError:
                            print(
                                "ERROR: Could not read number for diagram width on line "
                                + str(lc)
                                + ":\n\t"
                                + line
                            )
                    elif raw[0] == "HEIGHT":
                        try:
                            height = float(raw[1])
                        except ValueError:
                            print(
                                "ERROR: Could not read number for diagram height on line "
                                + str(lc)
                                + ":\n\t"
                                + line
                            )
                    elif raw[0] == "OUTPUT-FILE" or raw[0] == "OUTPUT":
                        raw[1] = raw[1].lstrip()
                        if not raw[1].endswith(".pdf"):
                            print(
                                "WARNING: Output will be .pdf. Adding this to output file.\nFile will be saved as "
                                + raw[1]
                                + ".pdf"
                            )
                            outName = raw[1] + ".pdf"
                        else:
                            outName = raw[1]
                    elif raw[0] in ["ENERGY-UNITS", "ENERGYUNITS", "ENERGY UNITS"]:
                        energyUnits = raw[1]
                    elif raw[0] in ["FONT-SIZE", "FONTSIZE", "FONT SIZE"]:
                        try:
                            fontSize = int(raw[1])
                            plt.rcParams.update({"font.size": fontSize})
                        except ValueError:
                            print(
                                "ERROR: Could not read integer for font size on line "
                                + str(lc)
                                + ":\n\t"
                                + line
                            )
                            print("Default will be used...")
                    else:
                        print(
                            "WARNING: Skipping unknown line " + str(lc) + ":\n\t" + line
                        )
    if stateBlock:
        print("WARNING: Final closing '}' is missing.")
    if height == 0:
        print("ERROR: Image height not set! e.g.:\nheight = 8")
        sys.exit("Height not set")
    if width == 0:
        print("ERROR: Image width not set! e.g.:\nwidth = 8")
        sys.exit("Width not set")
    if outName == "":
        print(
            "ERROR: output file name not set! e.g.:\n output-file = energyLevellerExample.pdf"
        )
        sys.exit("Output name not set")

    outDiagram = Diagram(width, height, fontSize, outName)
    outDiagram.energyUnits = energyUnits
    for color in colorsToAdd:
        outDiagram.COLORS[color] = colorsToAdd[color]
    maxColumn = 0
    for state in statesList:
        outDiagram.AddState(state)
        if state.column > maxColumn:
            maxColumn = state.column
    outDiagram.columns = maxColumn + 1

    return outDiagram


######################################################################################################
#          Example printing function. Skip to bottom.
######################################################################################################


def MakeExampleFile() -> None:
    """Create an example input file."""
    output = open("energyLevellerExample.inp", "w")

    output.write(
        "output-file     = energyLevellerExample.pdf\nwidth           = 8\nheight          = 8\nenergy-units    = $\\Delta$E"
        "  kJ/mol\nfont size       = 10\n\n#   This is a comment. Lines that begin with a # are ignored.\n#   "
        "Available colours are those accepted by matplotlib \n\n#   Now begins the states input\n\n#—————–  Pa"
        "th 1 ————————————————\n\n#   Add the first path, all paths are relative to the reactant energies so\n"
        "#   start at zero\n\n{\n    name        = reactants\n    text-colour = black\n    label       = CH$_3"
        "$O$\\cdot$ + X\n    energy      = 0.0\n    labelColour = black\n    linksto     = pre-react1:red, tra"
        "nsition2:#003399, pre-react3:#009933\n    column      = 1\n}\n\n{\n    name        = pre-react1\n    "
        "text-colour = red\n    label       = CH$_3$O$\\cdot$ $\\ldots$ X\n    energy      = -10.5\n    labelC"
        "olour = red\n    linksto     = transition1:red\n    column      = 2\n}\n\n{\n    name        = transi"
        "tion1\n    text-colour = red\n    label       = [CH$_3$O$\\cdot$ $\\ldots$ X]$^{++}$\n    energy     "
        " =    +20.1\n    labelColour = red\n    linksto     = post-react1:red\n    column      = 3\n}\n\n{\n "
        "   name        = post-react1\n    text-colour = red\n    label       = $\\cdot$CH$_2$OH $\\ldots$ X\n"
        "    energy      = -8.2\n    labelColour = red\n    linksto     = products:red\n    column      = 4\n "
        "   legend      = Catalyst 2\n}\n\n#   All the paths in this practical end at the same energy… why?\n\n{\n    name        = products\n    text-colour = black\n    label       =    $\\cdot$CH$_2$OH + X\n  "
        "  energy      = -2.0\n    labelColour = black\n    column      = 5\n}\n#—————–  Path 2 ——————————————"
        "——\n{\n    name        = transition2\n    text-colour = #003399\n    label       = [CH$_3$O$\\cdot$]$"
        "^{++}$\n    energy      = +30.1\n    labelColour = #003399\n    linksto     = products:#003399\n    c"
        "olumn      = 3\n    legend      = Uncatalysed\n}\n\n#—————–  Path 3 ————————————————\n{\n    name    "
        "    = pre-react3\n    text-colour = #009933\n    label       =    CH$_3$O$\\cdot$ $\\ldots$ X\n    en"
        "ergy      = -8.3\n    labelColour = #009933\n    linksto     = transition3:#009933\n    column      ="
        " 2\n    legend      = Catalyst 1\n    labelOffset = 0,1\n    textOffset  = 0,1.4\n}\n\n{\n    name   "
        "     = transition3\n    text-colour = #009933\n    label       = [CH$_3$O$\\cdot$ $\\ldots$ X]$^{++}$"
        "\n    energy      = +25.4\n    labelColour = #009933\n    linksto     = post-react3:#009933\n    colu"
        "mn      = 3\n}\n\n{\n    name        = post-react3\n    text-colour = #009933\n    label       = $\\c"
        "dot$CH$_2$OH $\\ldots$ X\n    energy      = -6.1\n    labelColour = #009933\n    linksto     = produc"
        "ts:#009933\n    column      = 4\n    labelOffset = 0,1\n    textOffset  = 0,1.4\n}\n"
    )

    output.close()
    print("Made example file as 'energyLevellerExample.inp'.")


######################################################################################################
#           Main driver function
######################################################################################################


def main(inp_path: str) -> None:
    """Main function to run the energy leveller."""
    print("o=======================================================o")
    print("         Beginning Energy Level Diagram")
    print("o=======================================================o")
    if len(sys.argv) == 1 and inp_path == "":
        print("\nI need an input file!\n")
        if not os.path.exists("energyLevellerExample.inp"):
            print("\nAn example file will be made.")
            MakeExampleFile()
        sys.exit("No Input file.")

    if len(sys.argv) > 2:
        print("Incorrect arguments. Correct call:\npython EnergyLeveler.py <INPUT FILE>")
        sys.exit("Incorrect Arguments.")
    elif len(sys.argv) == 2:
        diagram = ReadInput(sys.argv[1])
    else:
        diagram = ReadInput(inp_path)

    diagram.MakeLeftRightPoints()
    diagram.Draw()

    print("o=======================================================o")
    print("         Image " + diagram.outputName + " made!")
    print("o=======================================================o")


if __name__ == "__main__":
    main("")
