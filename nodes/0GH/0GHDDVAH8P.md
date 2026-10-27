---
tag: 0GHDDVAH8P
kind: definition
name: Frobenius endomorphism
msc: [13A35]
defines: 0T3WVTD675
uses: [0GYGHKX834, 0P7CH1CND5, 0396VGFA78, 0GGE0Z0JQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_endomorphism
    locator: Definition
inventory: [QGBM1TH5P6]
---

## Definition

Let $p$ be a prime number and let $R$ be a [[commutative ring|0GYGHKX834]] of [[characteristic|0P7CH1CND5]] $p$.
The Frobenius endomorphism of $R$ is the map $F \colon R \to R$, $F(x) = x^p$.
It is a [[ring homomorphism|0GGE0Z0JQ1]] from $R$ to $R$.

## Remarks

The map $F$ preserves products because $R$ is commutative. It preserves sums by the [[freshman's dream|0396VGFA78]].
If $R$ is an [[integral domain|09S3PFBEPM]], then $F$ is injective.
If $R$ is a [[finite field|08RTDHX1SK]], then $F$ is an automorphism of $R$.
On $\mathbb{F}_p$, the map $F$ is the identity, by Fermat's little theorem.

## Explanations

### L1 human

In characteristic $p$, raising to the $p$-th power respects addition and multiplication.
So it is a homomorphism from the ring to itself.
This simple map is a basic tool in the study of finite fields.
