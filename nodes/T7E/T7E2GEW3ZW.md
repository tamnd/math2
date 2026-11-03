---
tag: T7E2GEW3ZW
kind: definition
name: Lagrangian density
msc: [70S05, 49S05]
defines: SANYJGZ311
uses: [JRQZ803Q5Y, PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_(field_theory)
---

## Definition

Let $n, k \ge 1$ and let $U \subseteq \R^n$ be an open set, a region of spacetime with coordinates $x = (x^0, \dots, x^{n-1})$.
A *field* on $U$ is a smooth map $\varphi = (\varphi^1, \dots, \varphi^k) \colon U \to \R^k$, and $\partial_\mu \varphi^a = \partial \varphi^a / \partial x^\mu$.
A *(first-order) Lagrangian density* is a smooth function
$$\mathcal{L} \colon U \times \R^k \times \R^{k n} \to \R, \qquad (x, y^a, z^a_\mu) \mapsto \mathcal{L}(x, y, z).$$
Along a field $\varphi$ it is evaluated as $\mathcal{L}(x, \varphi(x), \partial \varphi(x))$.
The *action* of $\varphi$ on a region $D$ with compact closure in $U$ is
$$S_D[\varphi] = \int_D \mathcal{L}\big(x, \varphi(x), \partial \varphi(x)\big) \, d^n x.$$

## Remarks

The action is an [[integral functional|JRQZ803Q5Y]] with the integrand $\mathcal{L}$.
Its smooth critical points under variations with compact support in $U$ are the solutions of the [[Euler–Lagrange equations|PS0VV149ET]]
$$\frac{\partial \mathcal{L}}{\partial y^a} - \partial_\mu \left( \frac{\partial \mathcal{L}}{\partial z^a_\mu} \right) = 0, \qquad a = 1, \dots, k,$$
with summation over $\mu$ and with all terms evaluated along $\varphi$.

Example: let $n = 4$, $k = 1$, $\eta = \mathrm{diag}(1, -1, -1, -1)$ and $m \ge 0$.
The density $\mathcal{L} = \frac{1}{2} \eta^{\mu\nu} \partial_\mu \varphi \, \partial_\nu \varphi - \frac{1}{2} m^2 \varphi^2$ has $\partial \mathcal{L} / \partial y = -m^2 \varphi$ and $\partial \mathcal{L} / \partial z_\mu = \eta^{\mu\nu} \partial_\nu \varphi$.
So its Euler–Lagrange equation is $\eta^{\mu\nu} \partial_\mu \partial_\nu \varphi + m^2 \varphi = 0$, the [[Klein–Gordon equation|AYCCDQWCJF]].

Non-example: the expression $\int_U \int_U K(x, x') \varphi(x) \varphi(x') \, d^n x \, d^n x'$ with a kernel $K$ is not the integral of a Lagrangian density, because the integrand at $x$ depends on the values of $\varphi$ at other points.

Densities that also depend on higher derivatives of $\varphi$ are used too; then the Euler–Lagrange equations contain more terms.
On a manifold, a Lagrangian density is a horizontal $n$-form on the first jet bundle, written $\mathcal{L} \, d^n x$ in coordinates.
