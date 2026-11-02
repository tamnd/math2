---
tag: VGPTRNE3FF
kind: definition
name: Bifurcation set
msc: [58K35, 58K05]
defines: JV45S0KQE6
uses: [0V33BNKZ9S, 0YTCMFB4HC, 0693Y2METT]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Definition

Let $n, k \ge 1$ and let $V \colon \R^n \times \R^k \to \R$ be a [[smooth function|0V33BNKZ9S]], written $V(x, c)$ with state $x \in \R^n$ and control $c \in \R^k$.
A point $x$ is a *degenerate critical point* of $V(\cdot, c)$ if:

1. $\nabla_x V(x, c) = 0$, so $x$ is a [[critical point|0YTCMFB4HC]] of $V(\cdot, c)$, and
2. $\det H_x V(x, c) = 0$, where $H_x V$ is the [[Hessian matrix|0693Y2METT]] of second derivatives in the variables $x$.

The *bifurcation set* of the family $V$ is the set
$$B_V = \set{c \in \R^k : V(\cdot, c) \text{ has a degenerate critical point}}.$$

## Remarks

Example: the cusp family $V(x, a, b) = x^4/4 + a x^2/2 + b x$ with $n = 1$, $k = 2$.
Clause 1 reads $x^3 + a x + b = 0$ and clause 2 reads $3x^2 + a = 0$.
Then $a = -3x^2$ and $b = 2x^3$, and eliminating $x$ gives $B_V = \set{(a, b) : 4a^3 + 27b^2 = 0}$, a curve with a cusp at the origin.

Non-example: for $V(x, c) = x^2 + c x$ the only critical point is $x = -c/2$, and $V'' = 2 \ne 0$, so clause 2 always fails and $B_V$ is empty.

Let $M = \set{(x, c) : \nabla_x V(x, c) = 0}$ and let $\chi \colon M \to \R^k$ be the projection $(x, c) \mapsto c$.
When $M$ is a smooth submanifold of dimension $k$, which holds for generic families, $B_V$ is the set of critical values of $\chi$.
Some authors also add the Maxwell set, where two critical values of $V(\cdot, c)$ are equal; this node uses the narrower meaning.
