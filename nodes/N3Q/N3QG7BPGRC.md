---
tag: N3QG7BPGRC
kind: definition
name: Coordinate descent
msc: [90C06, 65K05, 90C25]
defines: 6YGTSHB3MN
uses: [07GR3TNW4H, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_descent
---

## Definition

Let $f \colon \R^n \to \R$ be a function, let $e_1, \dots, e_n$ be the standard basis vectors of $\R^n$, and let $x_0 \in \R^n$.
*Coordinate descent* produces a sequence $(x_k)$ as follows.
At step $k$ an index $i_k \in \set{1, \dots, n}$ is chosen, cyclically ($i_k = (k \bmod n) + 1$) or at random, and
$$x_{k+1} = x_k + s_k e_{i_k}, \qquad \text{where } s_k \in \operatorname*{arg\,min}_{s \in \R} f(x_k + s e_{i_k}).$$
So $x_{k+1}$ differs from $x_k$ in coordinate $i_k$ only.

## Remarks

A common variant replaces exact minimisation by a step along one partial derivative, $x_{k+1} = x_k - \eta \, \partial_{i_k} f(x_k) \, e_{i_k}$.

Example: $f(x, y) = x^2 + x y + y^2$ with $x_0 = (0, 1)$ and cyclic order.
Minimising $x^2 + x y + y^2$ over $x$ gives $x = -y/2$, and over $y$ gives $y = -x/2$, so the iterates are $(0, 1), (-\tfrac12, 1), (-\tfrac12, \tfrac14), (-\tfrac18, \tfrac14), \dots$, which tend to the minimiser $(0, 0)$.

Non-example: an update that changes two coordinates at once, such as a full [[gradient|0ABK9V9Y64]] step, is not a coordinate descent step.

The method can fail for nonsmooth [[convex functions|07GR3TNW4H]].
For $f(x, y) = 3\abs{x - y} + \abs{x + y}$ at the point $(1, 1)$, one has $f(t, 1) = 3\abs{t - 1} + \abs{t + 1} > 2 = f(1, 1)$ for every $t \ne 1$, and likewise $f(1, t) > 2$ for $t \ne 1$.
So every coordinate step returns $(1, 1)$, although the minimum $0$ is at $(0, 0)$.
