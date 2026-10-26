---
tag: ~ef2b7bb1
kind: statement
role: theorem
name: One-sided limits of a monotone function exist
msc: [26A48]
uses: [~963e8644, ~471ab2b3]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: Some basic applications and results
---

## Statement

Let $a < c < b$ and let $f \colon (a, b) \to \mathbb{R}$ be increasing.
Then both [[one-sided limits|~963e8644]] of $f$ at $c$ exist, and
$$\lim_{x \to c^-} f(x) = \sup_{a < x < c} f(x) \le f(c) \le \inf_{c < x < b} f(x) = \lim_{x \to c^+} f(x).$$

## Remarks

The proof is the same as for the [[monotone convergence theorem|~471ab2b3]]. The supremum exists because $f(c)$ is an upper bound.
A similar statement holds for decreasing functions, with the inequalities reversed.
So $f$ is continuous at $c$ exactly when the two one-sided limits are equal. Otherwise $c$ is a [[jump discontinuity|~36155e25]].
Mathlib states the left limit as `Monotone.tendsto_nhdsLT`.

## Explanations

### L1 human

An increasing function can only move up as $x$ approaches $c$ from the left.
Its values are bounded by $f(c)$, so they settle at a limit.
