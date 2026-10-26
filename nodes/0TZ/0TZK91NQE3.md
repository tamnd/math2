---
tag: 0TZK91NQE3
kind: example
name: The sequence r^n tends to infinity for r > 1
msc: [40A05]
instance_of: [0VQA7F720Z]
uses: [0MNM54WB99, 09AZCV6GMC]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_progression
    locator: Properties
---

## Example

Let $r$ be a real number with $r > 1$.
Then $r^n \to +\infty$ as $n \to \infty$, in the sense of a [[sequence tending to infinity|09AZCV6GMC]].
Write $r = 1 + h$ with $h > 0$. By Bernoulli's inequality, $r^n \ge 1 + n h$ for each natural number $n$.
Let $M$ be a real number, and choose a natural number $N$ with $N h > M$. Then $r^n > M$ for all $n \ge N$.

## Remarks

For $r < -1$ the sequence $r^n$ does not tend to $+\infty$ or to $-\infty$. Its terms change sign, but $|r^n| \to +\infty$.
Exponential growth is faster than polynomial growth. The node [[exponentials dominate powers in sequences|0MVTCFW42K]] makes this precise.

## Explanations

### L1 human

Doubling again and again gives $1, 2, 4, 8, 16, \dots$, and these numbers grow without bound.
Each factor $r > 1$ does the same, but a factor close to $1$ needs more steps.
