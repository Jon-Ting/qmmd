from math import log, exp
from typing import Optional, Tuple

# Eyring-Polanyi equation: k_off = (kappa*kB*T/h) * exp(-dGrevbarr/(R*T))
kappa = 1  # Transmission coefficient, reflects fraction of flux through TSS proceeds to P without recrossing TSS
# (Assumes that the no-recrossing assumption of TST holds perfectly)
kB = 1.380649 * 10 ** -23  # Boltzmann constant, relates avg relative KE of particles (g) with T [J/K]
h = 6.62607015 * 10 ** -34  # Planck's constant, relates photon E to its f, quantum of electromagnetic action [Js]
R = 8.314462618  # Ideal gas constant, equivalent to kB, but expressed in per mole [J/molK]
cal2J = 4.184


def energyUnitsConversion(E_kcal: Optional[float], E_kJ: Optional[float], verbose: bool = False) -> Tuple[float, float]:
    """Convert between kcal and kJ.

    Parameters
    ----------
    E_kcal : float, optional
        Energy (kcal).
    E_kJ : float, optional
        Energy (kJ).
    verbose : bool
        Whether to display details.

    Returns
    -------
    E_kcal : float
        Energy (kcal).
    E_kJ : float
        Energy (kJ).

    Examples
    --------
    >>> energyUnitsConversion(100, None, True)
    """
    if E_kcal is None:  # If no value is provided
        if E_kJ is None:
            raise ValueError("Both E_kcal & E_kJ are missing! Provide one.")
        E_kcal = E_kJ/cal2J
    elif E_kJ is None:
        E_kJ = E_kcal*cal2J
    else:
        # Both provided, check consistency or prioritize? Legacy code raised error.
        # But legacy code actually had a bug where if both provided it raised exception "missing".
        raise ValueError("Both E_kcal & E_kJ provided! Provide only one.")
    if verbose:
        print("E_kcal =", E_kcal, "kcal/mol, E_kJ =", E_kJ, "kJ/mol")
    return E_kcal, E_kJ


def eyringEquation(k: Optional[float], dGbarr: Optional[float], T: float, verbose: bool = False) -> Tuple[float, float]:
    """Calculate off rate or elimination barrier from each other at a specific temperature using Eyring-Polanyi equation.

    Parameters
    ----------
    k : float, optional
        Off rate (s^-1).
    dGbarr : float, optional
        Elimination barrier (kcal/mol).
    T : float
        Temperature (K)
    verbose : bool
        Whether to display details.

    Returns
    -------
    k : float
        Off rate (s^-1).
    dGbarr : float
        Elimination (kcal/mol).

    Examples
    --------
    >>> eyringEquation(None, 4.5, 300, True)
    """
    if k is None:  # If no value is provided
        if dGbarr is None:
            raise ValueError("Both k & dGbarr are missing! Provide one.")
        if verbose:
            print("\n--------------------------------------\n\n# Converting energy unit...")
        _, dGbarr_kJ = energyUnitsConversion(dGbarr, None)  # Convert to kJ/mol
        dGbarr_J = dGbarr_kJ * 1000  # Convert to J/mol
        k = (kappa*kB*T/h) * exp(-dGbarr_J/(R*T))  # Calculate off rate
    elif dGbarr is None:
        dGbarr_J = -R*T*log(h*k/(kappa*kB*T))
        dGbarr = dGbarr_J / (cal2J*1000)
    else:
        raise ValueError("Both k & dGbarr provided! Provide only one.")
    
    if verbose:
        print("\n--------------------------------------\n\n# Using Eyring-Polanyi equation...")
        print("At T =", T, "K, k =", k, "s^-1, dGbarr =", dGbarr, "kcal/mol")
    return k, dGbarr


def timeUnitsConversion(k: Optional[float], t_half: Optional[float], RT: Optional[float], verbose: bool = False) -> Tuple[float, float, float]:
    """Interconvert between off rate (s^-1), half life (s), and residence time (s).

    Parameters
    ----------
    k : float, optional
        Off rate (s^-1).
    t_half : float, optional
        Half life (s).
    RT : float, optional
        Residence time (s)
    verbose : bool
        Whether to display details.

    Returns
    -------
    k : float
        Off rate (s^-1).
    t_half : float
        Half life (s).
    RT : float
        Residence time (s).

    Examples
    --------
    >>> timeUnitsConversion(None, 30.8, None, True)
    """
    if k is not None:  # If value is provided
        t_half, RT = log(2)/k, 1/k
    elif t_half is not None:
        k, RT = log(2)/t_half, t_half/log(2)
    elif RT is not None:
        k, t_half = 1/RT, RT*log(2)
    else:
        raise ValueError("All parameters are missing! Provide one.")
    if verbose:
        print("\n--------------------------------------\n\n# Kinetic parameters conversion...")
        print("k =", k, "s^-1, t_half =", t_half, "s, RT =", RT, "s")
    return k, t_half, RT


if __name__ == "__main__":
    T = 310.15  # Temperature, assumes RT at the moment [K]
    k, dGbarr = None, 30.8  # off rate [s^-1], elimination barrier [kcal/mol]
    t_half, RT = None, None  # half_life [s], residence time [s]

    k, dGbarr = eyringEquation(k, dGbarr, T, True)
    k, t_half, RT = timeUnitsConversion(k, t_half, RT, True)

