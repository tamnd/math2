---
tag: 7GEXM87S0H
kind: example
name: The exponential map from the additive reals to the positive reals
msc: [20A05]
instance_of: [08MG7H8JW5, 0JYTG5K9Y4]
illustrates: [0N2P0XRTDF]
uses: [0RMVS7RXZX, 08J2M1JYAG, 085PND4KNT]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Examples
---

## Example

Let $(\mathbb{R}, +)$ be the [[real numbers|08J2M1JYAG]] with addition, and let $(\mathbb{R}_{>0}, \times)$ be the positive real numbers with multiplication.
The [[exponential function|0RMVS7RXZX]] gives a map $\exp : \mathbb{R} \to \mathbb{R}_{>0}$ with $\exp(x + y) = \exp(x)\exp(y)$. Thus it is a homomorphism.
Its kernel is $\{0\}$, because $\exp(x) = 1$ only for $x = 0$. Thus the map is [[injective|0N2P0XRTDF]].
Each $y > 0$ is $\exp(\ln y)$, so the map is onto. Thus $\exp$ is an [[isomorphism|085PND4KNT]].

## Remarks

The inverse isomorphism is the natural logarithm.
