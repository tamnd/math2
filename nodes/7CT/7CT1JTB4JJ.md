---
tag: 7CT1JTB4JJ
kind: concept
name: A priori estimate
msc: [35B45, 35A01]
sources:
  - url: https://en.wikipedia.org/wiki/A_priori_estimate
same_as:
  wikidata: Q4660961
  wikipedia: A priori estimate
---

## Summary

An a priori estimate is a bound on a solution of a differential equation in terms of the data.
It is proved under the assumption that the solution already exists and is regular enough.
It is proved before, and independently of, any existence result.
A priori estimates are the main input of existence proofs by continuity, by fixed points, or by compactness, and they also give uniqueness and stability.

## Explanations

### L1 human

Suppose one wants to show that an equation has a solution, but cannot write it down.
A common strategy is to first assume a solution exists and show it cannot be too large.
This bound is the a priori estimate: "a priori" because it comes before knowing that a solution exists.
For example, a solution of $-u'' = f$ on $(0, 1)$ with $u(0) = u(1) = 0$ always satisfies $\max \abs{u} \le \frac{1}{8} \max \abs{f}$.
With such bounds in hand, approximate solutions stay under control and a limit gives a true solution.
