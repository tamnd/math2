---
tag: SEVHW7TPPZ
kind: definition
name: Krein space
msc: [46C20, 47B50]
defines: NFN044536P
uses: [48P4A1CX85, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Indefinite_inner_product_space
---

## Definition

Let $K$ be a complex vector space and let $[\cdot, \cdot]$ be a [[Hermitian form|48P4A1CX85]] on $K$.
The pair $(K, [\cdot, \cdot])$ is a *Krein space* if there are subspaces $K_+$ and $K_-$ of $K$ such that:

1. $K = K_+ \oplus K_-$ as a direct sum of vector spaces.
2. $[x, y] = 0$ for all $x \in K_+$ and $y \in K_-$.
3. $(K_+, [\cdot, \cdot])$ is a [[Hilbert space|HM2HHE3J51]].
4. $(K_-, -[\cdot, \cdot])$ is a Hilbert space.

Such a splitting is a *fundamental decomposition* of $K$.

## Remarks

Let $P_\pm$ be the projections of $K$ onto $K_\pm$ along the decomposition, and let $J = P_+ - P_-$.
Then $\ip{x}{y}_J = [Jx, y]$ is a Hilbert space inner product on $K$, and $[x, y] = \ip{Jx}{y}_J$.
The map $J$ is the *fundamental symmetry*; the decomposition is not unique, but all the norms $\ip{x}{x}_J^{1/2}$ are equivalent.
If $K_-$ has finite dimension $\kappa$, the space is a *Pontryagin space* $\Pi_\kappa$.

Example: $K = \C^2$ with $[x, y] = x_1 \overline{y_1} - x_2 \overline{y_2}$, $K_+ = \C e_1$ and $K_- = \C e_2$.
Clause 2 holds since $[e_1, e_2] = 0$, and $[x, x] = \abs{x_1}^2$ on $K_+$ and $-[x, x] = \abs{x_2}^2$ on $K_-$ are positive definite.
The vector $e_1 + e_2$ satisfies $[e_1 + e_2, e_1 + e_2] = 0$, so the form is indefinite.

Non-example: $K = \C^2$ with $[x, y] = x_1 \overline{y_1}$.
The vector $e_2$ satisfies $[e_2, y] = 0$ for every $y$.
In a Krein space, write $e_2 = x_+ + x_-$; then $[x_+, x_+] = [e_2, x_+] = 0$ forces $x_+ = 0$, and in the same way $x_- = 0$.
So the form of a Krein space is nondegenerate, and this degenerate form admits no fundamental decomposition.
