---
tag: 33WFDJAXQ3
kind: definition
name: Method of separation of variables for heat conduction
msc: [35K05, 35C05, "80A19"]
defines: DWMTKJ07PT
uses: [VNB1BFDEYK, PR2DV03M4H, S36XX2PVNH, 7P72CCAMGZ, CS4ZZX092Z]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_of_variables
---

## Definition

Let $\ell > 0$ and $\alpha > 0$, and let $f \colon [0, \ell] \to \R$ be square-integrable.
Consider the [[heat equation|VNB1BFDEYK]] for a rod with [[thermal diffusivity|CS4ZZX092Z]] $\alpha$, ends held at temperature $0$ and initial temperature $f$:
$$u_t = \alpha u_{xx} \ (0 < x < \ell,\ t > 0), \qquad u(0, t) = u(\ell, t) = 0, \qquad u(x, 0) = f(x).$$
The *method of [[separation of variables|PR2DV03M4H]]* for this problem consists of the following steps.

1. Seek nonzero solutions of the equation and the boundary conditions of the form $u(x, t) = X(x)\, T(t)$.
2. Substituting gives $T'(t) / (\alpha T(t)) = X''(x) / X(x)$; both sides must equal a constant $-\mu$, so $X'' + \mu X = 0$ with $X(0) = X(\ell) = 0$, and $T' + \alpha \mu T = 0$.
3. Solve this [[Sturm–Liouville problem|7P72CCAMGZ]]: its eigenvalues are $\mu_k = (k \pi / \ell)^2$ with eigenfunctions $X_k(x) = \sin(k \pi x / \ell)$, $k = 1, 2, \ldots$, and then $T_k(t) = e^{-\alpha \mu_k t}$.
4. Superpose: $u(x, t) = \sum_{k \ge 1} b_k e^{-\alpha (k \pi / \ell)^2 t} \sin(k \pi x / \ell)$, with $b_k = \frac{2}{\ell} \int_0^\ell f(x) \sin(k \pi x / \ell)\, dx$ the coefficients of the [[Fourier sine series|S36XX2PVNH]] of $f$.

The same steps apply to other linear homogeneous boundary conditions and to rectangles, cylinders and balls, with the matching eigenfunctions.

## Remarks

For each $t_0 > 0$ the series converges uniformly on $[0, \ell] \times [t_0, \infty)$ with all its derivatives, because of the factors $e^{-\alpha \mu_k t}$, and its sum solves the problem.
Example: for $\ell = \pi$, $\alpha = 1$ and $f(x) = \sin x + 3 \sin 3x$, the method gives $u(x, t) = e^{-t} \sin x + 3 e^{-9t} \sin 3x$.
Check: $u_t = -e^{-t} \sin x - 27 e^{-9t} \sin 3x = u_{xx}$, $u(0, t) = u(\pi, t) = 0$ and $u(x, 0) = f(x)$.
Non-example: with the end condition $u(0, t) = 1$, $u(\ell, t) = 0$, the boundary conditions are not homogeneous, and no product $X(x) T(t)$ with $T$ nonconstant satisfies them.
One first subtracts the steady state $1 - x / \ell$, and then the method applies to the difference.
For large $t$, the first term dominates, so the temperature decays like $e^{-\alpha \pi^2 t / \ell^2}$.
