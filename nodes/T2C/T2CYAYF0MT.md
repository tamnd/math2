---
tag: T2CYAYF0MT
kind: statement
role: theorem
name: Gauss's law for potentials
msc: [31B15, 31B10]
uses: [DCMFQ01QGS, 0JX86PSSA9, QDXXWA1QGF, DYR1QFNGNJ, FQTXV6BQZG]
about: [DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_law_for_gravity
---

## Statement

Let $n \ge 3$ and let $\sigma_n$ be the area of the unit sphere of $\R^n$.
Let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\R^n$ with finite mass and compact [[support|FQTXV6BQZG]], and let $U^\mu(x) = \int \abs{x - y}^{2-n} \, d\mu(y)$ be its [[Newtonian potential|DCMFQ01QGS]].
Let $\Omega \subseteq \R^n$ be a bounded open set with $C^1$ boundary $\partial\Omega$ and outward unit normal $\nu$.
Assume that $\partial\Omega$ does not meet the support of $\mu$.
Then
$$\int_{\partial\Omega} \frac{\partial U^\mu}{\partial \nu} \, dS = -(n-2)\,\sigma_n \, \mu(\Omega).$$

## Remarks

Proof idea: first take $\mu = \delta_y$ with $y \notin \partial\Omega$.
If $y \notin \overline{\Omega}$, the function $x \mapsto \abs{x - y}^{2-n}$ is harmonic on a neighbourhood of $\overline{\Omega}$, and the flux is $0$ by the [[divergence theorem|0JX86PSSA9]] (or [[Green's first identity|QDXXWA1QGF]] with $u = 1$).
If $y \in \Omega$, remove a small ball about $y$; the flux through the small sphere is $(2-n) r^{1-n} \cdot \sigma_n r^{n-1} = -(n-2)\sigma_n$.
The general case follows by integrating in $y$ against $\mu$ and exchanging the integrals, which is allowed because $\partial\Omega$ stays at positive distance from the support of $\mu$.
In $\R^3$ the constant is $-4\pi$: with the gravitational field $g = \nabla(G U^\mu)$ pointing towards the masses, the flux of $g$ out of a closed surface is $-4\pi G$ times the enclosed mass.
The hypothesis on $\partial\Omega$ is needed: for a point mass at a point where $\partial\Omega$ is smooth, the flux counts only half of that mass.

## Explanations

### L1 human

Draw any closed surface around some masses.
The total amount of gravitational field going in through the surface only depends on how much mass is inside, not on where it sits or how the surface is shaped.
Masses outside the surface contribute nothing: their field goes in on one side and out on the other.

### L2 human

This is the integral form of the distributional equation $\Delta U^\mu = -(n-2)\sigma_n \mu$, obtained by integrating over $\Omega$ and using the divergence theorem.
It gives a quick proof of the shell theorem by symmetry: for a radial mass distribution, the flux through a sphere fixes the radial derivative of the potential.
The same argument with the logarithmic kernel in the plane gives the constant $-2\pi$.
