---
tag: BCF1EX9W2M
kind: concept
name: Generalized coordinates
msc: [70G10, 70H03]
uses: [MGYKGP7PW3, AXA8HN8Y45]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_coordinates
same_as:
  wikidata: Q1057607
  wikipedia: Generalized coordinates
---

## Summary

Generalized coordinates are numbers $q_1, \dots, q_n$ that fix the position of a mechanical system and can be varied independently of each other.
They are local coordinates on the [[configuration space|MGYKGP7PW3]], chosen so that the [[holonomic constraints|AXA8HN8Y45]] hold automatically.
Angles, lengths and other convenient parameters can serve, not only Cartesian coordinates.
Lagrangian and Hamiltonian mechanics write the equations of motion in generalized coordinates.

## Explanations

### L1 human

A pendulum bob in the plane has two Cartesian coordinates $x, y$, but they are tied by $x^2 + y^2 = \ell^2$.
The single angle $\theta$ of the rod from the vertical already tells where the bob is: $x = \ell \sin\theta$ and $y = -\ell\cos\theta$.
This angle is a generalized coordinate.
It is free: every value of $\theta$ gives an allowed position, so the constraint never has to be checked again.
