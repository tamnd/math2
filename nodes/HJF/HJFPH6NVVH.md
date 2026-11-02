---
tag: HJFPH6NVVH
kind: definition
name: Minkowski plane
msc: [51B20]
defines: VB2D03PD9Y
uses: [FGKNAFNHA3]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_plane
---

## Definition

A *Minkowski plane* is an [[incidence structure|FGKNAFNHA3]] $(\mathcal{P}, \mathcal{Z}, \in)$ of points and circles, where circles are subsets of $\mathcal{P}$.
It comes with two equivalence relations $\parallel_+$ and $\parallel_-$ on $\mathcal{P}$.
Two points are *parallel* if they are $(+)$-parallel or $(-)$-parallel.
The following conditions hold:

1. for any points $P, Q$ there is exactly one point $R$ with $P \parallel_+ R$ and $R \parallel_- Q$;
2. for every circle $z$, every point $P$ and each sign $\pm$, exactly one point of $z$ is $(\pm)$-parallel to $P$;
3. any three pairwise non-parallel points lie on exactly one circle;
4. for every circle $z$, every point $P \in z$ and every point $Q \notin z$ not parallel to $P$, there is exactly one circle $z'$ with $P, Q \in z'$ and $z \cap z' = \set{P}$;
5. every circle has at least three points, and there is a circle $z$ and a point not on $z$.

## Remarks

Example: let $L = \R \cup \set{\infty}$ be the real projective line.
The classical real Minkowski plane has points $L \times L$, with $(x_1, y_1) \parallel_+ (x_2, y_2)$ when $x_1 = x_2$ and $(x_1, y_1) \parallel_- (x_2, y_2)$ when $y_1 = y_2$.
Its circles are the graphs of the maps $x \mapsto (ax + b)/(cx + d)$ of $L$ with $ad - bc \ne 0$.
Clause 1 holds with $R = (x_1, y_2)$, and clause 2 holds because each circle is the graph of a bijection of $L$.
Clause 3 holds because for distinct $x_1, x_2, x_3$ and distinct $y_1, y_2, y_3$ there is exactly one such map with $x_i \mapsto y_i$.

Non-example: the same points and parallelisms with the graphs of all bijections of $L$ as circles fail clause 3, since many bijections take three given values at three given points.

Equivalently, the classical plane comes from a hyperboloid of one sheet.
Its circles are the plane sections that contain no line of the hyperboloid, and its two families of lines give the parallel classes.
