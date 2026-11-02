---
tag: 3MKSJ1J04K
kind: concept
name: Deformation quantization
msc: [53D55, 16S80]
specializes: [QP92G4ZGJE]
sources:
  - url: https://en.wikipedia.org/wiki/Deformation_quantization
same_as:
  wikidata: Q131143202
  wikipedia: Deformation quantization
---

## Summary

Deformation quantization equips the smooth functions on a [[Poisson manifold|A2KQ49Y4NF]] with a noncommutative star product.
The star product is a formal power series in a parameter $\hbar$.
The commutator of the star product reproduces the [[Poisson bracket|2S0MXDT4YH]] at first order in $\hbar$.
The Moyal product on $\R^{2n}$ is the first example.
[[Kontsevich's formality theorem|XXA9D45E0N]] shows that every Poisson manifold admits a star product.

## Explanations

### L1 human

In classical mechanics, observables are functions on phase space, and they commute: $fg = gf$.
In quantum mechanics, observables are operators, and position and momentum do not commute.
Deformation quantization keeps the functions but changes their product, adding correction terms in powers of Planck's constant $\hbar$.
At $\hbar = 0$ the old commutative product comes back.
For position $x$ and momentum $p$ the new product satisfies $x * p - p * x = \hbar$, the formal version of the canonical commutation relation.
