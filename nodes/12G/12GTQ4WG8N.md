---
tag: 12GTQ4WG8N
kind: definition
name: Geometric measure theory
msc: [49Q15, 28A75, 49Q20]
defines: JW431VDN08
uses: [Q1TGZK8RN6, 7N0GFMW05R, 360H7MD9RD, N3QA80M44M, 0QNVQ4VD9T]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_measure_theory
---

## Definition

Let $n \ge 1$ and $0 \le m \le n$.
For $E \subseteq \R^n$, let $\mathcal{H}^m(E)$ be its $m$-dimensional [[Hausdorff measure|Q1TGZK8RN6]].
A set $E \subseteq \R^n$ is *countably $m$-rectifiable* if there are [[Lipschitz maps|0QNVQ4VD9T]] $f_j \colon \R^m \to \R^n$, $j = 1, 2, \dots$, with $\mathcal{H}^m\left( E \setminus \bigcup_j f_j(\R^m) \right) = 0$.
*Geometric measure theory* is the branch of analysis that studies:

1. the measure-theoretic structure of subsets of $\R^n$ and of Riemannian manifolds, measured by Hausdorff measures, in particular the [[rectifiable sets|7N0GFMW05R]] and their approximate tangent planes;
2. generalised surfaces built from them, such as [[currents|360H7MD9RD]] and [[varifolds|N3QA80M44M]];
3. variational problems for these objects, such as the minimisation of area, with the existence and regularity of their solutions.

## Remarks

The rectifiable sets are the sets on which the tools of calculus, such as tangent planes and the area formula, still work almost everywhere.

Example: the graph $E = \set{(x, \abs{x}) : x \in [-1, 1]}$ in $\R^2$ is $1$-rectifiable, since it is the image of a Lipschitz map of an interval, and $\mathcal{H}^1(E) = 2\sqrt{2}$.
Its tangent line exists at every point except the corner $(0, 0)$.

Non-example: the four-corner Cantor set in $\R^2$, obtained by keeping repeatedly the four corner squares of side $1/4$ of each square, has $0 < \mathcal{H}^1 < \infty$.
It is purely $1$-unrectifiable: it meets every Lipschitz image of $\R$ in a set of $\mathcal{H}^1$-measure $0$.

## Explanations

### L1 human

Geometric measure theory measures the size of rough sets and builds generalised surfaces from them, so that problems such as finding a least-area surface always have solutions.
