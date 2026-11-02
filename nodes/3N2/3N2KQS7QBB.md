---
tag: 3N2KQS7QBB
kind: definition
name: von Mises–Fisher distribution
msc: [62H11, "60E05"]
defines: V8ZZ7A2FMF
uses: [T62369RFH6, 0ZY9DX8FBF, 0DVDCMA2DK, 8GZJQBPBY0]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Mises%E2%80%93Fisher_distribution
---

## Definition

Let $p \ge 2$ and let $S^{p-1} \subseteq \R^p$ be the unit [[sphere|T62369RFH6]] with its surface measure $\sigma$.
Let $\mu \in S^{p-1}$ and $\kappa > 0$.
Let $I_\nu$ be the modified Bessel function of the first kind of order $\nu$.
The *von Mises–Fisher distribution* $\operatorname{vMF}(\mu, \kappa)$ is the [[distribution|0DVDCMA2DK]] on $S^{p-1}$ with this [[density|0ZY9DX8FBF]] with respect to $\sigma$:
$$f(x) = C_p(\kappa) \exp(\kappa \mu^T x), \qquad C_p(\kappa) = \frac{\kappa^{p/2 - 1}}{(2\pi)^{p/2} I_{p/2 - 1}(\kappa)}.$$
For $\kappa = 0$ it is defined as the uniform distribution on $S^{p-1}$.
The vector $\mu$ is the *mean direction* and $\kappa$ is the *concentration parameter*.

## Remarks

Example: for $p = 3$, $I_{1/2}(\kappa) = \sqrt{2/(\pi \kappa)} \sinh \kappa$, so $C_3(\kappa) = \kappa / (4 \pi \sinh \kappa)$.
Check: in spherical coordinates with $\mu$ as north pole, $\int_{S^2} e^{\kappa \cos \theta} \, d\sigma = 2\pi \int_0^\pi e^{\kappa \cos \theta} \sin \theta \, d\theta = 4 \pi \sinh(\kappa)/\kappa$.
Non-example: a density proportional to $\exp(\kappa (\mu^T x)^2)$ with $\kappa > 0$ is not von Mises–Fisher.
It takes the same value at $x$ and $-x$, so its maximum is attained at both $\mu$ and $-\mu$, while a von Mises–Fisher density has a single maximum.
The density is largest at $x = \mu$ and smallest at $x = -\mu$, and it depends on $x$ only through the angle to $\mu$.
For $p = 2$, writing $x = (\cos \theta, \sin \theta)$ gives the von Mises density $e^{\kappa \cos(\theta - \theta_0)} / (2 \pi I_0(\kappa))$.
The maximum likelihood estimate of $\mu$ from a sample is its mean direction.
