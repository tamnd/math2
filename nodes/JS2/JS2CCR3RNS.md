---
tag: JS2CCR3RNS
kind: statement
role: theorem
name: Poincaré inequality
msc: ["46E35", 26D10]
uses: [M4CEZ5K9HP, SASP14MA1Z, YM3JZ34PME, JQ9WXC729D]
about: [M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9_inequality
same_as:
  wikidata: Q1751496
  wikipedia: Poincaré inequality
---

## Statement

Let $n \ge 1$ and let $U \subset \R^n$ be a bounded open set.

1. Let $1 \le p < \infty$. There is a constant $C = C(n, p, U)$ such that $\norm{u}_{L^p(U)} \le C \norm{\nabla u}_{L^p(U)}$ for all $u$ in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}_0(U)$.
2. Assume moreover that $U$ is connected and has $C^1$ boundary, and let $1 \le p \le \infty$. There is a constant $C = C(n, p, U)$ such that
$$\norm{u - u_U}_{L^p(U)} \le C \norm{\nabla u}_{L^p(U)} \quad \text{for all } u \in W^{1,p}(U),$$
where $u_U = \frac{1}{\abs{U}} \int_U u \, dx$ is the mean value of $u$ on $U$.

## Remarks

For part 1 one can take $U$ inside a slab $\set{0 < x_1 < d}$.
For smooth $u$ with compact support, $u(x) = \int_0^{x_1} \partial_1 u \, dt$, and [[Hölder's inequality|JQ9WXC729D]] gives $\norm{u}_{L^p} \le d \norm{\partial_1 u}_{L^p}$; density extends this to $W^{1,p}_0(U)$.
Part 2 is proved by contradiction.
If it failed, there would be functions with mean $0$, $L^p$ norm $1$ and gradients tending to $0$.
The [[Rellich–Kondrachov theorem|YM3JZ34PME]] would give a limit with zero gradient, hence constant on the connected set $U$.
This limit has mean $0$, so it is $0$, which contradicts the norm $1$.

The hypotheses are needed.
In part 2 one must subtract the mean, since constant functions have zero gradient.
Connectedness is needed: on two disjoint intervals, a function equal to $1$ on one and $-1$ on the other has mean $0$, zero gradient and nonzero norm.

## Explanations

### L1 human

A function that vanishes on the boundary of a bounded region cannot be large inside unless its slope is large somewhere.
The Poincaré inequality says that the size of the function is bounded by the size of its slope, up to a constant that depends on the region.
For functions without boundary values, the same holds after subtracting the average value.

### L2 human

The inequality shows that $\norm{\nabla u}_{L^2}$ is a norm on $H^1_0(U)$ equivalent to the full $H^1$ norm.
This is exactly the coercivity needed to apply the Lax–Milgram theorem to the Dirichlet problem for $-\Delta u = f$.
The best constant for $p = 2$ in part 1 is $1 / \sqrt{\lambda_1}$, where $\lambda_1$ is the first Dirichlet eigenvalue of $-\Delta$ on $U$.
