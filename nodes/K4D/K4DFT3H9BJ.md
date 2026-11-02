---
tag: K4DFT3H9BJ
kind: concept
name: Field of extremals
msc: [49K05]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Summary

A field of extremals is a family of solutions of the [[Euler–Lagrange equation|PS0VV149ET]] that covers a region of the $(x, y)$ plane.
Exactly one curve of the family passes through each point of the region.
The slopes of the curves define a slope function $p(x, y)$ on the region.
Embedding an extremal in such a field is the key step of the Weierstrass theory of sufficient conditions for a strong minimum.
It is the classical counterpart of the method of characteristics for the Hamilton–Jacobi equation.

## Explanations

### L1 human

Think of the lines of a flow that fill a strip without crossing, like parallel straight lines.
For the length functional $\int \sqrt{1 + y'^2} \, dx$ the extremals are straight lines, and the lines $y = x + c$ for all real $c$ form a field covering the whole plane.
Each point lies on exactly one of these lines, and the slope function is the constant $p = 1$.
A pencil of lines through one point outside a region also forms a field on that region; this is a central field.
When a minimiser is surrounded by such a field, one can compare it with every nearby curve, not only with smooth small perturbations.
