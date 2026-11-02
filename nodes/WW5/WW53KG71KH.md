---
tag: WW53KG71KH
kind: statement
role: theorem
name: Fubini's theorem for series
msc: [40B05, 40A05]
uses: [Z4H7272S9S, 0W3K3QPEWT, WK5V372TG3, 0R0T1VWH5X, 067SYD2J4B]
about: [70HJTK5VZH]
sources:
  - url: https://en.wikipedia.org/wiki/Fubini%27s_theorem
---

## Statement

Let $(a_{m,n})_{m, n \in \N}$ be a [[double sequence|WK5V372TG3]].

1. If $a_{m,n} \ge 0$ for all $m, n$, then $\sum_{(m,n) \in \N \times \N} a_{m,n} = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty} a_{m,n}$ as elements of $[0, \infty]$, where the left side is the supremum of the finite sums.
2. If $a_{m,n} \in \C$ and the family $(a_{m,n})_{(m,n) \in \N \times \N}$ is [[summable|Z4H7272S9S]], then for each $m$ the series $\sum_n a_{m,n}$ converges [[absolutely|0W3K3QPEWT]], the series $\sum_m \sum_n a_{m,n}$ converges absolutely, and
$$\sum_{(m,n) \in \N \times \N} a_{m,n} = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty} a_{m,n}.$$

## Remarks

For part 1, every finite subset of $\N \times \N$ lies in a rectangle, and every iterated partial sum $\sum_{m \le M} \sum_{n \le N}$ is a finite sum; comparing suprema gives the equality.
For part 2, split the real and imaginary parts into positive and negative parts, each bounded by $\abs{a_{m,n}}$, and apply part 1 to each.
Summability of a complex family over $\N \times \N$ is equivalent to $\sum_{m} \sum_{n} \abs{a_{m,n}} < \infty$, by part 1.
The statement is the case of the counting measure in [[Tonelli's theorem|067SYD2J4B]] and [[Fubini's theorem|0R0T1VWH5X]].
Example: for $\abs{x} < 1$ and $\abs{y} < 1$, the family $x^m y^n$ is summable, and its sum is $\frac{1}{1 - x} \cdot \frac{1}{1 - y}$.
Without summability the conclusion fails: [[interchange of summation order|MZM1AFXY82]] gives a double sequence whose two iterated sums differ.

## Explanations

### L1 human

To add all the entries of an infinite table, you may add each row first and then add the row totals.
This is safe when all entries are nonnegative, or when the sum of the absolute values is finite.
Without such a condition, adding row by row can give a different answer than adding column by column.

### L2 human

The theorem is the discrete form of Fubini's theorem, and it is used constantly with power series and Dirichlet series.
Typical uses are the [[Cauchy product of absolutely convergent series|0AN28XQ45Z]], the rearrangement of a double power series, and the exchange of two sums in number theory.
The nonnegative case needs no hypothesis at all, which makes it the usual first step: one checks $\sum_m \sum_n \abs{a_{m,n}} < \infty$ and then applies part 2.
