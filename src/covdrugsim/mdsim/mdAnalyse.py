# TODO: Create and add other functions to this file


def sumCharge(
    inpFileName: str, outFileName: str, correction: float = 0.002, verbose: bool = False
) -> None:
    """
    Sum charges from a file and apply a correction factor.

    Parameters
    ----------
    inpFileName : str
        Path to the input file containing charges.
    outFileName : str
        Path to the output file to write corrected charges.
    correction : float, optional
        Correction factor to add to each charge (default is 0.002).
        This accounts for rounding errors in some charge generation tools.
    verbose : bool, optional
        Whether to print the total charges.
    """
    totalCharge = 0.0
    with open(inpFileName, "r") as inpfile, open(outFileName, "w") as outfile:
        for chargeStr in inpfile:
            try:
                charge = float(chargeStr) + correction
                totalCharge += charge
                if charge >= 0:
                    outfile.write(" {:3f}\n".format(charge))
                else:
                    outfile.write("{:3f}\n".format(charge))
            except ValueError:
                print("{} is not a number!".format(chargeStr))
    if verbose:
        print("Total charges: {0}".format(totalCharge))


if __name__ == "__main__":
    sumCharge("charges.txt", "totCharge.txt", verbose=True)
