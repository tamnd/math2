---
tag: BS24BGYFJJ
kind: definition
name: Strong Cesàro summability
msc: [40F05, 40G05]
defines: 750MCA763X
uses: [0JH4MN4K1C, 0NB643K60Q, N8ZGG7EW6J]
sources:
  - url: https://en.wikipedia.org/wiki/Ces%C3%A0ro_summation
---

## Definition

Let $\sum_{k \ge 0} a_k$ be a [[series|0JH4MN4K1C]] of real or complex numbers with [[partial sums|0NB643K60Q]] $s_k = a_0 + \dots + a_k$.
Let $q > 0$ be a real number and let $s$ be a number.
The series is *strongly Cesàro summable* with exponent $q$ to $s$ if
$$\lim_{n \to \infty} \frac{1}{n + 1} \sum_{k = 0}^{n} \abs{s_k - s}^q = 0.$$

## Remarks

Example: a convergent series with sum $s$ is strongly Cesàro summable to $s$ for every $q > 0$.
Indeed $\abs{s_k - s}^q \to 0$, and the arithmetic means of a sequence tending to $0$ also tend to $0$.

Non-example: Grandi's series $1 - 1 + 1 - \cdots$ is [[Cesàro summable|N8ZGG7EW6J]] to $1/2$, but it is not strongly Cesàro summable with any exponent.
Its partial sums alternate between $1$ and $0$.
For any $s$, one of $\abs{1 - s}$ and $\abs{s}$ is at least $1/2$.
So at least half of the terms $\abs{s_k - s}^q$ are at least $2^{-q}$, and the means do not tend to $0$.

For $q \ge 1$, the power mean inequality gives
$$\abs{\frac{1}{n+1} \sum_{k=0}^{n} (s_k - s)} \le \left( \frac{1}{n+1} \sum_{k=0}^{n} \abs{s_k - s}^q \right)^{1/q},$$
so strong Cesàro summability to $s$ implies Cesàro summability to $s$.
