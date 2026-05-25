import json
import os
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from qmmd.mdsim import config

sns.set(context="talk", font_scale=0.8)


def analyse_base_interaction(
    md_path: str,
    inhibitor: int = 1,
    system_type: str = "cov",
    replicates: List[int] = [1, 2],
    dist_thresh: float = 10,
    sort_dict: bool = False,
    num_subplots: int = 6,
    save_dir: Optional[str] = None,
    show: bool = True,
) -> None:
    """
    Analyse base interactions from MD simulations.

    Parameters
    ----------
    md_path : str
        Path to the MD data directory.
    inhibitor : int, optional
        Inhibitor ID.
    system_type : {"cov", "noncov"}, optional
        Type of system.
    replicates : List[int], optional
        List of replicates to analyse.
    dist_thresh : float, optional
        Distance threshold for base interactions.
    sort_dict : bool, optional
        Whether to sort and store the residue data.
    num_subplots : int, optional
        Number of subplots.
    save_dir : str, optional
        Directory to save the plots.
    show : bool, optional
        Whether to show the plot.
    """
    curr_dir = os.getcwd()
    for i in replicates:
        # Update data paths
        data_dir = os.path.join(
            md_path, str(inhibitor), "MD", system_type, f"Rep{i}", "analysis", "base"
        )
        system_dir = os.path.join(curr_dir, str(inhibitor), system_type)
        store_dir = os.path.join(system_dir, f"within_{dist_thresh}A")

        if not os.path.exists(system_dir):
            os.makedirs(system_dir)

        if sort_dict:
            # Sorting and storing the residue data
            within_dist_dict = {"arg": [], "glu": [], "asp": [], "his": [], "lys": []}
            res_dict_path = os.path.join(system_dir, "residue_dict.txt")
            if not os.path.exists(res_dict_path):
                residue_dict = {
                    "arg": [],
                    "glu": [],
                    "asp": [],
                    "his": [],
                    "lys": [],
                    "ligand": [],
                }
            else:
                with open(res_dict_path, "r") as f:
                    residue_dict = json.load(f)
                # Empty the .dat files
                for residue in residue_dict.keys():
                    list_path = os.path.join(system_dir, f"{residue}_list.txt")
                    if os.path.exists(list_path):
                        open(list_path, "w").close()

            # Sort out all .dat files
            if os.path.exists(data_dir):
                for filename in os.listdir(data_dir):
                    if ".dat" not in filename:
                        continue
                    for residue in residue_dict.keys():
                        if residue in filename:
                            if not os.path.exists(res_dict_path):
                                list_path = os.path.join(system_dir, f"{residue}_list.txt")
                                with open(list_path, "a+") as res_list_file:
                                    res_list_file.write(f"{filename}\n")
                                    residue_dict[residue].append(filename)

                            dat_path = os.path.join(data_dir, filename)
                            if not os.path.exists(store_dir):
                                os.makedirs(store_dir)

                            close_list_path = os.path.join(store_dir, "close_res_list.txt")
                            with open(dat_path, "r") as dist_data:
                                with open(close_list_path, "a+") as close_res_file:
                                    for line_entry in dist_data:
                                        try:
                                            distance = float(line_entry.split()[-1])
                                            if distance <= dist_thresh:
                                                within_dist_dict[residue].append(filename)
                                                close_res_file.write(f"{filename}\n")
                                                break
                                        except (ValueError, IndexError):
                                            continue

                with open(os.path.join(store_dir, "within_dist_dict.txt"), "w") as f:
                    json.dump(within_dist_dict, f, indent=4)
                if not os.path.exists(res_dict_path):
                    with open(res_dict_path, "w") as f:
                        json.dump(residue_dict, f, indent=4)

        # Analyse each residue
        within_dist_path = os.path.join(store_dir, "within_dist_dict.txt")
        res_dict_path = os.path.join(system_dir, "residue_dict.txt")

        if not os.path.exists(within_dist_path) or not os.path.exists(res_dict_path):
            print(f"Missing required dict files for Rep {i}. Skipping analysis.")
            continue

        with open(within_dist_path, "r") as f:
            within_dist_dict = json.load(f)
        with open(res_dict_path, "r") as f:
            residue_dict = json.load(f)

        chosen_dict = within_dist_dict
        target_H = "CYS481" if "non" in system_type else "Ca"

        fig = plt.figure(figsize=(config.SINGLE_PLOT_WIDTH, config.SINGLE_PLOT_HEIGHT))
        fig.subplots_adjust(
            top=0.97, bottom=0.15, left=0.14, right=0.96, wspace=0.15, hspace=0.15
        )
        fig.text(
            0.02, 0.5, r"Distance ($\AA$)", va="center", ha="center", rotation="vertical"
        )

        for residue in ["arg"]:
            label_list = []
            combined_df = pd.DataFrame(
                list(np.arange(0.000, 100.000, 0.005)), columns=["Time (ns)"]
            )
            if residue not in chosen_dict:
                continue

            for dat_file in chosen_dict[residue]:
                resname = dat_file.split(".")[0].split("_")[-1].upper()
                dat_path = os.path.join(data_dir, dat_file)
                if os.path.exists(dat_path):
                    df = pd.read_csv(dat_path, index_col=0, sep=r"\s+")
                    df.columns = [resname]
                    combined_df = pd.concat([combined_df, df], axis=1)
                    label_list.append(resname)

            if combined_df.shape[1] > 1:
                combined_df.plot(
                    x="Time (ns)",
                    y=label_list,
                    kind="line",
                    ax=plt.gca(),
                    lw=0.3,
                    linestyle=":",
                )
                leg = plt.legend(loc="upper right", fontsize="small")
                plt.setp(leg.get_lines(), linewidth=4)

        if save_dir:
            save_path = os.path.join(save_dir, f"Distance_Arg_Rep_{i}.png")
            plt.savefig(save_path)
        if show:
            plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyse base interactions from MD simulations.")
    parser.add_argument("md_path", type=str, help="Path to the MD data directory.")
    parser.add_argument("--inhibitor", type=int, default=1, help="Inhibitor ID.")
    parser.add_argument("--system", type=str, default="cov", help="System type.")
    parser.add_argument("--sort", action="store_true", help="Sort residue data.")
    args = parser.parse_args()

    analyse_base_interaction(
        args.md_path, inhibitor=args.inhibitor, system_type=args.system, sort_dict=args.sort
    )
