---
tag: E7JDFDPM1X
kind: concept
name: Order of a PDE
msc: [35A99]
specializes: [0XK0G19SK8]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_differential_equation
---

## Summary

The order of a [[partial differential equation|GC5BDZ6QBC]] is the highest order of a partial derivative of the unknown function that occurs in it.
It is the first number used to sort PDEs, and it controls how many initial or boundary conditions a well-posed problem needs.
See the [[definition|YFFEKD37RP]].

## Explanations

### L1 human

Count how many times the unknown is differentiated in each term, and take the largest count.
The [[transport equation|PVD7VZJZ9B]] $\partial_t u + \partial_x u = 0$ has order $1$.
The [[wave equation|5EHD2XBQDG]] $\partial_t^2 u = \partial_x^2 u$ has order $2$.
A mixed derivative such as $\partial_x \partial_y u$ also counts as order $2$.
