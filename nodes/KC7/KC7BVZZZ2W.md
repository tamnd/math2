---
tag: KC7BVZZZ2W
kind: definition
name: Postnikov tower
msc: [55S45, 55P20]
defines: EKGEZGHYBW
uses: [0WB6DH499T, P976WYEFMB, AJHEYJE5XY]
sources:
  - url: https://en.wikipedia.org/wiki/Postnikov_system
---

## Definition

Let $X$ be a [[path-connected space|0WB6DH499T]] with base point, and let $\pi_k$ denote the $k$-th [[homotopy group|P976WYEFMB]].
A *Postnikov tower* of $X$ is a sequence of pointed path-connected spaces $X_n$, $n \ge 1$, with pointed maps $f_n \colon X \to X_n$ and $p_{n} \colon X_{n} \to X_{n-1}$ for $n \ge 2$, such that:

1. $p_n \circ f_n = f_{n-1}$ for all $n \ge 2$.
2. $f_n$ induces an isomorphism $\pi_k(X) \to \pi_k(X_n)$ for all $k \le n$.
3. $\pi_k(X_n) = 0$ for all $k > n$.

## Remarks

Every path-connected CW complex has a Postnikov tower, built by attaching cells of dimension at least $n + 2$ to $X$ to kill $\pi_k$ for $k > n$.
Up to homotopy, $p_n$ can be taken to be a fibration, and then its fibre is an [[Eilenberg–MacLane space|AJHEYJE5XY]] $K(\pi_n(X), n)$.
The map from $X$ to the homotopy limit of the tower is a weak homotopy equivalence.

Example: let $X = K(G, m)$.
Take $X_n$ a point for $n < m$ and $X_n = X$ for $n \ge m$, with the evident maps.
Clause 2 holds since $\pi_k(X) = 0$ for $k < m$, and clause 3 holds since $\pi_k(X) = 0$ for $k > m$.

Non-example: for $X = S^2$, the choice $X_2 = S^2$ with $f_2 = \id$ fails clause 3, since $\pi_3(S^2) \cong \Z \ne 0$.
A valid choice is $X_2 = \C P^\infty$, a $K(\Z, 2)$.
