---
tag: 4RJNW3X9PS
kind: proof
name: Proof of the finite form of Jensen's inequality by induction
msc: [26D15]
proves: 0RWMRTPC87
uses: [0VV0HSW1ZS, 0TK8Y3J5RW, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Jensen%27s_inequality
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $n \ge 1$. For each $n$, the claim is the inequality for all $x_1, \dots, x_n \in I$ and all weights $w_i \ge 0$ with sum $1$.

1. First, a weighted average stays in $I$. Let $y = \sum_{i=1}^{m} v_i x_i$ with $x_i \in I$, $v_i \ge 0$ and $\sum_i v_i = 1$.
2. Let $p = \min_i x_i$ and $q = \max_i x_i$. Then $p = \sum_i v_i p \le y \le \sum_i v_i q = q$.
3. Both $p$ and $q$ lie in $I$, and $I$ is an [[interval|0TK8Y3J5RW]]. So $y \in I$. In particular, both sides of the inequality are defined.
4. Base case $n = 1$. Then $w_1 = 1$, and both sides equal $f(x_1)$.
5. Induction step. Let $n \ge 2$ and assume the claim for $n - 1$ points. Let $x_1, \dots, x_n$ and $w_1, \dots, w_n$ be as in the statement.
6. If $w_n = 1$, then $w_i = 0$ for $i < n$, since the weights are nonnegative with sum $1$. Both sides equal $f(x_n)$.
7. Otherwise $w_n < 1$. Put $s = 1 - w_n = w_1 + \cdots + w_{n-1} > 0$, and $y = \sum_{i=1}^{n-1} \frac{w_i}{s} x_i$.
8. The weights $w_i / s$ for $i < n$ are nonnegative with sum $1$. So $y \in I$ by step 3.
9. We have $\sum_{i=1}^{n} w_i x_i = s y + w_n x_n$, with $s + w_n = 1$ and $s \in (0, 1]$.
10. By the definition of a [[convex function|0VV0HSW1ZS]] with $t = s$, $f(s y + w_n x_n) \le s f(y) + w_n f(x_n)$.
11. By the induction hypothesis for the $n - 1$ points $x_1, \dots, x_{n-1}$, $f(y) \le \sum_{i=1}^{n-1} \frac{w_i}{s} f(x_i)$.
12. Multiplying by $s > 0$ and using step 10 gives $f\big(\sum_{i=1}^{n} w_i x_i\big) \le \sum_{i=1}^{n-1} w_i f(x_i) + w_n f(x_n) = \sum_{i=1}^{n} w_i f(x_i)$.
13. By induction, the inequality holds for every $n \ge 1$.

## Idea

A weighted average of $n$ points is a two-point average of $x_n$ and the average $y$ of the other points. Convexity handles the two-point split, and the induction hypothesis handles $y$. The renormalized weights $w_i / s$ are what make the inner average a genuine average.
