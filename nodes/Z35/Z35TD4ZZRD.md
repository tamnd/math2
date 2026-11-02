---
tag: Z35TD4ZZRD
kind: statement
role: theorem
name: Littlewood's Tauberian theorem
msc: ["40E05", "40G10"]
uses: [EZXPY4A19C, D6XWK1NRY1, 0RYTGBJAGN, 0CVVKY7GY2]
about: [EZXPY4A19C, D6XWK1NRY1]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood%27s_Tauberian_theorem
same_as:
  wikidata: Q16249478
  wikipedia: Littlewood's Tauberian theorem
---

## Statement

Let $(a_n)_{n \ge 0}$ be complex numbers such that $\sum_{n \ge 0} a_n x^n$ converges for $0 \le x < 1$.
Assume that the series $\sum a_n$ is [[Abel summable|EZXPY4A19C]] to $s$, that is, $\sum_{n \ge 0} a_n x^n \to s$ as $x \to 1^-$.
Assume also that $a_n = O(1/n)$ in [[big O notation|0RYTGBJAGN]].
Then $\sum_{n \ge 0} a_n$ [[converges|0CVVKY7GY2]] and its sum is $s$.

## Remarks

Littlewood's original proof was long.
Karamata found a short proof.
It first controls the sums $\sum a_n g(x^n)$ for polynomials $g$ and then approximates the indicator function of an interval from above and below by polynomials, which isolates the partial sum $s_N$.
The same method proves the [[Hardy–Littlewood Tauberian theorem|N42JDBT0VA]].

The Tauberian condition cannot be dropped.
For $a_n = (-1)^n$, $\sum a_n x^n = \frac{1}{1+x} \to \frac12$, but $\sum (-1)^n$ diverges; here $n a_n$ is unbounded.

## Explanations

### L1 human

Abel summation damps the $n$-th term by $x^n$ and lets $x \to 1$.
It can give a value to a divergent series.
Littlewood's theorem says that this cannot happen when the terms shrink at least like $1/n$: then the Abel value is the true sum.

### L2 human

The theorem strengthens [[Tauber's theorem|8SK3GQ4S0M]], where the condition is $n a_n \to 0$, and it is the Abel analogue of [[Hardy's Tauberian theorem for Cesàro means|BWWZB1F0HY]].
Because Abel summation is stronger than Cesàro summation, it implies Hardy's theorem.
Littlewood's theorem was a starting point of the systematic study of Tauberian theorems by Hardy and Littlewood.
