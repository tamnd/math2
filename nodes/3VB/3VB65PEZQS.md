---
tag: 3VB65PEZQS
kind: statement
role: theorem
name: Hermite–Hadamard inequality
msc: [26D15, 26A51]
uses: [0VV0HSW1ZS, 0QM4TXT3DR]
about: [07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Hermite–Hadamard_inequality
same_as:
  wikidata: Q1035624
  wikipedia: Hermite–Hadamard inequality
---

## Statement

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a [[convex function|0VV0HSW1ZS]].
Then $f$ is Riemann integrable on $[a, b]$ and
$$f\Big( \frac{a + b}{2} \Big) \le \frac{1}{b - a} \int_a^b f(x) \, dx \le \frac{f(a) + f(b)}{2}.$$

## Remarks

Proof idea: a convex function on $[a, b]$ is bounded and is continuous on $(a, b)$, so it is integrable.
For the left inequality, convexity gives $f\big(\frac{a+b}{2}\big) \le \frac{1}{2}\big(f(x) + f(a + b - x)\big)$; integrate over $x \in [a, b]$.
For the right inequality, the graph lies below the chord: $f(x) \le \frac{b - x}{b - a} f(a) + \frac{x - a}{b - a} f(b)$; integrate this bound, whose mean value is $\frac{f(a) + f(b)}{2}$.

Example: $f(x) = x^2$ on $[0, 1]$ gives $\frac{1}{4} \le \frac{1}{3} \le \frac{1}{2}$.

For a concave function both inequalities are reversed.

## Explanations

### L1 human

The average value of a convex function over an interval lies between two simple numbers.
It is at least the value at the midpoint, and at most the average of the two end values.
Geometrically, the graph lies above a supporting line at the midpoint and below the chord joining the ends.

### L2 human

The inequality gives error bounds for the midpoint rule and the trapezoidal rule: for a convex integrand the midpoint rule underestimates the integral and the trapezoidal rule overestimates it.
It is a two-sided refinement of [[Jensen's inequality|0RWMRTPC87]] for the uniform distribution on $[a, b]$.
