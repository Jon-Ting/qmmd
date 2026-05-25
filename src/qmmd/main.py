import argparse
import sys
from qmmd.datasets import genExampleXYZs
from qmmd.qmcalc.genScripts import genAllScripts
from qmmd.qmcalc.tabulate import writeToExcel
from qmmd.qmcalc.unitConv import energyUnitsConversion, eyringEquation, timeUnitsConversion
from qmmd.qmcalc.jobSubmit import submit_jobs


def main():
    parser = argparse.ArgumentParser(description="QMMD: Automate QM and MD for covalent drugs.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command to run")

    # init-struct (example XYZ generation)
    parser_init = subparsers.add_parser("init-struct", help="Generate example XYZ files")
    parser_init.add_argument("out_dir", type=str, help="Directory to store example XYZ files")

    # gen-scripts
    parser_gen = subparsers.add_parser("gen-scripts", help="Generate Gaussian input and HPC job scripts")
    parser_gen.add_argument("inp_dir", type=str, help="Directory containing molecule directories with XYZ files")
    parser_gen.add_argument("--verbose", action="store_true", help="Enable verbose output")

    # submit-jobs
    parser_sub = subparsers.add_parser("submit-jobs", help="Recursively submit job scripts to the scheduler")
    parser_sub.add_argument("target_dir", type=str, help="Directory to search for job scripts")
    parser_sub.add_argument("--pattern", type=str, default="*.sh", help="Filename pattern for job scripts")
    parser_sub.add_argument("--verbose", action="store_true", help="Enable verbose output")

    # tabulate
    parser_tab = subparsers.add_parser("tabulate", help="Tabulate Gaussian output values to Excel")
    parser_tab.add_argument("out_dir", type=str, help="Directory containing Gaussian output files")
    parser_tab.add_argument("--verbose", action="store_true", help="Enable verbose output")

    # unit-conv
    parser_conv = subparsers.add_parser("unit-conv", help="Interconvert energy and kinetic units")
    parser_conv.add_argument("--kcal", type=float, help="Energy in kcal/mol")
    parser_conv.add_argument("--kj", type=float, help="Energy in kJ/mol")
    parser_conv.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    if args.command == "init-struct":
        genExampleXYZs(args.out_dir)
        print(f"Example XYZ files generated in {args.out_dir}")
    elif args.command == "gen-scripts":
        genAllScripts(args.inp_dir, verbose=args.verbose)
    elif args.command == "submit-jobs":
        submit_jobs(args.target_dir, filename_pattern=args.pattern, verbose=args.verbose)
    elif args.command == "tabulate":
        writeToExcel(args.out_dir, verbose=args.verbose)
    elif args.command == "unit-conv":
        if args.kcal is not None or args.kj is not None:
            energyUnitsConversion(args.kcal, args.kj, verbose=args.verbose)
        else:
            print("Please provide either --kcal or --kj")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
