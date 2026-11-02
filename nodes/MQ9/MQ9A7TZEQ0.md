---
tag: MQ9A7TZEQ0
kind: definition
name: Simple Lie group
msc: ["22E46", "22E15", "22E10"]
defines: AM7YJP8AR6
uses: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_Lie_group
---

## Definition

Let $G$ be a connected real or complex [[Lie group|7JBRGCVJRB]], and let $\mathfrak{g}$ be its Lie algebra.
The group $G$ is a *simple Lie group* if $\mathfrak{g}$ is a simple Lie algebra, that is:

1. $\mathfrak{g}$ is not abelian, and
2. the only ideals of $\mathfrak{g}$ are $0$ and $\mathfrak{g}$.

## Remarks

Example: $G = SU(2)$, with Lie algebra $\mathfrak{su}(2) \cong \R^3$ and the cross product as bracket.
The bracket is not identically zero, so clause 1 holds.
If an ideal $I$ contains $x \ne 0$, it contains $x \times y$ for all $y$, and these vectors fill the plane $x^\perp$.
The cross product of two independent vectors of that plane is a nonzero multiple of $x$, so $I = \R^3$, and clause 2 holds.

Non-example: $G = U(n)$ with $n \ge 2$.
Its Lie algebra $\mathfrak{u}(n)$ of skew-Hermitian matrices contains the ideal $i\R\, I_n$ of scalar matrices, which is neither $0$ nor $\mathfrak{u}(n)$, so clause 2 fails.
For $n = 1$ the group $U(1)$ is abelian, so clause 1 fails.

For connected $G$, the connected normal Lie subgroups of $G$ correspond to the ideals of $\mathfrak{g}$.
So $G$ is simple exactly when it is not abelian and has no connected normal Lie subgroups other than $\set{e}$ and $G$.
A simple Lie group may have a nontrivial discrete centre, so it need not be a simple group in the sense of abstract group theory.
Some authors also require the centre to be trivial or finite.
