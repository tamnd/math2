---
tag: ADKK56VZHW
kind: concept
name: Distinguished triangle
msc: [18G80]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulated_category
---

## Summary

A distinguished triangle is a sequence $X \to Y \to Z \to X[1]$ of morphisms in a [[triangulated category|T2V7GJJ2EN]] that belongs to the chosen class of exact triangles.
It is the analogue of a short exact sequence: $Z$ plays the role of a cokernel of $X \to Y$, and $X[1]$ records the connecting map.
In the [[derived category|5ST7NVJFSM]], every short exact sequence of complexes gives a distinguished triangle.
In the homotopy category of chain complexes the standard example is built from the [[mapping cone|6CXPGB13WD]].

## Explanations

### L1 human

A distinguished triangle is three objects and three maps that go around in a circle, with a shift on the way back.
It says that $Z$ is what is left of $Y$ after removing the image of $X$, in a homotopy-invariant sense.
Unlike a cokernel, $Z$ also remembers what $X \to Y$ kills, shifted by one degree.
For complexes, the triangle $X \to Y \to \operatorname{Cone}(f) \to X[1]$ of a chain map $f$ is the basic example.
