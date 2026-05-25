import os
import subprocess
from typing import Optional


def submit_jobs(
    target_dir: str, filename_pattern: str = "*.sh", verbose: bool = False
) -> None:
    """
    Recursively find and submit jobs to the scheduler.
    Equivalent to the legacy gsub.sh script.

    Parameters
    ----------
    target_dir : str
        Directory to start searching for job scripts.
    filename_pattern : str
        Glob pattern for job scripts.
    verbose : bool
        Whether to print detailed output.
    """
    if verbose:
        print(f"Looking for {filename_pattern} files to submit to Scheduler...")
        print("-" * 50)

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(filename_pattern.replace("*", "")):
                file_path = os.path.join(root, file)
                if verbose:
                    print(f"Found {file_path}, processing...")

                # Equivalent to dos2unix: ensure LF line endings
                with open(file_path, "rb") as f:
                    content = f.read()
                with open(file_path, "wb") as f:
                    f.write(content.replace(b"\r\n", b"\n"))

                if verbose:
                    print("Submitting...")

                try:
                    # Attempt to call qsub
                    result = subprocess.run(
                        ["qsub", file_path], capture_output=True, text=True, check=True
                    )
                    if verbose:
                        print(f"Success: {result.stdout.strip()}")
                except subprocess.CalledProcessError as e:
                    print(f"Error submitting {file_path}: {e.stderr.strip()}")
                except FileNotFoundError:
                    print(
                        "Error: 'qsub' command not found. Are you on a system with a scheduler?"
                    )
                    return

    if verbose:
        print("\nDone!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Submit jobs to the scheduler.")
    parser.add_argument("target_dir", type=str, help="Directory to search for job scripts.")
    parser.add_argument("--pattern", type=str, default="*.sh", help="Filename pattern.")
    parser.add_argument("--verbose", action="store_true", help="Verbose output.")
    args = parser.parse_args()

    submit_jobs(args.target_dir, args.pattern, args.verbose)
