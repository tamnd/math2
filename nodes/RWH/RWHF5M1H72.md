---
tag: RWHF5M1H72
kind: statement
role: theorem
name: Gauss's law
msc: [78A30, 31B10]
uses: [YZ7Q9DP8RT, 6XPSV47R56, 026J1MG2NW, 0MWV6ZTK6S, 0JX86PSSA9]
about: [YZ7Q9DP8RT]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_law
same_as:
  wikidata: Q173356
  wikipedia: Gauss's law
---

## Statement

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
Let $\rho \colon \R^3 \to \R$ be a bounded, measurable [[charge density|6XPSV47R56]] with compact support, and let $E$ be its [[electric field|YZ7Q9DP8RT]].
Let $\Omega \subset \R^3$ be a bounded open set with $C^1$ boundary $\partial \Omega$ and outward unit normal $n$.
Then the [[flux|026J1MG2NW]] of $E$ through $\partial \Omega$ is
$$\int_{\partial \Omega} E \cdot n \, dA = \frac{1}{\varepsilon_0} \int_\Omega \rho(y) \, dy.$$
If moreover $\rho$ is continuously differentiable, then $E$ is continuously differentiable and its [[divergence|0MWV6ZTK6S]] is $\nabla \cdot E = \rho / \varepsilon_0$ on $\R^3$.

## Remarks

The proof reduces to one point charge by superposition and Fubini's theorem.
For a charge $q$ at $y$, the field $q (x - y) / (4 \pi \varepsilon_0 \abs{x - y}^3)$ has divergence zero away from $y$.
By the [[divergence theorem|0JX86PSSA9]], its flux through $\partial \Omega$ equals its flux through a small sphere around $y$ if $y \in \Omega$, which is $q / \varepsilon_0$, and it is $0$ if $y \notin \overline{\Omega}$.
For point charges, the same holds when no charge lies on $\partial \Omega$: the flux is the sum of the charges inside $\Omega$ divided by $\varepsilon_0$.
Example: a ball of radius $R$ with uniform total charge $Q$ has, at distance $r > R$ from its centre, a radial field of size $Q / (4 \pi \varepsilon_0 r^2)$, by symmetry and the integral form.

## Explanations

### L1 human

Gauss's law counts charge by looking only at a closed surface around it.
The total outflow of the electric field through the surface tells how much charge is inside.
Charges outside the surface contribute nothing, because their field lines enter and leave again.

### L2 human

Gauss's law is the integral form of the equation $\nabla \cdot E = \rho / \varepsilon_0$, which is the first of [[Maxwell's equations|9BWWD4QK8Y]].
It is equivalent to Coulomb's law for static fields, once one also knows that the field is curl-free.
With symmetry, it gives the field of spheres, cylinders and planes without any integration.
Combined with $E = -\nabla \varphi$, it yields Poisson's equation for the electric potential.
