---
tag: YAYGMKC33F
kind: definition
name: Adjoint representation of a Lie algebra
msc: [17B10, 17B05]
defines: 54XSPNAM1J
uses: [5JJYBJ6A8K, H5D71JE8TA, 0J7H0YBFDJ, ZKFN197MBR]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_representation
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
Let $\mathfrak{gl}(\mathfrak g)$ be the Lie algebra of $k$-linear [[endomorphisms|0J7H0YBFDJ]] of $\mathfrak g$, with bracket $[S, T] = ST - TS$.
For $x \in \mathfrak g$, define $\operatorname{ad}_x \colon \mathfrak g \to \mathfrak g$ by $\operatorname{ad}_x(y) = [x, y]$.
The *adjoint representation* of $\mathfrak g$ is the map $\operatorname{ad} \colon \mathfrak g \to \mathfrak{gl}(\mathfrak g)$, $x \mapsto \operatorname{ad}_x$.

## Remarks

The map $\operatorname{ad}$ is a [[Lie algebra homomorphism|H5D71JE8TA]].
Indeed, applied to $z$, the equation $\operatorname{ad}_{[x, y]} = \operatorname{ad}_x \operatorname{ad}_y - \operatorname{ad}_y \operatorname{ad}_x$ reads $[ [x, y], z] = [x, [y, z]] - [y, [x, z]]$, a form of the [[Jacobi identity|ZKFN197MBR]].
Its kernel is the center $\set{x \in \mathfrak g : [x, y] = 0 \text{ for all } y}$.

Example: in $\mathfrak{sl}_2(k)$ with basis $e, h, f$ and $[h, e] = 2e$, $[h, f] = -2f$, $[e, f] = h$, the matrix of $\operatorname{ad}_h$ in this basis is $\operatorname{diag}(2, 0, -2)$.

Non-example: the map $x \mapsto -\operatorname{ad}_x$, that is $x \mapsto (y \mapsto [y, x])$, is linear, but if $\operatorname{char} k \ne 2$ it is a homomorphism only when every bracket $[x, y]$ is central.
Its value on $[x, y]$ is $-\operatorname{ad}_{[x, y]}$, while the bracket of the values is $[\operatorname{ad}_x, \operatorname{ad}_y] = \operatorname{ad}_{[x, y]}$.

For a Lie group $G$ with Lie algebra $\mathfrak g$, $\operatorname{ad}$ is the differential at the identity of the [[adjoint representation of the group|P6ZP0TE07M]].
