---
tag: CEC3DESCFT
kind: concept
name: Meixner polynomials
msc: [33C45, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Meixner_polynomials
same_as:
  wikidata: Q6810444
  wikipedia: Meixner polynomials
---

## Summary

The Meixner polynomials $M_n(x; \beta, c)$ are the orthogonal polynomials of the negative binomial (Pascal) distribution on the nonnegative integers.
They are a discrete analogue of the [[Laguerre polynomials|WAMRHWW82R]], which arise from them in a limit.
They sit in the [[Askey scheme|RR2S05C09B]] at the level of the ${}_2F_1$ series, together with the Jacobi and Krawtchouk polynomials.

## Explanations

### L1 human

Repeat a trial with success probability $c$ until a fixed number $\beta$ of failures, and count the successes.
Such counts follow a negative binomial distribution, with weights proportional to $\frac{(\beta)_x}{x!} c^x$ on $x = 0, 1, 2, \dots$.
The Meixner polynomials are the polynomials in $x$ that are perpendicular to each other for these weights.
They play for this distribution the role that the Laguerre polynomials play for the gamma distribution.
