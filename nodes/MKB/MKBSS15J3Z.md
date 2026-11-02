---
tag: MKBSS15J3Z
kind: definition
name: Orientation of a manifold
msc: [57N65, 55M05]
defines: 913WEQERBE
uses: [QQQ9B1DK4P, 4BVWH0BN28, SGHMSBHHA0, 0QJJAQ6ZYZ, F45VQ47GPV, 04AJE0M271, T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Orientability
---

## Definition

Let $M$ be a [[topological manifold|QQQ9B1DK4P]] of dimension $n \ge 1$, and use integral [[relative homology|4BVWH0BN28]].
For each $x \in M$, the [[excision theorem|SGHMSBHHA0]] gives $H_n(M, M \setminus \set{x}) \cong H_n(\R^n, \R^n \setminus \set{0}) \cong \Z$.
A *local orientation* of $M$ at $x$ is a choice of generator $\mu_x$ of $H_n(M, M \setminus \set{x})$.
An *orientation* of $M$ is a function $x \mapsto \mu_x$ assigning a local orientation to each point, with the following local consistency.
Each $x \in M$ has a chart neighbourhood $U \cong \R^n$ containing an open ball $B$ of finite radius about $x$, and a class $\mu_B \in H_n(M, M \setminus B)$.
For every $y \in B$, the image of $\mu_B$ in $H_n(M, M \setminus \set{y})$ is $\mu_y$.
$M$ is *orientable* if it has an orientation.

## Remarks

A connected orientable manifold has exactly two orientations.
For a [[smooth manifold|F45VQ47GPV]], an orientation in this sense is the same as a choice of [[orientation|0QJJAQ6ZYZ]] of each tangent space $T_x M$ that is locally given by a chart.
It is also the same as an atlas whose transition maps have positive Jacobian determinant.
Replacing $\Z$ by a commutative ring $R$ gives $R$-orientations; every manifold has a unique $\Z/2$-orientation.

Example: the [[sphere|T62369RFH6]] $S^n$ is orientable.
Fix a generator $\mu \in H_n(S^n) \cong \Z$; its image in each $H_n(S^n, S^n \setminus \set{y})$ is a generator, and one takes this image as $\mu_y$.
The condition holds with $\mu_B$ the image of $\mu$ in $H_n(S^n, S^n \setminus B)$ for every chart ball $B$.

Non-example: the open [[Möbius strip|04AJE0M271]] is not orientable.
Following a local orientation once around the central circle returns the opposite generator, so no continuous choice exists.
