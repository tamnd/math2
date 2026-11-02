---
tag: YBVSDT89T6
kind: statement
role: theorem
name: Sierpiński's theorem on measurable midpoint convex functions
msc: [26A51, 39B62, 28A20]
uses: [1TQ1JQXEWP, YYNCJSR0PJ, 2Z2QVWZ262, 07Q7CNM5WF, 0X3WGX95FE, 0Q1D85B8G6, MQA1VVCJ63]
about: [1TQ1JQXEWP]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
---

## Statement

Let $I \subseteq \R$ be an open [[interval|0Q1D85B8G6]], and let $f \colon I \to \R$ be [[midpoint convex|1TQ1JQXEWP]].
Assume that $f$ is Lebesgue [[measurable|YYNCJSR0PJ]].
Then $f$ is [[continuous|0X3WGX95FE]] on $I$, and $f$ is [[convex|07Q7CNM5WF]].

## Remarks

The idea of the proof: the sets $\set{x \in I : f(x) \le n}$, for $n = 1, 2, \ldots$, are measurable and cover $I$, so one of them, say $A$, has positive [[Lebesgue measure|2Z2QVWZ262]].
By a theorem of Steinhaus type, the set of midpoints $\set{(a + b)/2 : a, b \in A}$ contains a nonempty open interval $J$.
For $a, b \in A$, midpoint convexity gives $f\big(\frac{a + b}{2}\big) \le \frac{f(a) + f(b)}{2} \le n$, so $f$ is bounded above on $J$.
The [[Bernstein–Doetsch theorem|MQA1VVCJ63]] then gives continuity and convexity.

Measurability cannot be dropped: a discontinuous additive function $a \colon \R \to \R$ is midpoint convex, but it is not convex, and by this theorem it is not measurable.
Example of use: if $f$ is midpoint convex and is a pointwise limit of continuous functions, then $f$ is measurable, hence convex.

## Explanations

### L1 human

Midpoint convexity alone allows very irregular functions, but all of them are so wild that they cannot even be measured.
Sierpiński's theorem says that any midpoint convex function that is measurable is a genuine convex function.
In practice this means that every midpoint convex function one meets in analysis is convex.

### L2 human

The theorem follows the pattern of the regularity results for Cauchy's equation, where a measurable additive function is linear.
The key step turns measurability into an upper bound on an interval, and then the [[Bernstein–Doetsch theorem|MQA1VVCJ63]] takes over.
The same argument works for functions that are bounded above on a set of positive measure, and an analogue holds with Baire category instead of measure.
