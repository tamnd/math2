---
tag: HBHNB63J7R
kind: statement
role: proposition
name: Continuity of measure from below and above
msc: [28A12]
uses: [P15VQS5DJ9, PR11BZQQPG, D7KB9HFCGZ, 05M5SWSZZD, 0X8HBKCSYB]
about: [PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Measure_(mathematics)
---

## Statement

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]], and let $A_1, A_2, \ldots$ be sets in $\Sigma$.

1. (Continuity from below.) If $A_1 \subseteq A_2 \subseteq \cdots$, then $\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} \mu(A_n)$.
2. (Continuity from above.) If $A_1 \supseteq A_2 \supseteq \cdots$ and $\mu(A_1) < \infty$, then $\mu\left(\bigcap_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} \mu(A_n)$.

The [[limits|05M5SWSZZD]] are taken in $[0, \infty]$.

## Remarks

For part 1, put $B_1 = A_1$ and $B_n = A_n \setminus A_{n-1}$ for $n \ge 2$.
The sets $B_n$ are pairwise disjoint, their union is $\bigcup_n A_n$, and $B_1 \cup \cdots \cup B_n = A_n$.
[[Countable additivity|D7KB9HFCGZ]] gives $\mu(\bigcup_n A_n) = \sum_n \mu(B_n)$, and the partial sums of this series are the numbers $\mu(A_n)$.
For part 2, apply part 1 to the increasing sets $A_1 \setminus A_n$, and subtract from the finite number $\mu(A_1)$.

For Lebesgue measure $\lambda$ on $\R$ and a point $x$, the sets $[x - 1/n, x + 1/n]$ decrease to $\set{x}$ and have measure $2/n$.
Part 2 gives $\lambda(\set{x}) = 0$.

The hypothesis $\mu(A_1) < \infty$ in part 2 is needed.
For Lebesgue measure, the sets $A_n = [n, \infty)$ decrease to $\varnothing$, but $\lambda(A_n) = \infty$ for every $n$.

## Explanations

### L1 human

If sets grow and fill out a limit set, their measures grow to the measure of the limit set.
If sets shrink to a limit set, their measures shrink to its measure, provided one starts from a set of finite measure.
So measures behave well under monotone limits.

### L2 human

For a finitely additive measure on a σ-algebra, continuity from below is equivalent to countable additivity.
So it is a useful way to check that a set function is a measure.
It is the set version of the monotone convergence theorem.
For [[probability measures|0X8HBKCSYB]] both parts hold without extra hypothesis, since every set has finite measure.
Continuity of measures underlies the Borel–Cantelli lemmas and the right-continuity of distribution functions.
