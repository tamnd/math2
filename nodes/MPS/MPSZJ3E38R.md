---
tag: MPSZJ3E38R
kind: definition
name: Perron method
msc: [31B20, 31A25, 35J25]
defines: AEZ7PPCNQS
uses: [Z1MHMGFNFW, 8D56GQ4AG8, 02BH3MCBQB, 05D5EGMFYV, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] with [[boundary|05D5EGMFYV]] $\partial\Omega$, and let $f \colon \partial\Omega \to \R$ be a bounded function.
The *Perron family* of $f$ is the set $\mathcal{S}_f$ of all [[subharmonic functions|Z1MHMGFNFW]] $v$ on $\Omega$ such that
$$\limsup_{x \to \xi, \, x \in \Omega} v(x) \le f(\xi) \quad \text{for every } \xi \in \partial\Omega.$$
The *Perron solution* of $f$ is the function $H_f \colon \Omega \to \R$ given by the [[supremum|0BTMQ04556]]
$$H_f(x) = \sup_{v \in \mathcal{S}_f} v(x).$$
The *Perron method* is the construction of $H_f$ as a candidate solution of the [[Dirichlet problem|8D56GQ4AG8]] with boundary data $f$.

## Remarks

The family $\mathcal{S}_f$ is not empty, since it contains the constant $\inf f$, and each $v \in \mathcal{S}_f$ is at most $\sup f$ by the maximum principle; so $H_f$ is finite.
Perron's theorem says that $H_f$ is harmonic on $\Omega$.
Its proof replaces a function of the family by its Poisson integral on a small ball, which keeps it in the family and makes it larger.
Example: on the unit disc with $f(\xi) = \xi_1$, the function $v(x) = x_1$ belongs to $\mathcal{S}_f$, and the maximum principle gives $v \le x_1$ for every $v \in \mathcal{S}_f$, so $H_f(x) = x_1$.
Non-example: $v(x) = x_1 + \frac12$ is subharmonic but not in $\mathcal{S}_f$, since its boundary values exceed $f$ by $\frac12$.
A boundary point $\xi$ at which $H_f(x) \to f(\xi)$ for every continuous $f$ is called a regular boundary point.
