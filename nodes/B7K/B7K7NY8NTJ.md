---
tag: B7K7NY8NTJ
kind: conjecture
name: Selberg's 1/4 conjecture
msc: [11F72, 11F12, 58J50]
uses: [1H6R856P3C, VEKV1EM77B, X6XGGH5FPW, F4NWZNTRMD, 3R959YSNYP, 0BQAA2BK3Q]
about: [F4NWZNTRMD, 1H6R856P3C]
sources:
  - url: https://en.wikipedia.org/wiki/Selberg%27s_1/4_conjecture
same_as:
  wikidata: Q7447522
  wikipedia: Selberg's 1/4 conjecture
history:
  posed_by: "Atle Selberg"
  first_stated: "1965"
---

## Statement

Let $\Gamma$ be a [[congruence subgroup|1H6R856P3C]] of the [[modular group|VEKV1EM77B]] $\mathrm{SL}_2(\Z)$, acting on the [[upper half-plane|X6XGGH5FPW]] $\mathbb H$.
Let $\Delta = -y^2 (\partial_x^2 + \partial_y^2)$ be the hyperbolic [[Laplace–Beltrami operator|F4NWZNTRMD]] on $L^2(\Gamma \backslash \mathbb H)$.
The conjecture states that every nonzero [[eigenvalue|0BQAA2BK3Q]] $\lambda$ of $\Delta$ on $L^2(\Gamma \backslash \mathbb H)$ satisfies $\lambda \ge \tfrac14$.

## Remarks

The eigenfunctions in question are the [[Maass cusp forms|3R959YSNYP]] for $\Gamma$, since the continuous spectrum is $[\tfrac14, \infty)$.
Selberg proved the bound $\lambda \ge \tfrac{3}{16}$.
The best bound known is $\lambda \ge \tfrac{975}{4096}$, due to Kim and Sarnak.
The conjecture is known for $\mathrm{SL}_2(\Z)$ itself and for congruence subgroups of small level.
It is the archimedean case of the generalised Ramanujan conjecture for $\mathrm{GL}_2$: an eigenvalue $\lambda = \tfrac14 - s^2$ with $0 < s < \tfrac12$ would give a non-tempered local component at the real place.
The arithmetic hypothesis matters: for general cofinite Fuchsian groups, eigenvalues below $\tfrac14$ can occur.

## Explanations

### L1 human

The quotient of the upper half-plane by a congruence group is a surface with a few cusps, and it can vibrate at certain frequencies.
Selberg predicted that, apart from the trivial vibration, all frequencies are at least $\tfrac14$, the bottom of the continuous spectrum.
This means that these arithmetic surfaces are very well connected, with no slow vibration, and it has consequences for counting problems and for expander graphs.
