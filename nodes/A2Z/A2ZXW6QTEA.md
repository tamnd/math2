---
tag: A2ZXW6QTEA
kind: definition
name: Dandelin spheres
msc: [51M04, 51N20]
defines: W3DCQ22JA3
uses: [7TPBQPPN97, P9CM4GQ2T0, 00HJCMC2CD, 0VKCCEXBJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Dandelin_spheres
---

## Definition

Let $K$ be a right circular [[cone|7TPBQPPN97]] in $\R^3$ with vertex $V$.
Let $\pi$ be a plane not through $V$ that meets $K$ in a [[conic section|00HJCMC2CD]] $C$.
A *Dandelin sphere* of $K$ and $\pi$ is a [[sphere|P9CM4GQ2T0]] $\Sigma$ such that:

1. $\Sigma$ is tangent to $K$ along a circle, that is, $\Sigma$ is inscribed in $K$;
2. $\Sigma$ is tangent to the plane $\pi$ at one point.

## Remarks

When $C$ is an [[ellipse|0VKCCEXBJ1]] there are exactly two Dandelin spheres, one on each side of $\pi$.
For a hyperbola there are two, one in each nappe, and for a parabola there is one.
Check of the focal property for an ellipse: let $\Sigma_1, \Sigma_2$ touch $\pi$ at $F_1, F_2$ and touch $K$ along circles $c_1, c_2$.
For $P \in C$, the generator line $VP$ meets $c_1$ and $c_2$ at points $Q_1, Q_2$.
Two tangent segments from $P$ to the same sphere have the same length, so $PF_1 = PQ_1$ and $PF_2 = PQ_2$.
Hence $PF_1 + PF_2 = Q_1 Q_2$, which is the distance between the parallel circles $c_1$ and $c_2$ measured along a generator, the same for all $P$; so $C$ is an ellipse with foci $F_1, F_2$.
When $C$ is not a circle, the plane of each circle $c_i$ meets $\pi$ in a line, which is the directrix belonging to the focus $F_i$.
Non-example: take a small sphere inscribed in $K$ near the vertex, on the vertex side of $\pi$ and far from it.
It is tangent to $K$ along a circle but does not touch $\pi$, so clause 2 fails.
