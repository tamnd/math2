---
tag: X84R2EWQJP
kind: statement
role: proposition
name: Jensen inequality as a functional inequality
msc: [39B62, 26A51]
uses: [1TQ1JQXEWP, 21SXYJYC59, 0Q1D85B8G6, YQB2B0EXY8, 0RWMRTPC87, MQA1VVCJ63, YBVSDT89T6]
about: [1TQ1JQXEWP]
sources:
  - url: https://en.wikipedia.org/wiki/Jensen%27s_inequality
---

## Statement

Let $I \subseteq \R$ be an [[interval|0Q1D85B8G6]], and let $f \colon I \to \R$ be [[midpoint convex|1TQ1JQXEWP]], that is,
$$f\left(\frac{x + y}{2}\right) \le \frac{f(x) + f(y)}{2} \quad \text{for all } x, y \in I.$$
Let $n \ge 1$, let $x_1, \ldots, x_n \in I$, and let $q_1, \ldots, q_n$ be nonnegative rational numbers with $q_1 + \cdots + q_n = 1$.
Then
$$f\left(\sum_{i=1}^n q_i x_i\right) \le \sum_{i=1}^n q_i f(x_i).$$

## Remarks

The idea of the proof is Cauchy's forward and backward induction.
By induction on $k$, the inequality holds for $m = 2^k$ points with equal weights $1/m$.
For the step, split the points into two halves of $2^{k-1}$ points and apply midpoint convexity to the two averages.
For $n < 2^k$ points with mean $\bar x = \frac{1}{n} \sum x_i$, add $2^k - n$ copies of $\bar x$; the case $m = 2^k$ gives $f(\bar x) \le \frac{1}{2^k}\big(\sum f(x_i) + (2^k - n) f(\bar x)\big)$, which rearranges to $f(\bar x) \le \frac1n \sum f(x_i)$.
For rational weights $q_i = k_i / N$, repeat each point $x_i$ exactly $k_i$ times and use the equal-weight case with $N$ points.
The step that rearranges uses that $f(\bar x)$ is a real number.

Example: with $f(x) = x^2$, $q_1 = 1/3$ and $q_2 = 2/3$, the statement gives $\big(\frac{x_1 + 2x_2}{3}\big)^2 \le \frac{x_1^2 + 2x_2^2}{3}$.
The statement is the form of [[Jensen's inequality|0RWMRTPC87]] that holds without any regularity, as a consequence of the [[functional inequality|YQB2B0EXY8]] of midpoint convexity alone.
For real weights it can fail: a discontinuous additive function is midpoint convex, but it is not convex, so the inequality fails for some real weights.

## Explanations

### L1 human

Midpoint convexity is an inequality about averages of two points.
This result upgrades it to weighted averages of any finite number of points, as long as the weights are rational.
So the midpoint rule alone already controls all rational [[convex combinations|21SXYJYC59]].

### L2 human

The result is the first step in the regularity theory of midpoint convex functions.
Passing from rational to real weights needs some continuity, and results such as the [[Bernstein–Doetsch theorem|MQA1VVCJ63]] and [[Sierpiński's theorem|YBVSDT89T6]] supply it under weak hypotheses.
The same forward and backward induction proves the inequality of arithmetic and geometric means.
