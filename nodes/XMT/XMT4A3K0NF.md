---
tag: XMT4A3K0NF
kind: definition
name: Classical field theory
msc: [70S05, 70S20, 35L05]
defines: V6J6HAMXRM
uses: [SANYJGZ311, PS0VV149ET, GC5BDZ6QBC, CX4M8K61AB]
sources:
  - url: https://en.wikipedia.org/wiki/Classical_field_theory
---

## Definition

Let $n, k \ge 1$ and let $U \subseteq \R^n$ be an open set, a region of spacetime with coordinates $x^0, \dots, x^{n-1}$.
A *classical (Lagrangian) field theory* on $U$ with $k$ field components is given by a [[Lagrangian density|SANYJGZ311]] $\mathcal{L}(x, y^a, z^a_\mu)$ on $U \times \R^k \times \R^{kn}$.
Its *fields* are the smooth maps $\varphi \colon U \to \R^k$.
Its *field equations* are the [[Euler–Lagrange equations|PS0VV149ET]] of $\mathcal{L}$:
$$\frac{\partial \mathcal{L}}{\partial y^a}\big(x, \varphi, \partial \varphi\big) - \sum_{\mu = 0}^{n-1} \frac{\partial}{\partial x^\mu} \left( \frac{\partial \mathcal{L}}{\partial z^a_\mu}\big(x, \varphi, \partial \varphi\big) \right) = 0, \qquad a = 1, \dots, k.$$
A *solution* is a field that satisfies these equations on $U$.

## Remarks

The field equations form a system of $k$ [[partial differential equations|GC5BDZ6QBC]] of order at most two for $\varphi$.

Example: for $n = 2$, $k = 1$ and $\mathcal{L} = \frac{1}{2} z_0^2 - \frac{c^2}{2} z_1^2$ with $c > 0$, one has $\partial \mathcal{L} / \partial y = 0$, $\partial \mathcal{L} / \partial z_0 = z_0$ and $\partial \mathcal{L} / \partial z_1 = -c^2 z_1$.
The field equation is $\partial_0^2 \varphi - c^2 \partial_1^2 \varphi = 0$, the one-dimensional wave equation.

Non-example: the expression $\varphi \, \partial_0^2 \varphi$ depends on a second derivative of the field, so it is not a first-order Lagrangian density in the sense above.
Field theories with such higher-order densities exist, but their Euler–Lagrange equations have extra terms.

In the geometric setting, the fields are sections of a [[fiber bundle|CX4M8K61AB]] $Y \to X$ over a spacetime manifold $X$.
The Lagrangian density is then defined on the first jet bundle of $Y$.
Field theories can also be given by Hamiltonian formulations, or directly by field equations without a Lagrangian.
