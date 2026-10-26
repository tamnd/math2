---
tag: 0E7VBYGFF7
kind: statement
role: theorem
name: Riemann rearrangement theorem
aliases: [riemann-series-theorem]
msc: [40A05]
uses: [02YRQXZDCS, 0HRJ2Y74T3]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_series_theorem
    locator: Statement of the theorem
same_as:
  wikidata: Q1752516
  wikipedia: Riemann series theorem
---

## Statement

Let $\sum a_n$ be a real series that [[converges conditionally|02YRQXZDCS]].
Let $M$ be a real number.
Then there is a [[rearrangement|0HRJ2Y74T3]] $\sum a_{\sigma(n)}$ that converges to $M$.
There is also a rearrangement that diverges to $+\infty$, and one that diverges to $-\infty$.

## Remarks

The positive terms and the negative terms each give a divergent series, and $a_n \to 0$. Take positive terms until the partial sum exceeds $M$, then negative terms until it falls below $M$, and repeat.
So a real series converges absolutely if and only if all its rearrangements converge to the same sum.
For the [[alternating harmonic series|0JQ5Y3WWVE]], take two positive terms, then one negative term, and repeat. The sum becomes $\frac{3}{2} \ln 2$.

## History

Augustin-Louis Cauchy is usually credited with the first remark that a new order can change a sum. He studied the alternating harmonic series in 1833.
The theorem is named after Bernhard Riemann.

## Explanations

### L1 human

A conditionally convergent series has positive terms with an infinite total and negative terms with an infinite total.
By a careful choice of order, we can steer the partial sums to any target.
