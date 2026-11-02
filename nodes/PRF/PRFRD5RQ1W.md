---
tag: PRFRD5RQ1W
kind: definition
name: Subobject classifier
msc: [18B25, 03G30]
defines: NKP5TPQ79X
uses: [A2DE66937D, EK85VSSRMR, Q05K04QJ71, Y2NP1JFR86, FS1FKAE89H, CNCXNWKC6R, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Subobject_classifier
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] with finite limits, and let $1$ be its [[terminal object|EK85VSSRMR]].
A *subobject classifier* is an object $\Omega$ of $\mathcal{C}$ with a morphism $\top \colon 1 \to \Omega$ with the following property.
For every [[monomorphism|Y2NP1JFR86]] $m \colon S \to X$, there is exactly one morphism $\chi_m \colon X \to \Omega$ for which the square
$$\begin{array}{ccc} S & \longrightarrow & 1 \\ {\scriptstyle m}\downarrow & & \downarrow{\scriptstyle \top} \\ X & \xrightarrow{\chi_m} & \Omega \end{array}$$
is a [[pullback|Q05K04QJ71]].
The morphism $\chi_m$ is the *characteristic morphism* of $m$.

## Remarks

Equivalently, when $\mathcal{C}$ is locally small, there is a natural bijection between the [[subobjects|FS1FKAE89H]] of $X$ and $\Hom(X, \Omega)$, and $\Omega$ represents the subobject functor.
Example: in $\mathbf{Set}$, take $\Omega = \set{0, 1}$ and $\top(*) = 1$; for $S \subseteq X$, the unique $\chi$ is the characteristic function, since the pullback of $\set{1}$ along $\chi$ is $\chi^{-1}(1) = S$.
Non-example: the category of [[groups|G5S1M9]] has no subobject classifier.
Its terminal object is the trivial group, so every pullback of $\top \colon 1 \to \Omega$ is the kernel of a homomorphism, which is a normal subgroup.
A subgroup of order $2$ in $S_3$ is not normal, so it is not classified.
In a presheaf category $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$, the object $\Omega(c)$ is the set of [[sieves|CNCXNWKC6R]] on $c$, and $\top$ picks the maximal sieves.
