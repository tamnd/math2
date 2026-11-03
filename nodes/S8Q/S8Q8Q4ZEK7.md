---
tag: S8Q8Q4ZEK7
kind: definition
name: Pareto front
msc: [90C29, 90B50]
defines: NJ1QWE4Q3Y
uses: [E560RGEKPP]
sources:
  - url: https://en.wikipedia.org/wiki/Pareto_front
---

## Definition

Let $k \ge 1$ and let $Y \subseteq \R^k$ be a set of attainable objective vectors, for example $Y = F(X)$ for a [[multi-objective problem|E560RGEKPP]] $F \colon X \to \R^k$ to be minimized.
For $y, y' \in \R^k$, the vector $y$ *dominates* $y'$ if $y_i \le y'_i$ for all $i$ and $y \ne y'$.
The *Pareto front* of $Y$ is the set of points of $Y$ that are not dominated by any point of $Y$:
$$\mathcal{P}(Y) = \set{y \in Y : \text{there is no } y' \in Y \text{ with } y'_i \le y_i \text{ for all } i \text{ and } y' \ne y}.$$

## Remarks

For $Y = F(X)$, the Pareto front is the image of the set of Pareto optimal points.
For maximization problems the inequalities are reversed.

Example: $Y = \set{(1, 4), (2, 2), (3, 3), (4, 1)}$.
The point $(3, 3)$ is dominated by $(2, 2)$.
None of the points $(1, 4)$, $(2, 2)$ and $(4, 1)$ dominates another, so the Pareto front is $\set{(1, 4), (2, 2), (4, 1)}$.

Non-example: for the disk $Y = \set{y \in \R^2 : y_1^2 + y_2^2 \le 1}$, the point $(0, 0)$ is not on the front, because $(-1/2, -1/2) \in Y$ dominates it.
The front of the disk is the arc $\set{(\cos t, \sin t) : \pi \le t \le 3\pi/2}$.
