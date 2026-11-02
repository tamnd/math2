---
tag: 6J4C2P3ZHC
kind: example
name: Klein bottle
msc: [57K20]
instance_of: [VGJJVBZ1MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_bottle
same_as:
  wikidata: Q23638
  wikipedia: Klein bottle
---

## Example

Let $Q = [0, 1] \times [0, 1]$ be the unit square.
The *Klein bottle* $K$ is the quotient of $Q$ by the identifications
$$(0, y) \sim (1, y) \quad \text{and} \quad (x, 0) \sim (1 - x, 1) \qquad \text{for } x, y \in [0, 1].$$
Then $K$ is a closed [[surface|VGJJVBZ1MQ]].
Check: every point has a disc neighbourhood, made of pieces of $Q$ glued along the identified edges.
Also $K$ is compact and connected as a quotient of $Q$.
The four corners become one vertex, the edges give two edges, and $Q$ gives one face, so the Euler characteristic is $\chi(K) = 1 - 2 + 1 = 0$.
The strip $\set{(x, y) : \abs{x - 1/2} \le 1/4}$ with its top and bottom edges glued by $(x, 0) \sim (1 - x, 1)$ is a [[Möbius strip|04AJE0M271]] in $K$, so $K$ is not orientable.

## Remarks

By the [[classification of surfaces|2SFM73YET0]], $K$ is homeomorphic to the connected sum $\R P^2 \# \R P^2$.
Its fundamental group has the presentation $\langle a, b \mid a b a^{-1} b \rangle$.
Gluing two Möbius strips along their boundary circles also gives $K$.
The Klein bottle cannot be embedded in $\R^3$, since a closed surface embedded in $\R^3$ bounds a region and is therefore orientable.
It has immersions in $\R^3$ and embeddings in $\R^4$.

## Explanations

### L1 human

Take a rubber sheet, glue two opposite sides to make a tube, then glue the two ends of the tube with a flip.
In ordinary space the flip forces the tube to pass through its own wall, which gives the familiar glass bottle picture.
The result has no inside and no outside: a walker on it can come back mirror-reversed.
