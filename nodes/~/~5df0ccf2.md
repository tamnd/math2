---
tag: ~5df0ccf2
kind: definition
name: Linear isometry
msc: [15A04, 46B04]
defines: ~9d8bcdb8
uses: [~e7fa47d7, ~1b1da4fe]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Linear isometry
---

## Definition

Let $V$ and $W$ be [[normed vector spaces|~8e6f0eef]] over $\R$ or $\C$.
A *linear isometry* from $V$ to $W$ is a [[linear map|~2402e937]] $T \colon V \to W$ with
$$\norm{T(v)} = \norm{v} \qquad \text{for all } v \in V.$$

## Remarks

A linear isometry is injective, because $T(v) = 0$ implies $\norm{v} = 0$.
It keeps distances: $\norm{T(u) - T(v)} = \norm{u - v}$.
Between inner product spaces, it keeps inner products, see [[the next statement|~34824f04]].
Between spaces of the same finite dimension, a linear isometry is bijective.

## Explanations

### L1 human

A linear isometry is a linear map that keeps all lengths.
Rotations and reflections of the plane are examples.
A map that keeps lengths cannot squeeze anything to zero.
