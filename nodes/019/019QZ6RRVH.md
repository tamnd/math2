---
tag: 019QZ6RRVH
kind: statement
role: theorem
name: Integral test
aliases: [integral-test-for-convergence]
msc: [40A05]
uses: [0MX1HZBBXJ, 0VCTBJMEJF, 069HKV4X1E]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_test_for_convergence
    locator: Statement of the test
same_as:
  wikidata: Q1155313
  wikipedia: Integral test for convergence
---

## Statement

Let $N$ be an integer and let $f \colon [N, \infty) \to \mathbb{R}$ be a decreasing function with $f(x) \ge 0$ for all $x \ge N$.
Then the series $\sum_{n=N}^{\infty} f(n)$ converges if and only if the [[improper integral|0VCTBJMEJF]] $\int_N^{\infty} f(x)\, dx$ converges.

## Remarks

A decreasing function is Riemann integrable on each bounded interval, so the integrals $\int_N^b f(x)\, dx$ exist.
The proof uses the [[comparison of a series and an integral|069HKV4X1E]]. When both converge,
$$\int_N^{\infty} f(x)\, dx \le \sum_{n=N}^{\infty} f(n) \le f(N) + \int_N^{\infty} f(x)\, dx.$$
With $f(x) = 1/x^p$ it gives the [[p-series test|0ZNSSK8ZK1]].
Mathlib states the convergence direction for an antitone function, in `AntitoneOn.summable_of_integrableOn_Ioi`.

## Explanations

### L1 human

Draw rectangles of width $1$ and height $f(n)$ under or over the graph of $f$.
The total area of the rectangles is the sum of the series, and it stays within $f(N)$ of the area under the graph.
