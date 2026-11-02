---
tag: SSWFTA4GP8
kind: statement
role: theorem
name: Whitney's theorem on folds and cusps
msc: [57R45, 58K25, 58K40]
uses: [1JG3HFWX3T, F45VQ47GPV, 7PN9MD1PQB, 0KZZ70ZHXP]
about: [1JG3HFWX3T]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Statement

Let $M$ be a smooth surface, and give $C^\infty(M, \R^2)$ the [[Whitney $C^\infty$ topology|7PN9MD1PQB]].
The smooth maps $f \colon M \to \R^2$ with the following property form a dense subset of $C^\infty(M, \R^2)$.
At every point $p \in M$, there are local coordinates centred at $p$ and at $f(p)$ in which $f$ has one of these forms:

1. $(x, y) \mapsto (x, y)$, a regular point;
2. $(x, y) \mapsto (x, y^2)$, a fold point;
3. $(x, y) \mapsto (x, y^3 + x y)$, a cusp point.

## Remarks

At a fold point the [[singular set|1JG3HFWX3T]] is a smooth curve and the kernel of the differential is transverse to it.
At a cusp point the kernel is tangent to the singular curve.
For the cusp map $f(x, y) = (x, y^3 + xy)$ the singular set is the parabola $x = -3y^2$, and its image is the cusp curve $(-3y^2, -2y^3)$, which satisfies $27 v^2 = -4 u^3$ in the target coordinates $(u, v)$.
The proof uses transversality of the jet of $f$ to the subsets of the jet space defined by these singularities.
Worse singularities have codimension greater than $2$, so generic maps of a surface avoid them.
Both the fold and the cusp are stable germs, so they cannot be removed by small perturbations.
The theorem is due to Whitney and was a starting point of the theory of [[stable maps|1991WETZF9]].

## Explanations

### L1 human

Project a smooth surface onto a plane, as when you look at a curved object and see its outline.
Whitney's theorem says that, after a tiny wiggle of the surface, only two kinds of special points appear.
Along fold curves the surface turns over like the edge of a folded sheet of paper.
At isolated cusp points a fold curve stops, and its outline forms a sharp spike.
Nothing more complicated is typical.

### L2 human

This is the first nontrivial case of the classification of generic singularities of maps between manifolds of equal dimension.
In the language of [[Thom–Boardman singularities|A9TYDPD5D7]], folds are the $\Sigma^{1,0}$ points and cusps are the $\Sigma^{1,1,0}$ points.
Higher-dimensional analogues are the [[Morin singularities|DF8CJ1A9MF]], and the fold and cusp reappear in [[catastrophe theory|6FKJ6SXP3G]] as the fold and cusp catastrophes.
