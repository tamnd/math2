---
tag: WGGS3ER8XN
kind: definition
name: Geodesics in general relativity
msc: [83C10, 53C22, 53C50]
defines: RNRTS8WWNM
uses: [63ZKC7AFX2, NSYMQMHPDN, CAZYGE1T4E, FZBA1HA9ZM, YG74WHC3S9]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesics_in_general_relativity
---

## Definition

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]] with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$, and let $I \subseteq \R$ be an interval.
A smooth curve $\gamma \colon I \to M$ is a *geodesic* if the following holds.
$$\nabla_{\dot\gamma} \dot\gamma = 0.$$
In local coordinates this reads
$$\frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\lambda} \frac{dx^\beta}{d\lambda} = 0,$$
where $\lambda$ is the parameter of the curve and $\Gamma^\mu_{\alpha\beta}$ are the [[Christoffel symbols|FZBA1HA9ZM]] of $g$.
Along a geodesic $g(\dot\gamma, \dot\gamma)$ is constant, and a nonconstant geodesic is called timelike, null or spacelike if this constant is negative, zero or positive.

## Remarks

For a timelike geodesic the parameter $\lambda$ is an affine function of the [[proper time|YG74WHC3S9]] $\tau$, and one usually takes $\lambda = \tau$.
Example: in Minkowski space with $g = -dt^2 + dx^2 + dy^2 + dz^2$, all Christoffel symbols vanish.
So the geodesics are the straight lines $x^\mu(\lambda) = a^\mu + b^\mu \lambda$ with affine parameter.
With $b = (1, v, 0, 0)$ and $\abs{v} < 1$, it is the world line of a particle in uniform motion.
Non-example: for $0 < a < 1$, the curve $t \mapsto (t, a\cos t, a\sin t, 0)$ in units with $c = 1$ is timelike, since $g(\dot\gamma, \dot\gamma) = -1 + a^2 < 0$.
It is not a geodesic, since $\nabla_{\dot\gamma}\dot\gamma = (0, -a\cos t, -a\sin t, 0) \neq 0$; it is the world line of a particle in circular motion.
Timelike geodesics are the critical points of the proper time functional, and light rays in geometric optics follow null geodesics.
