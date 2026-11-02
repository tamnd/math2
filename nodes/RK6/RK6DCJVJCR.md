---
tag: RK6DCJVJCR
kind: statement
role: theorem
name: Ramanujan's 1psi1 summation
msc: [33D15]
uses: [EB4N9RQR51, Y1X8ZZQ7VM]
about: [EB4N9RQR51]
sources:
  - url: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
---

## Statement

Let $a, b, q, z \in \C$ with $0 < \abs{q} < 1$, $a \ne 0$, $b \notin \set{q^{-m} : m \ge 0}$, and $\abs{b/a} < \abs{z} < 1$.
For an integer $n \ge 1$ put $(a; q)_{-n} = 1 / (a q^{-n}; q)_n$, so that $(a; q)_n$ is defined for all $n \in \Z$ through the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
Then
$$\sum_{n=-\infty}^{\infty} \frac{(a; q)_n}{(b; q)_n} z^n = \frac{(q; q)_\infty\, (b/a; q)_\infty\, (az; q)_\infty\, (q/(az); q)_\infty}{(b; q)_\infty\, (q/a; q)_\infty\, (z; q)_\infty\, (b/(az); q)_\infty}.$$
In the notation of [[bilateral basic hypergeometric series|EB4N9RQR51]], the left side is ${}_1\psi_1(a; b; q, z)$.

## Remarks

The condition $\abs{z} < 1$ makes the part with $n \ge 0$ converge, and $\abs{b/a} < \abs{z}$ makes the part with $n < 0$ converge.
Proof idea: for $b = q$ the terms with $n < 0$ vanish and the identity is the [[q-binomial theorem|VVT27RB46B]]; then $b = q^{m+1}$ follows by a shift of the summation index.
Both sides are analytic in $b$ in a disc, and they agree on the points $q^{m}$, $m \ge 1$, which accumulate at $0$, so they agree everywhere by the identity theorem.
Example: with $b = 0$ (a limit) and $z$ replaced by $-z/a$, letting $a \to \infty$ turns the identity into the [[Jacobi triple product|JFP2DGMNXT]].
The identity is due to Ramanujan, who stated it without proof; Hahn and Jackson gave the first published proofs around 1950.

## Explanations

### L1 human

This formula sums a two-sided series, running over all integers $n$, whose terms are ratios of $q$-Pochhammer symbols.
The answer is a ratio of eight infinite products.
It is the two-sided version of the $q$-binomial theorem.

### L2 human

Many product formulas of the theory of partitions and of theta functions are special cases.
It is the starting point for the bilateral series ${}_r\psi_r$, of which Bailey's ${}_6\psi_6$ summation is the main generalization.
