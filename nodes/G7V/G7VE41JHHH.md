---
tag: G7VE41JHHH
kind: concept
name: Hadamard finite part
msc: ["45E99", 26A42]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_regularization
same_as:
  wikidata: Q15998917
  wikipedia: Hadamard regularization
---

## Summary

The Hadamard finite part gives a value to an integral that diverges because the integrand has a non-integrable singularity, such as $\int_{-1}^{1} \frac{\varphi(t)}{t^2}\, dt$.
One cuts out a small neighbourhood of the singularity, computes the integral, and drops the terms that blow up as the neighbourhood shrinks.
It extends the [[Cauchy principal value|0SYR10HD4R]], which handles poles of first order.
Finite part integrals are the integrals in [[hypersingular integral equations|QVRP8FSAZM]].

## Explanations

### L1 human

The integral of $1/t^2$ over $(\varepsilon, 1)$ is $1/\varepsilon - 1$, which grows without bound as $\varepsilon \to 0$.
The finite part throws away the growing piece $1/\varepsilon$ and keeps $-1$.
So a positive function can have a negative finite part integral, and this is not a mistake.
The rule is useful because it agrees with differentiating a principal value integral under the integral sign.
