---
tag: 13F5JZPDD0
kind: concept
name: De Rham cohomology of varieties
msc: [14F40, 14F10]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%A4hler_differential
---

## Summary

Let $X$ be a smooth variety over a field $k$.
Its algebraic de Rham cohomology is the hypercohomology of the complex of algebraic differential forms on $X$.
It replaces smooth differential forms by [[Kähler differentials|7HCFARHG7D]], so it makes sense over any field.
Over $\C$, Grothendieck showed that it agrees with the singular cohomology of $X(\C)$ with complex coefficients.
It is the algebraic form of [[de Rham cohomology|GX74C07T0G]] and a model for later cohomology theories such as [[crystalline cohomology|EVXCN06FW3]].

## Explanations

### L1 human

On a manifold, de Rham cohomology counts closed differential forms that are not derivatives.
On a variety, one can do the same with forms built from polynomials, such as $dx$ or $x \, dy$.
For the punctured line $\C \setminus \{0\}$, with functions $t^n$ for all integers $n$, every form $t^n \, dt$ with $n \ne -1$ is the derivative of $t^{n+1}/(n+1)$.
The form $dt/t$ is closed but not a derivative, and it spans the first cohomology.
This matches the one loop around the origin in the topology of the punctured plane.
