---
tag: YPRZTC01QC
kind: example
name: 1 + 1 + 1 + 1 + ⋯
msc: [40A05, 11M06]
instance_of: [0JWMJSTBSG]
uses: [1XWBY4N0VT, VJCJYXGTDY, EZXPY4A19C, N8ZGG7EW6J]
sources:
  - url: https://en.wikipedia.org/wiki/1_%2B_1_%2B_1_%2B_1_%2B_%E2%8B%AF
same_as:
  wikidata: Q2555219
  wikipedia: 1 + 1 + 1 + 1 + ⋯
---

## Example

The series
$$\sum_{n=1}^{\infty} 1 = 1 + 1 + 1 + 1 + \cdots$$
has $N$-th partial sum $s_N = N$, which tends to $+\infty$.
So it is a [[divergent series|0JWMJSTBSG]].

## Remarks

The [[Cesàro means|N8ZGG7EW6J]] $(s_1 + \cdots + s_N)/N = (N+1)/2$ also tend to $+\infty$.
For $0 < x < 1$, $\sum_{n \ge 1} x^n = x/(1-x)$, which tends to $+\infty$ as $x \to 1^-$, so the series is not [[Abel summable|EZXPY4A19C]].
[[Zeta function regularization|VJCJYXGTDY]] assigns it the value $-1/2$.
Indeed $\sum_n n^{-s} = \zeta(s)$ for $\operatorname{Re} s > 1$, the series of the example is formally the case $s = 0$, and the analytic continuation of the [[Riemann zeta function|1XWBY4N0VT]] has $\zeta(0) = -1/2$.
No linear and stable method can give it a finite value $S$: stability gives $S = 1 + S$, which is impossible.

## Explanations

### L1 human

Adding $1$ forever gives totals $1, 2, 3, \ldots$ that grow without bound.
This is the simplest divergent series.
The value $-1/2$ that sometimes appears for it comes from the Riemann zeta function at $0$, not from ordinary addition.
