---
tag: FRKAPMVZ7M
kind: definition
name: Riesz measure of a subharmonic function
msc: [31B05, 31A05]
defines: PR8KWEA3MH
uses: [Z1MHMGFNFW, 0E0B6RA8K0, HZNEQQBCW4, 02BH3MCBQB, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $u$ be [[subharmonic|Z1MHMGFNFW]] on $\Omega$ and not identically $-\infty$ on any connected component of $\Omega$.
Then $u$ is locally integrable on $\Omega$.
Moreover, there is a unique positive [[Radon measure|HZNEQQBCW4]] $\mu_u$ on $\Omega$ such that
$$\int_\Omega u \, \Delta\psi \, d\lambda = \int_\Omega \psi \, d\mu_u \qquad \text{for all } \psi \in C_c^\infty(\Omega),$$
where $\lambda$ is Lebesgue measure and $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
The measure $\mu_u$ is the *Riesz measure* of $u$.
In other words, $\mu_u = \Delta u$ in the sense of distributions.

## Remarks

Some authors normalise differently, for example by $\frac{1}{2\pi}\Delta u$ in the plane, so that $\log\abs{z}$ has Riesz measure $\delta_0$.
If $u$ is of class $C^2$, then $\mu_u = (\Delta u)\, \lambda$.
The function $u$ is [[harmonic|0DEB0JMN0W]] on an open subset $V$ of $\Omega$ if and only if $\mu_u(V) = 0$.

Example: let $u(x) = \abs{x}^2$ on $\R^n$.
Integration by parts gives $\int \abs{x}^2 \Delta\psi \, d\lambda = \int \Delta(\abs{x}^2)\, \psi \, d\lambda = 2n \int \psi \, d\lambda$, so $\mu_u = 2n\,\lambda$.
Example: for $u(z) = \log\abs{z}$ on $\C = \R^2$, Green's formula gives $\mu_u = 2\pi\,\delta_0$.

Non-example: for $v(x) = -\abs{x}^2$, the distribution $\Delta v = -2n\,\lambda$ is a negative measure.
This matches the fact that $v$ is not subharmonic, so the hypothesis of the definition fails and $v$ has no Riesz measure.
