---
tag: 17G0RXTAH6
kind: definition
name: Linear-fractional programming
msc: [90C32, 90C05]
defines: XVBF9EJY10
uses: [VNMXB0J2KA, 1TTKMRW8PD]
sources:
  - url: https://en.wikipedia.org/wiki/Linear-fractional_programming
---

## Definition

Let $A$ be a real $m \times n$ matrix, let $b \in \R^m$, let $c, d \in \R^n$ and let $\alpha, \beta \in \R$.
Let $S = \set{x \in \R^n : A x \le b}$, and assume that $d^T x + \beta > 0$ for every $x \in S$.
The *linear-fractional program* given by these data is the problem
$$\text{maximize } \frac{c^T x + \alpha}{d^T x + \beta} \quad \text{subject to} \quad x \in S.$$
*Linear-fractional programming* is the study and solution of such programs.

## Remarks

Example: maximize $(x + 1)/(y + 1)$ subject to $0 \le x \le 1$ and $0 \le y \le 1$.
The denominator $y + 1$ is at least $1$ on the [[feasible region|1TTKMRW8PD]], so the definition applies.
The numerator is at most $2$ and the denominator at least $1$, so the ratio is at most $2$, with equality at $(1, 0)$.

Non-example: maximize $(x + 1)/y$ subject to $-1 \le y \le 1$ is not a linear-fractional program in this sense, because the denominator is not positive on the whole feasible region.

Charnes–Cooper transformation: put $t = 1/(d^T x + \beta)$ and $z = t x$.
If $S$ is nonempty and bounded, the program is equivalent to the [[linear program|VNMXB0J2KA]]
$$\text{maximize } c^T z + \alpha t \quad \text{subject to} \quad A z \le b t, \quad d^T z + \beta t = 1, \quad t \ge 0,$$
and an optimal $(z, t)$ has $t > 0$ and gives the optimal $x = z / t$.
The objective is both quasiconvex and quasiconcave on $S$, so when $S$ is a nonempty polytope an optimum is attained at a vertex of $S$.
When $d = 0$ and $\beta = 1$, the program is a linear program.
