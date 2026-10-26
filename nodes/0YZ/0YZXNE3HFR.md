---
tag: 0YZXNE3HFR
kind: statement
role: theorem
name: Mercator series
msc: [30B10, 33B10]
uses: [0044CPHJBV, 07X1QA6BRW, 01X5CVV1Q5, 0S4EMDQS2F]
sources:
  - url: https://en.wikipedia.org/wiki/Mercator_series
    locator: Derivation
same_as:
  wikidata: Q677568
  wikipedia: Mercator series
---

## Statement

For every real $x$ with $-1 < x \le 1$,
$$\ln(1 + x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} x^n = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots.$$

## Remarks

For $|x| < 1$, integrate the [[geometric series|01X5CVV1Q5]] $\frac{1}{1 + t} = \sum (-t)^n$ term by term from $0$ to $x$.
At $x = 1$ the series converges by the alternating series test. [[Abel's theorem|0S4EMDQS2F]] gives $\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \cdots$.
Mathlib states the form $\sum_{n \ge 0} \frac{x^{n+1}}{n+1} = -\ln(1 - x)$ as `Real.hasSum_pow_div_log_of_abs_lt_one`.

## History

Johannes Hudde found the series in 1656 and Isaac Newton in 1665, but neither of them published it.
Nicholas Mercator found it independently and used it in his book Logarithmotechnia of 1668.

## Explanations

### L1 human

The logarithm of $1 + x$ is a power series in $x$, for $x$ in $(-1, 1]$.
At $x = 1$ it gives the alternating harmonic series, with sum $\ln 2$.
