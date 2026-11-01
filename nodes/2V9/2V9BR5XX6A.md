---
tag: 2V9BR5XX6A
kind: statement
role: theorem
name: Matlis duality
msc: [13C11, 13J10]
uses: [G9Q61B8A7C, NJ3APQ8BHH, QCJN05GN64, AK1ZRCXR32, YQNZTQGP1X, 0670T59HGE]
about: [QCJN05GN64, G9Q61B8A7C]
sources:
  - url: https://en.wikipedia.org/wiki/Matlis_duality
same_as:
  wikidata: Q6787678
  wikipedia: Matlis duality
---

## Statement

Let $(R, \mathfrak{m}, k)$ be a [[complete local ring|G9Q61B8A7C]] that is [[Noetherian|0670T59HGE]], with maximal ideal $\mathfrak{m}$ and [[residue field|NJ3APQ8BHH]] $k$.
Let $E = E_R(k)$ be the [[injective hull|QCJN05GN64]] of $k$, and for an $R$-module $M$ write $M^\vee = \Hom_R(M, E)$.
Then:

1. If $M$ is a [[Noetherian module|AK1ZRCXR32]], then $M^\vee$ is an [[Artinian module|YQNZTQGP1X]].
2. If $M$ is an Artinian module, then $M^\vee$ is a Noetherian module.
3. If $M$ is Noetherian or Artinian, then the natural map $M \to M^{\vee\vee}$ is an isomorphism.

Hence $M \mapsto M^\vee$ is an anti-equivalence between the category of Noetherian $R$-modules and the category of Artinian $R$-modules.

## Remarks

The key facts are that $E$ is an Artinian module, that $\Hom_R(k, E) \cong k$, and that the map $R \to \Hom_R(E, E)$ is an isomorphism when $R$ is complete.
For a Noetherian local ring that is not complete, $\Hom_R(E, E)$ is the completion $\hat{R}$, and the duality relates Artinian $R$-modules with finitely generated $\hat{R}$-modules.
For modules of finite length, the duality preserves length.
Example: for $R = k[\![x]\!]$ one has $E = k[x^{-1}]$, with $x$ acting by $x \cdot x^{-j} = x^{-j+1}$ and $x \cdot 1 = 0$; then $R^\vee = E$ and $E^\vee = R$.

## Explanations

### L1 human

Over a complete local ring there is one special injective module $E$.
Mapping into $E$ turns modules with no infinite increasing chains of submodules into modules with no infinite decreasing chains, and back.
Doing it twice returns the module you started with.

### L2 human

Matlis duality is the analogue, for modules over a complete local ring, of the duality $V \mapsto V^*$ for finite-dimensional vector spaces.
It is used to pass from local cohomology modules, which are Artinian, to finitely generated modules.
This is how [[Grothendieck's local duality|VA3DY2YX83]] is usually stated and applied.
