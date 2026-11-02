---
tag: GQG0VMXER2
kind: definition
name: Algebraic dimension
msc: [32J10, 32J18]
defines: F0GF0JEZTG
uses: [JSGWAN2RJV, W6FTSF57T1, D7TR0YWR9H, 0TVJZYB6SH, 0V032VWTHD]
sources:
  - url: https://en.wikipedia.org/wiki/Moishezon_manifold
---

## Definition

Let $X$ be a [[compact|0TVJZYB6SH]], [[connected|0V032VWTHD]] [[complex manifold|JSGWAN2RJV]].
Let $\mathcal{M}(X)$ be the set of [[meromorphic functions|W6FTSF57T1]] on $X$; with pointwise operations it is a field that contains $\C$ as the constant functions.
The *algebraic dimension* of $X$ is
$$a(X) = \operatorname{trdeg}_\C \mathcal{M}(X),$$
the [[transcendence degree|D7TR0YWR9H]] of $\mathcal{M}(X)$ over $\C$.

## Remarks

By [[Siegel's theorem|ENXCWPTG92]], $a(X)$ is an integer with $0 \le a(X) \le \dim X$.

Example: for $X = \mathbb{CP}^n$, the functions $z_1/z_0, \ldots, z_n/z_0$ are meromorphic.
They are algebraically independent over $\C$, because on the chart $\set{z_0 \ne 0} \cong \C^n$ they are the coordinate functions, and a nonzero polynomial does not vanish on all of $\C^n$.
So $a(\mathbb{CP}^n) \ge n$, and by Siegel's bound $a(\mathbb{CP}^n) = n$.

Example: the diagonal [[Hopf surface|PNFNGBXRM3]] has algebraic dimension $1$, and an [[Inoue surface|GPSVJK3R4X]] has algebraic dimension $0$.

Non-example: if $X$ is the disjoint union of two copies of $\mathbb{CP}^1$, the connectedness hypothesis fails.
Then $\mathcal{M}(X)$ is not a field: the function equal to $1$ on one copy and $0$ on the other is a nonzero zero divisor.

The notion extends to irreducible compact complex spaces.
A compact connected complex manifold $X$ with $a(X) = \dim X$ is a [[Moishezon manifold|8ZW9P9JRQD]].
