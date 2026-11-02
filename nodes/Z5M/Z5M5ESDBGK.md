---
tag: Z5M5ESDBGK
kind: definition
name: 3-manifold
msc: [57K30]
defines: R20TB2KEQQ
uses: [QQQ9B1DK4P, 0S1FJ8VEX9, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/3-manifold
---

## Definition

A *$3$-manifold* is a topological space $M$ such that:

1. $M$ is [[Hausdorff|0S1FJ8VEX9]];
2. $M$ is second countable;
3. every point of $M$ has an open neighbourhood [[homeomorphic|0QT00PB5G2]] to an open subset of $\R^3$.

Equivalently, it is a [[topological manifold|QQQ9B1DK4P]] of dimension $3$.
A *$3$-manifold with boundary* allows open subsets of the closed half-space $\set{x \in \R^3 : x_3 \ge 0}$ in clause 3, and a *closed* $3$-manifold is a compact one without boundary.

## Remarks

Example: the $3$-torus $T^3 = \R^3 / \Z^3$ is a closed $3$-manifold.
The quotient map $\R^3 \to T^3$ restricted to any open cube of side $1/2$ is a homeomorphism onto an open subset, and $T^3$ is Hausdorff, second countable and compact.

Non-example: the cone $C = (T^2 \times [0, 1]) / (T^2 \times \set{0})$ on the torus fails clause 3 at the cone point $v$.
The local homology group $H_3(C, C \setminus \set{v})$ is $\tilde H_2(T^2) \cong \Z$, which matches $\R^3$, but $H_2(C, C \setminus \set{v}) \cong \tilde H_1(T^2) \cong \Z^2$, while at a point of $\R^3$ this group is $0$.

Other standard examples are the $3$-sphere $S^3$, the [[lens spaces|AZBTMF196E]] and the [[Poincaré homology sphere|NHERCK7C43]].

## Explanations

### L1 human

The definition asks that every point have a small region around it shaped like a piece of ordinary space.
The first two clauses exclude pathological spaces.
Gluing opposite faces of a cube gives an example with no edge or corner anywhere.
A cone on a torus is not an example, because the tip of the cone does not look like a point of space.
