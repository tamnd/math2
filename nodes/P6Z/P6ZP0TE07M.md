---
tag: P6ZP0TE07M
kind: concept
name: Adjoint representation of a Lie group
msc: ["22E60", "22E15"]
specializes: [WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_representation
same_as:
  wikidata: Q1017106
  wikipedia: Adjoint representation
---

## Summary

The adjoint representation of a [[Lie group|7JBRGCVJRB]] $G$ is an action of $G$ on its own Lie algebra $\mathfrak{g}$.
It comes from differentiating conjugation at the identity.
It is a [[representation|WYGRXCG2RN]] $\operatorname{Ad} \colon G \to GL(\mathfrak{g})$ that every Lie group carries.
Its derivative is the map $X \mapsto [X, \cdot\,]$ on the Lie algebra, and its kernel, for a connected group, is the centre of $G$.
It is the starting point for root systems, the Killing form and the classification of semisimple groups.

## Explanations

### L1 human

Each element $g$ of a group acts on the group by conjugation, $h \mapsto g h g^{-1}$, and this map fixes the identity.
Its effect on tangent vectors at the identity is a linear map of the Lie algebra, called $\operatorname{Ad}(g)$.
For a group of matrices this is simply $X \mapsto g X g^{-1}$, a change of basis applied to the matrix $X$.
For a commutative group, conjugation does nothing, so every $\operatorname{Ad}(g)$ is the identity.
