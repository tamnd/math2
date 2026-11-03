---
tag: A7H11C2JMM
kind: object
name: Witt algebra
msc: [17B68, 17B66, 17B65]
instance_of: [5JJYBJ6A8K]
uses: [5JJYBJ6A8K, QMY5JTZZB8, 68FGQEBD6J, 1ZAT1Z967A]
sources:
  - url: https://en.wikipedia.org/wiki/Witt_algebra
same_as:
  wikidata: Q444054
  wikipedia: Witt algebra
---

## Description

The *Witt algebra* $W$ is the complex [[Lie algebra|5JJYBJ6A8K]] with basis $\set{L_n : n \in \Z}$ and bracket
$$[L_m, L_n] = (m - n)\, L_{m+n}, \qquad m, n \in \Z.$$
It is realized by the derivations of the [[Laurent polynomial ring|QMY5JTZZB8]] $\C[z, z^{-1}]$, with $L_n = -z^{n+1} \frac{d}{dz}$.

Check of the bracket: for vector fields $u\, \frac{d}{dz}$ and $v\, \frac{d}{dz}$ the [[bracket|68FGQEBD6J]] is $(u v' - v u') \frac{d}{dz}$.
With $u = -z^{m+1}$ and $v = -z^{n+1}$ this gives $\big((n+1) - (m+1)\big) z^{m+n+1} \frac{d}{dz} = (m - n)\left(-z^{m+n+1} \frac{d}{dz}\right) = (m - n) L_{m+n}$.
Since the bracket of vector fields is antisymmetric and satisfies the Jacobi identity, so does the bracket of $W$.

The elements $L_{-1}, L_0, L_1$ span a subalgebra isomorphic to [[$\mathfrak{sl}_2(\C)$|1ZAT1Z967A]]: indeed $[L_1, L_{-1}] = 2L_0$ and $[L_0, L_{\pm 1}] = \mp L_{\pm 1}$.
The element $L_0$ acts diagonally: $[L_0, L_n] = -n L_n$, so $W$ is graded by $\Z$.

## Remarks

Up to isomorphism, the Witt algebra has exactly one nontrivial one-dimensional central extension, the Virasoro algebra.
The name also refers to a related finite-dimensional Lie algebra over a field of characteristic $p > 0$: the Lie algebra of derivations of the truncated polynomial ring $k[z]/(z^p)$, of dimension $p$.

## Explanations

### L1 human

The Witt algebra is the Lie algebra of polynomial vector fields on the circle, written with the complex coordinate $z$.
Its basis vector fields $L_n$ are indexed by all integers, so it is infinite-dimensional.
The bracket rule $[L_m, L_n] = (m - n) L_{m+n}$ is simple enough to compute by hand.
It describes the infinitesimal symmetries of a circle under smooth changes of coordinate, which is why it appears in two-dimensional conformal field theory.
