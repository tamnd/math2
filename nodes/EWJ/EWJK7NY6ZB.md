---
tag: EWJK7NY6ZB
kind: statement
role: theorem
name: Duistermaat–Heckman formula
msc: [53D20, 55N91]
uses: [ZARM34FZ6Z, CAN490EPRT, 3N66TM3TSQ, 2Z2QVWZ262]
about: [ZARM34FZ6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Duistermaat%E2%80%93Heckman_formula
same_as:
  wikidata: Q5312666
  wikipedia: Duistermaat–Heckman formula
---

## Statement

Let $(M, \omega)$ be a compact [[symplectic manifold|CAN490EPRT]] of dimension $2n$.
Let a torus $T$ act on $M$ with a [[moment map|ZARM34FZ6Z]] $\mu \colon M \to \mathfrak{t}^*$, and assume that the fixed points of $T$ are isolated.
At a fixed point $p$, identify $(T_p M, \omega_p)$ with $\C^n$ by an $\omega_p$-compatible complex structure.
Let $w_{1,p}, \ldots, w_{n,p} \in \mathfrak{t}^*$ be the weights of the action of $T$ on it, with signs fixed by the same convention as the sign of $\mu$.
Then for every $X \in \mathfrak{t}$ with $\langle w_{j,p}, X \rangle \ne 0$ for all $j$ and $p$,
$$\int_M e^{\langle \mu, X \rangle} \frac{\omega^n}{n!} = (2\pi)^n \sum_{p \in M^T} \frac{e^{\langle \mu(p), X \rangle}}{\prod_{j=1}^n \langle w_{j,p}, X \rangle}.$$

## Remarks

If $X$ is replaced by $iX$, the integral on the left becomes an oscillatory integral.
The right side is then exactly its stationary phase approximation, so this approximation has no error.
An equivalent form concerns the [[pushforward measure|3N66TM3TSQ]] $\mu_*(\omega^n / n!)$, the Duistermaat–Heckman measure.
It has a piecewise polynomial density with respect to [[Lebesgue measure|2Z2QVWZ262]] on the affine span of $\mu(M)$.
This form holds without the assumption of isolated fixed points.
A modern proof uses equivariant cohomology and the Atiyah–Bott–Berline–Vergne localization formula.

Example: the circle acts on the unit sphere $S^2$ by rotation about the vertical axis, $\omega$ is the area form of total area $4\pi$, and $\mu$ is the height $z$.
By Archimedes, the area between heights $a < b$ is $2\pi(b - a)$, so the pushforward measure is $2\pi$ times Lebesgue measure on $[-1, 1]$.
Then $\int_{S^2} e^{tz} \omega = 2\pi (e^t - e^{-t}) / t$, which matches the two fixed points $z = 1$ and $z = -1$ with weights $1$ and $-1$.

## Explanations

### L1 human

When a torus symmetry acts on a compact symplectic manifold, certain integrals over the whole manifold can be computed from the few points that the symmetry fixes.
The formula replaces an integral by a finite sum.
It also says that the symplectic volume is spread over the moment polytope by a piecewise polynomial density.

### L2 human

On $S^2$ the density is constant, which is Archimedes' theorem that slices of a sphere of equal height have equal area.
The formula is an early instance of localization in equivariant cohomology, and it inspired many results on exact integration, including path integral heuristics in physics.
Together with the [[Atiyah–Guillemin–Sternberg convexity theorem|5CTHC6612N]] it gives a detailed picture of the image of a moment map.
