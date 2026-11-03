---
tag: YD04KYV1YR
kind: statement
role: theorem
name: Kolmogorov four-fifths law
msc: [76F05]
uses: [VY307F8Z0S, YQ2KYDWRD0, 18KXZHVF4M, ZSP670B8RR, NM5Q4845Z4]
about: [VY307F8Z0S, YQ2KYDWRD0]
sources:
  - url: https://en.wikipedia.org/wiki/Turbulence
---

## Statement

Consider statistically stationary, homogeneous and isotropic [[turbulence|VY307F8Z0S]] governed by the incompressible [[Navier–Stokes equations|18KXZHVF4M]].
Let $\nu$ be the kinematic [[viscosity|NM5Q4845Z4]], and let a force act at large scales of size about $L$.
Let $\varepsilon$ be the mean rate of energy dissipation per unit mass.
Let $\delta u(r) = (\mathbf{u}(\mathbf{x} + \mathbf{r}) - \mathbf{u}(\mathbf{x})) \cdot \mathbf{r} / r$ be the longitudinal velocity increment, with $r = \abs{\mathbf{r}}$.
Assume that, in the limit $\nu \to 0$, $\varepsilon$ stays finite and positive.
Then, in this limit, for separations $r$ in the inertial range, much smaller than $L$,
$$\langle \delta u(r)^3 \rangle = -\frac{4}{5} \, \varepsilon \, r.$$

## Remarks

The derivation starts from the [[Kármán–Howarth equation|ZSP670B8RR]], an exact consequence of the Navier–Stokes equations for the two-point velocity correlation of homogeneous isotropic turbulence.
In a stationary state it relates $\langle \delta u^3 \rangle$, a viscous term proportional to $\nu \, d\langle \delta u^2 \rangle / dr$, the forcing and $\varepsilon$.
For $r \ll L$ the forcing term is negligible, and as $\nu \to 0$ the viscous term vanishes at fixed $r$, leaving the four-fifths law.
Kolmogorov derived it in 1941.

It is the main exact result of the statistical theory of turbulence, with no adjustable constant.
The minus sign says that the velocity increments are skewed towards negative values, the signature of energy transfer to small scales in the [[energy cascade|YQ2KYDWRD0]].
It agrees with the 1941 similarity theory for $p = 3$, but it holds independently of the similarity hypotheses.
The hypothesis that $\varepsilon$ stays positive as $\nu \to 0$, the dissipation anomaly, is supported by experiments and simulations but is not proved for the Navier–Stokes equations.

## Explanations

### L1 human

In turbulence, take two points a short distance apart and compare their velocities along the line joining them.
The four-fifths law says that the average of the cube of this difference is negative and grows exactly in proportion to the distance.
The factor is $4/5$ times the energy dissipation rate.
The negative sign is the trace of energy flowing from big eddies to small ones.
It is one of the very few exact formulas known about turbulence.

### L2 human

Unlike most scaling laws in turbulence, the four-fifths law is derived from the equations of motion.
Its assumptions are homogeneity, isotropy, stationarity and a finite dissipation rate in the inviscid limit.
It is used to measure $\varepsilon$ in experiments and to check numerical simulations.
There is a related four-thirds law for the mixed third-order structure function $\langle \delta u \, \abs{\delta \mathbf{u}}^2 \rangle = -\frac43 \varepsilon r$.
