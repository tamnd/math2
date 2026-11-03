---
tag: A2N76EGN5Y
kind: definition
name: Cosmic inflation
msc: ["83F05"]
defines: 81HPA9X0Y1
uses: [ECJMS4VDTF, J70F32P86W, QF1K65J7HD, PPHFS2P4G4]
sources:
  - url: https://en.wikipedia.org/wiki/Cosmic_inflation
---

## Definition

Let $a$ be the [[scale factor|J70F32P86W]] of a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]], with Hubble parameter $H = \dot a / a > 0$, in units with $c = 1$.
An *inflationary epoch* is a time interval $J$ on which the expansion accelerates:
$$\ddot a(t) > 0 \quad \text{for all } t \in J.$$
*Cosmic inflation* is the hypothesis that the early universe went through such an epoch before the radiation-dominated era.
During this epoch $a$ grew by a very large factor.

## Remarks

Equivalent forms: $\ddot a > 0$ holds exactly when the comoving Hubble radius $1/(aH) = 1/\dot a$ decreases, and exactly when the [[deceleration parameter|QF1K65J7HD]] satisfies $q < 0$.
By the second [[Friedmann equation|PPHFS2P4G4]] with $\Lambda = 0$, it holds exactly when $\rho + 3p < 0$, that is, for matter with $\rho > 0$, when $w = p/\rho < -1/3$.
Example: a homogeneous scalar field $\phi$ with potential $V$ has $\rho = \tfrac{1}{2}\dot\phi^2 + V(\phi)$ and $p = \tfrac{1}{2}\dot\phi^2 - V(\phi)$, so $\rho + 3p = 2(\dot\phi^2 - V(\phi))$, and it inflates exactly while $\dot\phi^2 < V(\phi)$.
Non-example: in the radiation era $a \propto t^{1/2}$, so $\ddot a = -\tfrac{1}{4} t^{-3/2} \cdot \text{const} < 0$, and the expansion decelerates.
The amount of inflation is measured by the number of e-folds $N = \ln\left( a(t_{\text{end}}) / a(t_{\text{start}}) \right)$.
Alan Guth proposed inflation in 1981 as a solution of the horizon and flatness problems.
