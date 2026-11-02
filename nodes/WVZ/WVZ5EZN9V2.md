---
tag: WVZ5EZN9V2
kind: statement
role: theorem
name: GAGA
msc: [32C35, 14F06]
uses: [A4H4CZ2V35, 56RXEJ8Z6S, PQ6Q143ARJ]
about: [56RXEJ8Z6S, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_geometry_and_analytic_geometry
same_as:
  wikidata: Q4724004
  wikipedia: Algebraic geometry and analytic geometry
---

## Statement

Let $X$ be a projective scheme over $\C$, for example a [[projective variety|A4H4CZ2V35]].
Let $X^{an}$ be the associated complex analytic space, with its sheaf $\mathcal{O}_{X^{an}}$ of holomorphic functions.
For a [[coherent sheaf|56RXEJ8Z6S]] $\mathcal{F}$ on $X$, let $\mathcal{F}^{an} = \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{O}_{X^{an}}$, a coherent analytic sheaf on $X^{an}$.

1. For every coherent sheaf $\mathcal{F}$ on $X$ and every $i \ge 0$, the natural map $H^i(X, \mathcal{F}) \to H^i(X^{an}, \mathcal{F}^{an})$ of [[sheaf cohomology|PQ6Q143ARJ]] groups is an isomorphism.
2. The functor $\mathcal{F} \mapsto \mathcal{F}^{an}$ is an equivalence between the category of coherent sheaves on $X$ and the category of coherent analytic sheaves on $X^{an}$.

## Remarks

The idea of the proof: both statements are first checked on $\mathbb{P}^n$, by comparing the cohomology of the sheaves $\mathcal{O}(d)$, which is the same in both settings.
For a general coherent sheaf one uses that it has a resolution by sums of sheaves $\mathcal{O}(d)$, together with Serre's theorems on twisting and induction on dimension.

Example: by part 2 applied to ideal sheaves, every closed analytic subset of $\mathbb{P}^n_\C$ is algebraic; this is Chow's theorem.
In particular, every compact [[complex manifold|JSGWAN2RJV]] that embeds holomorphically in $\mathbb{P}^n_\C$ is a projective algebraic variety, and every holomorphic map between projective varieties is algebraic.

The properness of $X$ is essential.
On $X = \mathbb{A}^1_\C$, the holomorphic function $e^z$ is a global section of $\mathcal{O}_{X^{an}}$ that is not a polynomial.
So part 1 fails already for $i = 0$ and $\mathcal{F} = \mathcal{O}_X$.
The theorem extends to all proper schemes over $\C$, by a result of Grothendieck.

## Explanations

### L1 human

GAGA, named after Serre's paper "Géométrie algébrique et géométrie analytique", says that for projective varieties over the complex numbers, algebraic and holomorphic objects are the same.
Holomorphic vector bundles, holomorphic sections and their cohomology all come from algebra.
So one can use analysis to prove theorems about algebraic varieties and conversely.

### L2 human

GAGA is what allows results proved with analytic tools, such as Hodge theory and the Kodaira vanishing theorem, to be stated and used for algebraic varieties.
It also shows that the Picard group of a projective variety equals the group of holomorphic line bundles on the associated complex manifold.
For non-proper varieties the two theories differ, as the example of $e^z$ on the affine line shows.
