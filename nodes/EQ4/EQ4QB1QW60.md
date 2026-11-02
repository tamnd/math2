---
tag: EQ4QB1QW60
kind: concept
name: Dawson function
msc: ["33B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Dawson_function
same_as:
  wikidata: Q3055353
  wikipedia: Dawson function
---

## Summary

The Dawson function is $F(x) = e^{-x^2} \int_0^x e^{t^2}\, dt$.
It is a scaled form of the imaginary error function: $F(x) = \frac{\sqrt{\pi}}{2} e^{-x^2} \operatorname{erfi} x$, where $\operatorname{erfi} x = -i \operatorname{erf}(ix)$ and $\operatorname{erf}$ is the [[error function|7Y56QCZSZJ]].
It is the imaginary part of the [[Faddeeva function|3GHGFTMFQR]] on the real line, up to the factor $\frac{2}{\sqrt{\pi}}$.
It appears in plasma physics, in spectroscopy and in the Hilbert transform of the Gaussian.

## Explanations

### L1 human

The integral of $e^{t^2}$ grows extremely fast, and the factor $e^{-x^2}$ tames this growth.
What is left is a small odd function: it rises from $0$, reaches a maximum of about $0.54$ near $x \approx 0.92$, and then decays like $\frac{1}{2x}$.
So the Dawson function is a bounded smooth bump on the positive side with its mirror image on the negative side.
