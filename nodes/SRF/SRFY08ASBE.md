---
tag: SRFY08ASBE
kind: proof
name: Proof that a linear isometry preserves the inner product by polarisation
msc: [15A04, 46C05]
proves: 0R7VXTYHYZ
uses: [0717XXPWM6, 05FKHRT0B4, 0KG4D8AP6G, 0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
---

## Proof

We write both inner products with the polarisation identity, which uses only norms.

1. Let $V$ and $W$ be inner product spaces over $\R$ or $\C$, with [[inner products|0VGSYBWHV2]] written $\ip{\cdot}{\cdot}$ and [[induced norms|0KG4D8AP6G]] $\norm{\cdot}$. Let $T \colon V \to W$ be a [[linear isometry|0717XXPWM6]], so $\norm{T(x)} = \norm{x}$ for all $x \in V$.
2. Let $u, v \in V$. First let the scalars be real. By the [[polarisation identity|05FKHRT0B4]] in $W$, $\ip{T(u)}{T(v)} = \frac{1}{4} \left( \norm{T(u) + T(v)}^2 - \norm{T(u) - T(v)}^2 \right)$.
3. By linearity, $T(u) + T(v) = T(u + v)$ and $T(u) - T(v) = T(u - v)$.
4. Since $T$ keeps norms, $\norm{T(u + v)} = \norm{u + v}$ and $\norm{T(u - v)} = \norm{u - v}$.
5. So $\ip{T(u)}{T(v)} = \frac{1}{4} \left( \norm{u + v}^2 - \norm{u - v}^2 \right) = \ip{u}{v}$, by the polarisation identity in $V$.
6. Now let the scalars be complex, with the inner products linear in the first argument. By the polarisation identity in $W$, $\ip{T(u)}{T(v)} = \frac{1}{4} \sum_{k=0}^{3} i^k \norm{T(u) + i^k T(v)}^2$.
7. By linearity, $T(u) + i^k T(v) = T(u + i^k v)$ for each $k$. Since $T$ keeps norms, $\norm{T(u + i^k v)} = \norm{u + i^k v}$.
8. So $\ip{T(u)}{T(v)} = \frac{1}{4} \sum_{k=0}^{3} i^k \norm{u + i^k v}^2 = \ip{u}{v}$, by the polarisation identity in $V$.

## Idea

The polarisation identity expresses an inner product through norms of a few combinations of the two vectors. A linear map sends these combinations to the same combinations of the images, and an isometry keeps their norms. So it keeps the inner product.
