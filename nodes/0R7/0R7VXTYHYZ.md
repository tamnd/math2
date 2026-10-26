---
tag: 0R7VXTYHYZ
kind: statement
role: proposition
name: A linear isometry preserves the inner product
msc: [15A04, 46C05]
uses: [0717XXPWM6, 05FKHRT0B4]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Linear isometry
---

## Statement

Let $V$ and $W$ be inner product spaces over $\R$ or $\C$, with the induced norms, and let $T \colon V \to W$ be a [[linear isometry|07SJXTWVQW]].
Then, for all $u, v \in V$,
$$\langle T(u), T(v) \rangle = \langle u, v \rangle.$$

## Remarks

The proof applies the [[polarisation identity|05FKHRT0B4]], which writes inner products in terms of norms.
Conversely, a linear map that keeps inner products keeps norms.
So a linear isometry also keeps angles and orthogonality.

## Explanations

### L1 human

If a linear map keeps lengths, then it also keeps angles.
The reason is that lengths determine inner products, by polarisation.
So rigid linear motions keep the whole geometry.
