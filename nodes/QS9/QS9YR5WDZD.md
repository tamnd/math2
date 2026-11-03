---
tag: QS9YR5WDZD
kind: definition
name: De Donder–Weyl theory
msc: [70S05, 70G45, 49S05]
defines: DB5ZVAPY30
uses: [SANYJGZ311, ZQYMWVT1TT, PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/De_Donder%E2%80%93Weyl_theory
---

## Definition

Let $n, k \ge 1$ and let $U \subseteq \R^n$ be open, with coordinates $x^1, \dots, x^n$.
Let $\mathcal{L}(x, y^a, z^a_\mu)$ be a first-order [[Lagrangian density|SANYJGZ311]] for fields $\varphi \colon U \to \R^k$, where $z^a_\mu$ stands for $\partial_\mu \varphi^a$.

1. The *polymomenta* are $p^\mu_a = \dfrac{\partial \mathcal{L}}{\partial z^a_\mu}(x, y, z)$.
2. The density $\mathcal{L}$ is *regular* if, for all fixed $(x, y)$, the map $z \mapsto p$ is a diffeomorphism onto an open set; then $z = z(x, y, p)$ is its inverse.
3. For regular $\mathcal{L}$, the *De Donder–Weyl Hamiltonian* is
$$H(x, y, p) = p^\mu_a \, z^a_\mu(x, y, p) - \mathcal{L}\big(x, y, z(x, y, p)\big),$$
with summation over $\mu$ and $a$.
4. The *De Donder–Weyl equations* for $\varphi$ and $p^\mu_a \colon U \to \R$ are
$$\partial_\mu \varphi^a = \frac{\partial H}{\partial p^\mu_a}, \qquad \sum_{\mu = 1}^n \partial_\mu p^\mu_a = -\frac{\partial H}{\partial y^a}.$$

*De Donder–Weyl theory* is the description of the field theory of $\mathcal{L}$ by $H$ and these equations.

## Remarks

The map $z \mapsto p$ is a fiberwise [[Legendre transformation|ZQYMWVT1TT]].
For regular $\mathcal{L}$, a smooth $\varphi$ solves the [[Euler–Lagrange equations|PS0VV149ET]] of $\mathcal{L}$ if and only if $\varphi$ together with $p^\mu_a = \partial \mathcal{L} / \partial z^a_\mu (x, \varphi, \partial \varphi)$ solves the De Donder–Weyl equations.

Example: for $n = 1$, the variable $x^1 = t$ is time, there is one momentum $p_a$ per coordinate, $H$ is the usual Hamiltonian, and the equations are Hamilton's equations $\dot\varphi^a = \partial H / \partial p_a$, $\dot p_a = -\partial H / \partial y^a$.

Example: for $n = 4$, $k = 1$, $\eta = \mathrm{diag}(1, -1, -1, -1)$ and $\mathcal{L} = \frac{1}{2} \eta^{\mu\nu} z_\mu z_\nu - \frac{1}{2} m^2 y^2$, one has $p^\mu = \eta^{\mu\nu} z_\nu$, which is invertible.
Then $H = \frac{1}{2} \eta_{\mu\nu} p^\mu p^\nu + \frac{1}{2} m^2 y^2$, and the equations $\partial_\mu \varphi = \eta_{\mu\nu} p^\nu$, $\partial_\mu p^\mu = -m^2 \varphi$ give the Klein–Gordon equation $\eta^{\mu\nu} \partial_\mu \partial_\nu \varphi + m^2 \varphi = 0$.

Non-example: for $n = 2$, $k = 1$ and $\mathcal{L} = z_1$, the polymomenta are $p^1 = 1$, $p^2 = 0$ for all $z$, so the map $z \mapsto p$ is not injective and clause 2 fails.
