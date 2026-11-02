---
tag: QTVC6F2P9D
kind: statement
role: theorem
name: Pontryagin duality theorem
msc: [43A40, 22B05]
uses: [ZR09S9R3AW, FMW57WNPDB, H1WNVN5V7F]
about: [FMW57WNPDB, ZR09S9R3AW]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]], let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]], and let $\widehat{\widehat{G}}$ be the Pontryagin dual of $\widehat{G}$.
For $x \in G$, define $\alpha_G(x) \in \widehat{\widehat{G}}$ by $\alpha_G(x)(\chi) = \chi(x)$ for all [[characters|H1WNVN5V7F]] $\chi \in \widehat{G}$.
Then the map $\alpha_G \colon G \to \widehat{\widehat{G}}$ is an isomorphism of topological groups.

## Remarks

It is easy to check that $\alpha_G$ is a continuous homomorphism.
Injectivity means that continuous characters separate the points of $G$.
This is a hard step; one proof uses the Gelfand–Raikov theorem, or the Peter–Weyl theorem in the compact case.
Surjectivity and openness are usually proved with the Plancherel theorem, or by reducing to compactly generated groups of the form $\R^n \times \Z^m \times K$ with $K$ compact.
Example: $\widehat{\Z} \cong \mathbb{T}$ and $\widehat{\mathbb{T}} \cong \Z$, where $n \in \Z$ gives the character $z \mapsto z^n$ of $\mathbb{T}$, and the theorem says that $n \mapsto (z \mapsto z^n)$ is the natural isomorphism.
The map $\alpha_G$ is natural in $G$, so duality is a contravariant equivalence of the category of locally compact abelian groups with itself.
The theorem needs local compactness: for general abelian topological groups the dual may fail to be locally compact, and $\alpha_G$ may fail to be an isomorphism.

## Explanations

### L1 human

Every locally compact abelian group has a dual group made of its waves, its continuous characters.
The theorem says that taking the dual twice brings back the original group, in a natural way.
So the group and its dual carry the same information, seen from two sides.
The circle and the integers are dual to each other, and the real line is dual to itself.

### L2 human

Duality turns properties of $G$ into properties of $\widehat{G}$: compact groups have discrete duals, and discrete groups have compact duals.
A compact group is connected exactly when its discrete dual is torsion-free.
Closed subgroups $H \subseteq G$ correspond to closed subgroups of $\widehat{G}$ through annihilators, with $\widehat{G/H}$ equal to the annihilator of $H$.
The theorem is the background of the [[Fourier transform on LCA groups|VHN5VW5Q92]].
The transform turns functions on $G$ into functions on $\widehat{G}$, and duality lets the inverse transform go back from $\widehat{G}$ to $G$.
It also underlies the [[Plancherel theorem for abelian groups|V9K9TG0K3J]] and [[Bochner's theorem|ZRHAG4NXHC]].
