---
tag: NDS0H727BA
kind: definition
name: Unit in the last place
msc: [65G50, 65Y04]
defines: HFBST11CT6
uses: [RTKRSC3KPH, JA3QXVF2B8]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_in_the_last_place
---

## Definition

Consider a [[floating-point|RTKRSC3KPH]] system with base $\beta$, precision $p$ and minimal exponent $e_{\min}$.
Let $x \ne 0$ be a floating-point number written as $x = \pm (d_0 . d_1 \ldots d_{p-1})_\beta \times \beta^{e}$, with $d_0 \ne 0$ if $e > e_{\min}$.
The *unit in the last place* of $x$ is
$$\mathrm{ulp}(x) = \beta^{\,e - p + 1},$$
the value of the digit position $d_{p-1}$.

## Remarks

Example: with $\beta = 10$ and $p = 3$, the number $x = 3.14 = 3.14 \times 10^{0}$ has $e = 0$, so $\mathrm{ulp}(x) = 10^{-2}$; its neighbours are $3.13$ and $3.15$.
Non-example: in the same system, $0.001$ is not the ulp of $3.14$, since $3.141$ is not a floating-point number of precision $3$.
The ulp of $1$ is $\beta^{1-p}$, the [[machine epsilon|JA3QXVF2B8]].
Several variants of the definition exist; some define $\mathrm{ulp}(x)$ for every real $x$ as the gap between the two floating-point numbers closest to $x$.
They agree away from powers of $\beta$.
Rounding to nearest gives an error of at most $\tfrac12 \mathrm{ulp}$ of the result.
