---
tag: EBHS26MHZT
kind: definition
name: Successive minima
msc: [11H06, 52C07]
defines: YDMBKD8FP2
uses: [WN9V7WSJKF, 02AS45T3H9, 0R6EWFKRCF, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%27s_second_theorem
---

## Definition

Let $n \ge 1$ and let $\Lambda \subset \R^n$ be a [[lattice|WN9V7WSJKF]].
Let $K \subset \R^n$ be a [[convex|02AS45T3H9]] [[compact|0R6EWFKRCF]] set with nonempty interior that is symmetric about the origin, that is, $-x \in K$ for all $x \in K$.
For $\lambda > 0$ write $\lambda K = \set{\lambda x : x \in K}$.
Let $k \in \set{1, \dots, n}$.
The *$k$-th successive minimum* $\lambda_k(K, \Lambda)$ of $\Lambda$ for $K$ is the infimum of all $\lambda > 0$ such that $\lambda K \cap \Lambda$ contains $k$ [[linearly independent|0CRMGPAH83]] vectors.

## Remarks

The infimum is attained, and $0 < \lambda_1 \le \lambda_2 \le \dots \le \lambda_n < \infty$.
Example: for $\Lambda = \Z^2$ and $K = [-1, 1] \times [-2, 2]$, one has $\lambda K = [-\lambda, \lambda] \times [-2\lambda, 2\lambda]$.
The vector $(0, 1)$ lies in $\lambda K$ exactly when $\lambda \ge 1/2$, and no nonzero integer vector lies in $\lambda K$ for $\lambda < 1/2$, so $\lambda_1 = 1/2$.
A vector independent of $(0, 1)$ has first coordinate of absolute value at least $1$, so it needs $\lambda \ge 1$, and $(1, 0)$ enters at $\lambda = 1$; so $\lambda_2 = 1$.
Non-example: the strip $K = \R \times [-1, 1]$ is convex and symmetric but not compact.
Then $(1, 0) \in \lambda K$ for every $\lambda > 0$, so the infimum defining $\lambda_1$ is $0$ and the minima lose their meaning.
When $K$ is the closed unit ball, $\lambda_k$ is the smallest $r$ such that $\Lambda$ has $k$ linearly independent vectors of length at most $r$.
