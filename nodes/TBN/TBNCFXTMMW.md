---
tag: TBNCFXTMMW
kind: problem
name: Hamburger moment problem
msc: [44A60, 28A12]
uses: [PR11BZQQPG, 0G9EKM0E15, 01XAHPADBA, 01MMVW8CKC]
about: [01XAHPADBA, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Hamburger_moment_problem
same_as:
  wikidata: Q5644349
  wikipedia: Hamburger moment problem
history:
  posed_by: "Hans Hamburger"
  first_stated: "1920"
---

## Problem

Let $(m_n)_{n \ge 0}$ be a [[sequence|0G9EKM0E15]] of real numbers.
Decide whether there is a positive Borel [[measure|PR11BZQQPG]] $\mu$ on the real line $\R$ such that $x^n$ is $\mu$-integrable and
$$m_n = \int_{\R} x^n \, d\mu(x) \quad \text{for all } n \ge 0.$$
The numbers $m_n$ are then the [[moments|01XAHPADBA]] of $\mu$.

## Remarks

The existence question is solved.
Hamburger proved that such a measure exists if and only if, for every $n \ge 0$, the Hankel matrix $(m_{j+k})_{j,k=0}^{n}$ is [[positive semidefinite|01MMVW8CKC]].
Equivalently, $\sum_{j,k=0}^{n} m_{j+k} c_j c_k \ge 0$ for all $n$ and all real numbers $c_0, \ldots, c_n$, since this sum is $\int \left( \sum_j c_j x^j \right)^2 d\mu$ when $\mu$ exists.
Unlike the Hausdorff moment problem on $[0, 1]$, the measure need not be unique.
The moment problem is called determinate when it is unique.
Carleman's condition $\sum_{n \ge 1} m_{2n}^{-1/(2n)} = \infty$ is sufficient for uniqueness.
The moments of the standard normal distribution satisfy it, so that distribution is determined by its moments.
The log-normal distribution is a classical example whose moments do not determine it.

## Explanations

### L1 human

The problem asks which lists of numbers are the moments of some mass distribution spread over the whole real line.
The answer is a positivity test: certain square tables built from the list must behave like squared lengths, never giving a negative value.
On an unbounded line, two different distributions can share all their moments.
So the moments may fail to pin down the distribution, which matters in probability when one tries to identify a law from its moments.
