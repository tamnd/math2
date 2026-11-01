---
tag: MY8BG4EE0F
kind: definition
name: Perfect field
msc: [12F15, 12F10]
defines: VWBVKT794W
uses: [0P7CH1CND5, 0GHDDVAH8P, 00X2A9G9W3, 03J8BS7FMV, 08RTDHX1SK]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_field
---

## Definition

Let $K$ be a field.
The field $K$ is *perfect* if one of the following holds:

1. $K$ has [[characteristic|0P7CH1CND5]] $0$;
2. $K$ has characteristic $p > 0$ and the [[Frobenius endomorphism|0GHDDVAH8P]] $x \mapsto x^p$ of $K$ is surjective, that is, $K^p = K$.

## Remarks

A field $K$ is perfect if and only if every [[irreducible polynomial|00X2A9G9W3]] in $K[x]$ is [[separable|03J8BS7FMV]], if and only if every algebraic extension of $K$ is separable.

Example: a [[finite field|08RTDHX1SK]] $\F_q$ of characteristic $p$ is perfect.
Check: the Frobenius map is an injective ring homomorphism, and an injective map from a finite set to itself is surjective.

Non-example: $K = \F_p(t)$ is not perfect.
The element $t$ is not a $p$-th power.
If $(f/g)^p = t$ with polynomials $f, g$, then $f^p = t g^p$.
The degree of the left side is divisible by $p$, while the degree of the right side is not.
Accordingly, $x^p - t$ is irreducible over $K$ but not separable.
