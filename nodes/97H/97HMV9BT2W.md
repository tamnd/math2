---
tag: 97HMV9BT2W
kind: statement
role: theorem
name: Cauchy–Kovalevskaya theorem
msc: [35A10, 35A20, 35A01]
uses: [GC5BDZ6QBC, E7JDFDPM1X, 081WKEDK6C, 0PJXBR6QA3]
about: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Kovalevskaya_theorem
same_as:
  wikidata: Q1614464
  wikipedia: Cauchy–Kovalevskaya theorem
---

## Statement

Let $k \ge 1$ and $N \ge 1$ be integers, and write the variables in $\R \times \R^n$ as $(t, x)$.
Consider a system of $N$ [[partial differential equations|GC5BDZ6QBC]] for an unknown $u = (u_1, \dots, u_N)$ of the following form.
$$\partial_t^k u = F\left(t, x, \left(\partial_t^j \partial_x^\alpha u\right)_{j < k, \ j + \abs{\alpha} \le k}\right).$$
Here $\alpha$ runs over [[multi-indices|0PJXBR6QA3]] in $\N^n$.
Let $x_0 \in \R^n$, and let $\varphi_0, \dots, \varphi_{k-1}$ be $\R^N$-valued [[real-analytic functions|081WKEDK6C]] on a neighbourhood of $x_0$.
Assume that $F$ is real-analytic on a neighbourhood of the point $\left(0, x_0, (\partial_x^\alpha \varphi_j(x_0))_{j < k, \ j + \abs{\alpha} \le k}\right)$.
Then there is a neighbourhood $W$ of $(0, x_0)$ in $\R \times \R^n$ and a real-analytic function $u$ on $W$ that solves the system in $W$.
Moreover $u$ satisfies the initial conditions $\partial_t^j u(0, x) = \varphi_j(x)$ for $j = 0, \dots, k - 1$ and all $x$ with $(0, x) \in W$.
Any two real-analytic solutions with these properties agree on a neighbourhood of $(0, x_0)$.

## Remarks

The equation and the initial conditions determine all derivatives of $u$ at $(0, x_0)$, so the Taylor series of a real-analytic solution is fixed; this gives uniqueness.
For existence, the proof shows that this Taylor series converges by the method of majorants: one compares with an explicit system whose analytic solution dominates the coefficients.
The form of the equation matters: the equation must be solved for $\partial_t^k u$, and the right side may contain neither $\partial_t^k u$ nor any derivative of total order greater than $k$.
Without this, the conclusion fails: for the [[heat equation|VP2HN86VAG]] $\partial_t u = \partial_x^2 u$ with $u(0, x) = 1/(1 - x)$, the formal power series solution is $\sum_{j \ge 0} \frac{(2j)!}{j!} \frac{t^j}{(1 - x)^{2j + 1}}$, which diverges for every $t \ne 0$.
Analyticity of the data is also needed; for smooth data, existence can fail even for a linear equation, as Lewy's example of an operator without [[local solvability|P6E9RZNRBZ]] shows.
Uniqueness among all smooth solutions, not only analytic ones, holds for linear equations by [[Holmgren's uniqueness theorem|1VVKF0Y19B]].

## Explanations

### L1 human

Suppose that an equation and its starting values are given by convergent power series.
The theorem says that then there is a solution near the starting surface, again given by a convergent power series.
It is the basic existence theorem for partial differential equations.
It needs strong hypotheses: everything must be analytic, and the equation must be solved for the highest time derivative.

### L2 human

The theorem gives local existence in the analytic class for any noncharacteristic Cauchy problem, after a change of variables that makes the initial surface $t = 0$.
It does not say that the problem is well posed: [[Hadamard's example|SZ6MEVM89M]] shows that for the Laplace equation the analytic solution exists but depends discontinuously on the data.
So for evolution equations one looks for theories in Sobolev or $C^\infty$ spaces, such as the energy method for hyperbolic equations.
For ordinary differential equations, with $n = 0$, the theorem reduces to the existence of analytic solutions to analytic initial value problems.
