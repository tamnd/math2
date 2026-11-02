---
tag: T9A1DZ4AQK
kind: definition
name: Pontryagin–Thom construction
msc: [57R90, 55N22, 57R75]
defines: 9HXYTNKB24
uses: [F45VQ47GPV, VKFW27WXEZ, 5MNYT3AFPH]
sources:
  - url: https://en.wikipedia.org/wiki/Cobordism
---

## Definition

Let $M$ be a smooth manifold and let $N \subset M$ be a compact smooth [[submanifold|VKFW27WXEZ]] without boundary, of codimension $k$, with normal vector bundle $\nu$.
Choose an inner product on $\nu$ and a closed tubular neighbourhood $U$ of $N$.
Let $e \colon D(\nu) \to U$ be a diffeomorphism from the unit disc bundle that is the identity on the zero section.
Let $\operatorname{Th}(\nu) = D(\nu) / S(\nu)$ be the [[Thom space|5MNYT3AFPH]] of $\nu$ with base point $*$.
The *Pontryagin–Thom collapse map* $c \colon M \to \operatorname{Th}(\nu)$ is the following map:
$$c(x) = \begin{cases} [e^{-1}(x)] & \text{if } x \in U, \\ * & \text{if } x \notin U. \end{cases}$$
Suppose that $\nu$ comes with a framing, that is, a trivialisation $\nu \cong N \times \R^k$.
The map $\operatorname{Th}(N \times \R^k) \to D^k / S^{k-1} \cong S^k$ forgets the point of $N$.
Its composite with $c$ is a map $M \to S^k$.

## Remarks

The map $c$ is continuous because the boundary of $U$ is the image of $S(\nu)$, which goes to the base point; its homotopy class does not depend on the choices.
Example: for $N$ a point of $M = S^n$, the normal bundle is $\R^n$ with its standard framing, and $c \colon S^n \to D^n / S^{n-1} \cong S^n$ has degree $\pm 1$.
Non-example of the framed version: the circle $N = \R P^1$ in $M = \R P^2$ has the Möbius bundle as normal bundle, which has no framing.
The collapse map still exists, with target $\operatorname{Th}(\nu) \cong \R P^2$, but it does not give a map to $S^1$.

For $M = S^{n+k}$, Pontryagin's theorem says that the construction gives a bijection between framed cobordism classes of closed framed $n$-dimensional submanifolds of $S^{n+k}$ and the homotopy group $\pi_{n+k}(S^k)$.
The inverse sends a smooth map, made transverse to a point, to the preimage of that point with the pulled back framing.

## Explanations

### L1 human

Keep a thin tube around the submanifold and squash the rest of the space to one point.
When the tube is a product, the tube with its outer wall squashed is a sphere, so the result is a map to a sphere.
This dictionary between submanifolds and maps lets homotopy theory count manifolds up to cobordism.
