---
tag: ZNZP5A2QH5
kind: definition
name: Representation of a Lie algebra
msc: [17B10]
defines: TZAZ163QGK
uses: [5JJYBJ6A8K, H5D71JE8TA, G8FEGYDSNE, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_representation
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $F$, and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
Let $\mathfrak{gl}(V)$ be the [[general linear Lie algebra|G8FEGYDSNE]] of all linear maps $V \to V$, with bracket $[A, B] = AB - BA$.
A *representation* of $\mathfrak{g}$ on $V$ is a [[Lie algebra homomorphism|H5D71JE8TA]] $\rho \colon \mathfrak{g} \to \mathfrak{gl}(V)$.
So $\rho$ is linear and $\rho([x, y]) = \rho(x)\rho(y) - \rho(y)\rho(x)$ for all $x, y \in \mathfrak{g}$.

## Remarks

Equivalently, a $\mathfrak{g}$-module is a vector space $V$ with a bilinear map $\mathfrak{g} \times V \to V$, $(x, v) \mapsto x \cdot v$, such that $[x, y] \cdot v = x \cdot (y \cdot v) - y \cdot (x \cdot v)$.
The two notions match through $x \cdot v = \rho(x)(v)$; the dimension of $V$ is the dimension of the representation.
Example: the [[adjoint representation|54XSPNAM1J]] $\operatorname{ad} \colon x \mapsto [x, \cdot\,]$ on $V = \mathfrak{g}$.
The condition $\operatorname{ad}[x, y] = [\operatorname{ad} x, \operatorname{ad} y]$ is the Jacobi identity.
Non-example: on $\mathfrak{gl}_n(F)$ with $n \ge 2$, the map $x \mapsto x^T$ is linear, but $([x, y])^T = y^T x^T - x^T y^T = -[x^T, y^T]$, which differs from $[x^T, y^T]$ when $[x, y] \ne 0$ and $F$ does not have characteristic $2$.
The map $x \mapsto -x^T$ is a representation, the dual of the defining one.
Representations of $\mathfrak{g}$ are the same as left modules over the [[universal enveloping algebra|SCZ8PRVY00]] $U(\mathfrak{g})$.
