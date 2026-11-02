---
tag: W8H1WX0JHG
kind: concept
name: Lambert summation
msc: ["40G10", "11M45"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert_summation
same_as:
  wikidata: Q6481320
  wikipedia: Lambert summation
---

## Summary

Lambert summation is a [[summability method|8X25Q4XYMN]] built on [[Lambert series|HATVWNZNMR]] $\sum n a_n \frac{x^n}{1 - x^n}$, multiplied by $1 - x$, with $x \to 1$ from below.
It is regular, so it gives the usual sum to every convergent series.
It is closely tied to the [[prime number theorem|0EHBY5Y84N]].
The series $\sum_{n \ge 1} \mu(n)/n$ is Lambert summable to $0$ by a short computation, and a Tauberian theorem upgrades this to convergence.

## Explanations

### L1 human

A Lambert series groups the terms of a series along divisors: $\frac{x^n}{1 - x^n} = x^n + x^{2n} + x^{3n} + \cdots$.
Lambert summation uses this grouping as a damping device.
It suits series from number theory, whose terms are built from divisors and primes.
For the Möbius function, the grouping makes almost everything cancel, which gives a quick Lambert sum.
