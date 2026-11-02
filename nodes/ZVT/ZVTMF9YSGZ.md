---
tag: ZVTMF9YSGZ
kind: definition
name: Quiver
msc: [16G20, 05C20]
defines: RE9YFFS3TS
uses: [0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Quiver_(mathematics)
---

## Definition

A *quiver* is a quadruple $Q = (Q_0, Q_1, s, t)$ where:

1. $Q_0$ is a set, whose elements are the *vertices*;
2. $Q_1$ is a set, whose elements are the *arrows*;
3. $s, t \colon Q_1 \to Q_0$ are maps, sending an arrow $a$ to its *source* $s(a)$ and its *target* $t(a)$.

One writes $a \colon i \to j$ when $s(a) = i$ and $t(a) = j$.
The quiver is *finite* if $Q_0$ and $Q_1$ are finite.

## Remarks

Example: the Kronecker quiver has $Q_0 = \set{1, 2}$, $Q_1 = \set{a, b}$ and $s(a) = s(b) = 1$, $t(a) = t(b) = 2$.
It satisfies the definition, though it has two arrows with the same source and target; a simple [[directed graph|0KFYGSHHF5]] would not allow this.
A loop is an arrow $a$ with $s(a) = t(a)$, and it is also allowed.
Non-example: an undirected graph is not a quiver as it stands, since its edges have no source and target, so clause 3 fails.
Choosing an orientation of each edge turns it into a quiver.
A path of length $n \ge 1$ is a sequence of arrows $a_1, \dots, a_n$ with $t(a_r) = s(a_{r+1})$; there is also a trivial path $e_i$ at each vertex $i$.
In Mathlib, `Quiver` is a class on a type of vertices, with a type of arrows for each pair of vertices.
