"""This is the example_solver.py script for solving 1D hydraulics."""
import math as m


def calc_discharge(b, h, m_bank, S, k_st=None, n_m=None, D_90=None):
    """
    Calulate discharge in SI units. Provide one of the optional parameters k_st, n_m, or D_90.

    Arguments:
        b (float): width (m)
        h (float): depth (m)
        m_bank (float): bank slope (-)
        S (float): slope (-)
        k_st (float): Strickler roughness (optional)
        n_m (float): Manning roughness (optional)
        D_90 (float): D90 for roughness (optional)

    Returns:
        ``float`` of discharge in CMS
    """
    if n_m:
        k_st = 1 / n_m
    elif D_90:
        k_st = 26 / (D_90 ** (1/6))
    A = h * (b + h * m_bank)
    P = b + 2 * h * (m_bank ** 2 + 1) ** 0.5
    return k_st * m.sqrt(S) * (A / P) ** (2 / 3) * A


def interpolate_h(Q, b, S0, m_bank=1.0, n_m=0.04, prec=0.001, **kwargs):
    """
    Inverse calculation of normal water depth for a given discharge and channel geometry
    uses Raphson-Newton Algorithm

    Arguments:
        Q (float): of target discharge in (m3/s)
        b (float): of channel base width in (m)
        S0 (float): of channel (energy) slope is (m/m)
        m_bank (float): of channel bank inclination (dimensionless), default=1.0
        n_m (float): of Manning's n, default=0.04
        prec (float): of result precision (don't be too picky)
        kst (float): of Strickler value supersedes n_m
        d90 (float): of surface grain size supersedes n_m

    Returns:
        ``float``  of flow depth in M
    """

    # parse keyword arguments
    for k in kwargs.items():
        if "kst" in k[0]:
            try:
                n_m = 1 / float(k[1])
            except TypeError:
                print("ERROR: Provided kst value (%s) is not a number." % str(k[1]))
                return None
            except ZeroDivisionError:
                print("ERROR: Provided kst value must not be zero.")
                return None
        if "d90" in k[0]:
            try:
                n_m = float(k[1])**(1/6) / 26.0
            except TypeError:
                print("ERROR: Provided kst value (%s) is not a number." % str(k[1]))
                return None

    # use  for interpolation of flow depth
    stability_exit = int(1/prec)  # no iteration should need 10000 steps...
    stability_counter = 0
    h_n = 10.0 * prec
    err = 1.0
    while err > prec:
        A = b * h_n + m_bank * h_n ** 2
        P = b + 2 * h_n * m.sqrt(m_bank ** 2 + 1)
        Qk = A ** (5 / 3) * m.sqrt(S0) / (n_m * P ** (2 / 3))

        dA_dh = b + 2 * m_bank * h_n  # correction factor for flow cross section
        dP_dh = 2 * m.sqrt(m_bank ** 2 + 1)  # correction factor for wetted perimeter

        _f = n_m * Q * P ** (2 / 3) - A ** (5 / 3) * m.sqrt(S0)  # correction factor
        df_dh = 2 / 3 * n_m * Q * P ** (-1 / 3) * dP_dh - 5 / 3 * A ** (2 / 3) * m.sqrt(S0) * dA_dh
        h_n = abs(h_n - _f / df_dh)  # compute new value for flow depth

        err = abs(Q - Qk) / Q

        stability_counter += 1
        if stability_counter > stability_exit:
            print("WARNING: No convergence reached. Interpolation break.")
            h_n = None
            break
    msg0 = "\nInterpolated water depth: %0.5f m." % h_n
    msg1 = "\nTarget discharge: %0.5f m3/s." % Q
    msg2 = "\nYielded discharge: %0.5f m3/s." % Qk
    print("Finished interpolation." + msg0, msg1, msg2)
    return h_n


if __name__ == '__main__':
    # -- START MODIFICATION BLOCK: MODIFY INPUT PARAMETERS HERE
    # Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    h_init = 1.55   # flow depth for discharge calculation (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_m = 1 / k_st  # Manning's n
    S_0 = 0.005     # channel slope
    # -- END MODIFICATION BLOCK

    Q = calc_discharge(b, h_init, m_bank, S_0, k_st=k_st)
    print("Calculated discharge = %0.3f m3/s for flow depth = %.3f m." % (Q, h_init))

    # call the solver with user-defined channel geometry and discharge
    h_n = interpolate_h(Q, b, n_m=n_m, m_bank=m_bank, S0=S_0, prec=10**-5)
