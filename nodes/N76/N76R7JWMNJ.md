---
tag: N76R7JWMNJ
kind: statement
role: theorem
name: Gradient estimates for harmonic functions
msc: [31B05]
uses: [0DEB0JMN0W, 0HYPR64JM2, 0JX86PSSA9, 0ABK9V9Y64]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Statement

Let $n \ge 1$ and let $\omega_n$ be the volume of the unit ball of $\R^n$.
Let $u$ be [[harmonic|0DEB0JMN0W]] on an open set containing the closed ball $\overline{B}(x_0, r)$.

1. The [[gradient|0ABK9V9Y64]] of $u$ at the centre satisfies
$$\abs{\nabla u(x_0)} \le \frac{n}{r} \, \max_{\overline{B}(x_0, r)} \abs{u}.$$
2. For every multi-index $\alpha$ of order $k = \abs{\alpha}$,
$$\abs{\partial^\alpha u(x_0)} \le \frac{C_k}{r^{n+k}} \int_{B(x_0, r)} \abs{u(y)} \, dy, \qquad C_0 = \frac{1}{\omega_n}, \quad C_k = \frac{(2^{n+1} n k)^k}{\omega_n} \ (k \ge 1).$$

## Remarks

Proof idea for part 1: each partial derivative $\partial_i u$ is harmonic, so by the [[mean value property|0HYPR64JM2]] over the ball and the [[divergence theorem|0JX86PSSA9]],
$$\partial_i u(x_0) = \frac{1}{\omega_n r^n} \int_{B(x_0, r)} \partial_i u \, dy = \frac{1}{\omega_n r^n} \int_{\partial B(x_0, r)} u \, \nu_i \, dS.$$
The last integral is at most $\max \abs{u}$ times the area $n \omega_n r^{n-1}$ of the sphere, which gives $\abs{\partial_i u(x_0)} \le \frac{n}{r} \max \abs{u}$.
The same argument for the derivative in the direction of $\nabla u(x_0)$ gives the bound for $\abs{\nabla u(x_0)}$.
Part 2 follows by induction on $k$, applying the same argument on balls of radius $r/k$.
Example: $u(x, y) = x$ on the unit disc has $\abs{\nabla u} = 1$ and $\max \abs{u} = 1$, within the bound $2$ of part 1.
The estimates are interior: they control derivatives at the centre by the size of $u$ on the ball, and they fail near the boundary of the domain.
For instance $u_m(x, y) = \operatorname{Re}(x + iy)^m$ on the unit disc has $\abs{u_m} \le 1$ but $\abs{\nabla u_m(1, 0)} = m$.

## Explanations

### L1 human

A harmonic function cannot change quickly unless it is large.
If it stays between $-M$ and $M$ on a ball of radius $r$, its slope at the centre is at most $n M / r$.
Big balls therefore force small slopes, and this is why bounded harmonic functions on the whole space are constant.

### L2 human

These estimates give Liouville's theorem, the real analyticity of harmonic functions, and the compactness of bounded families of harmonic functions through the Arzelà–Ascoli theorem.
They are the model for interior Schauder and Sobolev estimates for general elliptic equations.
For nonnegative harmonic functions there is a sharper form, $\abs{\nabla u(x_0)} \le \frac{n}{r} u(x_0)$, which leads to Harnack's inequality.
