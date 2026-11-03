---
tag: SCKMWJ9JYT
kind: definition
name: Conic optimization
msc: [90C25, 90C22, 90C46]
defines: PAPN0JNEKN
uses: [6VE4KA12VD, QFY1JR1TK4, 0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Conic_optimization
---

## Definition

Let $V$ be a finite-dimensional real [[inner product|0NB0AWGJBW]] space and let $K \subseteq V$ be a closed [[convex cone|6VE4KA12VD]].
Let $c \in V$, let $A \colon V \to \R^m$ be a linear map and let $b \in \R^m$.
The *conic optimization problem* with these data is: minimise $\ip{c}{x}$ over $x \in V$ subject to $A x = b$ and $x \in K$.

## Remarks

Its *dual problem* is: maximise $b^T y$ over $y \in \R^m$ subject to $c - A^* y \in K^*$, where $A^*$ is the adjoint of $A$ and $K^* = \set{s \in V : \ip{s}{x} \ge 0 \text{ for all } x \in K}$ is the [[dual cone|QFY1JR1TK4]].
Weak duality holds: if $x$ and $y$ are feasible, then $\ip{c}{x} - b^T y = \ip{c - A^* y}{x} \ge 0$.

Example: take $V = \R^n$ with the dot product and $K = \R^n_{\ge 0}$, a closed convex cone.
Then the problem is the linear program "minimise $c^T x$ subject to $A x = b$, $x \ge 0$".

Non-example: "minimise $x_1$ subject to $x \in \Z^n_{\ge 0}$, $A x = b$" is not a conic problem, because $\Z^n_{\ge 0}$ is not convex.

The cone is often required to be proper, that is closed, convex, with nonempty interior and containing no line; then $K^*$ is proper too.
