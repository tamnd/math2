---
tag: GVMM9GC7CE
kind: definition
name: Diffusion process
msc: [60J60, 60H10]
defines: 9HDQ094ADQ
uses: [22735FGJV6, 0B77KZCQ51, VPA41PWRR1, 2J1RVQB0CM]
sources:
  - url: https://en.wikipedia.org/wiki/Diffusion_process
---

## Definition

Let $d, m \ge 1$, let $b \colon \R^d \to \R^d$ and $\sigma \colon \R^d \to \R^{d \times m}$ be Lipschitz continuous, and let $W$ be an $m$-dimensional [[Wiener process|22735FGJV6]].
The *diffusion process* (Itô diffusion) with drift $b$ and dispersion $\sigma$ started at $x \in \R^d$ is the unique continuous adapted solution $(X_t)_{t \ge 0}$ of
$$dX_t = b(X_t)\, dt + \sigma(X_t)\, dW_t, \qquad X_0 = x.$$
The matrix $a = \sigma \sigma^{\mathsf{T}}$ is its diffusion matrix.

## Remarks

The process is a strong [[Markov process|0B77KZCQ51]], and by [[Itô's lemma|2J1RVQB0CM]] its [[generator|VPA41PWRR1]] acts on twice continuously differentiable functions $f$ with compact support by
$$Lf(x) = \frac12 \sum_{i,j=1}^d a_{ij}(x) \frac{\partial^2 f}{\partial x_i \partial x_j}(x) + \sum_{i=1}^d b_i(x) \frac{\partial f}{\partial x_i}(x).$$
Example: $d = m = 1$, $b(x) = -\theta x$ with $\theta > 0$ and $\sigma(x) = 1$ give the Ornstein–Uhlenbeck process; both coefficients are Lipschitz, and $Lf = \tfrac12 f'' - \theta x f'$.
Non-example: the Poisson process is a Markov process but not a diffusion, because its paths jump.
In a wider sense, a diffusion is any strong Markov process with continuous paths; the Itô diffusions above form the main class.
