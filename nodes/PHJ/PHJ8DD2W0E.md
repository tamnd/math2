---
tag: PHJ8DD2W0E
kind: definition
name: Bergman projection
msc: [32A36, 32A25, 30H20]
defines: 6J1X63Z7QZ
uses: [2D619WTPYC, 0B8KZRT28M, 8RWDHW0CXC, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_kernel
---

## Definition

Let $\Omega \subseteq \C^n$ be a domain, and let $L^2(\Omega)$ be the [[Lebesgue space|SASP14MA1Z]] of square-integrable functions for Lebesgue measure $dV$.
Let $A^2(\Omega) \subseteq L^2(\Omega)$ be the [[Bergman space|2D619WTPYC]] of holomorphic functions in $L^2(\Omega)$, which is a closed subspace.
The *Bergman projection* of $\Omega$ is the [[orthogonal projection|0B8KZRT28M]]
$$P \colon L^2(\Omega) \to A^2(\Omega).$$
It is given by
$$P f(z) = \int_\Omega K(z, w) \, f(w) \, dV(w),$$
where $K$ is the [[Bergman kernel|8RWDHW0CXC]] of $\Omega$.

## Remarks

The integral formula follows from the reproducing property: for $f \in L^2(\Omega)$, $Pf(z) = \ip{Pf}{K(\cdot, z)} = \ip{f}{K(\cdot, z)}$, since $K(\cdot, z) \in A^2(\Omega)$ and $f - Pf$ is orthogonal to $A^2(\Omega)$.
Example: on the unit disc, the functions $z^k$, $k \ge 0$, form an orthogonal basis of $A^2$, and $\ip{\bar z}{z^k} = \int_{\mathbb{D}} \bar z \, \bar z^k \, dV = 0$ for every $k$, so $P \bar z = 0$.
Similarly $P \abs{z}^2 = \frac{1}{2}$, since $\ip{\abs{z}^2}{1} = \int_{\mathbb{D}} \abs{z}^2 dV = \frac{\pi}{2}$ and $\norm{1}^2 = \pi$, and $\abs{z}^2$ is orthogonal to $z^k$ for $k \ge 1$.
Non-example: the orthogonal projection of $L^2(\Omega)$ onto the harmonic functions in $L^2(\Omega)$ is a different operator, the harmonic Bergman projection; on the unit disc it fixes $\bar z$.
$P$ is self-adjoint, $P^2 = P$, and $\norm{P} = 1$ when $A^2(\Omega) \ne \set{0}$.
On smoothly bounded strongly pseudoconvex domains, $P$ maps $C^\infty(\bar\Omega)$ into itself.
