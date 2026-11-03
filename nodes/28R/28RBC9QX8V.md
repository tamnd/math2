---
tag: 28RBC9QX8V
kind: definition
name: Lagrangian relaxation
msc: [90C46, 90C10, 90C27]
defines: P9HK0R14WX
uses: [NS0Q42Y3FX, 9GX3WH5EQF, 07Q7CNM5WF, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_relaxation
---

## Definition

Let $X \subseteq \R^n$ be a nonempty set, let $c \in \R^n$, let $A$ be a real $m \times n$ matrix and let $b \in \R^m$.
Consider the [[optimization problem|NS0Q42Y3FX]]
$$z = \sup \set{c^T x : A x \le b, \ x \in X}.$$
For a vector $\lambda \in \R^m$ with $\lambda \ge 0$, the *Lagrangian relaxation* with multipliers $\lambda$ is the problem
$$L(\lambda) = \sup \set{c^T x + \lambda^T (b - A x) : x \in X}.$$
The *Lagrangian dual* is the problem of minimizing $L(\lambda)$ over all $\lambda \ge 0$; its value is denoted $z_D$.

## Remarks

Weak duality: $L(\lambda) \ge z$ for every $\lambda \ge 0$, since for $x \in X$ with $A x \le b$ the added term $\lambda^T (b - A x)$ is nonnegative.
Hence $z_D \ge z$.
The function $L$ is a supremum of affine functions of $\lambda$, so it is [[convex|07Q7CNM5WF]]; when $X$ is finite it is piecewise affine.

Geoffrion's theorem: let $X$ be a finite nonempty set, for instance the set of integer points of a bounded polyhedron.
Let $\operatorname{conv}(X)$ be the [[convex hull|0FQSDC2EQ2]] of $X$, and assume that some $x \in \operatorname{conv}(X)$ satisfies $A x \le b$.
Then
$$z_D = \max \set{c^T x : A x \le b, \ x \in \operatorname{conv}(X)}.$$
So for an [[integer program|9GX3WH5EQF]] the Lagrangian bound is at least as strong as the linear programming bound, and equal to it when the polyhedron describing $X$ is integral.

Example: let $X = \set{0, 1}$, $n = m = 1$, $c = 1$ and the constraint $2x \le 1$.
Then $z = 0$, and $L(\lambda) = \max(\lambda, 1 - \lambda)$, whose minimum over $\lambda \ge 0$ is $z_D = 1/2$ at $\lambda = 1/2$.
This matches Geoffrion's theorem: the maximum of $x$ over $[0, 1]$ with $2x \le 1$ is $1/2$.
The difference $z_D - z = 1/2$ is a duality gap.

Non-example: relaxing the constraint with a negative multiplier $\lambda < 0$ does not give a bound in general, since the added term can be negative at feasible points.
For equality constraints $A x = b$, the multipliers may have any sign.
