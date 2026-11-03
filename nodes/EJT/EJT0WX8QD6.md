---
tag: EJT0WX8QD6
kind: statement
role: theorem
name: Cartan's criterion
msc: [17B20, 17B30]
uses: [5JJYBJ6A8K, TWVQT18JXE, W7A2R0GR3T, EY9DN7QAX1, 1ZB13N78XW, G8FEGYDSNE, WKSSTQ69AK, 0KZDNGA561, 01NHFZF2SK, 1ZAT1Z967A]
about: [TWVQT18JXE, W7A2R0GR3T, EY9DN7QAX1]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan%27s_criterion
same_as:
  wikidata: Q5047038
  wikipedia: Cartan's criterion
---

## Statement

Let $k$ be a field of [[characteristic|1ZB13N78XW]] $0$, and let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over $k$ with [[Killing form|TWVQT18JXE]] $\kappa$.

1. Let $V$ be a finite-dimensional vector space over $k$ and let $\mathfrak g$ be a [[subalgebra|WKSSTQ69AK]] of $\mathfrak{gl}(V)$, the [[general linear Lie algebra|G8FEGYDSNE]]. If $\tr(xy) = 0$ for all $x \in [\mathfrak g, \mathfrak g]$ and $y \in \mathfrak g$, then $\mathfrak g$ is [[solvable|W7A2R0GR3T]]. Here $\tr$ is the [[trace|0KZDNGA561]] on $V$.
2. The Lie algebra $\mathfrak g$ is solvable if and only if $\kappa(x, y) = 0$ for all $x \in [\mathfrak g, \mathfrak g]$ and $y \in \mathfrak g$.
3. The Lie algebra $\mathfrak g$ is [[semisimple|EY9DN7QAX1]] if and only if $\kappa$ is [[nondegenerate|01NHFZF2SK]].

## Remarks

For part 1 one may extend scalars to an algebraic closure and show that each $x \in [\mathfrak g, \mathfrak g]$ is nilpotent; Engel's theorem then makes $[\mathfrak g, \mathfrak g]$ nilpotent, so $\mathfrak g$ is solvable.
Let $\lambda_1, \dots, \lambda_n$ be the eigenvalues of $x$, and let $\varphi$ be a $\Q$-linear map from their $\Q$-span to $\Q$.
Using the Jordan decomposition, the trace condition gives $\sum_i \varphi(\lambda_i) \lambda_i = 0$.
Applying $\varphi$ gives $\sum_i \varphi(\lambda_i)^2 = 0$, so $\varphi = 0$; as $\varphi$ is arbitrary, all $\lambda_i = 0$.
Part 2 follows from part 1 applied to the image of $\operatorname{ad}$, together with Lie's theorem for the converse.
For part 3, the radical $\set{x : \kappa(x, \mathfrak g) = 0}$ of $\kappa$ is an ideal on which $\kappa$ vanishes, hence solvable by part 2.
Conversely, every abelian ideal lies in the radical of $\kappa$.

Example: on the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2(k)$ with basis $e, h, f$, one has $\kappa(e, f) = 4$, $\kappa(h, h) = 8$, and the other pairings of basis vectors are $0$.
The Gram matrix has determinant $-128 \ne 0$, so $\mathfrak{sl}_2(k)$ is semisimple by part 3.

The direction "nondegenerate implies semisimple" in part 3 holds in every characteristic.
The other implications use characteristic $0$ in the trace argument above.

## Explanations

### L1 human

Cartan's criterion turns two structural questions about a Lie algebra into computations with one bilinear form, the Killing form.
The algebra is solvable when the form vanishes on brackets.
The algebra is semisimple when the form has no nonzero element orthogonal to everything.
Both are finite linear algebra checks once a basis and the brackets are known.

### L2 human

Part 3 is the usual entry point to semisimple Lie algebras.
From it one gets that a semisimple Lie algebra in characteristic $0$ is a direct sum of simple ideals.
One also gets that every derivation of it is inner.
The nondegenerate Killing form identifies a Cartan subalgebra with its dual, which puts an inner product on the real span of the roots and leads to root systems.
