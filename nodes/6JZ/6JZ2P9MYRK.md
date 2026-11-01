---
tag: 6JZ2P9MYRK
kind: definition
name: Representation theory of the symmetric group
msc: [20C30]
defines: 1VQC05EEYW
uses: [0515A6D2Y1, WYGRXCG2RN, FX3NEFYFFN, 0JV30XN73Z, 0DEBXAJ5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_theory_of_the_symmetric_group
---

## Definition

Let $n \ge 1$ be an integer, let $S_n$ be the [[symmetric group|0515A6D2Y1]] on $\set{1, \ldots, n}$, and let $F$ be a field.
A *representation of the symmetric group* $S_n$ over $F$ is a [[group representation|WYGRXCG2RN]] $\rho \colon S_n \to GL(V)$ with $V$ a vector space over $F$.
The *representation theory of the symmetric group* is the study of these representations, of their decomposition into [[irreducible representations|FX3NEFYFFN]], and of their characters.

## Remarks

Example: the sign map $\sgn \colon S_n \to \set{\pm 1} \subseteq GL_1(\C)$ is a representation of degree $1$, because $\sgn(\sigma\tau) = \sgn(\sigma)\sgn(\tau)$.
Non-example: let $\rho \colon S_3 \to GL_1(\C)$ send $1$ to $1$, each transposition to $-1$ and each $3$-cycle to $\omega = e^{2\pi i/3}$.
It is not a representation: the product of the transpositions $(1\,2)$ and $(2\,3)$ is a $3$-cycle, while $(-1)(-1) = 1 \ne \omega$.
Over $\C$, the number of irreducible representations of $S_n$ is the number of [[conjugacy classes|0DEBXAJ5SA]] of $S_n$.
Conjugacy classes correspond to cycle types, so this is the number $p(n)$ of [[partitions|0JV30XN73Z]] of $n$.
The Specht modules $S^\lambda$, for $\lambda$ a partition of $n$, are a complete list of irreducible complex representations, without repetition.
Over a field of characteristic $p$ with $p \le n$, the theory is the modular representation theory of $S_n$, and is much less understood.
