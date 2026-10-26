---
tag: 0W3K3QPEWT
kind: definition
name: Absolute convergence
aliases: [absolutely-convergent-series]
msc: [40A05]
defines: 0YBDSJARWN
uses: [0JH4MN4K1C, 0CVVKY7GY2]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
    locator: Definition for real and complex numbers
---

## Definition

Let $(a_n)$ be a real sequence.
The series $\sum a_n$ converges absolutely if the series $\sum |a_n|$ of absolute values [[converges|0CVVKY7GY2]].

## Remarks

The series $\sum |a_n|$ has nonnegative terms. So it converges exactly when its partial sums are bounded.
[[Absolutely convergent series converge|0Y123X48GA]], but the converse fails. The [[alternating harmonic series|0JQ5Y3WWVE]] converges, but not absolutely.
A convergent series that does not converge absolutely is [[conditionally convergent|02YRQXZDCS]].
The same definition works for complex terms, with the modulus in place of the absolute value.

## Explanations

### L1 human

A series converges absolutely if it still converges after we make all its terms nonnegative.
Then cancellation between positive and negative terms is not needed for convergence.
