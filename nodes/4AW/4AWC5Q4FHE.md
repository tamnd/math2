---
tag: 4AWC5Q4FHE
kind: definition
name: Superharmonic function
msc: [31B05, 31A05]
defines: X4V2S56YQQ
uses: [02BH3MCBQB, RN4G8SGP6P, Z1MHMGFNFW, 0E0B6RA8K0, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]].
For $a \in \R^n$ and $r > 0$, let $B(a, r)$ be the open ball and $S(a, r)$ the sphere of centre $a$ and radius $r$.
Let $\sigma_{a,r}$ be the surface measure on $S(a, r)$ normalised to total mass $1$.
A function $u \colon \Omega \to (-\infty, +\infty]$ is *superharmonic* if:

1. $u$ is [[lower semicontinuous|RN4G8SGP6P]].
2. $u$ is not identically $+\infty$ on any connected component of $\Omega$.
3. For every $a \in \Omega$ and $r > 0$ with $\overline{B(a, r)} \subseteq \Omega$,
$$u(a) \ge \int_{S(a, r)} u \, d\sigma_{a,r}.$$

## Remarks

A function $u$ is superharmonic if and only if $-u$ is [[subharmonic|Z1MHMGFNFW]] and not identically $-\infty$ on any component.
It suffices to require clause 3 for all small enough $r$ at each point.
A function $u$ of class $C^2$ is superharmonic if and only if its [[Laplacian|0E0B6RA8K0]] satisfies $\Delta u \le 0$.
A function is [[harmonic|0DEB0JMN0W]] if and only if it is both superharmonic and subharmonic.

Example: for $n \ge 3$ let $u(x) = \abs{x}^{2-n}$ on $\R^n$, with $u(0) = +\infty$.
It is lower semicontinuous and finite off $0$.
Its mean over $S(a, r)$ equals $\max(\abs{a}, r)^{2-n}$, which is at most $\abs{a}^{2-n} = u(a)$, and at $a = 0$ the value $+\infty$ dominates.
So $u$ is superharmonic.
In the plane, $u(x) = -\log\abs{x}$ is superharmonic in the same way.

Non-example: $u(x) = \abs{x}^2$ is continuous on $\R^n$, but its mean over $S(a, r)$ is $\abs{a}^2 + r^2 > u(a)$, so clause 3 fails.
