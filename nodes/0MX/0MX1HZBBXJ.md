---
tag: 0MX1HZBBXJ
kind: statement
role: proposition
name: A series of nonnegative terms converges iff its partial sums are bounded
msc: [40A05]
uses: [0CVVKY7GY2, 0NB643K60Q, 0FM6N4R0VB]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_convergence_theorem
    locator: Convergence of a monotone series
---

## Statement

Let $(a_n)$ be a real sequence with $a_n \ge 0$ for all $n$.
Then the series $\sum a_n$ converges if and only if its [[partial sums|0NB643K60Q]] $s_N = \sum_{n=0}^{N} a_n$ are bounded above.
In this case, $\sum_{n=0}^{\infty} a_n = \sup_N s_N$.

## Remarks

The partial sums increase, since $s_{N+1} - s_N = a_{N+1} \ge 0$. The result is then the [[monotone convergence theorem|0FM6N4R0VB]].
If the partial sums are not bounded, they tend to $+\infty$, and one writes $\sum a_n = +\infty$.
The [[comparison test|04Z5G0THN6]], the [[integral test|019QZ6RRVH]] and the [[Cauchy condensation test|0B96KMDDD1]] all rest on this fact.

## Explanations

### L1 human

When all terms are nonnegative, the running total can only go up.
So it either stays below some ceiling and converges, or it grows past every bound.
