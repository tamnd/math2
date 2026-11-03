---
tag: YADT1TBZ5A
kind: object
name: Sedenions
msc: [17A99, 17A45]
uses: [T9XW7RBEHY, 1HRMT3DSX2, N8K9SSVMRN, 8H3JKHAAHE]
sources:
  - url: https://en.wikipedia.org/wiki/Sedenion
same_as:
  wikidata: Q79188
  wikipedia: Sedenion
---

## Description

The *sedenions* $\mathbb{S}$ are the $16$-dimensional real algebra obtained from the [[octonions|1HRMT3DSX2]] $\mathbb{O}$ by the [[Cayley–Dickson construction|T9XW7RBEHY]] with parameter $\mu = -1$.
So a sedenion is a pair $(a, b)$ of octonions, with the product
$$(a, b)(c, d) = (ac - \bar{d} b,\; da + b\bar{c}),$$
where $\bar{x}$ is the octonion conjugate.
The unit is $(1, 0)$, and the conjugate of $(a, b)$ is $(\bar{a}, -b)$.

## Remarks

The sedenions are not commutative, not associative and not [[alternative|N8K9SSVMRN]].
They are still flexible and power-associative, as are all algebras of the Cayley–Dickson sequence that starts from $\R$.
They are not a [[division algebra|8H3JKHAAHE]]: by the Bott–Milnor–Kervaire theorem a real division algebra has dimension $1$, $2$, $4$ or $8$.
As $\mathbb{S}$ has finite dimension, it therefore has zero divisors: nonzero $x, y$ with $xy = 0$.
For the same reason the norm $N(a, b) = N(a) + N(b)$ is not multiplicative, so $\mathbb{S}$ is not a composition algebra.

## Explanations

### L1 human

The sedenions are the next step after the octonions in the doubling process that builds the complex numbers from the reals.
They have sixteen real coordinates.
At this step division breaks down: two nonzero sedenions can multiply to zero.
