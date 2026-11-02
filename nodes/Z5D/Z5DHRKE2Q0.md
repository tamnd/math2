---
tag: Z5DHRKE2Q0
kind: statement
role: theorem
name: Anderson–Kadec theorem
msc: [57N20, 46B20, 57N17]
uses: [3GAA614673, 06GZ956657, 0Z2P41SVDP, 0QT00PB5G2, HM2HHE3J51]
about: [3GAA614673, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Anderson%E2%80%93Kadec_theorem
same_as:
  wikidata: Q60790479
  wikipedia: Anderson–Kadec theorem
---

## Statement

Let $E$ be an infinite-dimensional [[separable|0Z2P41SVDP]] real [[Fréchet space|3GAA614673]], for example an infinite-dimensional separable [[Banach space|06GZ956657]].
Then $E$ is [[homeomorphic|0QT00PB5G2]] to the countable product $\R^{\N}$ with the product topology.
In particular, any two such spaces are homeomorphic, and each of them is homeomorphic to the separable [[Hilbert space|HM2HHE3J51]] $\ell^2$.

## Remarks

Kadec proved that all infinite-dimensional separable Banach spaces are homeomorphic, and Anderson proved that $\R^{\N}$ is homeomorphic to $\ell^2$.
The homeomorphisms are far from linear: $\ell^1$ and $\ell^2$ are homeomorphic but not isomorphic as Banach spaces.
Both hypotheses are needed.
In finite dimension, $\R^m$ and $\R^n$ are not homeomorphic for $m \ne n$, by invariance of domain, and neither is homeomorphic to $\R^{\N}$.
Without separability it fails: $\ell^\infty$ is not separable, so it is not homeomorphic to $\ell^2$.

## Explanations

### L1 human

The theorem says that, as far as topology alone is concerned, there is only one separable infinite-dimensional Fréchet space.
Norms, inner products and linear structure distinguish many such spaces, but if one only looks at open sets they all look like the product of countably many lines.
So topology cannot tell $\ell^1$ from $\ell^2$, even though linear algebra can.

### L2 human

The result is the starting point of infinite-dimensional topology.
Since all separable infinite-dimensional Fréchet spaces are homeomorphic, manifolds modelled on any of them can be compared purely topologically.
For Hilbert manifolds the smooth counterpart is the open embedding theorem.
It places every separable Hilbert manifold modelled on an infinite-dimensional separable Hilbert space inside its model space as an open set.
