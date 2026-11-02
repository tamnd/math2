---
tag: 4KFC9BE02Y
kind: example
name: 1 + 2 + 3 + 4 + ⋯
msc: [40A05, 11M06]
instance_of: [0JWMJSTBSG]
uses: [1XWBY4N0VT, VJCJYXGTDY, E3SRYCE5VN, EZXPY4A19C, N8ZGG7EW6J]
sources:
  - url: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
same_as:
  wikidata: Q2605420
  wikipedia: 1 + 2 + 3 + 4 + ⋯
---

## Example

The series of the positive integers is
$$\sum_{n=1}^{\infty} n = 1 + 2 + 3 + 4 + \cdots.$$
Its $N$-th partial sum is $s_N = N(N+1)/2$, which tends to $+\infty$.
So it is a [[divergent series|0JWMJSTBSG]].

## Remarks

It is not summable by [[Cesàro summation|N8ZGG7EW6J]], since the averages of $s_N$ also tend to $+\infty$.
It is not [[Abel summable|EZXPY4A19C]] either: for $0 < x < 1$, $\sum_{n \ge 1} n x^n = x/(1-x)^2$, which tends to $+\infty$ as $x \to 1^-$.
[[Zeta function regularization|VJCJYXGTDY]] assigns it the value $-1/12$.
For $\operatorname{Re} s > 1$, $\sum_n n^{-s} = \zeta(s)$, where $\zeta$ is the [[Riemann zeta function|1XWBY4N0VT]], and the series of the example is formally the case $s = -1$; the analytic continuation of $\zeta$ has $\zeta(-1) = -1/12$.
[[Ramanujan summation|E3SRYCE5VN]] also gives $-1/12$.
The value $-1/12$ is not a sum in the usual sense: the partial sums are all positive and grow without bound.

## Explanations

### L1 human

Adding $1 + 2 + 3 + \cdots$ gives totals that grow without limit, so the series has no ordinary sum.
The famous value $-1/12$ comes from a different procedure: one extends the function $\sum n^{-s}$ beyond the region where the series converges and evaluates it at $s = -1$.
This value appears in physics and in number theory, but it should not be read as the result of ordinary addition.
