---
tag: 0MTBGVZ4XJ
kind: statement
role: theorem
name: First isomorphism theorem for linear maps
msc: [15A04, 16D10]
uses: [0SVR29SV1V, 02YFME3RGW, 0JB228DCWB]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (modules)
---

## Statement

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a linear map.
Then the map
$$\bar T \colon V / \ker T \to \im T, \qquad v + \ker T \mapsto T(v),$$
is well defined, and it is a linear isomorphism.
Here $V / \ker T$ is the [[quotient space|0BR3FY5Q8M]] by the [[kernel|0S23E6YE83]], and $\im T$ is the [[image|0WSFKKT6FF]] of $T$.

## Remarks

In finite dimensions, it gives the [[rank–nullity theorem|0W4FSW1TVB]]: $\dim V - \dim \ker T = \dim \im T$.
The same theorem holds for groups, rings and modules.
For a surjective map $T$, it says $V / \ker T \cong W$.

## Explanations

### L1 human

A linear map identifies vectors that differ by an element of the kernel.
After we glue these vectors together, the map becomes one to one.
So the quotient by the kernel is a copy of the image.
