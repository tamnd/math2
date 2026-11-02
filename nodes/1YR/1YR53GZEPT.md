---
tag: 1YR53GZEPT
kind: concept
name: Optimal truncation
msc: [41A60, 40A05]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
---

## Summary

Optimal truncation is the rule of stopping a divergent [[asymptotic expansion|BJQTEPEZ9G]] just before its smallest term, for a fixed value of the variable.
For many series of factorial growth the error at this point is about the size of the smallest term.
This size is exponentially small in the large parameter.
So a divergent series can still give an approximation of very high accuracy.
The exponentially small error left after optimal truncation is the starting point of hyperasymptotics and of the theory of [[resurgent functions|37R4QJCARA]].

## Explanations

### L1 human

In a divergent asymptotic series the terms first get smaller and then start to grow again.
Adding terms helps while they shrink and hurts once they grow.
So the best one can do is to stop at the smallest term.
For example, for the series $1 - x + 2x^2 - 6x^3 + \cdots$ with terms $n!\, x^n$ and $x = 0.1$, the terms are smallest near $n = 10$, and stopping there gives an error of about $2 \cdot 10^{-4}$.
