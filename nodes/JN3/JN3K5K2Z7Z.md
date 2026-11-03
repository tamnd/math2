---
tag: JN3K5K2Z7Z
kind: definition
name: Formally real Jordan algebra
msc: [17C20, 17C90]
defines: WYE4E80T43
uses: [6C2MCVB8C7]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_algebra
---

## Definition

Let $J$ be a [[Jordan algebra|6C2MCVB8C7]] over $\R$, with product $(x, y) \mapsto xy$, and write $x^2 = xx$.
$J$ is *formally real* if for every $n \ge 1$ and all $x_1, \ldots, x_n \in J$, the equation $x_1^2 + \cdots + x_n^2 = 0$ implies $x_1 = \cdots = x_n = 0$.

## Remarks

Example: the real symmetric $n \times n$ matrices with $X \circ Y = \frac{1}{2}(XY + YX)$, so that $X \circ X = X^2$.
For symmetric $X$, $\tr(X^2) = \sum_{i, j} X_{ij}^2$.
If $X_1^2 + \cdots + X_n^2 = 0$, taking traces gives $\sum_k \sum_{i, j} (X_k)_{ij}^2 = 0$, so every $X_k$ is $0$.

Non-example: the commutative associative algebra $\R[\varepsilon]/(\varepsilon^2)$ is a Jordan algebra, but $\varepsilon^2 = 0$ with $\varepsilon \ne 0$.

Every formally real Jordan algebra is power-associative and has no nonzero nilpotent elements.
