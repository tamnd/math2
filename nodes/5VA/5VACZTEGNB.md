---
tag: 5VACZTEGNB
kind: definition
name: Dirac bracket
msc: [70H45, 53D17]
defines: QYP4KYN248
uses: [2S0MXDT4YH, F3D3X49ZBW]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_bracket
---

## Definition

Let $V \subseteq \R^{2n}$ be open, with the [[Poisson bracket|2S0MXDT4YH]] $\{\cdot, \cdot\}$ in canonical coordinates $(q, p)$.
Let $\chi_1, \ldots, \chi_{m}$ be smooth functions on $V$, and let $C = (C_{ab})$ be the matrix with $C_{ab} = \{\chi_a, \chi_b\}$.
Assume that $C$ is invertible at every point of $V$; so the $\chi_a$ are [[second class constraints|F3D3X49ZBW]].
Let $(C^{ab})$ be the inverse matrix of $C$.
The *Dirac bracket* of smooth functions $f, g$ on $V$ is
$$\{f, g\}_D = \{f, g\} - \sum_{a, b = 1}^{m} \{f, \chi_a\} \, C^{ab} \, \{\chi_b, g\}.$$

## Remarks

Since $C$ is antisymmetric and invertible, $m$ is even.
For each $c$, $\{f, \chi_c\}_D = \{f, \chi_c\} - \sum_{a, b} \{f, \chi_a\} C^{ab} C_{bc} = 0$, so the constraints commute with everything for the Dirac bracket.
The Dirac bracket is antisymmetric and satisfies the Jacobi identity, and its restriction to the constraint surface $\set{\chi_a = 0}$ is the Poisson bracket of the induced symplectic structure there.

Example: $n = 2$, $\chi_1 = q_2$, $\chi_2 = p_2$.
Then $C = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $C^{-1} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
A short computation gives
$$\{f, g\}_D = \frac{\partial f}{\partial q_1} \frac{\partial g}{\partial p_1} - \frac{\partial f}{\partial p_1} \frac{\partial g}{\partial q_1},$$
the bracket of the remaining pair $(q_1, p_1)$.

Non-example: for $n = 2$ and the single constraint $\chi_1 = p_2$, the matrix $C = (\{p_2, p_2\}) = (0)$ is not invertible, because $p_2$ is first class, so the Dirac bracket is not defined for it.
