---
tag: M2R0XWWW0R
kind: definition
name: Finsler manifold
msc: [53B40, 53C60]
defines: 5R6QZ388BB
uses: [F45VQ47GPV, WY6K3P4YCG, 0SCSQWXRA4, 0QQCG3JWJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Finsler_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] with [[tangent bundle|WY6K3P4YCG]] $TM$, and write $0$ for the zero section.
A *Finsler function* on $M$ is a continuous function $F \colon TM \to [0, \infty)$ such that:

1. $F$ is smooth on $TM \setminus 0$;
2. $F$ is positively homogeneous: $F(\lambda v) = \lambda F(v)$ for all $v \in TM$ and all $\lambda > 0$;
3. $F$ is strongly convex: for each $p \in M$ and nonzero $v \in T_pM$, the [[Hessian|0SCSQWXRA4]] at $v$ of $\tfrac{1}{2} F^2$ on $T_pM$ is [[positive definite|0QQCG3JWJ4]].

A *Finsler manifold* is a pair $(M, F)$ of a smooth manifold and a Finsler function on it.

## Remarks

Example: if $g$ is a Riemannian metric on $M$, then $F(v) = \sqrt{g(v, v)}$ is a Finsler function.
It is smooth away from $0$, homogeneous of degree $1$, and the Hessian of $\tfrac{1}{2}F^2 = \tfrac{1}{2} g(v, v)$ on $T_pM$ is $g_p$ itself, which is positive definite.

Non-example: on $\R^2$, $F(x, v) = \abs{v_1} + \abs{v_2}$ is positively homogeneous, but it is not smooth along the lines $v_1 = 0$ and $v_2 = 0$, so clause 1 fails.

Clauses 2 and 3 imply that $F(v) > 0$ for $v \ne 0$ and that $F$ satisfies the triangle inequality on each tangent space.
The function $F$ need not be symmetric: $F(-v) = F(v)$ is not required, and Randers metrics are standard examples with $F(-v) \ne F(v)$.
The length of a piecewise smooth curve $\gamma$ is $\int F(\gamma'(t)) \, dt$.
