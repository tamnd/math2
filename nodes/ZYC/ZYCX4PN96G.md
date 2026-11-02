---
tag: ZYCX4PN96G
kind: definition
name: Whitehead tower
msc: [55S45, 55P20]
defines: D3649AJ30F
uses: [0WB6DH499T, P976WYEFMB, 1A943BWBQT, AJHEYJE5XY, Y1YPE6PM52, EKGEZGHYBW]
sources:
  - url: https://en.wikipedia.org/wiki/Postnikov_system
---

## Definition

Let $X$ be a [[path-connected space|0WB6DH499T]] with base point, and let $\pi_k$ denote the $k$-th [[homotopy group|P976WYEFMB]].
A *Whitehead tower* of $X$ is a sequence of pointed spaces $X\langle n \rangle$, $n \ge 0$, with $X\langle 0 \rangle = X$.
It comes with pointed maps $q_n \colon X\langle n \rangle \to X\langle n - 1 \rangle$ for $n \ge 1$.
For each $n \ge 0$, the composite $r_n = q_1 \circ \cdots \circ q_n \colon X\langle n \rangle \to X$ must satisfy:

1. $X\langle n \rangle$ is [[$n$-connected|1A943BWBQT]], that is, $\pi_k(X\langle n \rangle) = 0$ for all $k \le n$.
2. $r_n$ induces an isomorphism $\pi_k(X\langle n \rangle) \to \pi_k(X)$ for all $k > n$.

The space $X\langle n \rangle$ is the *$n$-connected cover* of $X$.

## Remarks

For a CW complex $X$ a Whitehead tower exists and each $X\langle n \rangle$ is unique up to weak homotopy equivalence over $X$.
Up to homotopy, $q_n$ can be taken to be a fibration, and then its fibre is an [[Eilenberg–MacLane space|AJHEYJE5XY]] $K(\pi_n(X), n - 1)$.
For $X$ a CW complex, $X\langle 1 \rangle \to X$ is the [[universal cover|Y1YPE6PM52]].
The tower is dual to the [[Postnikov tower|EKGEZGHYBW]]: $X\langle n \rangle$ is the homotopy fibre of $X \to X_n$.

Example: for $X = S^3$, $X\langle 1 \rangle = X\langle 2 \rangle = S^3$, since $S^3$ is $2$-connected.
The cover $S^3\langle 3 \rangle \to S^3$ is a fibration with fibre $K(\Z, 2) = \C P^\infty$.

Non-example: for $X = S^1$, the identity $S^1 \to S^1$ as $X\langle 1 \rangle$ fails clause 1, since $\pi_1(S^1) \cong \Z \ne 0$.
The universal cover $\R \to S^1$ satisfies both clauses.
