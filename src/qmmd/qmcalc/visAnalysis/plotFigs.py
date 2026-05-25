import os
from typing import Dict, List, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from qmmd.qmcalc.visAnalysis.plotConfig import (
    barrier_data,
    benchmarking_data,
    charge_list,
    combination_dict,
)

sns.set(context="paper", font_scale=1.5)


def lin_reg(
    m: float,
    c: float,
    r2: float,
    xlimit: Tuple[float, float],
    leg_loc: str,
    font_size: str = "x-small",
) -> None:
    """
    Plot linear regression line and its equation/R2.

    Parameters
    ----------
    m : float
        Slope.
    c : float
        Intercept.
    r2 : float
        R-squared value.
    xlimit : Tuple[float, float]
        X-axis limits.
    leg_loc : str
        Legend location.
    font_size : str, optional
        Font size for the legend.
    """
    x = np.linspace(xlimit[0], xlimit[1], 2)
    y = m * x + c
    plt.plot(
        x, y, "--r", label="$y = {0:.1f}x + {1:.1f}$\n$R^2 = {2:.2f}$".format(m, c, r2)
    )
    plt.legend(loc=leg_loc, fontsize=font_size)
    plt.locator_params(axis="x", nbins=6)


def plot_benchmarking_bar(
    save_path: str = "Benchmarking Statistical Measures.png",
) -> None:
    """
    Plot benchmarking statistical measures.

    Parameters
    ----------
    save_path : str, optional
        Path to save the plot.
    """
    df = pd.DataFrame(benchmarking_data)
    fig = plt.figure(figsize=(8, 5))
    fig.subplots_adjust(top=0.95, bottom=0.15, left=0.1, right=0.98)
    data = df.groupby("Error (kcal/mol)").size()
    pal = sns.dark_palette("purple", len(data), reverse=True)
    rank = data.argsort().argsort()
    ax = sns.barplot(
        x="Method",
        y="Error (kcal/mol)",
        data=df,
        palette=np.array(pal[::-1])[rank],
        alpha=0.95,
    )
    for p in ax.patches:
        ax.annotate(
            format(p.get_height(), ".1f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 8),
            textcoords="offset pixels",
            fontsize=16,
        )
    ax.set(ylabel="Root-Mean-Square Error (kcal/mol)")
    plt.ylim(None, 5)
    plt.savefig(save_path)
    plt.close()


def plot_barriers_bar(
    save_path: str = "Elimination Barrier for Different Mechanisms.png",
) -> None:
    """
    Plot elimination barriers.

    Parameters
    ----------
    save_path : str, optional
        Path to save the plot.
    """
    df = pd.DataFrame(barrier_data)
    fig = plt.figure(figsize=(8, 6))
    fig.subplots_adjust(top=0.97, bottom=0.1, left=0.08, right=0.97)
    ax = sns.barplot(
        x="Inhibitor",
        y="Elimination Barrier (kcal/mol)",
        data=df,
        hue="Mechanism",
        palette="deep",
    )
    for p in ax.patches:
        ax.annotate(
            format(p.get_height(), ".1f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset pixels",
            fontsize=12,
        )
    leg = ax.legend()
    leg.set_title("")
    plt.legend(loc="upper left")
    plt.savefig(save_path)
    plt.close()


def plot_regression_analysis(
    data_path: str = ".", combination: str = "outputs/CombinationI"
) -> None:
    """
    Plot various regression analyses.

    Parameters
    ----------
    data_path : str, optional
        Path to the data directory.
    combination : str, optional
        Combination ID.
    """
    csv_file = os.path.join(
        data_path,
        "QM/Conformational_Analysis/Most_stable_conformers",
        f"{combination.split('/')[-1]}_Properties_Correlation.csv",
    )
    if not os.path.exists(csv_file):
        print(f"Warning: {csv_file} not found. Skipping regression plots.")
        return

    df = pd.read_csv(csv_file, index_col=0)
    prop_dict = combination_dict[combination[-1]]

    # 1. Inhibitor Distortion Energy
    _plot_single_regression(
        df,
        prop_dict["DI"]["Inhibitor"],
        "Inhibitor Distortion Energy (kcal/mol)",
        "Addition Barrier (kcal/mol)",
        r"Inhibitor Distortion Energy (kcal/mol)",
        "$\Delta G^\u2021$ (kcal/mol)",
        f"{combination}/Inhibitor Distortion Energy.png",
    )

    # 2. TS S-C Distance
    _plot_single_regression(
        df,
        prop_dict["SC"],
        "TS S-C Distance (A)",
        "Addition Barrier (kcal/mol)",
        r"Transition State S-C$\beta$ Distance ($\AA$)",
        "$\Delta G^\u2021$ (kcal/mol)",
        f"{combination}/TS S-C Distance.png",
    )

    # 3. Inhibitor LUMO Energy
    _plot_single_regression(
        df,
        prop_dict["LUMO"],
        "Inhibitor LUMO Energy (kcal/mol)",
        "Addition Barrier (kcal/mol)",
        "Inhibitor LUMO Energy (kcal/mol)",
        "$\Delta G^\u2021$ (kcal/mol)",
        f"{combination}/Inhibitor LUMO Energy.png",
    )

    # 4. Beta-Carbon Charges (Multi-plot)
    _plot_charge_correlations(df, prop_dict, combination)


from scipy.stats import linregress


def _plot_single_regression(
    df: pd.DataFrame,
    config_dict: Dict[str, Any],
    x_col: str,
    y_col: str,
    x_label: str,
    y_label: str,
    save_path: str,
) -> None:
    """Internal helper to plot a single regression analysis."""
    x_offset, y_offset, leg, fontsize = (
        config_dict["X-AXIS"],
        config_dict["Y-AXIS"],
        config_dict["LEG"],
        config_dict["FONTSIZE"],
    )
    
    # Calculate regression coefficients dynamically
    mask = ~df[x_col].isna() & ~df[y_col].isna()
    res = linregress(df[x_col][mask], df[y_col][mask])
    m, c, r2 = res.slope, res.intercept, res.rvalue**2

    fig = plt.figure(figsize=(6, 4))
    ax = sns.scatterplot(x=x_col, y=y_col, data=df, hue="Inhibitor", legend=False, s=100)
    ax.set(xlabel=x_label, ylabel=y_label)
    for line in range(1, df.shape[0] + 1):
        ax.text(
            df[x_col][line] + x_offset,
            df[y_col][line] + y_offset,
            df["Inhibitor"][line],
            horizontalalignment="center",
            size="small",
            color="black",
        )
    lin_reg(m, c, r2, plt.xlim(), leg, fontsize)
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()


def _plot_charge_correlations(
    df: pd.DataFrame, prop_dict: Dict[str, Any], combination: str
) -> None:
    """Internal helper to plot multiple charge correlations."""
    fig = plt.figure(figsize=(10, 14))
    fig.subplots_adjust(
        top=0.9, bottom=0.1, left=0.1, right=0.95, wspace=0.3, hspace=0.45
    )
    fig.suptitle(
        r"Correlation between $\beta$-Carbon Charge and Addition Barrier",
        horizontalalignment="center",
        fontsize=16,
        weight="bold",
    )
    for i, model in enumerate(charge_list):
        chosen_dict = prop_dict["Charge"][model]
        x_axis, y_axis, leg, txt_align, fontsize, x_name = (
            chosen_dict["X-AXIS"],
            chosen_dict["Y-AXIS"],
            chosen_dict["LEG"],
            chosen_dict["ALIGN"],
            chosen_dict["FONTSIZE"],
            chosen_dict["X-NAME"],
        )
        
        # Calculate regression coefficients dynamically
        y_col = "Addition Barrier (kcal/mol)"
        mask = ~df[x_name].isna() & ~df[y_col].isna()
        res = linregress(df[x_name][mask], df[y_col][mask])
        m, c, r2 = res.slope, res.intercept, res.rvalue**2

        ax1 = fig.add_subplot(4, 2, i + 1)
        sns.scatterplot(
            x=x_name,
            y=y_col,
            data=df,
            hue="Inhibitor",
            legend=False,
            s=100,
            ax=ax1,
        )
        for line in range(1, df.shape[0] + 1):
            ax1.text(
                df[x_name][line] + x_axis,
                df[y_col][line] + y_axis,
                df["Inhibitor"][line],
                horizontalalignment=txt_align,
                size="small",
                color="black",
            )
        lin_reg(m, c, r2, ax1.get_xlim(), leg, fontsize)
    plt.savefig(f"{combination}/Beta-Carbon Charges.png")
    plt.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Plot various analysis figures.")
    parser.add_argument(
        "--type",
        type=str,
        default="Regression",
        choices=["Bar", "Regression"],
        help="Analysis type.",
    )
    parser.add_argument("--data_path", type=str, default=".", help="Data path.")
    args = parser.parse_args()

    if args.type == "Bar":
        plot_benchmarking_bar()
        plot_barriers_bar()
    elif args.type == "Regression":
        plot_regression_analysis(args.data_path)
