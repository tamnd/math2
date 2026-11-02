---
tag: JMVHZ6HDNZ
kind: statement
role: theorem
name: Legendre–Hadamard condition
msc: [49K10, 35J50]
uses: [JRQZ803Q5Y, WMPCR723MJ, 4C3BANJ8AH]
about: [4C3BANJ8AH]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre%E2%80%93Clebsch_condition
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set and let $m \ge 1$.
Let $L \colon \overline{\Omega} \times \R^m \times \R^{m \times n} \to \R$, written $L(x, u, \xi)$ with $\xi = (\xi^i_\alpha)$, be of class $C^2$.
Let $J(u) = \int_\Omega L(x, u, \nabla u) \, dx$ be the [[integral functional|JRQZ803Q5Y]] on $C^1(\overline{\Omega}; \R^m)$.
Let $u_0 \in C^1(\overline{\Omega}; \R^m)$ be a [[weak local minimiser|WMPCR723MJ]] of $J$ among functions with the same boundary values.
Then for every $x \in \Omega$, every $a \in \R^m$ and every $b \in \R^n$,
$$\sum_{i, j = 1}^{m} \sum_{\alpha, \beta = 1}^{n} \frac{\partial^2 L}{\partial \xi^i_\alpha \, \partial \xi^j_\beta}\big(x, u_0(x), \nabla u_0(x)\big) \, a_i a_j b_\alpha b_\beta \ge 0.$$

## Remarks

The [[second variation|4C3BANJ8AH]] at $u_0$ is nonnegative for all test functions $\varphi \in C^1_c(\Omega; \R^m)$.
One tests it with $\varphi(x) = \varepsilon \, \eta(x) \, a \sin(b \cdot x / \varepsilon)$ for a fixed smooth cut-off function $\eta$ supported near $x_0$.
As $\varepsilon \to 0$, only the term quadratic in $\nabla \varphi$ survives, and its limit is a positive multiple of the stated quadratic form at $x_0$ weighted by $\eta^2$.

The condition asks for positivity only on rank-one matrices $a \otimes b = (a_i b_\alpha)$, not on all of $\R^{m \times n}$.
For $m = 1$ or $n = 1$ every matrix is of the form $a \otimes b$.
Then the condition says that the Hessian of $L$ in $\xi$ is positive semidefinite, as in the one-dimensional Legendre condition.

Example: for $m = n = 2$ and $L(\xi) = \det \xi$, the quadratic form is $2 \det(a \otimes b) = 0$, so the condition holds although the Hessian of $\det$ is indefinite.
For a $C^2$ integrand, the condition at every $\xi$ is equivalent to rank-one convexity of $\xi \mapsto L(x, u, \xi)$.

## Explanations

### L1 human

For maps with several components and several variables, a minimiser need not make the integrand convex in all gradient directions.
It only has to be convex along very special directions, the rank-one matrices $a \otimes b$.
These are the directions in which a gradient can oscillate quickly, like a fine fold or a laminate.

### L2 human

The Legendre–Hadamard condition is the necessary condition from the second variation for vector-valued problems in several variables.
When it holds with a strict inequality and a uniform constant, the Euler–Lagrange system is called strongly elliptic, which is the basic hypothesis of linear elliptic theory for systems.
It is the infinitesimal form of rank-one convexity, which in turn is implied by Morrey's quasiconvexity.
