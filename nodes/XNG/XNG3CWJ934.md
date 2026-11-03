---
tag: XNG3CWJ934
kind: concept
name: Fin heat transfer
msc: [80A19, 34B05]
sources:
  - url: https://en.wikipedia.org/wiki/Fin_(extended_surface)
---

## Summary

A fin is a thin solid that sticks out from a hot surface to increase the area that exchanges heat with a fluid.
Fin heat transfer studies the temperature along the fin and the heat it removes.
For a straight fin, the model combines [[conduction|SW8X60GYZT]] along the fin with [[convection|RK24AYNG4Z]] from its sides.
This gives a linear second-order ordinary differential equation with exponential and hyperbolic solutions.

## Explanations

### L1 human

The ribs on a motorcycle engine and the metal combs on a computer chip are fins.
Heat flows from the base into the fin and leaks into the air along its whole length.
So the fin gets cooler towards its tip, and the far parts of a long fin do little work.
The fin equation tells how fast the temperature falls along the fin and how much heat the fin removes.
