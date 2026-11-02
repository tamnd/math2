---
tag: CAB1ARHH31
kind: definition
name: Finite volume method
msc: [65M08, 65N08, 35L65]
defines: HGKN8E09RS
uses: [8RA7AMWSAF, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_volume_method
---

## Definition

Let $\Omega \subset \R^d$ be a bounded polygonal domain and $F \colon \R \to \R^d$ a $C^1$ flux.
Consider the [[conservation law|8RA7AMWSAF]] $u_t + \nabla \cdot F(u) = 0$, with $\nabla \cdot$ the [[divergence|0MWV6ZTK6S]].
Partition $\Omega$ into polygonal control volumes $K_i$, and write $e_{ij}$ for the common face of $K_i$ and $K_j$.
Let $n_{ij}$ be the unit normal of $e_{ij}$ pointing from $K_i$ to $K_j$.
A numerical flux is a function $H(a, b, n)$ with two properties:

1. consistency: $H(a, a, n) = F(a) \cdot n$ for all $a$ and $n$;
2. conservation: $H(a, b, n) = -H(b, a, -n)$.

Let $u_i(t)$ approximate the average of $u$ over $K_i$.
The *finite volume method* evolves these numbers by
$$\abs{K_i} \frac{d u_i}{dt} = -\sum_{j} \abs{e_{ij}} \, H(u_i, u_j, n_{ij}),$$
where the sum runs over the neighbours $K_j$ of $K_i$, and $\abs{\cdot}$ denotes volume or area.
Boundary faces use fluxes built from the boundary conditions.

## Remarks

The scheme is the exact balance law $\frac{d}{dt} \int_{K_i} u = -\int_{\partial K_i} F(u) \cdot n$, with the face integrals replaced by numerical fluxes.
By clause 2, the flux from $K_i$ to $K_j$ is the negative of the flux from $K_j$ to $K_i$.
So $\sum_i \abs{K_i} u_i$ changes only through the boundary of $\Omega$.

Example: for $u_t + a u_x = 0$ with $a > 0$ on cells of width $\Delta x$, take the upwind flux $H(u_i, u_{i+1}, +1) = a u_i$.
This gives $u_i' = -a (u_i - u_{i-1}) / \Delta x$.
Consistency holds since $H(v, v, +1) = a v = F(v)$.

Non-example: the scheme $u_i' = -u_i (u_{i+1} - u_{i-1}) / (2 \Delta x)$ for Burgers' equation $u_t + (u^2/2)_x = 0$ is not in flux form.
It has no numerical flux, so clause 2 has no meaning for it.
It does not conserve $\sum_i u_i$ and can produce shocks with wrong speeds.
