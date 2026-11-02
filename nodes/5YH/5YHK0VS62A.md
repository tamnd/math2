---
tag: 5YHK0VS62A
kind: concept
name: String diagram
msc: [18M30, 18M05]
sources:
  - url: https://en.wikipedia.org/wiki/String_diagram
same_as:
  wikidata: Q7623974
  wikipedia: String diagram
---

## Summary

A string diagram is a picture of a morphism in a [[monoidal category|M3MSQ3NKAE]]: wires stand for objects and boxes stand for morphisms.
Composition is drawn by stacking boxes and the monoidal product by placing them side by side.
A theorem of Joyal and Street says that diagrams that deform into each other in the plane, with wires kept upward, denote the same morphism.
So many computations with coherence isomorphisms become moves of pictures.

## Explanations

### L1 human

Draw each object as a vertical line and each morphism as a box with lines entering at the bottom and leaving at the top.
Doing one process after another stacks the boxes; doing two processes in parallel puts them next to each other.
The equation $(g \otimes \id) \circ (\id \otimes f) = (\id \otimes f) \circ (g \otimes \id)$ becomes obvious: one may slide box $g$ above or below box $f$ on its own wire.
String diagrams are used in quantum computing, in linear algebra with tensors, and in the study of knots.
