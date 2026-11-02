---
tag: EJ556BJNFM
kind: statement
role: theorem
name: Perron's formula
msc: [11M41, 11N37, 44A15]
uses: [8MWTEF6462, 0YBDSJARWN, CHESR1W1CY]
about: [8MWTEF6462]
sources:
  - url: https://en.wikipedia.org/wiki/Perron%27s_formula
same_as:
  wikidata: Q2759571
  wikipedia: Perron's formula
---

## Statement

Let $a \colon \set{1, 2, 3, \dots} \to \C$ and let $F(s) = \sum_{n \ge 1} a(n) n^{-s}$ be its [[Dirichlet series|8MWTEF6462]].
Let $\sigma_a$ be the abscissa of [[absolute convergence|0YBDSJARWN]] of $F$, assume $\sigma_a < \infty$, and let $c > \max(0, \sigma_a)$.
For $x > 0$, let $A^*(x) = \sum_{n < x} a(n) + \frac{1}{2} a(x)$, where the last term is present only when $x$ is an integer.
Then for every $x > 0$,
$$A^*(x) = \lim_{T \to \infty} \frac{1}{2\pi i} \int_{c - iT}^{c + iT} F(s) \, \frac{x^{s}}{s} \, ds.$$

## Remarks

The proof rests on the discontinuous integral.
Fix $c > 0$, and for $y > 0$ let $I(y) = \lim_{T \to \infty} \frac{1}{2\pi i} \int_{c - iT}^{c + iT} \frac{y^{s}}{s} \, ds$.
Then $I(y) = 1$ for $y > 1$, $I(1) = 1/2$, and $I(y) = 0$ for $0 < y < 1$.
For $y > 1$ one closes the path to the left and picks up the residue $1$ at $s = 0$; for $y < 1$ one closes it to the right, where there is no pole.
One applies this with $y = x/n$ to each term $a(n) n^{-s}$ and exchanges sum and limit.
The exchange uses the explicit error bound of the discontinuous integral and the absolute convergence of $F$ on $\operatorname{Re} s = c$.
The limit cannot be replaced by an absolutely convergent integral in general.
For $F = 1$, that is $a(1) = 1$ and $a(n) = 0$ otherwise, the integrand $x^{s}/s$ has modulus of order $1/\abs{s}$ on the line.
Example: take $a = \Lambda$, the [[von Mangoldt function|0NK8JTE1NN]], so that $F(s) = -\zeta'(s)/\zeta(s)$, and take $c > 1$.
Then the formula expresses the Chebyshev function $\psi(x)$ as a contour integral.
Shifting the contour to the left and collecting the residue $x$ at $s = 1$ is the route to the [[prime number theorem|0EHBY5Y84N]].

## Explanations

### L1 human

Perron's formula recovers the partial sums of the coefficients of a Dirichlet series from the values of the series on a vertical line.
It works because the integral of $x^{s}/s$ along a vertical line acts as a switch: it is $1$ when $x > 1$ and $0$ when $x < 1$.
So each term $a(n)$ is counted exactly when $n < x$.

### L2 human

The formula is an inverse Mellin transform: by the Mellin representation of Dirichlet series, $F(s)/s$ is the Mellin transform at $-s$ of the summatory function.
In practice one uses a truncated version with an explicit error term in $T$ and $x$, then moves the line of integration to the left of $\operatorname{Re} s = 1$.
The poles of $F(s) x^{s}/s$ then give the main terms, and bounds for $F$ in the critical strip control the error.
This is how the prime number theorem and its explicit formulas are derived from properties of the zeta function.
