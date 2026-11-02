---
tag: 9EA7KJ50AE
kind: statement
role: theorem
name: Sullivan conjecture
msc: [55P91, 55S10, 55R35]
uses: [7XRBR7AV3C, 5W95QFHXPR, 4Q3WY1RX91, T9DG8DDE75]
about: [7XRBR7AV3C]
sources:
  - url: https://en.wikipedia.org/wiki/Sullivan_conjecture
same_as:
  wikidata: Q17089125
  wikipedia: Sullivan conjecture
---

## Statement

Let $G$ be a finite group, let $BG$ be its [[classifying space|7XRBR7AV3C]], and let $X$ be a finite-dimensional [[CW complex|5W95QFHXPR]] with a basepoint.
Then the space $\operatorname{Map}_*(BG, X)$ of [[pointed|T9DG8DDE75]] continuous maps from $BG$ to $X$ is weakly contractible.
That is, the map from it to a point is a [[weak homotopy equivalence|4Q3WY1RX91]].

## Remarks

This form was proved by Haynes Miller in 1984, and is often called Miller's theorem.
The proof uses the category of unstable modules over the Steenrod algebra: one shows that the relevant Ext groups vanish and uses the unstable Adams spectral sequence.
The hypothesis that $X$ is finite-dimensional cannot be dropped: if $G \ne 1$, the identity map of $BG$ is not null-homotopic, since $\pi_1(BG) \cong G$ is nontrivial.

At work: every map from $B\Z/p$ to a finite-dimensional complex, such as a sphere $S^n$, is null-homotopic.
Sullivan's conjecture also has a fixed-point form, proved independently by Carlsson, by Lannes, and by Dwyer, Miller and Neisendorfer.
It says that, for a finite $p$-group acting on a finite complex, the fixed points agree with the homotopy fixed points after $p$-completion, under suitable hypotheses.

## Explanations

### L1 human

The classifying space of a finite group is an infinite-dimensional space with complicated cohomology.
The theorem says that it cannot be mapped in an essential way into any finite-dimensional complex.
Every pointed map can be deformed to the constant map, and in a coherent way.
So finite groups are invisible to finite complexes in this homotopical sense.

### L2 human

Miller's theorem was the starting point of the theory of Lannes' $T$ functor and unstable modules over the Steenrod algebra.
These methods give a homotopy-theoretic description of maps out of $BG$ in many cases.
Its fixed-point form compares the fixed points $X^G$ of a group action with the homotopy fixed points $X^{hG}$, and is parallel to the [[Segal conjecture|DE29ZC399Z]] for spectra.
