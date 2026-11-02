---
tag: HATVWNZNMR
kind: concept
name: Lambert series
msc: [30B50, 11A25]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert_series
same_as:
  wikidata: Q1577138
  wikipedia: Lambert series
---

## Summary

A Lambert series is a series of the form $\sum_{n \ge 1} a_n \frac{q^n}{1 - q^n}$ in a variable $q$ with $\abs{q} < 1$.
Expanding each fraction as a geometric series turns it into a power series whose coefficients are divisor sums $\sum_{d \mid m} a_d$.
This makes Lambert series a bridge between [[arithmetic functions|09115NQZ07]] and power series, used in the theory of partitions, modular forms and sums of squares.

## Explanations

### L1 human

Each term $q^n / (1 - q^n)$ is the geometric series $q^n + q^{2n} + q^{3n} + \cdots$, which collects the powers of $q$ whose exponent is a multiple of $n$.
Adding these up with weights $a_n$, the power $q^m$ receives the weight $a_d$ once for each divisor $d$ of $m$.
For example, with all $a_n = 1$, the coefficient of $q^m$ is the number of divisors of $m$, so $\sum_n q^n/(1 - q^n) = q + 2q^2 + 2q^3 + 3q^4 + \cdots$.
