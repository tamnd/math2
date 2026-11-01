---
tag: BVR56STQ32
kind: definition
name: Difference algebra
msc: [12H10, 39A05]
defines: Z1F7N07KFH
uses: [0B1261B5ED, 04C5ZBG1WT, 0VTH8KPCG2, 0T3WVTD675]
sources:
  - url: https://en.wikipedia.org/wiki/Difference_algebra
---

## Definition

A *difference ring* is a pair $(R, \sigma)$, where $R$ is a commutative [[ring|0B1261B5ED]] with identity and $\sigma \colon R \to R$ is a [[ring homomorphism|0VTH8KPCG2]], that is:

1. $\sigma(a + b) = \sigma(a) + \sigma(b)$ for all $a, b \in R$;
2. $\sigma(a b) = \sigma(a) \sigma(b)$ for all $a, b \in R$;
3. $\sigma(1) = 1$.

A *difference field* is a difference ring $(R, \sigma)$ in which $R$ is a [[field|04C5ZBG1WT]].
A difference ring is *inversive* if $\sigma$ is an automorphism.
*Difference algebra* is the study of difference rings, difference fields, and the difference equations and ideals over them.

## Remarks

Some authors require $\sigma$ to be an automorphism in the definition of a difference ring or field.
A *difference polynomial* over $(R, \sigma)$ is a polynomial in the variables $y, \sigma y, \sigma^2 y, \dots$, and a solution is an element $a$ of a difference ring extension at which it vanishes.

Example: $(\C(x), \sigma)$ with $\sigma(f)(x) = f(x + 1)$ is an inversive difference field.
The shift is additive and multiplicative, it fixes $1$, and its inverse is $f(x) \mapsto f(x - 1)$.

Example: a field $K$ of characteristic $p > 0$ with the [[Frobenius map|0T3WVTD675]] $\sigma(a) = a^p$ is a difference field.

Non-example: $(\Z, \sigma)$ with $\sigma(n) = 2n$ is not a difference ring.
It satisfies clause 1, but $\sigma(1) = 2 \ne 1$, so clause 3 fails, and $\sigma(1 \cdot 1) = 2 \ne 4 = \sigma(1)\sigma(1)$, so clause 2 fails too.
