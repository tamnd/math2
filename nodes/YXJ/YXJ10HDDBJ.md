---
tag: YXJ10HDDBJ
kind: definition
name: Regularity of minimizers
msc: [49N60, 35J50, 35B65]
defines: 8A8FBH4C7Y
uses: [JRQZ803Q5Y, M4CEZ5K9HP, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_nineteenth_problem
---

## Definition

Let $\Omega \subseteq \R^n$ be a bounded open set, let $m \ge 1$ and $1 < p < \infty$.
Let $J(u) = \int_\Omega L(x, u, \nabla u) \, dx$ be an [[integral functional|JRQZ803Q5Y]] for maps $u \colon \Omega \to \R^m$.
A map $u$ in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}(\Omega; \R^m)$ is a *minimiser* of $J$ if $J(u) \le J(u + \varphi)$ for all $\varphi \in W^{1,p}_0(\Omega; \R^m)$.
Let $k \ge 1$ and $0 < \alpha < 1$.

1. The minimiser $u$ is *regular* (of class $C^{k,\alpha}$) if it agrees almost everywhere with a map in $C^{k,\alpha}(\Omega; \R^m)$.
2. It is *partially regular* if there is a relatively closed set $\Sigma \subseteq \Omega$ of Lebesgue measure zero such that $u$ is regular on $\Omega \setminus \Sigma$.

The *regularity problem* for $J$ asks under which conditions on $L$ every minimiser is regular or partially regular.

## Remarks

Here $C^{k,\alpha}$ is the space of $C^k$ maps whose $k$-th derivatives are locally [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$.

Example: for $m = 1$ and $L(\xi) = \frac{1}{2} \abs{\xi}^2$, minimisers are weak solutions of $\Delta u = 0$.
By Weyl's lemma they are harmonic, hence smooth, so they are regular for every $k$ and $\alpha$.

Non-example: for $n = 1$, $m = 1$ and $L(x, u, \xi) = (\xi^2 - 1)^2$ on $\Omega = (0, 2)$, the function $u(x) = \min(x, 2 - x)$ is a minimiser among maps with its boundary values, since $J(u) = 0$.
It is Lipschitz but not $C^1$, so it is not regular in the sense of clause 1.
Here $L$ is not convex in $\xi$.

For $m = 1$ and smooth, uniformly convex $L(\xi)$ with bounded second derivatives, every minimiser in $W^{1,2}$ is smooth, by the De Giorgi–Nash–Moser theorem and Schauder estimates.
For $m \ge 2$ this fails in general, and partial regularity is the typical result for smooth, uniformly convex or strongly quasiconvex integrands with suitable growth.
