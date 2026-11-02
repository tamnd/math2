---
tag: RTAVY44P4Z
kind: definition
name: Legendrian submanifold
msc: [53D10, 53D12]
defines: Q2DMSTWZYZ
uses: [HBQ8BZ7XB5]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_geometry
---

## Definition

Let $(M, \xi)$ be a [[contact manifold|HBQ8BZ7XB5]] of dimension $2n + 1$.
A *Legendrian submanifold* of $(M, \xi)$ is a submanifold $L \subset M$ of dimension $n$ such that $T_x L \subset \xi_x$ for every $x \in L$.
A *Legendrian knot* is a Legendrian submanifold of a contact $3$-manifold that is diffeomorphic to a circle.

## Remarks

If $\xi = \ker \alpha$, the condition is that $\alpha$ restricts to zero on $L$.
Then $d\alpha$ also restricts to zero on $L$, so each $T_x L$ is an isotropic subspace of the symplectic vector space $(\xi_x, d\alpha)$, of dimension $2n$.
Hence a submanifold tangent to $\xi$ has dimension at most $n$, and Legendrian submanifolds are the tangent submanifolds of maximal dimension.

Example: in $\R^3$ with $\alpha = dz - y\,dx$, the $x$-axis $\set{y = z = 0}$ is Legendrian, since along it $dz = 0$ and $y = 0$.
More generally, for a smooth $f \colon \R \to \R$, the curve $\set{(x, f'(x), f(x))}$ is Legendrian, since $dz - y\,dx = f'(x)\,dx - f'(x)\,dx = 0$ on it.

Non-example: the $z$-axis in the same space is not Legendrian, since $\alpha(\partial_z) = 1 \ne 0$.
