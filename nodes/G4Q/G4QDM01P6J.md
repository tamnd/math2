---
tag: G4QDM01P6J
kind: concept
name: Homotopy lifting property
msc: [55R05, 55P05]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_lifting_property
same_as:
  wikidata: Q3983973
  wikipedia: Homotopy lifting property
---

## Summary

A map $p \colon E \to B$ has the homotopy lifting property with respect to a space $X$ if [[homotopies|9YA6S6HD9V]] of maps $X \to B$ lift to $E$.
The lift must start at a given lift of the starting map.
This property defines the fibrations of homotopy theory: [[Hurewicz fibrations|Y773B7EQA7]] have it for all spaces, and [[Serre fibrations|PB9JXQ2KC3]] for all cubes.
It is the formal dual of the [[homotopy extension property|D42X0F1EG1]] that defines [[cofibrations|W5WS5EY8ZM]].

## Explanations

### L1 human

Picture $E$ as a space sitting over $B$, with $p$ the shadow map.
A homotopy in $B$ is a moving shadow, and lifting it means finding a motion in $E$ whose shadow is exactly that motion.
The property asks that such a motion in $E$ exists whenever the starting position is given.
For the covering map $\R \to S^1$, $t \mapsto e^{2\pi i t}$, a path that winds once around the circle lifts to a path in $\R$ that moves from $0$ to $1$.
