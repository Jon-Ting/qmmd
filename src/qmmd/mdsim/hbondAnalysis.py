import os
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from qmmd.mdsim import config

sns.set(context="paper", font_scale=1.5)


def plot_hbond_analysis(
    md_path: str,
    inhibitor_list: List[int] = config.inhibitor_list,
    num_subplots: int = 6,
    fig_type: str = "Hist",
    save_path: Optional[str] = None,
    show: bool = True,
) -> None:
    """
    Plot H-bond analysis from MD simulations.

    Parameters
    ----------
    md_path : str
        Path to the MD data directory.
    inhibitor_list : List[int], optional
        List of inhibitor IDs to plot.
    num_subplots : int, optional
        Number of subplots.
    fig_type : {"Hist", "Line"}, optional
        Type of plot.
    save_path : str, optional
        Path to save the plot.
    show : bool, optional
        Whether to show the plot.
    """
    plots_width, plots_height = config.SIX_PLOTS_WIDTH, config.SIX_PLOTS_HEIGHT
    num_row = int(num_subplots / 2)
    fig, axes = plt.subplots(
        nrows=num_row,
        ncols=2,
        sharex=True,
        sharey=True,
        figsize=(plots_width, plots_height),
    )

    if fig_type == "Line":
        fig.subplots_adjust(
            top=0.95, bottom=0.06, left=0.08, right=0.97, wspace=0.15, hspace=0.15
        )
        fig.text(0.5, 0.02, "Time (ns)", va="center", ha="center")
        fig.text(
            0.02,
            0.5,
            "Number of H-Bonds",
            va="center",
            ha="center",
            rotation="vertical",
        )
    elif fig_type == "Hist":
        fig.subplots_adjust(
            top=0.95, bottom=0.07, left=0.09, right=0.97, wspace=0.15, hspace=0.15
        )
        fig.text(0.5, 0.02, "Number of H-Bonds", va="center", ha="center")
        fig.text(0.02, 0.5, "Population", va="center", ha="center", rotation="vertical")

    fig.suptitle(
        "Number of H-Bonds throughout MD Simulations of Different Inhibitors",
        horizontalalignment="center",
        fontsize=14,
        weight="bold",
    )

    subplot_index = 0
    for i, inhibitor in enumerate(inhibitor_list):
        combined_df = pd.DataFrame(
            list(np.arange(0.005, 100.005, 0.005)), columns=["Time (ns)"]
        )
        col_label = ["Time (ns)"]
        label_list, run_type_list = [], ["eq", "rep1", "rep2"]

        for j, run_type in enumerate(run_type_list):
            data_dir = os.path.join(md_path, "Overall_Analysis", str(inhibitor))
            for k in ["A", "B"]:
                dat_file = f"{run_type}_{k}_nhbvtime.dat"
                dat_name = f"{run_type.capitalize()} {inhibitor}{k}"
                dat_path = os.path.join(data_dir, dat_file)
                if os.path.exists(dat_path):
                    df = pd.read_csv(dat_path, index_col=0, sep=r"\s+")
                    df.reset_index(drop=True, inplace=True)
                    combined_df = pd.concat(
                        [combined_df, df], axis=1, ignore_index=True
                    )
                    label_list.append(dat_name)

        if len(label_list) > 0:
            combined_df.columns = col_label + label_list
            subplot_index += 1
            ax = plt.subplot(num_row, 2, subplot_index)
            if fig_type == "Line":
                combined_df.plot(
                    x="Time (ns)",
                    y=label_list,
                    kind="line",
                    ax=ax,
                    lw=0.1,
                    linestyle=":",
                )
                ax.xaxis.label.set_visible(False)
            elif fig_type == "Hist":
                combined_df.plot.bar(x="Time (ns)", y=label_list, ax=ax)
                ax.yaxis.label.set_visible(False)

            ax.tick_params(
                top=False,
                bottom=True,
                left=True,
                right=False,
                labelleft=True,
                labelbottom=True,
            )
            leg = ax.legend(loc="upper right", fontsize="small")
            plt.setp(leg.get_lines(), linewidth=4)

    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Plot H-bond analysis from MD simulations.")
    parser.add_argument("md_path", type=str, help="Path to the MD data directory.")
    parser.add_argument(
        "--type", type=str, default="Hist", choices=["Hist", "Line"], help="Type of plot."
    )
    args = parser.parse_args()

    plot_hbond_analysis(args.md_path, fig_type=args.type)
