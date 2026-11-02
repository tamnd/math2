---
tag: 7BGRWJGYWB
kind: definition
name: Euler transform
msc: [40A25, 65B10, 40G05]
defines: WT0HACKQV7
uses: [017BR1M98J, 092GEF38YD, 0JH4MN4K1C]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_transform
    locator: Euler transform
---

## Definition

Let $(a_n)_{n \ge 0}$ be a sequence of real or complex numbers, and consider the [[alternating series|017BR1M98J]] $\sum_{n \ge 0} (-1)^n a_n$.
The forward difference is $\Delta a_n = a_{n+1} - a_n$, and its iterates satisfy
$$\Delta^n a_0 = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} a_k,$$
with the [[binomial coefficients|092GEF38YD]] $\binom{n}{k}$.
The *Euler transform* of the series is the [[series|0JH4MN4K1C]]
$$\sum_{n \ge 0} \frac{(-1)^n \Delta^n a_0}{2^{n+1}}.$$
If $\sum (-1)^n a_n$ converges, then its Euler transform converges to the same sum.

## Remarks

Example: for $a_n = \frac{1}{n+1}$ one has $(-1)^n \Delta^n a_0 = \frac{1}{n+1}$, so the alternating harmonic series becomes $\sum_{n \ge 0} \frac{1}{(n+1) 2^{n+1}}$, which equals $\ln 2$.
For $a_n = 1$ the series $1 - 1 + 1 - \cdots$ diverges, but $\Delta^n a_0 = 0$ for $n \ge 1$ and the transform is $\frac12$; this is how Euler summation assigns the value $\frac12$ to it.
Non-example: for $a_n = 3^n$ one gets $\Delta^n a_0 = 2^n$, and the transform $\sum_{n \ge 0} \frac{(-1)^n}{2}$ diverges, so the transform does not always produce a convergent series.

## Explanations

### L1 human

The transform replaces the terms by weighted differences of the first terms.
For smooth terms the high differences are small, and the weights $2^{-n-1}$ make the new series converge fast.
