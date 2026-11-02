---
tag: SWWW9X4A3N
kind: concept
name: Functor of points
msc: [14A15, 18F20]
sources:
  - url: https://en.wikipedia.org/wiki/Functor_represented_by_a_scheme
same_as:
  wikidata: Q85762285
  wikipedia: Functor represented by a scheme
---

## Summary

The functor of points of a [[scheme|5A35TYZD02]] $X$ sends each scheme $T$ to the set of morphisms $T \to X$, called the $T$-points of $X$.
By the [[Yoneda lemma|D6DF1ARPVD]], the scheme $X$ is determined by this [[functor|28NQ0KRHD3]].
This lets one define schemes by the data they parametrize, as is done for moduli spaces and Hilbert schemes.

## Explanations

### L1 human

Instead of asking what a space is made of, one can ask what all the maps into it look like.
For the affine plane over $\Z$, a map from $\operatorname{Spec} A$ into it is just a pair $(a, b)$ of elements of the ring $A$.
So the plane "is" the rule that sends each ring $A$ to the set $A^2$.
Solutions of equations work the same way: the scheme of $x^2 + y^2 = 1$ sends $A$ to the set of solutions of $x^2 + y^2 = 1$ in $A$.
