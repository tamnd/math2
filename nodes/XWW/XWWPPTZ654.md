---
tag: XWWPPTZ654
kind: statement
role: theorem
name: Smoothed analysis of the simplex method
msc: [90C05, 68Q25, 68Q87]
uses: [MH272QHWPM, VNMXB0J2KA, 05AQE0QR0D, 0WQNRCNY3M, NWBJA4Q208]
about: [MH272QHWPM]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothed_analysis
---

## Statement

Let $m, n \ge 1$, let $\bar A$ be a real $m \times n$ matrix, let $\bar b \in \R^m$ and $c \in \R^n$.
Assume that each row $(\bar a_i, \bar b_i)$ of the matrix $(\bar A \mid \bar b)$ has Euclidean norm at most $1$, and let $0 < \sigma \le 1$.
Let $G$ and $g$ have independent [[Gaussian|05AQE0QR0D]] entries with mean $0$ and standard deviation $\sigma$.
Consider the perturbed [[linear program|VNMXB0J2KA]] "maximize $c^T x$ subject to $(\bar A + G) x \le \bar b + g$".
Then the [[expected|0WQNRCNY3M]] number of steps of the two-phase shadow-vertex [[simplex method|MH272QHWPM]] on it is bounded by a polynomial in $m$, $n$ and $1/\sigma$.

## Remarks

This is the theorem of Daniel Spielman and Shang-Hua Teng, which introduced smoothed analysis.
The shadow-vertex rule follows the vertices whose images are on the boundary of the projection of the feasible region onto a plane.
The proof bounds the expected number of edges of this two-dimensional "shadow" polygon for the perturbed data.

The bound holds for every input $(\bar A, \bar b)$, including the worst ones.
For instance, the [[Klee–Minty cube|NWBJA4Q208]] forces exponentially many steps for some pivot rules, but after a small random perturbation of its data the expected number of steps is polynomial.
As $\sigma \to 0$ the bound grows, in line with the exponential worst case; as $\sigma$ grows, the analysis approaches an average-case analysis.

## Explanations

### L1 human

The simplex method is fast on almost all problems met in practice, but slow on a few carefully built ones.
This theorem explains the gap: if the numbers of any problem are shaken by a little random noise, the method becomes fast on average.
So the bad examples are fragile, like a pencil balanced on its tip.

### L2 human

Worst-case analysis says the simplex method is exponential, while average-case analysis on random programs says it is polynomial, but random programs do not look like real ones.
Smoothed analysis measures the worst case over inputs of the expected time over small perturbations, and lies between the two.
Later work improved the polynomial bound for the shadow-vertex rule.
The idea has since been applied to many other algorithms, such as the $k$-means method and local search.
