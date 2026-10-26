---
tag: 0PAQM3H57X
kind: statement
role: theorem
name: Continuity is equivalent to sequential continuity
msc: [26A15]
uses: [0P27W9RW0G, 0MVDQEAB60, 0W8YHHGCJG]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Definition in terms of limits of sequences
---

## Statement

Let $D \subseteq \mathbb{R}$ and let $f \colon D \to \mathbb{R}$ be a function.
Then $f$ is [[continuous|0P27W9RW0G]] if and only if $f$ is [[sequentially continuous|0MVDQEAB60]].

## Remarks

The forward direction follows from the [[epsilon-delta form|0W8YHHGCJG]] of continuity.
For the converse, suppose that $f$ is not continuous at $a$. Then there is $\varepsilon > 0$ and for each $n$ a point $x_n$ with $|x_n - a| < 1/n$ and $|f(x_n) - f(a)| \ge \varepsilon$.
The equivalence holds in all metric spaces. Mathlib states it for sequential spaces, as `continuous_iff_seqContinuous`.

## Explanations

### L1 human

We can test continuity with sequences.
A function is continuous exactly when it sends every convergent sequence to a convergent sequence with the right limit.
