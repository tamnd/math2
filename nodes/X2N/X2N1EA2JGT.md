---
tag: X2N1EA2JGT
kind: problem
name: Eshelby's inclusion problem
msc: [74B05, 74M25, 74G05]
uses: [6W00ZECYT0, SX32X1D537, 8QS6QMJF5Z]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Eshelby%27s_inclusion
same_as:
  wikidata: Q17010929
  wikipedia: Eshelby's inclusion
history:
  posed_by: "John D. Eshelby"
  first_stated: "1957"
---

## Problem

Let all of $\R^3$ be filled by a homogeneous linear elastic material with [[elasticity tensor|SX32X1D537]] $C$.
Let $\Omega \subset \R^3$ be a bounded region, the inclusion.
Suppose that the material in $\Omega$ undergoes a prescribed eigenstrain $\varepsilon^*$, constant in $\Omega$ and zero outside.
An eigenstrain is a stress-free change of shape, such as one caused by thermal expansion or a phase change.
Let $\varepsilon(u)$ be the [[strain tensor|8QS6QMJF5Z]] of a displacement $u$, and let the stress be $\sigma = C : (\varepsilon(u) - \varepsilon^* \mathbf{1}_\Omega)$.
Find the displacement $u$ that vanishes at infinity and satisfies equilibrium $\operatorname{div} \sigma = 0$ in $\R^3$.
In particular, describe the strain and the stress inside $\Omega$.

## Remarks

Eshelby solved the problem in 1957 for an ellipsoidal inclusion.
His result: if $\Omega$ is an ellipsoid, the strain inside $\Omega$ is uniform and equals $\varepsilon = S : \varepsilon^*$, where $S$ is a fourth-order tensor, now called the Eshelby tensor.
For an isotropic material, $S$ depends only on the shape of the ellipsoid and on Poisson's ratio, not on its size.
Hence the stress inside the inclusion is also uniform.
For other shapes, such as a cube, the strain inside is not uniform.
The solution also gives the field of an inhomogeneity, an ellipsoid of a different material in a matrix under a uniform far-field load, by the equivalent inclusion method.
It is a basic tool in the micromechanics of composites and in estimates of effective elastic moduli.

## Explanations

### L1 human

Imagine a small region inside a large block that wants to grow or change shape, for example because it is heated.
The surrounding material resists, and both the region and its surroundings become stressed.
The problem asks for these stresses.
Eshelby found that when the region is an ellipsoid, the strain inside it is the same at every point, which makes the answer remarkably simple.
