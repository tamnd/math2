---
tag: Q43RD1GK8G
kind: statement
role: theorem
name: Morrey's lower semicontinuity theorem
msc: [49J45]
uses: [DVJ17KVWXP, H6GTJRG26G, M4CEZ5K9HP, JRQZ803Q5Y]
about: [DVJ17KVWXP, H6GTJRG26G]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconvexity_(calculus_of_variations)
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set, let $m \ge 1$, and let $f \colon \R^{m \times n} \to \R$ be continuous.
Let $J(u) = \int_\Omega f(\nabla u) \, dx$, an [[integral functional|JRQZ803Q5Y]] on maps $u \colon \Omega \to \R^m$.

1. $J$ is sequentially weak-$*$ lower semicontinuous on the [[Sobolev space|M4CEZ5K9HP]] $W^{1,\infty}(\Omega; \R^m)$ if and only if $f$ is [[quasiconvex|DVJ17KVWXP]].
2. Let $1 < p < \infty$ and assume $0 \le f(\xi) \le C (1 + \abs{\xi}^p)$ for a constant $C$. Then $J$ is sequentially [[weakly lower semicontinuous|H6GTJRG26G]] on $W^{1,p}(\Omega; \R^m)$ if and only if $f$ is quasiconvex.

## Remarks

For necessity, take $u_k(x) = \xi x + k^{-1} \varphi(kx)$ with $\varphi$ periodic on the unit cube and zero on its boundary.
Then $u_k$ converges weak-$*$ to the affine map $\xi x$, and $J(u_k)$ tends to $\abs{\Omega}$ times the average of $f(\xi + \nabla \varphi)$ over the cube.
Lower semicontinuity then gives the quasiconvexity inequality.
For sufficiency, one localises: on small cubes $\nabla u$ is nearly constant, and quasiconvexity controls the energy of the oscillations of $u_k$ around it.

Part 1 is Morrey's theorem; part 2 under these growth conditions is due to Acerbi and Fusco, after work of Meyers.

Example: $f(\xi) = \abs{\xi}^2 + (\det \xi)^2$ for $2 \times 2$ matrices is polyconvex, hence quasiconvex, so $J$ is weakly lower semicontinuous on $W^{1,4}(\Omega; \R^2)$.

When $m = 1$ or $n = 1$, quasiconvexity is convexity, and the theorem recovers the classical role of convexity in Tonelli's existence theorem.

## Explanations

### L1 human

The theorem answers exactly when the energy of a map can drop in a weak limit.
It cannot drop precisely when the integrand is quasiconvex, that is, when wiggling an affine map never lowers its energy.
So quasiconvexity is not just a convenient assumption; it is the right condition.

### L2 human

Combined with coercivity, the theorem gives existence of minimisers for vectorial problems by the direct method.
Its drawback is that quasiconvexity is hard to verify, which is why one often works with polyconvexity, a sufficient condition, and rank-one convexity, a necessary one.
When the integrand is not quasiconvex, the lower semicontinuous envelope of $J$ is the integral of the quasiconvex envelope of $f$, under suitable growth conditions.
This is the basis of the relaxation theory of microstructure in materials.
