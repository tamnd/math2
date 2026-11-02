---
tag: KCP52TPREW
kind: definition
name: Lie groupoid
msc: [22A22, 58H05]
defines: HNVW0E732J
uses: [FH3C0T643F, F45VQ47GPV, 0V33BNKZ9S, 7JBRGCVJRB, 96B4E2GPKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_groupoid
---

## Definition

A *Lie groupoid* $G_1 \rightrightarrows G_0$ is a [[groupoid|FH3C0T643F]] with set of objects $G_0$ and set of arrows $G_1$, with source and target maps $s, t \colon G_1 \to G_0$, such that:

1. $G_0$ and $G_1$ are [[smooth manifolds|F45VQ47GPV]];
2. $s$ and $t$ are [[smooth|0V33BNKZ9S]] submersions;
3. the composition $m \colon G_1 \times_{G_0} G_1 \to G_1$, defined on pairs $(h, g)$ with $s(h) = t(g)$, is smooth;
4. the unit map $u \colon G_0 \to G_1$, sending $x$ to the identity arrow at $x$, and the inversion $i \colon G_1 \to G_1$ are smooth.

Since $s$ and $t$ are submersions, the set $G_1 \times_{G_0} G_1 = \set{(h, g) \in G_1 \times G_1 : s(h) = t(g)}$ is an embedded submanifold of $G_1 \times G_1$, so clause 3 makes sense.

## Remarks

Example: a [[Lie group|7JBRGCVJRB]] $G$ is a Lie groupoid $G \rightrightarrows \set{*}$ with one object; the maps $s$ and $t$ to a point are submersions, and composition is the group product.

Example: for a smooth [[action|96B4E2GPKJ]] of a Lie group $G$ on a manifold $M$, the action groupoid has $G_0 = M$, $G_1 = G \times M$, $s(g, x) = x$, $t(g, x) = g \cdot x$, and $(h, g \cdot x)(g, x) = (hg, x)$.

Non-example: the compact group $(\Z/2)^{\N}$, viewed as a groupoid with one object, is not a Lie groupoid.
Its space of arrows is not a manifold: it is totally disconnected but has no isolated points, so it is not locally Euclidean of any dimension.

Some authors allow $G_1$ to be a non-Hausdorff manifold, which is needed for groupoids arising from foliations.
