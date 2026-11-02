---
tag: CJGKW80KBR
kind: concept
name: Krawtchouk polynomials
msc: [33C45, 94B25]
sources:
  - url: https://en.wikipedia.org/wiki/Kravchuk_polynomials
same_as:
  wikidata: Q4298931
  wikipedia: Kravchuk polynomials
---

## Summary

The Krawtchouk (or Kravchuk) polynomials $K_n(x; p, N)$ are the orthogonal polynomials of the [[binomial distribution|0WCWA1KT3M]] on $\set{0, 1, \dots, N}$.
They are a finite family: there is one polynomial for each degree $n = 0, \dots, N$.
In coding theory they describe the Hamming scheme, and they enter the MacWilliams identities and Delsarte's linear programming bound.

## Explanations

### L1 human

Toss a coin $N$ times, with probability $p$ of heads, and count the heads $x$.
The count follows the binomial distribution on the numbers $0$ to $N$.
The Krawtchouk polynomials are the polynomials in $x$ that are perpendicular to each other for this distribution.
The first nonconstant one is $1 - \frac{x}{Np}$, which averages to zero because the mean number of heads is $Np$.
