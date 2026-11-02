---
tag: BXYQE0Q1ST
kind: statement
role: proposition
name: Sub-mean value property
msc: [31B05, 31A05]
uses: [Z1MHMGFNFW, RN4G8SGP6P, PCZBE7EX01, 9XJ5FBQD7M, 0HYPR64JM2]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be open, and let $u \colon \Omega \to [-\infty, \infty)$ be [[upper semicontinuous|RN4G8SGP6P]].
For $a \in \R^n$ and $r > 0$ let $\sigma_{a,r}$ be the normalised surface measure on the sphere $S(a, r)$, and let $\lambda$ be Lebesgue measure.
Assume that each $a \in \Omega$ has some $\rho(a) > 0$ such that $u(a) \le \int u \, d\sigma_{a,r}$ for all $0 < r < \rho(a)$, that is, $u$ is [[subharmonic|Z1MHMGFNFW]] in the local sense.
Then for every $a \in \Omega$ and every $r > 0$ with $\overline{B(a, r)} \subseteq \Omega$:

1. $u(a) \le \displaystyle\int_{S(a, r)} u \, d\sigma_{a,r}$;
2. $u(a) \le \dfrac{1}{\lambda(B(a, r))} \displaystyle\int_{B(a, r)} u \, d\lambda$.

## Remarks

Proof idea: since $u$ is upper semicontinuous, there are continuous functions $\varphi_k$ on $S(a, r)$ that decrease to $u$ there.
Let $h_k$ be the harmonic function in $B(a, r)$ with boundary values $\varphi_k$, given by the [[Poisson integral formula|PCZBE7EX01]].
The function $u - h_k$ again satisfies the local sub-mean inequality, so the [[maximum principle for subharmonic functions|9XJ5FBQD7M]] gives $u \le h_k$ in the ball.
Hence $u(a) \le h_k(a) = \int \varphi_k \, d\sigma_{a,r}$, and monotone convergence gives part 1.
Part 2 follows by integrating part 1 over the radii from $0$ to $r$.

So a locally defined subharmonic function satisfies the inequality on every ball whose closure lies in $\Omega$, not only on small ones.
Example: $u(x) = \abs{x}^2$ on $\R^n$ has sphere mean $\abs{a}^2 + r^2$ and ball mean $\abs{a}^2 + \frac{n}{n+2} r^2$, both at least $\abs{a}^2$.
For a harmonic function both inequalities become equalities, which is the [[mean value property|0HYPR64JM2]].
The ball $\overline{B(a, r)}$ must lie in $\Omega$: for $u(x) = -\log\abs{x}$ on $\R^2 \setminus \set{0}$, which is harmonic there, the circle mean about $a = (1, 0)$ with $r = 2$ is $-\log 2 < 0 = u(a)$.

## Explanations

### L1 human

A subharmonic function at a point is never larger than its average over a sphere or a ball around that point.
The definition only asks this for tiny spheres, and this result says it then holds for every sphere that fits in the domain.

### L2 human

The global inequality is what makes subharmonic functions useful: it gives the maximum principle, local integrability, and comparison with harmonic functions on balls.
The averages over spheres of radius $r$ are increasing in $r$ and tend to $u(a)$ as $r \to 0$.
For $C^2$ functions the condition is equivalent to $\Delta u \ge 0$.
