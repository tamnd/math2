---
tag: 5NH9BXWAKR
kind: problem
name: Matrix Riemann–Hilbert problem
msc: ["30E25", 45F15, 47A68]
uses: [RY8YQ9JZF9, 0NAHXR1FRH, 012PBA0FMD, 0EB9N0S33C, 0X7SBS8E0F, 2M672PP7QR]
about: [RY8YQ9JZF9]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Hilbert_problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
  notes: "Hilbert listed it as the 21st of his problems in 1900. Riemann had studied the question in 1857."
---

## Problem

Let $\Gamma \subset \C$ be a smooth simple closed curve, oriented counterclockwise, with interior domain $D^+$ and exterior domain $D^-$.
Let $n \ge 1$ and let $G \colon \Gamma \to \mathrm{GL}_n(\C)$ be a [[Hölder continuous|012PBA0FMD]] map into the [[invertible|0EB9N0S33C]] complex $n \times n$ matrices.
Let $g \colon \Gamma \to \C^n$ be Hölder continuous.
Find a function $\Phi$ with values in $\C^n$ that is [[holomorphic|0NAHXR1FRH]] on $D^+$ and on $D^-$.
It may have at most a pole of prescribed order at $\infty$.
It must have continuous boundary values $\Phi^+$ from $D^+$ and $\Phi^-$ from $D^-$.
These must satisfy
$$\Phi^+(t) = G(t)\, \Phi^-(t) + g(t), \quad t \in \Gamma.$$
The *homogeneous* problem is the case $g = 0$.

## Remarks

This is the vector form of the [[Riemann–Hilbert problem|RY8YQ9JZF9]]; for $n = 1$ it is the scalar problem, which is solved in closed form with logarithms and Cauchy integrals.
For $n \ge 2$ the scalar method fails, because the values $G(t)$ need not commute.

The general theory rests on a factorization $G = G_+\, \Lambda\, G_-$ on $\Gamma$, where $G_+$ extends holomorphically and invertibly to $D^+$, $G_-$ does the same on $D^-$ including $\infty$, and $\Lambda(t) = \operatorname{diag}(t^{\kappa_1}, \ldots, t^{\kappa_n})$ when $0 \in D^+$.
Such a factorization exists for every Hölder continuous invertible $G$, and the integers $\kappa_1 \ge \cdots \ge \kappa_n$, the partial indices, are unique.
Their sum is the [[winding number|0X7SBS8E0F]] of $\det G$ about $0$.
The number of solutions of the homogeneous problem and the solvability conditions of the inhomogeneous problem are expressed by the partial indices, not by their sum alone.
The same structure appears for matrix symbols on the real line in the [[matrix Wiener–Hopf factorization|2M672PP7QR]].
No general method computes the partial indices or the factors of a given $G$ in closed form.

Example: if $G$ is diagonal, the problem splits into $n$ scalar problems, and the partial indices are the winding numbers of the diagonal entries.
If $G$ is triangular, the problem is solved by a chain of scalar problems.

The problem is linked to Hilbert's twenty-first problem, which asks for a linear system of differential equations with regular singular points and prescribed monodromy.
Plemelj gave a positive answer for regular singular systems in 1908 through this problem.
Bolibruch showed in 1989 that the version asking for Fuchsian systems has a negative answer in general.
Matrix Riemann–Hilbert problems on contours with prescribed jumps are also the basis of the nonlinear steepest descent method for integrable systems and random matrices.

## Explanations

### L1 human

One looks for a vector of functions that is holomorphic on both sides of a closed curve.
Across the curve the vector jumps: the values from inside equal a given matrix times the values from outside.
For a single function this is solved exactly, but with matrices the order of multiplication matters, and the problem becomes much harder.
Its answer is controlled by a list of integers, the partial indices, which are hidden inside the jump matrix.
