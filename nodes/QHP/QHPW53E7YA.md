---
tag: QHPW53E7YA
kind: definition
name: Steiner system
msc: [05B05, "51E10"]
defines: 7BPSC4T4M3
uses: [TGZATGBHTH, 0BBTH3YSZA]
sources:
  - url: https://en.wikipedia.org/wiki/Steiner_system
---

## Definition

Let $t, k, n$ be positive integers with $t < k < n$.
A Steiner system $S(t, k, n)$ is a pair $(X, \mathcal{B})$ where $X$ is a [[finite set|0BBTH3YSZA]] with $n$ elements.
The family $\mathcal{B}$ is a set of $k$-element subsets of $X$, called blocks.
The condition is that each $t$-element subset of $X$ is contained in exactly one block.

## Remarks

Equivalently, a Steiner system $S(t, k, n)$ is a $t$-$(n, k, 1)$ [[block design|TGZATGBHTH]].
Counting $t$-sets gives the number of blocks: $\binom{n}{t} / \binom{k}{t}$.
Example: on the $9$ points of the grid $(\Z/3\Z)^2$, the $12$ lines of the affine plane form an $S(2, 3, 9)$.
Two distinct points $p, q$ lie on exactly one line, namely $\set{p, q, -p - q}$.
Non-example: there is no $S(2, 3, 8)$.
In an $S(2, 3, n)$, the blocks through a point split the other $n - 1$ points into pairs, so $n - 1$ must be even, and $8 - 1 = 7$ is odd.
An $S(2, 3, n)$ is a Steiner triple system; for $n \ge 7$, one exists if and only if $n \equiv 1$ or $3 \pmod 6$.
A [[finite projective plane|2HWB7P1DZN]] of order $q$ is an $S(2, q + 1, q^2 + q + 1)$.
