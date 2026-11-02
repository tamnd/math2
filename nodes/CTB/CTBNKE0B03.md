---
tag: CTBNKE0B03
kind: definition
name: p-adic Lie group
msc: ["22E20", "22E35", "20E18"]
defines: 3AKM6EPV2F
uses: [92700QAB5Y, BT6T702C28, 0MZB06ST2B]
sources:
  - url: https://en.wikipedia.org/wiki/Pro-p_group
---

## Definition

Let $p$ be a prime and let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]].
Let $U \subseteq \Q_p^n$ be open.
A map $f \colon U \to \Q_p^m$ is *analytic* if each point of $U$ has an open neighbourhood on which each coordinate of $f$ is a convergent [[power series|0MZB06ST2B]].
A *$p$-adic analytic manifold* of dimension $n$ is a Hausdorff space $M$ with an atlas of charts.
The charts are homeomorphisms from open sets of $M$ onto open sets of $\Q_p^n$, and their transition maps are analytic.
A *$p$-adic Lie group* is a group $G$ with the structure of a $p$-adic analytic manifold such that:

1. the multiplication $G \times G \to G$, $(x, y) \mapsto xy$, is analytic;
2. the inversion $G \to G$, $x \mapsto x^{-1}$, is analytic.

## Remarks

Example: the group $\Z_p$ of $p$-adic integers under addition is an open subset of $\Q_p$, so the identity map is a chart.
Addition $(x, y) \mapsto x + y$ and negation $x \mapsto -x$ are polynomials, hence analytic.
So $\Z_p$ is a $p$-adic Lie group of dimension $1$.
The group $GL_n(\Q_p)$ is open in the space $\Q_p^{n^2}$ of matrices.
Its product and inverse are rational in the entries with nonvanishing denominators, so it is a $p$-adic Lie group of dimension $n^2$.

Non-example: the additive group $\R$ is not a $p$-adic Lie group with its usual topology.
Every open subset of $\Q_p^n$ is totally disconnected, so every $p$-adic analytic manifold is totally disconnected.
But $\R$ is connected and has more than one point.

Such groups are also called $p$-adic analytic groups.
Every $p$-adic Lie group is a totally disconnected locally compact Hausdorff group.
