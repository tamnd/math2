---
tag: 7ZGSJRYBGK
kind: concept
name: Airy stress function
msc: [74B05, 74G05]
sources:
  - url: https://en.wikipedia.org/wiki/Stress_functions
---

## Summary

An Airy stress function is a scalar function $\varphi$ of two variables whose second derivatives give the components of a plane [[stress|KG2XWEMJ30]] field.
Stresses defined this way automatically satisfy the equilibrium equations without body force.
For an isotropic material in [[plane stress|AS7WQTM99W]] or [[plane strain|JQT1GBRYTY]], compatibility reduces to the [[biharmonic equation|AS8A9F5SKE]] $\Delta^2 \varphi = 0$.
So a two-dimensional elasticity problem becomes a problem for one scalar function.

## Explanations

### L1 human

A plane stress field has three components that must satisfy two balance equations.
The trick is to write all three as second derivatives of one function, chosen so that the balance equations hold for every choice.
Then one only has to find that single function.
For example, $\varphi = \tfrac{s}{2} y^2$ gives a constant pull of size $s$ in the $x$ direction and no other stress.
Many classical solutions, such as the stress around a hole in a plate, were found by guessing a suitable Airy function.
