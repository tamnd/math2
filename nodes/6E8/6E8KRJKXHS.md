---
tag: 6E8KRJKXHS
kind: statement
role: theorem
name: Weierstrass–Erdmann corner conditions
msc: [49K05]
uses: [JRQZ803Q5Y, WMPCR723MJ, PS0VV149ET]
about: [PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass%E2%80%93Erdmann_condition
same_as:
  wikidata: Q7979831
  wikipedia: Weierstrass–Erdmann condition
---

## Statement

Let $a < b$ and let $L \colon [a, b] \times \R^n \times \R^n \to \R$, written $L(x, y, p)$, be of class $C^1$.
Let $J(y) = \int_a^b L(x, y, y') \, dx$ on piecewise $C^1$ functions $y \colon [a, b] \to \R^n$ with fixed values at $a$ and $b$.
Let $y_0$ be a piecewise $C^1$ [[strong local minimiser|WMPCR723MJ]] of $J$ in this class.
Let $c \in (a, b)$ be a corner of $y_0$, with one-sided derivatives $p_- = y_0'(c^-)$ and $p_+ = y_0'(c^+)$.
Then
$$L_p(c, y_0(c), p_-) = L_p(c, y_0(c), p_+),$$
$$L(c, y_0(c), p_-) - p_- \cdot L_p(c, y_0(c), p_-) = L(c, y_0(c), p_+) - p_+ \cdot L_p(c, y_0(c), p_+).$$

## Remarks

The first condition comes from variations $y_0 + \varepsilon h$ with $h$ supported near $c$.
The du Bois-Reymond form of the [[Euler–Lagrange equation|PS0VV149ET]] says that $L_p(x, y_0, y_0')$ equals a continuous function of $x$, so it has no jump at $c$.
The second condition comes from moving the corner point sideways, which is a variation of the independent variable $x$.

Example: let $J(y) = \int_0^2 (y'^2 - 1)^2 \, dx$ with $y(0) = y(2) = 0$.
The zigzag $y_0(x) = \min(x, 2 - x)$ has $J(y_0) = 0$, so it is a minimiser, with a corner at $1$ where $p_- = 1$ and $p_+ = -1$.
Here $L_p = 4p(p^2 - 1)$ and $L - p L_p = (p^2 - 1)^2 - 4p^2(p^2 - 1)$, and both vanish at $p = \pm 1$, as the theorem requires.

If $L_{pp} > 0$ everywhere, the map $p \mapsto L_p(x, y, p)$ is injective when $n = 1$, and the first condition forces $p_- = p_+$.
So for such Lagrangians minimisers have no corners.

## Explanations

### L1 human

Sometimes the best curve has a sharp bend, a corner.
The corner conditions say which bends are allowed.
Two quantities built from the integrand, often called the momentum and the energy, must take the same value just before and just after the corner.

### L2 human

The Euler–Lagrange equation holds on each smooth piece of a broken extremal, but it says nothing about how the pieces join.
The Weierstrass–Erdmann conditions supply the missing junction conditions, two of them, which match the freedom in the location and the slopes at a corner.
In Hamiltonian terms they say that the momentum $L_p$ and the Hamiltonian $p \cdot L_p - L$ are continuous along the extremal.
They explain why problems with Lagrangians that are not convex in $p$ often have broken minimisers.
