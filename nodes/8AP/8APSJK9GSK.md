---
tag: 8APSJK9GSK
kind: definition
name: Fokker–Planck equation
msc: [35Q84, 60J60]
defines: FVQWR7NS00
uses: [B219G9SHJA, 22735FGJV6, 0ZY9DX8FBF, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation
---

## Definition

Let $n, d \ge 1$.
Let $\mu \colon \R^n \times [0, \infty) \to \R^n$ and $\sigma \colon \R^n \times [0, \infty) \to \R^{n \times d}$ be smooth.
Let $D = \frac{1}{2}\sigma \sigma^T$, a symmetric positive semidefinite $n \times n$ matrix at each point.
The *Fokker–Planck equation* with drift $\mu$ and diffusion matrix $D$ is the equation for $p(x, t)$:
$$\partial_t p = -\sum_{i=1}^{n} \partial_{x_i}\big(\mu_i\, p\big) + \sum_{i,j=1}^{n} \partial_{x_i} \partial_{x_j}\big(D_{ij}\, p\big),$$
where $\partial$ denotes [[partial derivatives|09EGC6F8PT]].
It is associated with the [[stochastic differential equation|B219G9SHJA]] $dX_t = \mu(X_t, t)\, dt + \sigma(X_t, t)\, dW_t$, where $W$ is a $d$-dimensional [[Wiener process|22735FGJV6]].

## Remarks

Under suitable regularity of $\mu$ and $\sigma$, if $X_t$ has a smooth [[probability density|0ZY9DX8FBF]] $p(\cdot, t)$, then $p$ solves this equation.
Example: for $n = d = 1$, $\mu = 0$ and $\sigma = 1$, the equation is $p_t = \frac{1}{2} p_{xx}$.
Its solution $p(x, t) = (2\pi t)^{-1/2} e^{-x^2/(2t)}$ is the density of $W_t$; one checks $p_t = \frac{1}{2}p_{xx}$ by direct differentiation.
Non-example: $p_t = -\frac{1}{2} p_{xx}$ is not a Fokker–Planck equation, since it would need $D = -\frac{1}{2}$, which is not positive semidefinite.
The equation is also called the forward Kolmogorov equation.
In one dimension it reads $p_t = -(\mu p)_x + (D p)_{xx}$.
