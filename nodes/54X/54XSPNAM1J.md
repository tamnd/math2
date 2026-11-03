---
tag: 54XSPNAM1J
kind: concept
name: Adjoint representation of a Lie algebra
msc: [17B10, 17B05]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_representation
---

## Summary

The adjoint representation of a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak g$ is the map $\operatorname{ad}$ that sends $x$ to the linear map $y \mapsto [x, y]$.
By the Jacobi identity it is a [[Lie algebra homomorphism|H5D71JE8TA]] from $\mathfrak g$ to $\mathfrak{gl}(\mathfrak g)$, so $\mathfrak g$ acts on itself.
Its kernel is the center of $\mathfrak g$.
It is the derivative of the [[adjoint representation of a Lie group|P6ZP0TE07M]], and it underlies the Killing form and the root decomposition.

## Explanations

### L1 human

Each element $x$ of a Lie algebra gives a way to move the other elements: send $y$ to $[x, y]$.
This turns every element into a linear map on the algebra itself.
For example, in $\mathfrak{sl}_2$ with basis $e, h, f$, the element $h$ acts by $e \mapsto 2e$, $h \mapsto 0$, $f \mapsto -2f$.
Studying these linear maps, their eigenvalues for example, reveals the structure of the algebra.
