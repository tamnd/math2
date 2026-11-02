---
tag: J332CQ8SPB
kind: definition
name: Discontinuous Galerkin method
msc: [65M60, 65N30, 35L65]
defines: 6P5MCRDD9Q
uses: [8RA7AMWSAF, Y5B0PEBKE8, ZY4GY93C4B, 07GNX8GCYP]
sources:
  - url: https://en.wikipedia.org/wiki/Discontinuous_Galerkin_method
---

## Definition

Let $\Omega \subset \R^d$ be a bounded polygonal domain and let $F \colon \R \to \R^d$ be a $C^1$ flux.
Consider the scalar [[conservation law|8RA7AMWSAF]] $u_t + \nabla \cdot F(u) = 0$ on $\Omega$.
Let $\mathcal{T}_h$ be a mesh of $\Omega$ and $k \ge 0$ an integer.
Let $V_h$ be the functions that are [[polynomials|07GNX8GCYP]] of degree at most $k$ on each element $K$, with no continuity condition between elements.
Let $\hat H(a, b, n)$ be a numerical flux, such as a [[Riemann solver|ZY4GY93C4B]], with $\hat H(a, a, n) = F(a) \cdot n$ and $\hat H(a, b, n) = -\hat H(b, a, -n)$.
The *discontinuous Galerkin method* seeks $u_h(t) \in V_h$ such that, for every $K \in \mathcal{T}_h$ and every polynomial $v$ of degree at most $k$ on $K$,
$$\int_K \partial_t u_h \, v \, dx - \int_K F(u_h) \cdot \nabla v \, dx + \int_{\partial K} \hat H(u_h^-, u_h^+, n_K) \, v \, ds = 0.$$
Here $n_K$ is the outward unit normal of $K$, and $u_h^-$ and $u_h^+$ are the traces of $u_h$ from inside and outside $K$.

## Remarks

The equation is the weak form on one element, obtained by multiplying by $v$ and integrating by parts once.
The boundary flux $F(u) \cdot n_K$ is replaced by $\hat H$, because $u_h$ has two values on $\partial K$.
Since the test functions live on one element, the mass matrix is block diagonal and explicit time stepping is cheap.
Taking $v = 1$ on $K$ shows that the integral of $u_h$ over $K$ changes only through the fluxes on $\partial K$.

Example: for $k = 0$ and $d = 1$, with cells $K_i$ of width $\Delta x$, $u_h = u_i$ on $K_i$.
Here $\nabla v = 0$, and the conservation property of $\hat H$ turns the flux on the left face into $-\hat H(u_{i-1}, u_i)$, with $\hat H(a, b)$ short for $\hat H(a, b, +1)$.
The equation reads $\Delta x \, u_i' + \hat H(u_i, u_{i+1}) - \hat H(u_{i-1}, u_i) = 0$, a [[finite volume|HGKN8E09RS]] scheme.

Non-example: the continuous [[Galerkin method|Y5B0PEBKE8]] with continuous piecewise polynomials uses a space with continuity across elements and no numerical flux.
It does not have the element-by-element form above.
