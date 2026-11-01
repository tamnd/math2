---
tag: BX3V3NYM1Y
kind: concept
name: Infinitely divisible distribution
msc: ["60E07"]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_divisibility_(probability)
same_as:
  wikidata: Q1754066
  wikipedia: Infinite divisibility (probability)
---

## Summary

A probability distribution is infinitely divisible if, for every $n$, it is the law of a sum of $n$ [[independent and identically distributed|00MRN0FARV]] random variables.
The [[normal|05AQE0QR0D]], [[Poisson|0XB9GQTN9G]], [[gamma|0B80PAQD3C]] and [[Cauchy|0GPG24Q3GR]] laws are infinitely divisible, while no nondegenerate bounded law is.
Infinitely divisible laws are exactly the laws at time $1$ of [[Lévy processes|8NT5CFG2ZR]], and they are described by the [[Lévy–Khintchine representation|Q82B4H4Z4J]].
They are also the possible limits of sums of many small independent terms.

## Explanations

### L1 human

A law is infinitely divisible if it can be split into any number of equal independent parts.
Suppose the number of calls to a call centre in one hour is Poisson with mean $60$.
It is the sum of the calls in $60$ independent minutes, each Poisson with mean $1$.
It is also the sum over $3600$ independent seconds, each Poisson with mean $1/60$.
This works for every number of parts, so the Poisson law is infinitely divisible.
A fair coin with values $0$ and $1$ cannot be split even into two equal independent parts.
