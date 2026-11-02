---
tag: DJHVKR63H5
kind: definition
name: Unitary operator
msc: [47B15, 47A05]
defines: MM0EJ2GDE4
uses: [HM2HHE3J51, 6HSJBJ8TTQ]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_operator
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] and let $U \colon H \to H$ be a bounded linear operator with [[adjoint|6HSJBJ8TTQ]] $U^*$.
The operator $U$ is *unitary* when
$$U^* U = U U^* = I,$$
where $I$ is the identity operator of $H$.

## Remarks

Example: on $\ell^2(\Z)$ the bilateral shift $(Ux)_n = x_{n-1}$ has adjoint $(U^*x)_n = x_{n+1}$, and both $U^*U$ and $UU^*$ are the identity, so $U$ is unitary.

Non-example: on $\ell^2(\N)$ the unilateral shift $S(x_0, x_1, \ldots) = (0, x_0, x_1, \ldots)$ satisfies $S^*S = I$, but $SS^*$ sends $(1, 0, 0, \ldots)$ to $0$, so $SS^* \ne I$ and $S$ is not unitary.
It is an isometry that is not surjective.

Equivalent forms: $U$ is unitary if and only if $U$ is surjective and $\ip{Ux}{Uy} = \ip{x}{y}$ for all $x, y$, and if and only if $U$ is a surjective isometry.
In finite dimensions $U^*U = I$ already implies $UU^* = I$, but in infinite dimensions both conditions are needed, as the unilateral shift shows.
The spectrum of a unitary operator lies on the unit circle.
