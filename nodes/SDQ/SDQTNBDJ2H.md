---
tag: SDQTNBDJ2H
kind: concept
name: Identity component
msc: [22A05, 54D05]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_component
same_as:
  wikidata: Q5988368
  wikipedia: Identity component
---

## Summary

The identity component of a [[topological group|92700QAB5Y]] $G$ is the [[connected component|0JG9W3KA6B]] of $G$ that contains the identity element.
It is a closed normal subgroup of $G$, and the other connected components are its cosets.
The quotient of $G$ by its identity component is totally disconnected.
So every topological group is built from a connected group and a totally disconnected group.

## Explanations

### L1 human

Start at the identity of the group and collect every element you can reach without jumping across a gap.
The elements you collect form the identity component.
For example, in the group of invertible real $2 \times 2$ matrices, the identity component consists of the matrices with positive determinant.
The matrices with negative determinant form the other piece.
To reach them from the identity you would have to pass through a matrix of determinant zero, which is not in the group.
