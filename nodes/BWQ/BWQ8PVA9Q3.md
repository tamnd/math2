---
tag: BWQ8PVA9Q3
kind: statement
role: theorem
name: Aberth method
msc: [65H04]
uses: [07EXVNF9VP, 019MA1VTR2, YWZQC5E54B, 09FTAET5Z4]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Aberth_method
same_as:
  wikidata: Q4667181
  wikipedia: Aberth method
---

## Statement

Let $p$ be a polynomial of degree $n \ge 2$ with [[complex|09FTAET5Z4]] coefficients, whose [[roots|019MA1VTR2]] $r_1, \dots, r_n$ are pairwise distinct.
The *Aberth method*, also called the Aberth–Ehrlich method, updates $n$ approximations $z_1, \dots, z_n$ simultaneously by $z_i \mapsto z_i - w_i$, where
$$w_i = \frac{\dfrac{p(z_i)}{p'(z_i)}}{1 - \dfrac{p(z_i)}{p'(z_i)} \displaystyle\sum_{j \ne i} \frac{1}{z_i - z_j}}, \qquad i = 1, \dots, n.$$
Then there is $\delta > 0$ such that, if each starting value satisfies $\abs{z_i - r_i} < \delta$, the iterates are defined and converge to $r_1, \dots, r_n$, with cubic [[convergence|YWZQC5E54B]].

## Remarks

The step is [[Newton's method|07EXVNF9VP]] applied to the rational function
$$F_i(x) = \frac{p(x)}{\prod_{j \ne i} (x - z_j)},$$
which has the same root $r_i$ as $p$ but whose poles push $z_i$ away from the other approximations.
Indeed $F_i'/F_i = p'/p - \sum_{j \ne i} 1/(x - z_j)$, and $x - F_i(x)/F_i'(x)$ at $x = z_i$ is exactly $z_i - w_i$.
This repulsion tends to keep two approximations from converging to the same root.
At multiple roots the convergence is only linear.

## Explanations

### L1 human

The Aberth method moves guesses for all the roots of a polynomial at the same time.
Each guess takes a Newton step, but it is also repelled by the other guesses, like electric charges of the same sign.
So the guesses spread out, and each one settles on its own root.

### L2 human

It improves the Durand–Kerner method, which converges only quadratically near simple roots.
Each step costs $O(n^2)$ operations, and the steps can be done in parallel or in Gauss–Seidel fashion, using new values as soon as they are known.
It is the core of the MPSolve software for computing polynomial roots to high precision.
