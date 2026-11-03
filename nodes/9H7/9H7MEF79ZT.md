---
tag: 9H7MEF79ZT
kind: definition
name: Penalty method
msc: [90C30, 65K05]
defines: AY9Q1VNDJB
uses: [0EPW94MJ1P, 09WRNGPTMV]
sources:
  - url: https://en.wikipedia.org/wiki/Penalty_method
---

## Definition

Let $f, g_1, \dots, g_m, h_1, \dots, h_l \colon \R^n \to \R$ be continuous.
Consider the [[constrained problem|0EPW94MJ1P]] of minimizing $f(x)$ subject to $g_i(x) \le 0$ for $i = 1, \dots, m$ and $h_j(x) = 0$ for $j = 1, \dots, l$.
The *quadratic penalty function* with parameter $\mu > 0$ is
$$Q(x; \mu) = f(x) + \frac{\mu}{2} \left( \sum_{i=1}^m \max(0, g_i(x))^2 + \sum_{j=1}^l h_j(x)^2 \right).$$
The *quadratic penalty method* chooses parameters $0 < \mu_0 < \mu_1 < \cdots$ with $\mu_k \to \infty$.
For each $k$ it computes an approximate minimizer $x_k$ of $Q(\cdot\,; \mu_k)$ over $\R^n$, starting from $x_{k-1}$.

## Remarks

More generally, a *penalty function* is a continuous $P \colon \R^n \to [0, \infty)$ with $P(x) = 0$ exactly at the feasible points, and the method minimizes $f + \mu_k P$.

Assume the problem has a feasible point and each $x_k$ is an exact global minimizer of $Q(\cdot\,; \mu_k)$.
Then every limit point of $(x_k)$ is a global solution of the constrained problem.

Example: minimize $f(x) = x$ subject to $h(x) = x - 1 = 0$.
Then $Q(x; \mu) = x + \frac{\mu}{2}(x - 1)^2$, and $Q'(x; \mu) = 1 + \mu(x - 1) = 0$ gives $x_k = 1 - 1/\mu_k \to 1$.

Non-example: $P(x) = h(x)$ without the square is not a penalty function for the constraint $h(x) = 0$, since it is negative at infeasible points with $h(x) < 0$.
With it, $x + \mu(x - 1)$ is unbounded below for every $\mu > 0$.

The exact penalty $f + \mu \sum_i \max(0, g_i) + \mu \sum_j \abs{h_j}$ is not smooth, but under suitable hypotheses it has the solution as a [[local minimizer|09WRNGPTMV]] for every finite $\mu$ above a threshold.
