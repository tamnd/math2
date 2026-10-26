---
tag: 0ZVEAYVRC3
kind: concept
name: Law of large numbers
aliases: [lln]
msc: [60F05, 60F15]
uses: [0BFDHF2H7N, 0DFWHQ839T, 0AJN7WHBJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_large_numbers
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Law_of_large_numbers
    locator: Forms
same_as:
  wikidata: Q207952
  wikipedia: Law of large numbers
---

## Summary

The law of large numbers says that the average of many independent repetitions of a random experiment tends to the expected value.
For an [[i.i.d.|0AJN7WHBJZ]] sequence $X_1, X_2, \dots$ with finite mean $\mu$, the sample mean $\bar{X}_n = (X_1 + \dots + X_n)/n$ tends to $\mu$.
The [[weak law|0BFDHF2H7N]] gives convergence in probability, and the [[strong law|0DFWHQ839T]] gives almost sure convergence.

## Remarks

The law fails without a finite mean. For i.i.d. standard Cauchy variables, $\bar{X}_n$ is standard Cauchy for each $n$ and does not converge.
For indicator variables of an event $A$, the law says that the relative frequency of $A$ tends to $P(A)$. This links probability with long-run frequency.

## Explanations

### L1 human

If you toss a fair coin many times, the fraction of heads comes close to $1/2$.
The law of large numbers is the precise form of this experience. It is the reason why averages of many measurements are reliable.
