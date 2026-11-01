---
tag: GTHWVEB1NZ
kind: definition
name: Crystallographic group
msc: [20H15, 52C22]
defines: 7KTJKFQT2N
uses: [0H3YY8CPKH, 0XPR1E85W0, 0J1N3WTKM4, 0TVJZYB6SH, 087VJM5Q77, 0TKYAEJ8N7]
sources:
  - url: https://en.wikipedia.org/wiki/Space_group
---

## Definition

Let $n \ge 1$ and let $E(n)$ be the [[Euclidean group|0H3YY8CPKH]] of all [[isometries|0J1N3WTKM4]] of $\R^n$.
Each element of $E(n)$ is a map $x \mapsto Ax + b$ with $A$ in the [[orthogonal group|0TKYAEJ8N7]] $O(n)$ and $b \in \R^n$, and $E(n)$ carries the topology of $O(n) \times \R^n$.
A subgroup $\Gamma$ of $E(n)$ is a *crystallographic group* of dimension $n$ if:

1. $\Gamma$ is a discrete subgroup of $E(n)$.
2. The quotient space $\R^n / \Gamma$ of orbits is [[compact|0TVJZYB6SH]].

## Remarks

Example: the group $\Z^n$ of [[translations|087VJM5Q77]] $x \mapsto x + b$ with $b \in \Z^n$.
It is discrete, since distinct elements differ by a translation of length at least $1$.
The quotient $\R^n / \Z^n$ is the image of the compact cube $[0, 1]^n$, so it is compact; it is the $n$-dimensional torus.

Non-example: the translations $(x, y) \mapsto (x + k, y)$ of $\R^2$ with $k \in \Z$.
This group is discrete, but the quotient is an infinite cylinder, which is not compact, so clause 2 fails.

Equivalently, $\Gamma$ acts properly discontinuously on $\R^n$ with a compact fundamental domain.
Crystallographic groups of dimension $3$ are called space groups, and those of dimension $2$ are the [[wallpaper groups|MY3CBHARYQ]].
