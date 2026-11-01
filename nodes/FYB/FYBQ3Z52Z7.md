---
tag: FYBQ3Z52Z7
kind: concept
name: Horner's method
msc: [68W30, 13F20]
sources:
  - url: https://en.wikipedia.org/wiki/Horner%27s_method
same_as:
  wikidata: Q944658
  wikipedia: Horner's method
---

## Summary

Horner's method evaluates a polynomial of degree $n$ with $n$ multiplications and $n$ additions.
It rewrites $a_n x^n + \dots + a_0$ as a nested product $a_0 + x(a_1 + x(a_2 + \dots + x a_n))$.
The intermediate values are the coefficients of the quotient by $x - c$, so it also performs synthetic division.
It is the standard way to carry out [[polynomial evaluation|02MAKWDKGT]].

## Explanations

### L1 human

To compute $2x^3 - 6x^2 + 2x - 1$ at $x = 3$, you do not need the powers of $3$.
Start with $2$; multiply by $3$ and add $-6$ to get $0$; multiply by $3$ and add $2$ to get $2$; multiply by $3$ and add $-1$ to get $5$.
So the value is $5$.
Each step is one multiplication and one addition.
The [[definition|Z2EWA10YMB]] gives the recursion.
