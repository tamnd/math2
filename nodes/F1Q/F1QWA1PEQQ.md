---
tag: F1QWA1PEQQ
kind: statement
role: theorem
name: Tridiagonal matrix algorithm
msc: [65F05]
uses: [DARX1KZRHZ, 89P5GTKW87, 0JVJ2WCXZH, 0RKG5YW66Y, 0ATFVE08MW, 0GT4WWGWH2]
about: [DARX1KZRHZ, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
same_as:
  wikidata: Q1819156
  wikipedia: Tridiagonal matrix algorithm
---

## Statement

Let $n \ge 2$ and consider the [[linear system|0GT4WWGWH2]]
$$a_i x_{i-1} + b_i x_i + c_i x_{i+1} = d_i, \qquad i = 1, \dots, n,$$
with real or complex coefficients, $a_1 = 0$ and $c_n = 0$, whose matrix $A$ is [[tridiagonal|DARX1KZRHZ]].
Assume that $A$ is strictly [[diagonally dominant|89P5GTKW87]] by rows: $\abs{b_i} > \abs{a_i} + \abs{c_i}$ for all $i$.
The *tridiagonal matrix algorithm* (or *Thomas algorithm*) computes
$$c'_1 = \frac{c_1}{b_1}, \quad d'_1 = \frac{d_1}{b_1}, \qquad c'_i = \frac{c_i}{b_i - a_i c'_{i-1}}, \quad d'_i = \frac{d_i - a_i d'_{i-1}}{b_i - a_i c'_{i-1}} \quad (i = 2, \dots, n),$$
and then
$$x_n = d'_n, \qquad x_i = d'_i - c'_i x_{i+1} \quad (i = n - 1, \dots, 1).$$
Then every denominator $b_i - a_i c'_{i-1}$ is nonzero, $\abs{c'_i} < 1$ for all $i$, and $(x_1, \dots, x_n)$ is the unique solution of the system.
The algorithm uses $O(n)$ arithmetic operations.

## Remarks

The proof is an induction on $i$.
If $\abs{c'_{i-1}} < 1$, then $\abs{b_i - a_i c'_{i-1}} \ge \abs{b_i} - \abs{a_i} > \abs{c_i} \ge 0$, so the denominator is nonzero and $\abs{c'_i} < 1$.
The forward sweep is [[Gaussian elimination|0JVJ2WCXZH]] without pivoting, which keeps the tridiagonal shape, and it computes the [[LU decomposition|0RKG5YW66Y]] of $A$ with bidiagonal factors; the second sweep is [[back substitution|0ATFVE08MW]].
For diagonally dominant or symmetric positive definite matrices, the algorithm is also numerically stable.
Without such a hypothesis a denominator can vanish even when $A$ is invertible: for $b_1 = 0$, $c_1 = 1$, $a_2 = 1$, $b_2 = 0$, the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is invertible but the first step divides by $0$.
Example: the system $2x_1 - x_2 = 1$, $-x_1 + 2x_2 = 1$ is diagonally dominant by rows; the algorithm gives $c'_1 = -1/2$, $d'_1 = 1/2$, $d'_2 = (1 + 1/2)/(2 - 1/2) = 1$, so $x_2 = 1$ and $x_1 = 1/2 + 1/2 = 1$.

## Explanations

### L1 human

Many problems, such as heat flow along a rod or spline fitting, give systems where each equation involves only an unknown and its two neighbours.
The Thomas algorithm solves such a system in two sweeps: down the list, eliminating one unknown from each equation, and back up, reading off the unknowns one by one.
The work grows only in proportion to the number of unknowns, instead of its cube.

### L2 human

The algorithm is Gaussian elimination specialized to tridiagonal matrices, with no fill-in and no pivoting.
Strict diagonal dominance is a simple condition that guarantees it never divides by zero.
The finite difference matrix of $-u'' = f$, with rows $(-1, 2, -1)$, is only weakly diagonally dominant, but it is symmetric positive definite, and the algorithm works for it too.
For tridiagonal systems that are not diagonally dominant, one uses Gaussian elimination with partial pivoting on the band instead.
