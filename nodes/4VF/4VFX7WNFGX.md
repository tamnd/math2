---
tag: 4VFX7WNFGX
kind: definition
name: Birational geometry
msc: ["14E05"]
defines: 51YVV85GWB
uses: [HV6YBS0YDH, KA5890R9YM, 4D073CCYGV, 2D5SS6WM14]
sources:
  - url: https://en.wikipedia.org/wiki/Birational_geometry
---

## Definition

Let $k$ be a field and let $X$ and $Y$ be integral [[algebraic varieties|HV6YBS0YDH]] over $k$.
The varieties $X$ and $Y$ are *birationally equivalent* if there is a [[birational map|KA5890R9YM]] $X \dashrightarrow Y$, that is, a [[rational map|4D073CCYGV]] with a rational inverse.
A *birational invariant* is a property or a quantity attached to varieties that takes the same value on birationally equivalent varieties.
*Birational geometry* is the study of varieties up to birational equivalence and of their birational invariants.

## Remarks

Two integral varieties over $k$ are birationally equivalent exactly when their [[function fields|2D5SS6WM14]] are isomorphic as extensions of $k$.
Example: $\mathbb{P}^2$ and $\mathbb{P}^1 \times \mathbb{P}^1$ are birationally equivalent.
The map $[x : y : z] \mapsto ([x : z], [y : z])$ is defined where $z \ne 0$, and its inverse $([x : 1], [y : 1]) \mapsto [x : y : 1]$ is defined on the dense open set where both second coordinates are nonzero.
Both function fields are $k(s, t)$.
Non-example: $\mathbb{P}^1$ and a smooth plane cubic curve $E$ over $\C$ are not birationally equivalent.
For smooth projective curves a birational map extends to an isomorphism, and $\mathbb{P}^1$ has genus $0$ while $E$ has genus $1$.
The dimension, the geometric genus and the Kodaira dimension of smooth projective varieties are birational invariants.
