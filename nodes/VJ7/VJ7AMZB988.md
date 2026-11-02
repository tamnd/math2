---
tag: VJ7AMZB988
kind: statement
role: theorem
name: Askey–Gasper inequality
msc: [33C45, 26D15]
uses: [TRD7DSF2KR]
about: [TRD7DSF2KR]
sources:
  - url: https://en.wikipedia.org/wiki/Askey–Gasper_inequality
same_as:
  wikidata: Q4807194
  wikipedia: Askey–Gasper inequality
---

## Statement

Let $P_k^{(\alpha, \beta)}$ denote the [[Jacobi polynomials|TRD7DSF2KR]].
Let $\alpha, \beta$ be real numbers with $\beta \ge 0$ and $\alpha + \beta \ge -2$, and let $n \ge 0$ be an integer.
Then for every $x \in [-1, 1]$,
$$\sum_{k=0}^{n} \frac{P_k^{(\alpha, \beta)}(x)}{P_k^{(\beta, \alpha)}(1)} \ge 0.$$

## Remarks

The denominators are positive: $P_k^{(\beta, \alpha)}(1) = \frac{(\beta + 1)_k}{k!} > 0$ for $\beta \ge 0$.
For $\beta = 0$ all denominators equal $1$, and the inequality says $\sum_{k=0}^{n} P_k^{(\alpha, 0)}(x) \ge 0$ on $[-1, 1]$.
Check for $n = 1$ and $\alpha = \beta = 0$: the sum is $1 + x$, which is nonnegative on $[-1, 1]$ and vanishes at $x = -1$.
Askey and Gasper proved it in 1976.
A short proof by Ekhad (1993) treats the case $\beta = 0$ in its ${}_3F_2$ form.
An identity found with the Wilf–Zeilberger method writes this ${}_3F_2$ as a positive combination of other ${}_3F_2$ series.
These are nonnegative by Clausen's formula, which expresses them as squares of ${}_2F_1$ series.

## Explanations

### L1 human

Jacobi polynomials take both positive and negative values on $[-1, 1]$.
The inequality says that a certain weighted running sum of them never goes below zero.
It is surprising because the single terms change sign many times.
Its fame comes from its use by Louis de Branges in his 1985 proof of the Bieberbach conjecture.

### L2 human

Sums of the form $\sum_k c_k P_k^{(\alpha, \beta)}(x)$ are partial sums of Jacobi expansions, and their positivity is a question of positive summability kernels.
The case $\beta = 0$ can be rewritten as the positivity of a terminating ${}_3F_2$ hypergeometric series on $0 \le t < 1$.
De Branges needed this ${}_3F_2$ form for integer values of $\alpha$ to finish his proof.
