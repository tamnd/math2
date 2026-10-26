---
tag: 0GT85FBPTS
kind: example
name: Decimal expansion as a series
msc: [40A05]
instance_of: [0AF7X08PCR]
uses: [04Z5G0THN6, 01X5CVV1Q5]
sources:
  - url: https://en.wikipedia.org/wiki/Decimal_representation
    locator: Integer and fractional parts
---

## Example

Let $(d_n)_{n \ge 1}$ be a sequence of digits, with $d_n \in \{0, 1, \dots, 9\}$.
The decimal $0.d_1 d_2 d_3 \dots$ is the sum of the series
$$\sum_{n=1}^{\infty} \frac{d_n}{10^n}.$$
This series converges, and its sum lies in $[0, 1]$.

## Remarks

The series converges by the [[comparison test|04Z5G0THN6]] with the [[geometric series|01X5CVV1Q5]] $\sum 9/10^n = 1$.
Two different digit sequences can give the same number. For example, $0.4999\ldots = 0.5$.
Conversely, each real number in $[0, 1)$ has a decimal expansion.

## Explanations

### L1 human

A decimal like $0.314$ means $3/10 + 1/100 + 4/1000$.
An infinite decimal is the same idea with infinitely many terms, so it is a series.
