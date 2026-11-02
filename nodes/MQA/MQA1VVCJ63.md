---
tag: MQA1VVCJ63
kind: statement
role: theorem
name: Bernstein–Doetsch theorem
msc: [26A51, 39B62]
uses: [1TQ1JQXEWP, 07Q7CNM5WF, 0X3WGX95FE, 0Q1D85B8G6]
about: [1TQ1JQXEWP]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
---

## Statement

Let $I \subseteq \R$ be an open [[interval|0Q1D85B8G6]], and let $f \colon I \to \R$ be [[midpoint convex|1TQ1JQXEWP]].
Assume that $f$ is bounded above on some nonempty open interval $J \subseteq I$.
Then $f$ is [[continuous|0X3WGX95FE]] on $I$, and $f$ is [[convex|07Q7CNM5WF]].

## Remarks

The idea of the proof has three steps.
First, midpoint convexity and induction give $f(qx + (1 - q)y) \le q f(x) + (1 - q) f(y)$ for all dyadic rationals $q \in [0, 1]$, and this carries the upper bound from $J$ to a neighbourhood of every point of $I$.
Second, an upper bound $M$ near a point $x_0$ gives a lower bound there, from $f(x_0) \le \frac{f(x_0 + h) + f(x_0 - h)}{2}$.
Third, with $f$ locally bounded, the inequality with $q = 2^{-n}$ gives $\abs{f(x_0 + 2^{-n} h) - f(x_0)} \le 2^{-n} C$ for small $h$, which yields continuity; a continuous midpoint convex function is convex.

The boundedness hypothesis cannot be dropped.
A discontinuous additive function $a \colon \R \to \R$, built from a Hamel basis, is midpoint convex but not continuous, and it is unbounded above on every interval.
Example of use: a midpoint convex function on $(0, 1)$ with values in $[0, 1]$ is automatically convex.
The theorem holds in the same form for midpoint convex functions on an open convex subset of $\R^n$.

## Explanations

### L1 human

Midpoint convexity is a weak form of convexity that only looks at midpoints.
On its own it allows very wild functions.
The theorem says that the wildness disappears as soon as the function is bounded above on one small interval: then the function is continuous and truly convex.

### L2 human

The theorem is the convexity analogue of the classical results on Cauchy's equation, where an additive function bounded on an interval is linear.
It reduces many regularity questions to finding an upper bound on some interval.
For instance, Sierpiński's theorem obtains such a bound for measurable functions, and so shows that measurable midpoint convex functions are convex.
