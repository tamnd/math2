---
tag: GPQ9JNSDPA
kind: statement
role: theorem
name: Fefferman's expansion of the Bergman kernel
msc: [32A25, 32A36, 32T15]
uses: [8RWDHW0CXC, Z7RVXBA2KB, 0V33BNKZ9S]
about: [8RWDHW0CXC, Z7RVXBA2KB]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_kernel
---

## Statement

Let $n \ge 1$ and let $\Omega \subset \C^n$ be a bounded [[strongly pseudoconvex domain|Z7RVXBA2KB]] with $C^\infty$ boundary.
Let $\rho$ be a $C^\infty$ defining function of $\Omega$: a real [[smooth function|0V33BNKZ9S]] on a neighbourhood of $\overline{\Omega}$ with $\Omega = \set{\rho < 0}$ and $d\rho \ne 0$ on $\partial\Omega$.
Let $K(z) = K(z, z)$ be the [[Bergman kernel|8RWDHW0CXC]] of $\Omega$ on the diagonal.
Then there are functions $\varphi, \psi \in C^\infty(\overline{\Omega})$, with $\varphi > 0$ on $\partial\Omega$, such that
$$K(z) = \frac{\varphi(z)}{(-\rho(z))^{n+1}} + \psi(z) \log(-\rho(z)) \quad \text{for all } z \in \Omega.$$

## Remarks

The value of $\varphi$ on $\partial\Omega$ is an explicit expression in the first and second derivatives of $\rho$, built from the Levi form.
Hörmander had found this leading behaviour before Fefferman.
Fefferman's proof compares $\Omega$ near each boundary point with a model domain osculating it, and controls the error with estimates for the $\bar\partial$-Neumann problem.
Boutet de Monvel and Sjöstrand later gave a microlocal proof that describes the kernel off the diagonal as well.

Example: for the unit ball $B \subset \C^n$, $K(z) = \dfrac{n!}{\pi^n (1 - \abs{z}^2)^{n+1}}$.
With $\rho(z) = \abs{z}^2 - 1$ this is the expansion with $\varphi = n!/\pi^n$ and $\psi = 0$.
The logarithmic term is in general nonzero, and its coefficient $\psi$ on $\partial\Omega$ carries geometric information about the boundary.

Strong pseudoconvexity is needed for the exponent $n + 1$.
For the unit polydisc in $\C^2$, $K(z) = \pi^{-2}(1 - \abs{z_1}^2)^{-2}(1 - \abs{z_2}^2)^{-2}$.
Let $\delta$ be the distance to the boundary.
Near a point with $\abs{z_1} = 1$ and $\abs{z_2} < 1$, the kernel grows only like $\delta^{-2}$, not like $\delta^{-3}$.

## Explanations

### L1 human

The Bergman kernel measures how large a holomorphic function of unit size can be at a point.
Near the boundary of the domain it blows up.
Fefferman's theorem says exactly how it blows up on a smooth strongly pseudoconvex domain: like a power of the distance to the boundary, plus a correction with a logarithm.
The leading part is the same as for the ball, the simplest such domain.

### L2 human

The expansion is the analytic input of [[Fefferman's theorem on the extension of biholomorphisms|N95NQ0G3A6]], through the boundary behaviour of the [[Bergman metric|BB7S4NTZ6V]].
It shows that the [[Bergman projection|6J1X63Z7QZ]] and the Bergman metric of a strongly pseudoconvex domain look, near the boundary, like those of the ball.
The coefficients $\varphi$ and $\psi$ restricted to $\partial\Omega$ are local invariants of the boundary under biholomorphic maps.
This led Fefferman to a programme of computing them from the CR geometry of $\partial\Omega$.
