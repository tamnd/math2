---
tag: G7VG61YD4J
kind: problem
name: Hausdorff moment problem
msc: [44A60, 28A12]
uses: [PR11BZQQPG, 0G9EKM0E15, 01XAHPADBA]
about: [01XAHPADBA, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_moment_problem
same_as:
  wikidata: Q5682821
  wikipedia: Hausdorff moment problem
history:
  posed_by: "Felix Hausdorff"
  first_stated: "1921"
---

## Problem

Let $(m_n)_{n \ge 0}$ be a [[sequence|0G9EKM0E15]] of real numbers.
Decide whether there is a positive Borel [[measure|PR11BZQQPG]] $\mu$ on the closed interval $[0, 1]$ such that
$$m_n = \int_{[0,1]} x^n \, d\mu(x) \quad \text{for all } n \ge 0.$$
The numbers $m_n$ are then the [[moments|01XAHPADBA]] of $\mu$.

## Remarks

The problem is solved.
Write $(\Delta m)_n = m_{n+1} - m_n$ for the difference operator.
Hausdorff proved that such a measure exists if and only if the sequence is completely monotone, that is,
$$(-1)^k (\Delta^k m)_n \ge 0 \quad \text{for all } n, k \ge 0.$$
When the measure exists, it is unique.
Uniqueness holds because polynomials are dense in the continuous functions on $[0, 1]$ by the Weierstrass approximation theorem.
For example, $m_n = 1/(n + 1)$ is the moment sequence of Lebesgue measure on $[0, 1]$.

## Explanations

### L1 human

The moments of a mass distribution on $[0, 1]$ are its total mass, its mean position, its mean squared position, and so on.
The problem asks which lists of numbers can occur as such moments.
Not every list works: for instance, the moments can never increase, since $x^{n+1} \le x^n$ on $[0, 1]$.
Hausdorff found an exact test, a sign condition on all repeated differences of the list, and showed that the list then determines the distribution.
