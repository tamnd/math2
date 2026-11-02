---
tag: BVMH4AKV9F
kind: definition
name: Exposed point
msc: [52A20, 46A55]
defines: VN4M72SQW5
uses: [0XPR1E85W0, 07YQ1C78G0, 3MSGFJM2NX, K7N565NKCV]
sources:
  - url: https://en.wikipedia.org/wiki/Exposed_point
---

## Definition

Let $n \ge 1$ and let $C \subseteq \R^n$.
A point $x \in C$ is an *exposed point* of $C$ if there is a [[linear form|07YQ1C78G0]] $f \colon \R^n \to \R$ such that $f(x) > f(y)$ for all $y \in C$ with $y \ne x$.

## Remarks

Equivalently, there is a [[supporting hyperplane|K7N565NKCV]] $H$ of $C$ with $H \cap C = \set{x}$.
In a real topological vector space the same definition is used with continuous linear functionals.

Every exposed point is an [[extreme point|3MSGFJM2NX]].
Suppose $x = (1 - t) y + t z$ with $y, z \in C$, $y \ne z$ and $0 < t < 1$.
Then $x \ne y$ and $x \ne z$, so $f(y) < f(x)$ and $f(z) < f(x)$, and hence $f(x) = (1 - t) f(y) + t f(z) < f(x)$, a contradiction.

Example: in $[0, 1]^2$, the corner $(1, 1)$ is exposed by $f(x_1, x_2) = x_1 + x_2$, since $f \le 2$ on the square with equality only at $(1, 1)$.

Non-example: let $C$ be the stadium, the convex hull of the discs of radius $1$ centred at $(-1, 0)$ and $(1, 0)$.
The point $(1, 1)$ is extreme, but the only supporting line of $C$ through it is $y = 1$, which meets $C$ in the whole segment from $(-1, 1)$ to $(1, 1)$.
So no linear form is maximised on $C$ only at $(1, 1)$.
