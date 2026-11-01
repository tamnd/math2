---
tag: ERHGXV009H
kind: definition
name: Total variation
msc: [26A45]
defines: 8QA5DEWNYD
uses: [069P20KYQT, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
The *total variation* of $f$ on $[a, b]$ is
$$V_a^b(f) = \sup_P \sum_{i=1}^{n} \abs{f(x_i) - f(x_{i-1})},$$
where the [[supremum|0BTMQ04556]] runs over all [[partitions|069P20KYQT]] $P$ of $[a, b]$ given by $a = x_0 < x_1 < \cdots < x_n = b$.
The value $V_a^b(f)$ lies in $[0, \infty]$.

## Remarks

Example: for $f(x) = \sin x$ on $[0, 2\pi]$, the total variation is $4$.
The function is monotone on $[0, \pi/2]$, $[\pi/2, 3\pi/2]$ and $[3\pi/2, 2\pi]$, and on each of these pieces the variation is the absolute change $1$, $2$ and $1$.
Total variation is additive over adjacent intervals: $V_a^c(f) = V_a^b(f) + V_b^c(f)$ for $a < b < c$.

Non-example of finite total variation: the indicator function of the rationals on $[0, 1]$.
A partition alternating between rational and irrational points with $n$ subintervals gives the sum $n$, so the total variation is $\infty$.

If $f$ is continuously differentiable on $[a, b]$, then $V_a^b(f) = \int_a^b \abs{f'(x)}\, dx$.
