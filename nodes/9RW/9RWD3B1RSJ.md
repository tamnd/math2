---
tag: 9RWD3B1RSJ
kind: definition
name: Convex optimization
msc: [90C25, 52A41]
defines: 1W1BXJN9ER
uses: [07Q7CNM5WF, 02AS45T3H9, NS0Q42Y3FX]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_optimization
---

## Definition

Let $f_0, f_1, \dots, f_m \colon \R^n \to \R$ be functions, let $A$ be a real $p \times n$ matrix and let $b \in \R^p$.
The [[optimization problem|NS0Q42Y3FX]]
$$\text{minimize } f_0(x) \quad \text{subject to } f_i(x) \le 0 \ (i = 1, \dots, m), \quad Ax = b$$
is a *convex optimization problem* if:

1. The objective $f_0$ is a [[convex function|07Q7CNM5WF]].
2. Each inequality constraint function $f_i$, $1 \le i \le m$, is convex.
3. The equality constraints are affine, as in $Ax = b$.

More generally, minimizing a convex function $f_0 \colon C \to \R$ over a [[convex set|02AS45T3H9]] $C \subseteq \R^n$ is a convex optimization problem.
*Convex optimization* is the study of such problems.

## Remarks

Under clauses 2 and 3 the feasible set is convex, as an intersection of sublevel sets of convex functions and an affine subspace.
Every local minimizer is a global minimizer, and the set of minimizers is convex.
Maximizing a concave function over a convex set is also called a convex problem, since it is minimizing its negative.

Example: minimize $f_0(x) = x_1^2 + x_2^2$ subject to $f_1(x) = 1 - x_1 - x_2 \le 0$.
Here $f_0$ is convex and $f_1$ is affine, hence convex, so all clauses hold.
The minimizer is $(1/2, 1/2)$.

Non-example: minimize $x_1$ subject to $x_1^2 + x_2^2 - 1 = 0$.
The equality constraint is not affine, so clause 3 fails.
The feasible set is a circle, which is not convex.
