---
tag: YGHYD555Y7
kind: definition
name: Projective object
msc: [18G05]
defines: YXMXAGVC1Q
uses: [A2DE66937D, 859F0TFVA3, RVXDSY04KG, VJXS8AK67E, Y9CZ3MTNF1, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_object
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
An object $P$ of $\mathcal{C}$ is *projective* if, for every [[epimorphism|RVXDSY04KG]] $e \colon E \to X$ and every [[morphism|859F0TFVA3]] $f \colon P \to X$, there is a morphism $g \colon P \to E$ with $e \circ g = f$.

## Remarks

Equivalently, the [[hom functor|VJXS8AK67E]] $\Hom(P, -)$ sends epimorphisms to surjections of sets.
In an [[abelian category|Y9CZ3MTNF1]], $P$ is projective if and only if $\Hom(P, -)$ is an exact functor to abelian groups, and if and only if every short exact sequence $0 \to A \to B \to P \to 0$ splits.
In the category of modules over a ring, the projective objects are the [[projective modules|BFFA03GE3V]], that is, the direct summands of free modules.
In general categories some authors use only regular or strong epimorphisms in the definition; in abelian categories all these versions agree.

Example: $\Z$ is projective in the category of abelian groups.
Given an epimorphism $e \colon E \to X$ and $f \colon \Z \to X$, choose $u \in E$ with $e(u) = f(1)$, and let $g(n) = nu$; then $e(g(n)) = n f(1) = f(n)$.

Non-example: $\Z/2\Z$ is not projective in the category of abelian groups.
For the reduction $e \colon \Z \to \Z/2\Z$ and $f = 1_{\Z/2\Z}$, a lift $g \colon \Z/2\Z \to \Z$ would have to be $0$, since $\Z$ has no nonzero element of finite order, but then $e \circ g = 0 \ne f$.
