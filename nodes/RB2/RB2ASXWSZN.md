---
tag: RB2ASXWSZN
kind: statement
role: theorem
name: Four-point condition for tree metrics
msc: [92D15, "05C05", "54E35"]
uses: [0VKD1TP7F3, 062D9KXJB1, RK58WSHJSG]
about: [0VKD1TP7F3, 062D9KXJB1]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_matrices_in_phylogeny
---

## Statement

Let $X$ be a finite set and let $d$ be a metric on $X$.
Let $T$ be a [[tree|062D9KXJB1]] with positive edge lengths, and let $\varphi$ be an injective map from $X$ to the vertices of $T$.
Say that $(T, \varphi)$ *realizes* $d$ if the following holds.
For all $x, y \in X$, $d(x, y)$ is the total length of the path in $T$ from $\varphi(x)$ to $\varphi(y)$.
Call $d$ a *tree metric* if some such pair $(T, \varphi)$ realizes $d$.
Then $d$ is a tree metric if and only if, for all $x, y, z, w \in X$ (not necessarily distinct),
$$d(x, y) + d(z, w) \le \max\bigl(d(x, z) + d(y, w),\ d(x, w) + d(y, z)\bigr).$$

## Remarks

The inequality says that among the three sums $d(x, y) + d(z, w)$, $d(x, z) + d(y, w)$ and $d(x, w) + d(y, z)$, the two largest are equal.
Necessity: in a tree, four points split into two pairs whose connecting paths are joined by a middle path of length $\ell \ge 0$.
The sum for that pairing is the smallest, and the other two sums both exceed it by $2\ell$.
Sufficiency is proved by induction on $\abs{X}$.
The condition tells where on the tree for $X \setminus \set{x}$ the new point $x$ must be attached, and how long its pendant edge must be.
Example: take a tree with leaves $a, b, c, d$, pendant edges of length $1$, and a middle edge of length $2$ separating $\set{a, b}$ from $\set{c, d}$.
The three sums are $2 + 2 = 4$, $4 + 4 = 8$ and $4 + 4 = 8$.
Non-example: the Euclidean distance on the four corners of a unit square gives the sums $2$, $2$ and $2\sqrt{2}$.
The two largest differ, so this metric is not a tree metric.
Every [[ultrametric|A6DPR620B5]] satisfies the four-point condition.

## Explanations

### L1 human

Some distance tables come from a tree: each distance is the length of the path between two leaves.
The theorem gives a simple test for this using only four points at a time.
Pair up four points in the three possible ways and add the two distances in each pairing.
The table comes from a tree exactly when, for every four points, the two biggest of these three sums are equal.

### L2 human

In [[computational phylogenetics|KYCK3KFM4X]], distances between species estimated from sequences are fitted by trees, and the four-point condition says when an exact fit exists.
When it holds, there is exactly one such tree, up to isomorphism, in which every vertex of degree at most two is the image of a point of $X$.
Methods such as [[neighbor joining|M81NRAZVH0]] recover this tree from the distances.
The condition is weaker than the three-point condition of an [[ultrametric space|A6DPR620B5]], which characterizes trees with a root at equal height above all leaves.
Taking $z = w$ shows that the four-point condition implies the triangle inequality.
