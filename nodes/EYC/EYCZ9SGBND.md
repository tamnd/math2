---
tag: EYCZ9SGBND
kind: concept
name: Thin airfoil theory
msc: [76G25, 76B10]
specializes: [84K7TEWZ2Z]
sources:
  - url: https://en.wikipedia.org/wiki/Airfoil
---

## Summary

Thin airfoil theory is a linear model of steady plane flow of an ideal fluid around a thin wing section.
The section must have small camber and a small angle of attack.
It replaces the airfoil by a sheet of vortices along its chord.
This reduces the flow problem to the [[airfoil equation|W6Z6CWRE25]], a singular integral equation with an explicit solution.
Its main prediction is that the lift coefficient is $2\pi$ times the angle of attack, measured from the zero-lift angle.
For a symmetric section the lift acts at the quarter-chord point.
These results agree well with experiments before stall and are the starting point of wing theory.

## Explanations

### L1 human

A real wing section is a curved shape, and the exact flow around it is hard to compute.
If the section is thin and only slightly tilted, one can pretend that it is just its curved middle line, carrying a row of small whirls of air.
The strength of the whirls is chosen so that the air slides along the wing and leaves its rear edge smoothly.
For a flat plate tilted by $5$ degrees, about $0.087$ radians, the theory gives a lift coefficient of $2\pi \times 0.087 \approx 0.55$.
