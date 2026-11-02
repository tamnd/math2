---
tag: EKGEZGHYBW
kind: concept
name: Postnikov tower
msc: [55S45, 55P20]
sources:
  - url: https://en.wikipedia.org/wiki/Postnikov_system
same_as:
  wikidata: Q6941533
  wikipedia: Postnikov system
---

## Summary

A Postnikov tower of a path-connected space $X$ is a sequence of spaces $X_1 \leftarrow X_2 \leftarrow X_3 \leftarrow \cdots$ with maps from $X$.
The stage $X_n$ has the homotopy groups of $X$ up to degree $n$ and none above degree $n$.
Each stage maps to the previous one by a fibration with fibre an [[Eilenberg–MacLane space|AJHEYJE5XY]].
So the tower builds $X$ from Eilenberg–MacLane spaces, one homotopy group at a time.
The extra data needed to rebuild $X$ are cohomology classes called $k$-invariants.

## Explanations

### L1 human

Think of the homotopy groups of a space as layers.
The $n$-th stage of the Postnikov tower keeps the first $n$ layers and throws away all the layers above.
Going up the tower adds one layer at a time, and in the limit one recovers the space up to weak homotopy equivalence.
For example, for the circle every stage is the circle itself, since the circle has only one layer.
