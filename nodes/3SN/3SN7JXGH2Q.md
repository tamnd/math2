---
tag: 3SN7JXGH2Q
kind: definition
name: Variational capacity
msc: [31C45, 31B15, "46E35"]
defines: A1KWT817JX
uses: [0R6EWFKRCF, M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Definition

Let $n \ge 1$, let $1 < p < \infty$, let $\Omega \subseteq \R^n$ be an open set, and let $K \subseteq \Omega$ be a [[compact set|0R6EWFKRCF]].
Let $C_c^\infty(\Omega)$ be the set of smooth real functions with compact support in $\Omega$.
The *variational capacity* of $K$ relative to $\Omega$ is
$$\operatorname{cap}_p(K, \Omega) = \inf \set{ \int_\Omega \abs{\nabla u}^p \, dx : u \in C_c^\infty(\Omega), \ u \ge 1 \text{ on } K }.$$

## Remarks

For an open set $U \subseteq \Omega$ one sets $\operatorname{cap}_p(U, \Omega) = \sup \set{ \operatorname{cap}_p(K, \Omega) : K \subseteq U \text{ compact} }$.
For an arbitrary set $E \subseteq \Omega$ one sets $\operatorname{cap}_p(E, \Omega) = \inf \set{ \operatorname{cap}_p(U, \Omega) : E \subseteq U \subseteq \Omega, \ U \text{ open} }$.
The infimum does not change if the admissible functions are taken in the [[Sobolev space|M4CEZ5K9HP]] $W_0^{1,p}(\Omega)$ and continuous, with $u \ge 1$ on $K$.

Example: let $0 < r < R$, $p \ne n$, $\alpha = (p - n)/(p - 1)$, and let $\sigma_{n-1}$ be the area of the unit sphere in $\R^n$.
The radial function $u$ with $u = 1$ for $\abs{x} \le r$, $u = (\abs{x}^\alpha - R^\alpha)/(r^\alpha - R^\alpha)$ for $r \le \abs{x} \le R$, and $u = 0$ outside, solves the $p$-Laplace equation on the shell.
Its gradient has size $\abs{\alpha} \abs{x}^{\alpha - 1} / \abs{r^\alpha - R^\alpha}$, and integration in polar coordinates gives
$$\operatorname{cap}_p(\bar B_r, B_R) = \sigma_{n-1} \abs{\alpha}^{p-1} \abs{r^\alpha - R^\alpha}^{1-p}.$$
For $p = 2$ and $n = 3$ this is $4 \pi r R / (R - r)$.

Non-example of an admissible function: a function $u \in C_c^\infty(\Omega)$ with $u = 1/2$ on $K$ fails the condition $u \ge 1$ on $K$ and does not enter the infimum.

A related notion is the Sobolev $p$-capacity, which uses $\int_{\R^n} (\abs{u}^p + \abs{\nabla u}^p) \, dx$ and no reference set $\Omega$; for subsets of a bounded open set $\Omega$ both capacities have the same null sets.
