---
tag: YGMTZJY1MR
kind: definition
name: Heat kernel
msc: [35K08, 35K05]
defines: KD404MF042
uses: [VP2HN86VAG, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_kernel
---

## Definition

Let $n \ge 1$.
The *heat kernel* of $\R^n$ is the function $\Phi \colon \R^n \times (0, \infty) \to (0, \infty)$ given by
$$\Phi(x, t) = \frac{1}{(4 \pi t)^{n/2}} \exp\left( -\frac{\abs{x}^2}{4t} \right).$$
It solves the [[heat equation|VP2HN86VAG]] $\partial_t \Phi = \Delta \Phi$ on $\R^n \times (0, \infty)$, satisfies $\int_{\R^n} \Phi(x, t) \, dx = 1$ for every $t > 0$, and $\Phi(\cdot, t)$ tends to the Dirac measure at $0$ as $t \to 0^+$.

## Remarks

Check for $n = 1$: $\partial_t \Phi = \Phi \cdot \big( -\tfrac{1}{2t} + \tfrac{x^2}{4t^2} \big)$ and $\partial_x \Phi = -\tfrac{x}{2t} \Phi$, so $\partial_x^2 \Phi = \Phi \cdot \big( \tfrac{x^2}{4t^2} - \tfrac{1}{2t} \big)$, which is the same.
For bounded continuous $g$, the function $u(x, t) = \int_{\R^n} \Phi(x - y, t) g(y) \, dy$ solves the heat equation for $t > 0$ and tends to $g(x)$ as $t \to 0^+$.
For each $t$, $\Phi(\cdot, t)$ is the density of a [[normal distribution|05AQE0QR0D]] with mean $0$ and covariance $2t$ times the identity.
Non-example: $p(x, t) = (2 \pi t)^{-n/2} e^{-\abs{x}^2/(2t)}$ is not the heat kernel of $\partial_t = \Delta$; it solves $\partial_t p = \tfrac12 \Delta p$ and is the transition density of Brownian motion.
More generally, a domain with a boundary condition, or a Riemannian manifold, has a heat kernel $K(x, y, t)$.
It is the function such that $u(x, t) = \int K(x, y, t) g(y) \, dy$ solves the heat equation with that boundary condition and initial value $g$.
