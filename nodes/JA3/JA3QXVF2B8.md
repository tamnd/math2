---
tag: JA3QXVF2B8
kind: concept
name: Machine epsilon
msc: [65G50, 65Y04]
sources:
  - url: https://en.wikipedia.org/wiki/Machine_epsilon
same_as:
  wikidata: Q1780355
  wikipedia: Machine epsilon
---

## Summary

Machine epsilon measures the relative precision of a system of [[floating-point arithmetic|RTKRSC3KPH]].
It is the gap between $1$ and the next larger floating-point number, or, in another common convention, half of this gap.
The half-gap, called the unit roundoff, bounds the relative error of rounding a real number to the nearest floating-point number.
Almost every error bound in numerical analysis is stated in terms of it.

## Explanations

### L1 human

A computer stores numbers with a fixed number of binary digits.
Machine epsilon tells how fine this grid of numbers is near $1$.
In double precision it is $2^{-52} \approx 2.2 \times 10^{-16}$, so a computer can tell $1$ from $1 + 2^{-52}$ but rounds $1 + 2^{-54}$ back to $1$.
Since the grid scales with the size of the number, the same relative accuracy of about $16$ decimal digits holds for big and small numbers alike.
