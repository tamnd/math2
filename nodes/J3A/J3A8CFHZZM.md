---
tag: J3A8CFHZZM
kind: concept
name: Moyal product
msc: [53D55, 81S30]
sources:
  - url: https://en.wikipedia.org/wiki/Moyal_product
same_as:
  wikidata: Q6927583
  wikipedia: Moyal product
---

## Summary

The Moyal product $f \star g$ is a noncommutative product of functions on phase space $\R^{2n}$.
It is defined so that the [[Weyl quantization|RFNGJ09WDR]] of $f \star g$ is the product of the Weyl quantizations of $f$ and $g$.
As a power series in $\hbar$ it starts with $fg + \frac{i\hbar}{2}\{f, g\}$, so its commutator reproduces the [[Poisson bracket|2S0MXDT4YH]] at first order.
It is the first example of a star product in [[deformation quantization|3MKSJ1J04K]].

## Explanations

### L1 human

Operators in quantum mechanics do not commute, but functions on phase space do.
The Moyal product keeps the functions and changes the way they multiply, so that they behave like operators.
It is the ordinary product plus correction terms built from derivatives and powers of $\hbar$.
For position $x$ and momentum $p$ it gives $x \star p - p \star x = i\hbar$, the canonical commutation relation.
When $\hbar$ goes to $0$ the ordinary product comes back.
