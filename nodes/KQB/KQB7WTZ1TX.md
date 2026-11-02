---
tag: KQB7WTZ1TX
kind: statement
role: theorem
name: Regular value theorem
msc: [57R35, 58A05]
uses: [F45VQ47GPV, 6P9PXQDSEN, VKFW27WXEZ, BMY55EW3RF, 0B2RZ0778N, 0BXBADR94C, Z7R8J71SJN]
about: [VKFW27WXEZ, BMY55EW3RF]
sources:
  - url: https://en.wikipedia.org/wiki/Submersion_(mathematics)
---

## Statement

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]] of dimensions $m$ and $n$, and let $f \colon M \to N$ be a smooth map.
A point $y \in N$ is a *regular value* of $f$ if the [[differential|6P9PXQDSEN]] $df_x \colon T_xM \to T_yN$ is surjective for every $x \in f^{-1}(y)$.
Let $y$ be a regular value of $f$ with $f^{-1}(y)$ not empty.
Then the [[level set|0B2RZ0778N]] $f^{-1}(y)$ is an [[embedded submanifold|VKFW27WXEZ]] of $M$ of dimension $m - n$.
Its tangent space at each point $x \in f^{-1}(y)$ is $\ker df_x$.

## Remarks

The set of points where $df_x$ is surjective is open, so $f$ is a [[submersion|BMY55EW3RF]] on a neighbourhood of $f^{-1}(y)$.
In charts the claim becomes the [[implicit function theorem|0BXBADR94C]].
Near each $x$ there are coordinates in which $f$ is the projection onto the first $n$ coordinates, and the fibre is then a coordinate slice.
Example: $f \colon \R^{n+1} \to \R$, $f(x) = \abs{x}^2$, has $df_x(v) = 2 \langle x, v \rangle$, which is onto for $x \neq 0$.
So $1$ is a regular value and the unit sphere $S^n = f^{-1}(1)$ is a submanifold of dimension $n$.
The hypothesis is needed: $0$ is not a regular value of $g(x, y) = xy$, and $g^{-1}(0)$ is the union of the two axes, which is not a submanifold.

## Explanations

### L1 human

Solve an equation $f(x) = y$ on a smooth space.
If the equation is "non-degenerate" at every solution, the solutions form a smooth space again, of dimension equal to the number of unknowns minus the number of equations.
This is how one shows that spheres, many matrix groups and other familiar shapes are manifolds.

### L2 human

The theorem is the main tool for producing examples of manifolds.
For instance, the orthogonal group $O(n)$ is the fibre over the identity of the map $A \mapsto A^T A$ into symmetric matrices.
The identity is a regular value, so $O(n)$ is a manifold of dimension $n(n-1)/2$.
By [[Sard's theorem|Z7R8J71SJN]] almost every value is regular, so the theorem applies to almost every fibre.
It is the special case of transversality to a point, and the same proof gives that the preimage of a submanifold under a transverse map is a submanifold.
