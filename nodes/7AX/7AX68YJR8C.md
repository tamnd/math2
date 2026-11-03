---
tag: 7AX68YJR8C
kind: concept
name: Differential flatness
msc: [93C10, 93B27, 93B18]
sources:
  - url: https://en.wikipedia.org/wiki/Flatness_(systems_theory)
same_as:
  wikidata: Q1426175
  wikipedia: Flatness (systems theory)
---

## Summary

A nonlinear [[control system|ZPDTVZQN5K]] is differentially flat if it has a flat output.
This is a list of functions of the state, the input and finitely many input derivatives, as many as there are inputs.
From it every state and input can be recovered by differentiation alone, with no differential equation to solve.
Then every trajectory of the system is given by a free choice of a curve for the flat output.
This makes motion planning easy: one draws the desired path of the flat output and reads off the state and the input.
Flatness was introduced by Fliess, Lévine, Martin and Rouchon, and it generalizes the controllability of linear systems.

## Explanations

### L1 human

For many machines there is one special quantity that tells everything.
For a cart pushed by a force, the position is enough: the velocity is its derivative and the force is mass times its second derivative.
So to plan a motion, one only has to draw a smooth curve for the position.
A flat system is a system with such a special quantity, called the flat output.
