---
tag: E8TQZG66XM
kind: definition
name: Heat kernel on a Riemannian manifold
msc: [58J35, 35K08]
defines: 327NP6S7H5
uses: [7CBT4SM83Y, F4NWZNTRMD, KD404MF042, B8TYKV7AA1]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_kernel
---

## Definition

Let $(M, g)$ be a closed [[Riemannian manifold|7CBT4SM83Y]] with volume measure $dv$, and let $\Delta = -\operatorname{div} \operatorname{grad}$ be its [[Laplace–Beltrami operator|F4NWZNTRMD]], with the sign that makes it nonnegative.
The *heat kernel* of $M$ is the function $K \colon (0, \infty) \times M \times M \to \R$ such that:

1. $K$ is continuous, and it is smooth in $t$ and $x$;
2. $\partial_t K(t, x, y) + \Delta_x K(t, x, y) = 0$ for all $t > 0$ and $x, y \in M$;
3. for every continuous $f \colon M \to \R$ and every $x \in M$, $\int_M K(t, x, y) f(y) \, dv(y) \to f(x)$ as $t \to 0^+$.

Such a function exists and is unique.

## Remarks

If $\phi_0, \phi_1, \ldots$ is an orthonormal basis of $L^2(M)$ of eigenfunctions with $\Delta \phi_j = \lambda_j \phi_j$, then
$$K(t, x, y) = \sum_{j \ge 0} e^{-t \lambda_j} \phi_j(x) \phi_j(y),$$
the series converging uniformly for $t \ge t_0 > 0$.
So $K(t, \cdot, \cdot)$ is the integral kernel of the operator $e^{-t\Delta}$, and $K$ is smooth, symmetric in $x$ and $y$, and positive.
The same definition, with $\Delta$ replaced by a Laplace-type operator on a vector bundle, gives heat kernels of operators such as the Hodge Laplacian.
On a complete noncompact manifold one takes the minimal positive fundamental solution; for $\R^n$ it is the Gaussian [[heat kernel|KD404MF042]].

Example: on $S^1 = \R / 2\pi\Z$ with $\Delta = -d^2/d\theta^2$, the eigenvalues are $k^2$ with eigenfunctions $e^{ik\theta}$, and
$$K(t, \theta, \theta') = \frac{1}{2\pi} \sum_{k \in \Z} e^{-k^2 t} e^{ik(\theta - \theta')}.$$
Each term solves the heat equation.
For fixed $t$, $K(t, \theta, \cdot)$ is the sum over $m \in \Z$ of the Gaussian kernel of $\R$ translated by $2\pi m$.
It is a positive kernel of total mass $1$ that concentrates at $\theta$ as $t \to 0^+$, which gives clause 3.

Non-example: on $S^1$ the constant $K \equiv 1/(2\pi)$ satisfies clauses 1 and 2, but $\int K f \to \frac{1}{2\pi}\int f$, not $f(x)$, so clause 3 fails.
