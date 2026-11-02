---
tag: Y9KH8P9JC0
kind: problem
name: Stieltjes moment problem
msc: [44A60]
uses: [CS7TWHY7JM, PR11BZQQPG, 01XAHPADBA, PQ1D8FQB3E, 01MMVW8CKC]
about: [CS7TWHY7JM, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Stieltjes_moment_problem
same_as:
  wikidata: Q7616380
  wikipedia: Stieltjes moment problem
history:
  posed_by: "Thomas Joannes Stieltjes"
  first_stated: "1894"
---

## Problem

Let $(m_n)_{n \ge 0}$ be a sequence of real numbers.
Decide whether there is a positive Borel [[measure|PR11BZQQPG]] $\mu$ on $[0, \infty)$ such that every $x^n$ is $\mu$-integrable and
$$m_n = \int_{[0, \infty)} x^n \, d\mu(x) \quad \text{for all } n \ge 0.$$
This is the [[moment problem|CS7TWHY7JM]] on the half-line $K = [0, \infty)$, and the $m_n$ are the [[moments|01XAHPADBA]] of $\mu$.

## Remarks

The existence question is solved.
Such a measure exists if and only if, for every $n \ge 0$, both [[Hankel matrices|PQ1D8FQB3E]] $(m_{j+k})_{j,k=0}^{n}$ and $(m_{j+k+1})_{j,k=0}^{n}$ are [[positive semidefinite|01MMVW8CKC]].
A measure with infinite support exists if and only if all the determinants of these matrices are strictly positive.
Necessity is direct: for real $c_0, \ldots, c_n$, the quadratic forms equal $\int p(x)^2 \, d\mu$ and $\int x \, p(x)^2 \, d\mu$ with $p(x) = \sum_j c_j x^j$, and $x \ge 0$ on the support.
The solution need not be unique; the log-normal distribution gives a sequence with many solutions.
A Stieltjes moment sequence can be determinate as a Stieltjes problem but indeterminate as a Hamburger problem.

## Explanations

### L1 human

The problem asks which lists of numbers are the moments of a mass distribution placed on the nonnegative half-line.
The answer is a positivity test on two square tables built from the list.
The second table is the first one with the list shifted by one place, and its positivity reflects that the mass sits where $x \ge 0$.
Stieltjes met this problem in his work on continued fractions.
