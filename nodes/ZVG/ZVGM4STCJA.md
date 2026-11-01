---
tag: ZVGM4STCJA
kind: definition
name: Numerical linear algebra
msc: [65F99, 65F05, 65F15]
defines: B8W28KDMB0
uses: [0VD9ZSWWJG, 0BQAA2BK3Q, 09VMDSRXWJ, AB3S6MHJ8X]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_linear_algebra
---

## Definition

*Numerical linear algebra* is the part of numerical analysis that studies algorithms in finite-precision arithmetic for these problems.
In each, $A$ is a real or complex [[matrix|0VD9ZSWWJG]].

1. solve a linear system $Ax = b$;
2. find $x$ that minimizes $\norm{Ax - b}_2$ (least squares);
3. find the [[eigenvalues|0BQAA2BK3Q]] and eigenvectors of a square matrix $A$;
4. find the [[singular values|09VMDSRXWJ]] and singular vectors of $A$.

An algorithm is judged by its cost, counted in arithmetic operations and memory, and by its accuracy under rounding errors.

## Remarks

An algorithm is *backward stable* when its computed answer is the exact answer for slightly perturbed data.
For a linear system this means $(A + \delta A)\hat x = b$ with $\norm{\delta A}$ of the order of the unit roundoff times $\norm{A}$.
For a backward stable method, the relative error of $\hat x$ is roughly bounded by the [[condition number|AB3S6MHJ8X]] of $A$ times the unit roundoff.
Example: Householder [[QR decomposition|0ERWG4NXQ9]] solves least squares problems in a backward stable way with about $2mn^2 - \tfrac{2}{3}n^3$ operations for an $m \times n$ matrix.
Non-example: computing the exact determinant of an integer matrix with rational arithmetic is a task of computer algebra.
It is not numerical linear algebra, because it does not work in finite precision and has no rounding error to analyse.
Direct methods, such as [[LU decomposition|0RKG5YW66Y]], finish in a fixed number of steps; iterative methods, such as [[power iteration|H4MQD841BR]], improve an approximation step by step.
