charge_list = ["Mulliken", "NBO", "MK", "Hirshfeld", "CM5", "QTAIM", "ChelpG", "Omega"]
charge_list_A = ["QTAIM", "Omega"]
charge_list_B = ["Mulliken", "NBO", "MK", "Hirshfeld", "CM5", "ChelpG"]
DI_list = ["Thiolate", "Inhibitor", "Activation", "Interaction"]

benchmarking_data = {"Measure": ["RMSD", "RMSD", "RMSD", "RMSD", "RMSD", "RMSD", "RMSD", "RMSD", "RMSD", "RMSD"],
                     "Method": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
                     "Error (kcal/mol)": [0.6, 1.0, 4.5, 2.1, 2.6, 1.8, 3.6, 0.5, 1.5, 0.4]}

barrier_data = {"Mechanism": ["Base-Catalysed Proton Abstraction", "Base-Catalysed Proton Abstraction", "Base-Catalysed Proton Abstraction", "Base-Catalysed Proton Abstraction", "Base-Catalysed Proton Abstraction",
                              "4-Membered Intramolecular Proton Transfer", "4-Membered Intramolecular Proton Transfer", "4-Membered Intramolecular Proton Transfer", "4-Membered Intramolecular Proton Transfer", "4-Membered Intramolecular Proton Transfer",
                              "6-Membered Intramolecular Proton Transfer", "6-Membered Intramolecular Proton Transfer", "6-Membered Intramolecular Proton Transfer", "6-Membered Intramolecular Proton Transfer", "6-Membered Intramolecular Proton Transfer"],
                "Inhibitor": ["1", "3", "47", "5", "9",
                           "1", "3", "47", "5", "9",
                           "1", "3", "47", "5", "9"],
                "Elimination Barrier (kcal/mol)": [11.0-(-5.9), 16.0-(-3.9), 13.9-(-4.0), 20.0-(-10.8), 14.2-(-5.5),
                                                   43.4-(-5.9), 42.7-(-3.9), 45.2-(-4.0), 52.0-(-10.8), 47.3-(-5.5),
                                                   24.9-(-5.9), 26.0-(-3.9), 26.3-(-4.0), 28.1-(-10.8), 30.0-(-5.5)]}

combination_dict = {
    "I": {
        "SC": {
            "X-AXIS": 0,
            "Y-AXIS": 0.4,
            "LEG": "upper right",
            "ALIGN": "center",
            "FONTSIZE": "medium",
            "X-NAME": r"TS S-C Distance ($\AA$)"
        },

        "LUMO": {
            "X-AXIS": 0,
            "Y-AXIS": 0.4,
            "LEG": "upper left",
            "ALIGN": "center",
            "FONTSIZE": "medium",
            "X-NAME": "Inhibitor LUMO Energy (kcal/mol)"
        },

        "Charge": {
            "Mulliken": {
                "X-AXIS": -0.03,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "small",
                "X-NAME": "Mulliken Charge (e)"
            },
            "NBO": {
                "X-AXIS": -0.01,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "small",
                "X-NAME": "NBO Charge (e)"
            },
            "MK": {
                "X-AXIS": 0.02,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "left",
                "FONTSIZE": "small",
                "X-NAME": "Merz-Kollman Charge (e)"
            },
            "Hirshfeld": {
                "X-AXIS": 0.005,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "left",
                "FONTSIZE": "x-small",
                "X-NAME": "Hirshfeld Charge (e)"
            },
            "CM5": {
                "X-AXIS": -0.005,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "small",
                "X-NAME": "CM5 Charge (e)"
            },
            "QTAIM": {
                "X-AXIS": -0.003,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "small",
                "X-NAME": "QTAIM Charge (e)"
            },
            "ChelpG": {
                "X-AXIS": -0.004,
                "Y-AXIS": 0.2,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "small",
                "X-NAME": "ChelpG Charge (e)"
            },
            "Omega": {
                "X-AXIS": -0.4,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "small",
                "X-NAME": "Electrophilicity Index"
            },
        },
        "DI": {
            "Thiolate": {
                "X-AXIS": -0.02,
                "Y-AXIS": 0,
                "LEG": "upper left",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "Thiolate Distortion Energy (kcal/mol)"
            },
            "Inhibitor": {
                "X-AXIS": -0.5,
                "Y-AXIS": 0.3,
                # "X-AXIS": -1.0,
                # "Y-AXIS": 0.7,
                "LEG": "best",
                "ALIGN": "left",
                "FONTSIZE": "medium",
                # "FONTSIZE": "x-small",
                "X-NAME": "Inhibitor Distortion Energy (kcal/mol)"
            },
            "Activation": {
                "X-AXIS": -0.3,
                "Y-AXIS": 0,
                "LEG": "upper left",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "Activation Energy (kcal/mol)"
            },
            "Interaction": {
                "X-AXIS": 0.18,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "left",
                "FONTSIZE": "x-small",
                "X-NAME": "Interaction Energy (kcal/mol)"
            },
        }
    },
    "G": {
        "LUMO": {
            "X-AXIS": 0,
            "Y-AXIS": 0.4,
            "LEG": "upper left",
            "ALIGN": "center",
            "FONTSIZE": "medium",
            "X-NAME": "Inhibitor LUMO Energy (kcal/mol)"
        },

        "Charge": {
            "Mulliken": {
                "X-AXIS": -0.04,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "Mulliken Charge (e)"
            },
            "NBO": {
                "X-AXIS": -0.01,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "NBO Charge (e)"
            },
            "MK": {
                "X-AXIS": 0.02,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "left",
                "FONTSIZE": "x-small",
                "X-NAME": "Merz-Kollman Charge (e)"
            },
            "Hirshfeld": {
                "X-AXIS": 0.004,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "left",
                "FONTSIZE": "x-small",
                "X-NAME": "Hirshfeld Charge (e)"
            },
            "CM5": {
                "X-AXIS": -0.005,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "CM5 Charge (e)"
            },
            "QTAIM": {
                "X-AXIS": -0.004,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "QTAIM Charge (e)"
            },
            "ChelpG": {
                "X-AXIS": -0.007,
                "Y-AXIS": 0.18,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "ChelpG Charge (e)"
            },
            "Omega": {
                "X-AXIS": -0.3,
                "Y-AXIS": 0,
                "LEG": "upper right",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "Electrophilicity Index"
            },
        },
        "DI": {
            "Thiolate": {
                "X-AXIS": -0.02,
                "Y-AXIS": 0,
                "LEG": "upper left",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "Thiolate Distortion Energy (kcal/mol)"
            },
            "Inhibitor": {
                "X-AXIS": -1.4,
                "Y-AXIS": 0.55,
                "LEG": "best",
                "ALIGN": "left",
                "FONTSIZE": "x-small",
                "X-NAME": "Inhibitor Distortion Energy (kcal/mol)"
            },
            "Activation": {
                "X-AXIS": -0.35,
                "Y-AXIS": 0.24,
                "LEG": "upper left",
                "ALIGN": "right",
                "FONTSIZE": "x-small",
                "X-NAME": "Activation Energy (kcal/mol)"
            },
            "Interaction": {
                "X-AXIS": 0.1,
                "Y-AXIS": 0,
                "LEG": "lower left",
                "ALIGN": "left",
                "FONTSIZE": "x-small",
                "X-NAME": "Interaction Energy (kcal/mol)"
            },
        }
    },
}
