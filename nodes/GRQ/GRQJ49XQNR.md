---
tag: GRQJ49XQNR
kind: concept
name: Szász–Mirakyan operator
msc: [41A36, 41A35, 41A25]
sources:
  - url: https://en.wikipedia.org/wiki/Sz%C3%A1sz%E2%80%93Mirakyan_operator
same_as:
  wikidata: Q7665169
  wikipedia: Szász–Mirakyan operator
---

## Summary

The Szász–Mirakyan operators approximate functions on the half-line $[0, \infty)$ by series built from the [[Poisson distribution|0XB9GQTN9G]].
They play for $[0, \infty)$ the role that [[Bernstein polynomials|0JT92VK307]] play for $[0, 1]$.
They are [[positive linear operators|AQDXWH4812]], so their convergence follows from Korovkin's theorem.

## Explanations

### L1 human

To approximate $f$ near a point $x \ge 0$, sample $f$ at the grid points $k/n$.
Weight the sample at $k/n$ by the probability that a Poisson random variable with mean $nx$ equals $k$.
The weights concentrate near $k/n \approx x$ as $n$ grows, so the weighted average approaches $f(x)$.
For $f(t) = t$ the average is exactly $x$, because the Poisson variable has mean $nx$.
