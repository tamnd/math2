---
tag: DWXSXSN2S2
kind: problem
name: Lagrange's problem of the strongest column
msc: [74P05, 74G60, 49K15]
uses: [E8JCKAE09C, 4GAM4KXSM8, PQ25NHV0KS]
about: [4GAM4KXSM8]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_critical_load
history:
  posed_by: Joseph-Louis Lagrange
  first_stated: "1770"
---

## Problem

Consider elastic columns of given length $L$, given volume $V$ and given material.
Among them, find the distribution of cross-section along the axis that makes the [[buckling|4GAM4KXSM8]] load as large as possible.
Let $A(x)$ be the cross-section area at $x \in [0, L]$.
In the classical form the cross-sections are geometrically similar, so the second moment of area is $I(x) = \alpha A(x)^2$ for a constant $\alpha > 0$.
For pinned ends the buckling load is the smallest eigenvalue $P$ of
$$E \alpha A(x)^2 w''(x) + P w(x) = 0, \qquad w(0) = w(L) = 0,$$
and the problem is to maximize it over $A \ge 0$ with $\int_0^L A(x) \, dx = V$.

## Remarks

For a uniform column the answer is [[Euler's critical load|E8JCKAE09C]], $P = \pi^2 E \alpha A^2 / L^2$ with $A = V/L$.
Lagrange studied the problem in the 1770s and concluded that the uniform cylinder is the strongest column, which is not correct.
T. Clausen found the optimal shape for pinned ends in 1851, and J. B. Keller rederived it in 1960 by the [[calculus of variations|PQ25NHV0KS]].
The optimal column is thicker in the middle and tapers towards the ends.
Its buckling load is $4/3$ times that of the uniform column of the same volume.
For clamped ends the optimal design has a double smallest eigenvalue, which makes the problem harder; this case was studied later by several authors.

## Explanations

### L1 human

If you have a fixed amount of material to make a column, how should you shape it so that it carries the biggest load before it bows out?
Putting more material in the middle, where bending is worst, and less at the ends helps.
For a column with hinged ends the best shape is a third stronger than a plain cylinder of the same weight.
