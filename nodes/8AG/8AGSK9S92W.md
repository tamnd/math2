---
tag: 8AGSK9S92W
kind: definition
name: Harmonic map
msc: ["58E20", 53C43]
defines: KZJYG9DS3M
uses: [7CBT4SM83Y, FZBA1HA9ZM, F4NWZNTRMD]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Definition

Let $(M, g)$ and $(N, h)$ be [[Riemannian manifolds|7CBT4SM83Y]] of dimensions $m$ and $n$, and let $u \colon M \to N$ be a smooth map.
Use local coordinates $x^i$ on $M$ and $y^\alpha$ on $N$.
The *tension field* of $u$ is
$$\tau(u)^\gamma = \Delta_g u^\gamma + \sum_{i,j,\alpha,\beta} g^{ij} \, \Gamma^\gamma_{\alpha\beta}(u) \, \partial_i u^\alpha \, \partial_j u^\beta, \qquad \gamma = 1, \dots, n,$$
where $\Delta_g$ is the [[Laplace–Beltrami operator|F4NWZNTRMD]] of $g$ and $\Gamma^\gamma_{\alpha\beta}$ are the [[Christoffel symbols|FZBA1HA9ZM]] of $h$.
The map $u$ is *harmonic* if $\tau(u) = 0$ on $M$.

## Remarks

The tension field is a section of $u^* TN$ and does not depend on the coordinates; it is the trace with respect to $g$ of the covariant derivative of $du$.
Let $M$ be compact.
Then $u$ is harmonic if and only if it is a critical point of the energy
$$E(u) = \frac{1}{2} \int_M \abs{du}^2 \, dV_g, \qquad \abs{du}^2 = \sum g^{ij} h_{\alpha\beta}(u) \, \partial_i u^\alpha \, \partial_j u^\beta,$$
which generalizes the Dirichlet energy; indeed $-\tau(u)$ is the gradient of $E$.

Example: let $N = \R$; then $\Gamma = 0$ and $u$ is harmonic if and only if $\Delta_g u = 0$.
Let $M$ be an interval with its standard metric; then $\tau(u) = 0$ is the geodesic equation, so harmonic maps from an interval are constant-speed geodesics.

Non-example: let $M = N = \R / 2\pi\Z$ with the standard metric and $u(\theta) = \theta + \frac{1}{2}\sin\theta$.
Here $\Gamma = 0$ and $\tau(u) = u''(\theta) = -\frac{1}{2}\sin\theta \ne 0$, so $u$ is not harmonic, although it is a diffeomorphism.
The identity map $\theta \mapsto \theta$ is harmonic.
