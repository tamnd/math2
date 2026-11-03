---
tag: 2B0YR3D0XA
kind: concept
name: Legendre transformation of thermodynamic potentials
msc: [80A10, 26A51]
specializes: [ZQYMWVT1TT]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_transformation
---

## Summary

In thermodynamics the [[Legendre transformation|ZQYMWVT1TT]] passes from one [[thermodynamic potential|MKZW03Q590]] to another by trading a variable for its conjugate.
Subtracting $TS$ from the internal energy, for example, replaces the entropy $S$ by the temperature $T$ as a natural variable.
No information is lost, because the transformation can be inverted.
This is how the enthalpy, the free energies and the grand potential all come from the internal energy.

## Explanations

### L1 human

Entropy is hard to control in the laboratory, but temperature is easy to fix with a heat bath.
So one wants a potential in which temperature, not entropy, is the variable.
The Legendre transformation gives it: replace $U$ by $U - TS$.
The slope $T = \partial U / \partial S$ becomes the new variable, and the new function still holds all the information of the old one.
