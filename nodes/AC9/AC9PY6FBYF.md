---
tag: AC9PY6FBYF
kind: statement
role: theorem
name: Multigrid method
msc: [65N55, 65F10, 65N22]
uses: [0EB9N0S33C, 54T6Y6DSY4, B8FVHNXAN1, G0EDYEDG4S, B4TTNHSTRX, X7HYEBA5SA, 2RPE77ACER, KE98SW3SBD, AFXZGQB4EN]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Multigrid_method
same_as:
  wikidata: Q1413101
  wikipedia: Multigrid method
---

## Statement

Let $A_h$ be an [[invertible|0EB9N0S33C]] real $n \times n$ matrix (the fine-grid matrix) and $A_H$ an invertible real $N \times N$ matrix with $N < n$ (the coarse-grid matrix).
Let $P$ be an $n \times N$ matrix (prolongation) and $R$ an $N \times n$ matrix (restriction).
Let $W$ be an invertible $n \times n$ matrix, and let $S = I - W^{-1} A_h$ be the iteration matrix of the smoother $x \mapsto x + W^{-1}(b - A_h x)$.
One step of the *two-grid method* for $A_h x = b$ applies $\nu \ge 1$ smoothing steps to $x$ and then the coarse-grid correction $x \mapsto x + P A_H^{-1} R (b - A_h x)$.

1. The error $e = x - A_h^{-1} b$ is mapped to $M e$, where $M = (I - P A_H^{-1} R A_h) S^{\nu}$.
2. (Hackbusch) Let $\norm{\cdot}$ be an operator norm, and let $C > 0$ and $\eta(\nu) \ge 0$ be numbers with $\norm{A_h^{-1} - P A_H^{-1} R} \le C / \norm{A_h}$ (approximation property) and $\norm{A_h S^{\nu}} \le \eta(\nu) \norm{A_h}$ (smoothing property). Then $\norm{M} \le C \, \eta(\nu)$.

## Remarks

Clause 1 follows by composing the error maps $e \mapsto S e$ of the smoother and $e \mapsto (I - P A_H^{-1} R A_h) e$ of the correction.
Clause 2 follows from the factorization $M = (A_h^{-1} - P A_H^{-1} R) \, A_h S^{\nu}$ and the two bounds.
Consider a family of [[finite difference|X7HYEBA5SA]] or finite element discretizations of an [[elliptic equation|B4TTNHSTRX]], with mesh widths $h$ and $H = 2h$.
Use damped [[Jacobi|B8FVHNXAN1]] smoothing and standard transfer matrices.
Under elliptic regularity assumptions, both properties hold with $C$ and $\eta$ independent of $h$, and $\eta(\nu) \to 0$.
Then for $\nu$ large enough the two-grid method contracts the error by a factor less than $1$ that does not depend on $h$.
Example: for $A_h$ symmetric positive definite and $S = I - A_h / \norm{A_h}_2$ in the [[matrix norm|54T6Y6DSY4]] $\norm{\cdot}_2$, one has $\norm{A_h S^\nu}_2 \le \max_{0 \le t \le 1} t (1 - t)^\nu \norm{A_h}_2 \le \norm{A_h}_2 / (\nu + 1)$.
Solving the coarse problem recursively by the same method gives the V-cycle and the W-cycle.

## Explanations

### L1 human

Simple methods such as Jacobi or [[Gauss–Seidel|G0EDYEDG4S]] remove the rough, oscillating part of the error quickly, but the smooth part only very slowly.
A smooth error can be represented well on a coarser grid with far fewer unknowns, where it is cheap to remove.
Multigrid alternates the two: smooth on the fine grid, correct on the coarse grid, and repeat over a hierarchy of grids.

### L2 human

For elliptic problems, multigrid reaches a fixed accuracy in $O(n)$ operations, which is optimal up to a constant.
The analysis splits into the smoothing property, a statement about the smoother alone, and the approximation property, a statement about the discretizations on the two grids.
Algebraic multigrid builds the coarse levels from the matrix alone, without a geometric grid.
Multigrid is also used as a [[preconditioner|KE98SW3SBD]] for the [[conjugate gradient method|AFXZGQB4EN]], and it is among the fastest [[iterative methods|2RPE77ACER]] for such problems.
