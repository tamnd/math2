---
tag: 5FR6JX04RS
kind: definition
name: Hilbert polynomial
msc: [13D40, 13A02]
defines: RMH4FBCFDA
uses: [8KB4SQGC0C, 07GNX8GCYP, 05QY1VEBYD, 04C5ZBG1WT, HP56DJECMT]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_series_and_Hilbert_polynomial
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $S = k[x_1, \dots, x_r]$ be the [[polynomial ring|07GNX8GCYP]] with each $x_i$ of degree $1$.
Let $M = \bigoplus_{n \in \Z} M_n$ be a [[finitely generated|05QY1VEBYD]] [[graded|8KB4SQGC0C]] $S$-module.
The Hilbert function of $M$ is $H_M(n) = \dim_k M_n$.
The *Hilbert polynomial* of $M$ is the unique polynomial $P_M \in \Q[t]$ such that $H_M(n) = P_M(n)$ for all sufficiently large integers $n$.

## Remarks

Such a polynomial exists by the [[Hilbert–Serre theorem|HP56DJECMT]], and it is unique because two polynomials that agree at infinitely many integers are equal.
Example: for $M = k[x, y, z]/(f)$ with $f$ homogeneous of degree $d$, the exact sequence $0 \to S(-d) \to S \to M \to 0$ gives $H_M(n) = \binom{n+2}{2} - \binom{n-d+2}{2}$ for $n \ge d$, so $P_M(t) = dt - d(d-3)/2$.
Non-example: the Hilbert function itself need not be a polynomial on all of $\N$; for $M = k = S/(x_1, \dots, x_r)$ one has $H_M(0) = 1$ and $H_M(n) = 0$ for $n \ge 1$, so $P_M = 0$ but $H_M(0) \neq P_M(0)$.
For $M = S$, the Hilbert polynomial is $\binom{t + r - 1}{r - 1}$, of degree $r - 1$.
