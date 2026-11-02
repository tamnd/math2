---
tag: E3SRYCE5VN
kind: concept
name: Ramanujan summation
msc: ["40G99", "11B68"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan_summation
same_as:
  wikidata: Q3533072
  wikipedia: Ramanujan summation
---

## Summary

Ramanujan summation assigns a value to a series $\sum_{n \ge 1} f(n)$ by taking the constant term in the [[Euler–Maclaurin formula|9P839VB8S7]] for its partial sums.
The value is expressed through $f(0)$, the odd derivatives of $f$ at $0$ and the [[Bernoulli numbers|0KC00K7KY4]].
It gives $1 + 2 + 3 + \cdots = -\frac{1}{12}$ and $1 + 1 + 1 + \cdots = -\frac12$, the values $\zeta(-1)$ and $\zeta(0)$ of the [[Riemann zeta function|1XWBY4N0VT]].
Unlike most [[summability methods|8X25Q4XYMN]], it is neither regular nor stable under shifting the index.

## Explanations

### L1 human

The partial sums $f(1) + \cdots + f(N)$ of a series often behave like an integral of $f$ plus correction terms plus a constant.
Ramanujan proposed to call that constant the "sum" of the series, even when the series diverges.
For $f(n) = n$, the partial sums are $\frac{N^2}{2} + \frac{N}{2}$ exactly, and the constant obtained by his rule is $-\frac{1}{12}$.
This number does not mean that the positive integers add up to a negative number; it is a different kind of value, attached to the function $f$.
