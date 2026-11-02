---
tag: RM64J2CP1M
kind: problem
name: Dedekind's problem
msc: ["06A07", "05A15", "06E30"]
uses: [481ZPQ0GC3]
about: [481ZPQ0GC3]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_number
history:
  posed_by: "Richard Dedekind"
  first_stated: "1897"
---

## Problem

For each integer $n \ge 0$, let $M(n)$ be the [[Dedekind number|481ZPQ0GC3]], the number of monotone Boolean functions of $n$ variables.
Find the value of $M(n)$ for every $n$, ideally by a closed formula.

## Remarks

No closed formula of a practical kind is known, and the problem is open in this form.
Exact values are known only for $n \le 9$; the value $M(9)$ was computed in 2023 with large computer searches.
Simple bounds come from antichains: every family of $\floor{n/2}$-element subsets of $\set{1, \ldots, n}$ is an antichain, so $M(n) \ge 2^{\binom{n}{\floor{n/2}}}$.
Kleitman proved that $\log_2 M(n) = (1 + o(1)) \binom{n}{\floor{n/2}}$ as $n \to \infty$, and finer asymptotic formulas are known.

## Explanations

### L1 human

The question is how many monotone yes/no rules on $n$ switches exist.
For a few switches one can count by hand: $2, 3, 6, 20, 168$ for $n = 0, 1, 2, 3, 4$.
The counts explode so quickly that even with computers only the first ten values are known.
A formula that gives them all is still missing.
