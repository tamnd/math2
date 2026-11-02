---
tag: DVB79BK06Y
kind: object
name: Raviart–Thomas elements
msc: [65N30, 65N12]
uses: [98GZ9DVHTA, 87VMQ892VW, 0MWV6ZTK6S, 07GNX8GCYP]
sources:
  - url: https://en.wikipedia.org/wiki/Raviart%E2%80%93Thomas_basis_functions
---

## Description

Let $T \subset \R^d$ be a simplex, a triangle when $d = 2$, and let $k \ge 0$ be an integer.
Let $P_k(T)$ be the [[polynomials|07GNX8GCYP]] of degree at most $k$ on $T$, and $\tilde P_k(T)$ the homogeneous ones of degree $k$.
The *Raviart–Thomas space* of index $k$ on $T$ is
$$RT_k(T) = P_k(T)^d + x \, \tilde P_k(T),$$
the vector fields $p(x) + x \, q(x)$ with $p \in P_k(T)^d$ and $q \in \tilde P_k(T)$.
The degrees of freedom are the moments of the normal component $v \cdot n$ on each face against $P_k$ of that face.
For $k \ge 1$ they also include the moments of $v$ against $P_{k-1}(T)^d$.
On a mesh, the global space is formed by the piecewise $RT_k$ fields whose normal moments agree on each interior face.

## Remarks

Lowest order on a triangle: $RT_0(T) = \set{x \mapsto a + b x : a \in \R^2, \ b \in \R}$, of dimension $3$.
On an edge $e$ with unit normal $n$, the points satisfy $x \cdot n = c$ for a constant $c$.
So $(a + b x) \cdot n = a \cdot n + b c$ is constant on $e$, and it is fixed by the flux $\int_e v \cdot n$.
The three fluxes determine $v$, which gives the three degrees of freedom.

The dimension of $RT_k(T)$ on a triangle is $(k + 1)(k + 3)$.
Matching the normal moments makes the normal component continuous across faces.
So the global space lies in $H(\operatorname{div})$, the $L^2$ fields with [[divergence|0MWV6ZTK6S]] in $L^2$.
The divergence maps $RT_k(T)$ onto $P_k(T)$.
Paired with discontinuous piecewise polynomials of degree $k$, these spaces give a stable [[mixed finite element method|87VMQ892VW]] for the Poisson equation.
They were introduced by Pierre-Arnaud Raviart and Jean-Marie Thomas.

## Explanations

### L1 human

Raviart–Thomas elements are building blocks for approximating flows, such as the flux of heat or of water through soil.
Instead of storing values at the corners, the lowest-order element stores how much flows through each edge of a triangle.
Neighbouring triangles share these edge fluxes, so whatever leaves one triangle enters the next.
This makes the computed flow conserve mass exactly, element by element.
