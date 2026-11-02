---
tag: 28ADY9WTV3
kind: definition
name: Maslov index
msc: [53D12]
defines: 91KJT4TXG8
uses: [0R9R0Y1HDK, 0TKYAEJ8N7, 0NQSV2EWDR, S1XK3HXHFX, H8ACPTMX08]
sources:
  - url: https://en.wikipedia.org/wiki/Maslov_index
---

## Definition

Identify $\R^{2n}$ with $\C^n$ by $(x, y) \mapsto x + iy$, with the symplectic form $\omega = \sum_{j=1}^n dx_j \wedge dy_j$.
A linear subspace $\Lambda \subset \R^{2n}$ is *Lagrangian* if $\dim \Lambda = n$ and $\omega(u, v) = 0$ for all $u, v \in \Lambda$.
Let $\Lambda(n)$ be the set of Lagrangian subspaces, the *Lagrangian Grassmannian*.

Every $\Lambda \in \Lambda(n)$ is $\Lambda = U \R^n$ for some $U$ in the [[unitary group|0R9R0Y1HDK]] $U(n)$.
This $U$ is unique up to right multiplication by an element of the [[orthogonal group|0TKYAEJ8N7]] $O(n)$.
Hence the map $\Lambda \mapsto \det(U)^2 \in S^1 \subset \C$ is well defined on $\Lambda(n)$.
Let $\gamma \colon [0, 1] \to \Lambda(n)$ be a continuous loop, so $\gamma(0) = \gamma(1)$.
Its *Maslov index* is the [[winding number|0NQSV2EWDR]] about $0$ of the loop $t \mapsto \det(U(t))^2$, where $\gamma(t) = U(t) \R^n$.

## Remarks

Example: $n = 1$ and $\gamma(t) = e^{i\pi t} \R \subset \C$ for $t \in [0, 1]$, the line through $0$ turned by half a turn.
Here $U(t) = e^{i\pi t}$ and $\det(U(t))^2 = e^{2\pi i t}$ winds once around $0$, so the Maslov index is $1$.

Non-example: in $\R^4 = \C^2$, the plane $P = \C \times \set{0}$ has dimension $2$, but $\omega$ pairs the vectors $(1, 0)$ and $(i, 0)$ of $P$ to $1 \ne 0$.
So $P$ is not Lagrangian, and a loop of planes through $P$ is not a loop in $\Lambda(2)$ and has no Maslov index.

The Maslov index depends only on the homotopy class of the loop, and it gives an isomorphism of the [[fundamental group|S1XK3HXHFX]] $\pi_1(\Lambda(n))$ with $\Z$.
For a [[Lagrangian submanifold|H8ACPTMX08]] $L \subset \R^{2n}$, a loop in $L$ gives the loop of tangent spaces in $\Lambda(n)$, and its Maslov index defines a class in $H^1(L; \Z)$, the Maslov class.
