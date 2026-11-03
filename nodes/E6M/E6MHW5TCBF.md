---
tag: E6MHW5TCBF
kind: statement
name: Fredholm alternative for regular Sturm–Liouville problems
role: theorem
msc:
- 34B24
- 34B27
about:
- 7WV6B2502K
uses:
- 7WV6B2502K
- 0BQAA2BK3Q
- TM8VQJWGHZ
sources:
- url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-eigenvalue-probs.tex#L356
  locator: ch-eigenvalue-probs.tex:356
---

## Statement

Fix a regular problem of [[Sturm–Liouville theory|7WV6B2502K]] on $[a,b]$ with coefficient functions $p$, $q$, $r$ and separated boundary conditions
$$\alpha_1 y(a) - \alpha_2 y'(a) = 0, \qquad \beta_1 y(b) + \beta_2 y'(b) = 0.$$
Fix also a value of the parameter $\lambda$.
Then exactly one of two things happens.

1. The homogeneous [[boundary value problem|TM8VQJWGHZ]]
$$(p y')' - q y + \lambda r y = 0$$
with these boundary conditions has a nonzero solution. In this case $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]] of the problem.
2. For every continuous function $f$ on $[a,b]$, the problem
$$(p y')' - q y + \lambda r y = f$$
with the same boundary conditions has one and only one solution.

## Remarks

In the usual meaning of "regular", the functions $p$, $r$ are positive on $[a,b]$, $p$ is continuously differentiable, $q$ and $r$ are continuous, and neither pair $(\alpha_1,\alpha_2)$ nor $(\beta_1,\beta_2)$ is zero.

So a number $\lambda$ that is not an eigenvalue makes the forced problem uniquely solvable for all continuous forcing terms.
