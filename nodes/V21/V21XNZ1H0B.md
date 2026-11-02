---
tag: V21XNZ1H0B
kind: statement
role: theorem
name: Tverberg's theorem
msc: [52A35, 52A37]
uses: [0XPR1E85W0, 0FQSDC2EQ2, 08QMKTWF9T, 888R24ZGNY, X5GS407VP8]
about: [0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Tverberg%27s_theorem
same_as:
  wikidata: Q7857350
  wikipedia: Tverberg's theorem
---

## Statement

Let $d \ge 1$ and $r \ge 2$ be integers, and let $X \subseteq \R^d$ be a finite set with at least $(r - 1)(d + 1) + 1$ points.
Then $X$ can be [[partitioned|08QMKTWF9T]] into $r$ disjoint sets $X_1, \dots, X_r$ whose [[convex hulls|0FQSDC2EQ2]] have a common point:
$$\operatorname{conv}(X_1) \cap \cdots \cap \operatorname{conv}(X_r) \ne \emptyset.$$

## Remarks

For $r = 2$ the bound is $d + 2$, and the theorem is [[Radon's theorem|888R24ZGNY]].

Example: with $d = 2$ and $r = 3$, any $7$ points in the plane can be split into three groups whose convex hulls share a point.
For instance, take the vertices of a large triangle, the vertices of a smaller triangle with the same centroid $c$, and the point $c$ itself.
The three groups formed by the large triangle, the small triangle and $\set{c}$ all have $c$ in their convex hulls.

The bound $(r - 1)(d + 1) + 1$ is sharp: there are sets of $(r - 1)(d + 1)$ points in $\R^d$ with no such partition.

Proof idea: Tverberg's original proof was a direct geometric argument.
A shorter proof by Sarkaria lifts the points to a space of dimension $(r - 1)(d + 1)$ using tensor products with vectors that sum to $0$, and applies the [[colorful Carathéodory theorem|X5GS407VP8]] there.

## Explanations

### L1 human

Radon's theorem splits enough points into two groups whose shapes overlap.
Tverberg's theorem does the same for any number $r$ of groups, all overlapping in one common point.
In the plane, seven points always split into three overlapping groups, and $3(r - 1) + 1$ points split into $r$ such groups.

### L2 human

A common point of a Tverberg partition is a kind of multidimensional median of the set, which links the theorem to the centerpoint theorem.
The topological Tverberg conjecture asked whether continuous maps of a simplex can replace convex hulls.
It holds when $r$ is a prime power and fails for some other values of $r$.
