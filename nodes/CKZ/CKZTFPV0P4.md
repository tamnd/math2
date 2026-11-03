---
tag: CKZTFPV0P4
kind: definition
name: Virial expansion
msc: [80A10, 82D05, 82B05]
defines: QMJ04KSQ59
uses: [YPT3SJSS5T, N7R0H2VNDJ, 0VP56B4EMX]
sources:
  - url: https://en.wikipedia.org/wiki/Virial_expansion
---

## Definition

Let a gas at temperature $T$ have molar volume $V_m$ and pressure $p$, and let $R$ be the molar gas constant.
The *virial expansion* of its [[equation of state|YPT3SJSS5T]] is the [[power series|0VP56B4EMX]] in $1/V_m$
$$\frac{p V_m}{R T} = 1 + \frac{B(T)}{V_m} + \frac{C(T)}{V_m^2} + \frac{D(T)}{V_m^3} + \cdots,$$
assumed to converge for small density $1/V_m$.
The left side is the compressibility factor $Z$.
The functions $B$, $C$, $D$, ... of $T$ alone are the second, third, fourth, ... *virial coefficients*.

## Remarks

The first term $1$ is the [[ideal gas|N7R0H2VNDJ]]; keeping it alone gives $pV_m = RT$.
In statistical mechanics, for a classical gas of molecules with a spherical pair potential $u(r)$, Boltzmann constant $k$ and Avogadro constant $N_A$,
$$B(T) = -2\pi N_A \int_0^\infty \left( e^{-u(r)/(kT)} - 1 \right) r^2 \, dr.$$
An expansion in the pressure, $Z = 1 + B'(T)\,p + C'(T)\,p^2 + \cdots$, is also used, with $B' = B/(RT)$.

Example: for the van der Waals equation, $Z = \frac{V_m}{V_m - b} - \frac{a}{R T V_m} = 1 + \left( b - \frac{a}{RT} \right) \frac{1}{V_m} + \frac{b^2}{V_m^2} + \cdots$, using the geometric series in $b/V_m$.
So $B(T) = b - a/(RT)$, which is negative at low temperature and positive at high temperature, and $C = b^2$.

Non-example: a Taylor expansion of $p$ in powers of $T - T_0$ at fixed density is not a virial expansion.
Its coefficients depend on the density and not on the temperature alone.
