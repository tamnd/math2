---
tag: QDXXWA1QGF
kind: statement
role: theorem
name: Green's identities
msc: [31B10, 35J05]
uses: [0JX86PSSA9, 0E0B6RA8K0, 0ABK9V9Y64, 06KWGHDN2J, BSJ8X2XRN9]
about: [0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_identities
same_as:
  wikidata: Q1544810
  wikipedia: Green's identities
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set with $C^1$ boundary $\partial\Omega$, outward unit normal $\nu$ and surface measure $dS$.
For a function $w$ of class $C^1$ near $\partial\Omega$, write $\partial w / \partial \nu = \nabla w \cdot \nu$ for its normal [[derivative|06KWGHDN2J]].
Let $u$ and $v$ be twice continuously differentiable on an open set that contains the closure $\overline{\Omega}$.

1. (First identity.) $\displaystyle \int_\Omega \left( u \, \Delta v + \nabla u \cdot \nabla v \right) dx = \int_{\partial\Omega} u \, \frac{\partial v}{\partial \nu} \, dS.$
2. (Second identity.) $\displaystyle \int_\Omega \left( u \, \Delta v - v \, \Delta u \right) dx = \int_{\partial\Omega} \left( u \, \frac{\partial v}{\partial \nu} - v \, \frac{\partial u}{\partial \nu} \right) dS.$
3. (Third identity.) For every $x \in \Omega$,
$$u(x) = \int_{\partial\Omega} \left( \Phi(y - x) \, \frac{\partial u}{\partial \nu}(y) - u(y) \, \frac{\partial \Phi}{\partial \nu_y}(y - x) \right) dS(y) - \int_\Omega \Phi(y - x) \, \Delta u(y) \, dy,$$
where $\Phi$ is the [[fundamental solution of the Laplacian|BSJ8X2XRN9]], normalised by $-\Delta\Phi = \delta$.

Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]] and $\nabla$ is the [[gradient|0ABK9V9Y64]].

## Remarks

The first identity is the [[divergence theorem|0JX86PSSA9]] applied to the vector field $u \nabla v$, whose divergence is $u \Delta v + \nabla u \cdot \nabla v$.
The second identity follows by writing the first one also with $u$ and $v$ exchanged and subtracting.
The third identity applies the second one with $v(y) = \Phi(y - x)$ on $\Omega$ minus a small ball $B(x, \varepsilon)$, and lets $\varepsilon \to 0$; the small sphere contributes $u(x)$ in the limit.
For the first identity it is enough that $u$ is of class $C^1$.
Example: with $u = 1$, the first identity gives $\int_\Omega \Delta v \, dx = \int_{\partial\Omega} \partial v / \partial \nu \, dS$; so a harmonic function has zero total flux through $\partial\Omega$.
Example: with $u = v$ harmonic, it gives $\int_\Omega \abs{\nabla u}^2 dx = \int_{\partial\Omega} u \, \partial u / \partial \nu \, dS$, which proves uniqueness for the Dirichlet problem.

## Explanations

### L1 human

Green's identities are the integration by parts formulas for the Laplacian.
They trade an integral over a region for an integral over its boundary.
In one dimension the first identity is just $\int_a^b (u v'' + u' v') \, dx = [u v']_a^b$.

### L2 human

These identities are the basic tool for boundary value problems of Laplace and Poisson type.
The first one gives energy estimates and uniqueness of solutions, and it underlies the weak formulation of elliptic equations.
The second one shows that the Laplacian is symmetric for functions that vanish on the boundary, which leads to the symmetry of Green's functions.
The third one is the representation formula: a function is determined inside $\Omega$ by its Laplacian, its boundary values and its normal derivatives.
It leads to the Poisson integral formula once a Green's function is known.
