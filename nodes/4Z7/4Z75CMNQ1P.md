---
tag: 4Z75CMNQ1P
kind: definition
name: Newtonian potential
msc: [31B15, 31B10]
defines: DCMFQ01QGS
uses: [JHKSF3XFY2, 6TJTWQ5HCR, DYR1QFNGNJ, FQTXV6BQZG, BSJ8X2XRN9, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_potential
---

## Definition

Let $n \ge 3$ and let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\R^n$ with finite total mass and compact [[support|FQTXV6BQZG]].
The *Newtonian potential* of $\mu$ is the function $U^\mu \colon \R^n \to [0, +\infty]$,
$$U^\mu(x) = \int \frac{d\mu(y)}{\abs{x - y}^{n-2}}.$$
It is the [[potential|JHKSF3XFY2]] of $\mu$ with respect to the [[Newtonian kernel|6TJTWQ5HCR]].

## Remarks

Example: for $n = 3$ and $\mu = m \, \delta_a$ a point mass, $U^\mu(x) = m / \abs{x - a}$.
Non-example: in $\R^3$ the function $u(x) = \abs{x}^2$ is not the Newtonian potential of any such $\mu$, since a Newtonian potential tends to $0$ at infinity.
The function $U^\mu$ is lower semicontinuous, [[harmonic|0DEB0JMN0W]] on $\R^n \setminus \operatorname{supp} \mu$, and $U^\mu(x) \abs{x}^{n-2} \to \mu(\R^n)$ as $\abs{x} \to \infty$.
If $\mu = f \, dx$ with $f \ge 0$ twice continuously differentiable with compact support, then $U^\mu$ is twice continuously differentiable and $\Delta U^\mu = -(n-2)\sigma_n f$, where $\sigma_n$ is the area of the unit sphere.
Equivalently, $U^\mu = (n-2)\sigma_n \, \Phi * \mu$, where $\Phi$ is the [[fundamental solution of the Laplacian|BSJ8X2XRN9]].
Some texts call $\Phi * f$ itself the Newtonian potential of $f$, and use the same name in the plane with the logarithmic kernel.
