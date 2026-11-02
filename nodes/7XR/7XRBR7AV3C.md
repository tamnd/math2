---
tag: 7XRBR7AV3C
kind: definition
name: Classifying space of a group
msc: [55R35, 20J06]
defines: WA796ZCNRX
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Classifying_space
---

## Definition

Let $G$ be a [[group|G5S1M9]], viewed as a discrete group.
A *classifying space* of $G$ is a path-connected [[CW complex|5W95QFHXPR]] $X$ such that:

1. The [[fundamental group|S1XK3HXHFX]] $\pi_1(X)$ is isomorphic to $G$.
2. The [[homotopy group|P976WYEFMB]] $\pi_n(X)$ is trivial for every $n \ge 2$.

Such a space is written $BG$.

## Remarks

A classifying space of $G$ is the same as an [[Eilenberg–MacLane space|AJHEYJE5XY]] $K(G, 1)$.
Any two classifying spaces of $G$ are [[homotopy equivalent|XZG6MTSWCN]].
Equivalently, $X$ is path-connected, $\pi_1(X) \cong G$, and its [[universal cover|Y1YPE6PM52]] is [[contractible|R5WP8Z69Q8]]; then $G$ acts freely on the universal cover and $X$ is the quotient.

Example: the circle $S^1$ is a classifying space of $\Z$.
Its fundamental group is $\Z$, and its universal cover $\R$ is contractible, so $\pi_n(S^1) = 0$ for $n \ge 2$.
In the same way, the torus is a classifying space of $\Z^2$, and the infinite real projective space $\R P^\infty$ is one of $\Z/2\Z$.

Non-example: the real projective plane $\R P^2$ has fundamental group $\Z/2\Z$, but its universal cover is the sphere $S^2$, so $\pi_2(\R P^2) \cong \pi_2(S^2) \cong \Z$.
Clause 2 fails, so $\R P^2$ is not a classifying space of $\Z/2\Z$.
