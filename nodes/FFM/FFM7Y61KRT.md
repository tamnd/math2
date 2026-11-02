---
tag: FFM7Y61KRT
kind: statement
role: theorem
name: Babenko–Beckner inequality
msc: ["42B10", "42A38"]
uses: [DPVM34ADZV, SASP14MA1Z, HXNJH6W23S, ZNEHMR2CCP]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Babenko%E2%80%93Beckner_inequality
same_as:
  wikidata: Q4837774
  wikipedia: Babenko–Beckner inequality
---

## Statement

Let $n \ge 1$, let $1 < p \le 2$, and let $q$ be the conjugate exponent, $\frac{1}{p} + \frac{1}{q} = 1$.
Put $A_p = \left( p^{1/p} / q^{1/q} \right)^{1/2}$.
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be the [[Fourier transform|DPVM34ADZV]].
Then for every $f \in L^1(\R^n) \cap L^p(\R^n)$,
$$\norm{\hat f}_{L^q(\R^n)} \le A_p^n\, \norm{f}_{L^p(\R^n)}.$$
The constant $A_p^n$ is the best possible: equality holds for $f(x) = e^{-\pi \abs{x}^2}$.

## Remarks

The inequality sharpens the [[Hausdorff–Young inequality|HXNJH6W23S]], whose constant is $1$; for $1 < p < 2$ one has $A_p < 1$.
K. I. Babenko proved it when $q$ is an even integer, and W. Beckner proved it for all $p$ in the range.
Beckner's proof goes through a sharp hypercontractive estimate for the Hermite semigroup and a central limit argument.

The equality case can be checked directly with the [[Fourier transform of the Gaussian|ZNEHMR2CCP]]: for $f(x) = e^{-\pi \abs{x}^2}$ one has $\hat f = f$ and $\norm{f}_r = r^{-n/(2r)}$ for every $r > 0$.
So $\norm{\hat f}_q / \norm{f}_p = \left( p^{1/p} / q^{1/q} \right)^{n/2} = A_p^n$.

Differentiating the inequality in $p$ at $p = 2$, where both sides are equal by Plancherel, gives the entropic uncertainty principle.

## Explanations

### L1 human

The Hausdorff–Young inequality says that the Fourier transform does not increase a certain size of a function.
The Babenko–Beckner inequality finds the exact best factor by which it shrinks that size.
The bell curve is the function for which the factor is reached.

### L2 human

This is a typical sharp inequality in analysis, with Gaussians as extremal functions.
The same happens for the logarithmic Sobolev inequality and the hypercontractivity of the Ornstein–Uhlenbeck semigroup, to which it is closely related.
Its derivative at $p = 2$ gives the Hirschman–Beckner entropic uncertainty principle, which in turn implies the Heisenberg inequality.
