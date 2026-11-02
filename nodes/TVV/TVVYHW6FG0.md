---
tag: TVVYHW6FG0
kind: definition
name: Dual pair
msc: [46A20]
defines: R68HNB5SVR
uses: [05EGHEQZAW, 0SQZMXB6GP]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_system
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$.
A *dual pair* over $\mathbb{K}$ is a triple $(X, Y, \langle \cdot, \cdot \rangle)$ such that:

1. $X$ and $Y$ are [[vector spaces|05EGHEQZAW]] over $\mathbb{K}$, and $\langle \cdot, \cdot \rangle \colon X \times Y \to \mathbb{K}$ is a [[bilinear form|0SQZMXB6GP]].
2. For every $x \in X$ with $x \ne 0$ there is $y \in Y$ with $\langle x, y \rangle \ne 0$.
3. For every $y \in Y$ with $y \ne 0$ there is $x \in X$ with $\langle x, y \rangle \ne 0$.

## Remarks

Some authors call any triple satisfying condition 1 a dual pair, and call it *separated* when 2 and 3 hold.
Example: $X = Y = \R^n$ with $\langle x, y \rangle = \sum_i x_i y_i$; if $x \ne 0$ then $\langle x, x \rangle > 0$, which gives 2, and 3 holds in the same way.
Example: for a Hausdorff locally convex space $E$, the triple $(E, E', \langle x, f \rangle = f(x))$ is a dual pair; condition 2 follows from the Hahn–Banach theorem, and condition 3 is trivial.
Non-example: $X = C([0, 1])$, $Y = \R$, $\langle f, t \rangle = t f(0)$ satisfies 1 and 3 but not 2, since the function $f(s) = s$ is nonzero and $\langle f, t \rangle = 0$ for all $t$.
