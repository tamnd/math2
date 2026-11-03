---
tag: D3XTQ5Z2QA
kind: concept
name: Jones calculus
msc: [78A10, 15A04]
sources:
  - url: https://en.wikipedia.org/wiki/Jones_calculus
same_as:
  wikidata: Q1323967
  wikipedia: Jones calculus
---

## Summary

Jones calculus describes fully polarized light by a vector in $\C^2$, the Jones vector.
It describes each linear optical element by a $2 \times 2$ complex matrix, its Jones matrix.
The effect of an element is matrix multiplication, and a chain of elements corresponds to the product of their matrices.
It turns questions about polarizers, wave plates and rotators into linear algebra.
It handles [[polarization of light|PJ8ZSJ0QDW]] with full phase information, but it cannot describe unpolarized or partially polarized light.

## Explanations

### L1 human

The polarization of a light beam can be stored in two complex numbers, one for the horizontal and one for the vertical part of the electric field.
Each optical device, such as a polarizer or a wave plate, changes these two numbers in a linear way, so it is a small $2 \times 2$ table of numbers.
To follow light through several devices, one multiplies these tables in order.
For example, a horizontal polarizer keeps the horizontal number and sets the vertical one to zero.
This makes it easy to compute how much light gets through a stack of filters.
