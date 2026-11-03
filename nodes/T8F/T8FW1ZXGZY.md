---
tag: T8FW1ZXGZY
kind: definition
name: Thermodynamic potential
msc: [80A10, 80A05]
defines: MKZW03Q590
uses: [F6JVQ12X43, SPY89W0RJ7, T8J5XRYBZZ, 3W28H76A82, ZQYMWVT1TT]
sources:
  - url: https://en.wikipedia.org/wiki/Thermodynamic_potential
---

## Definition

Consider a simple thermodynamic system with [[internal energy|F6JVQ12X43]] $U$ given as a function $U(S, V, N_1, \dots, N_r)$ of its [[entropy|SPY89W0RJ7]] $S$, volume $V$ and amounts of substance $N_1, \dots, N_r$.
Write $x_0 = S$, $x_1 = V$ and $x_{i+1} = N_i$, and let $y_j = \partial U / \partial x_j$ be the [[conjugate variable|3W28H76A82]] of $x_j$; thus $y_0 = T$, $y_1 = -p$ and $y_{i+1} = \mu_i$.
Here $T$ is the temperature, $p$ the pressure and $\mu_i$ the chemical potential of substance $i$.
Let $J$ be a nonempty proper subset of $\set{0, 1, \dots, r+1}$, and consider the [[state function|T8J5XRYBZZ]]
$$U[J] = U - \sum_{j \in J} x_j \, y_j.$$
Write it as a function of the variables $y_j$ for $j \in J$ and $x_j$ for $j \notin J$.
A *thermodynamic potential* of the system is $U$ itself or such a function $U[J]$.
These variables are the *natural variables* of the potential.

## Remarks

The function $U[J]$ is the [[Legendre transform|ZQYMWVT1TT]] of $U$ in the variables $x_j$ for $j \in J$, up to sign.
Its differential is $dU[J] = -\sum_{j \in J} x_j \, dy_j + \sum_{j \notin J} y_j \, dx_j$.
Example: $J = \set{0}$ gives the Helmholtz free energy $F = U - TS$ with natural variables $T, V, N_1, \dots, N_r$, and $dF = -S \, dT - p \, dV + \sum_i \mu_i \, dN_i$.
The other standard choices give the enthalpy $H = U + pV$, the Gibbs free energy $G = U - TS + pV$ and the grand potential $U - TS - \mu N$.
Non-example: for a monatomic ideal gas, $U = \frac{3}{2} N k T$ written as a function of $T, V, N$ is not a thermodynamic potential.
It does not depend on $V$ at all, so the pressure cannot be recovered from it.

## Explanations

### L1 human

A thermodynamic potential is an energy-like function whose derivatives in the right variables give all other quantities.
The trick is to choose the variables well: the same quantity written in the wrong variables loses information.
