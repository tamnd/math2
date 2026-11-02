---
tag: DHXXSN12JC
kind: concept
name: Subnormal number
msc: [65G50, 65Y04]
sources:
  - url: https://en.wikipedia.org/wiki/Subnormal_number
same_as:
  wikidata: Q1070094
  wikipedia: Subnormal number
---

## Summary

A subnormal number, also called a denormal number, is a nonzero [[floating-point|RTKRSC3KPH]] number smaller in absolute value than the smallest normalized floating-point number.
It has the minimal exponent and a leading significand digit $0$, so it has fewer significant digits.
Subnormal numbers fill the gap between $0$ and the smallest normalized number with evenly spaced values.
This *gradual underflow* ensures that $x - y = 0$ in floating-point arithmetic only when $x = y$.

## Explanations

### L1 human

Normal floating-point numbers get closer and closer together as they approach $0$, but the smallest one still leaves a relatively big jump down to $0$.
Subnormal numbers are extra points placed evenly in that jump.
They give up some precision so that very small results do not suddenly become $0$.
In double precision the smallest normal number is $2^{-1022}$, and the subnormal numbers go down to $2^{-1074}$.
