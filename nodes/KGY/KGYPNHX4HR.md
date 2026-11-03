---
tag: KGYPNHX4HR
kind: definition
name: Lie algebra homomorphism
msc: [17B05]
defines: H5D71JE8TA
uses: [5JJYBJ6A8K, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Definition

Let $\mathfrak g$ and $\mathfrak h$ be [[Lie algebras|5JJYBJ6A8K]] over the same field $k$.
A *Lie algebra homomorphism* is a $k$-[[linear map|0NRYHJPQG2]] $\varphi \colon \mathfrak g \to \mathfrak h$ such that $\varphi([x, y]) = [\varphi(x), \varphi(y)]$ for all $x, y \in \mathfrak g$.

## Remarks

A bijective homomorphism is an *isomorphism*; its inverse is again a homomorphism.

Example: let $k$ carry the zero bracket.
The trace $\tr \colon \mathfrak{gl}_n(k) \to k$ is linear, and $\tr [X, Y] = \tr(XY) - \tr(YX) = 0 = [\tr X, \tr Y]$.
So the trace is a homomorphism, with kernel $\mathfrak{sl}_n(k)$.

Non-example: if $n \ge 2$ and $\operatorname{char} k \ne 2$, the transpose $X \mapsto X^T$ on $\mathfrak{gl}_n(k)$ is linear but does not preserve brackets.
One has $[X, Y]^T = Y^T X^T - X^T Y^T = -[X^T, Y^T]$, which differs from $[X^T, Y^T]$ whenever $[X^T, Y^T] \ne 0$, for instance for $X = E_{12}$ and $Y = E_{21}$.
The map $X \mapsto -X^T$, on the other hand, is a homomorphism.

The kernel of a homomorphism is an [[ideal|JWMTXQ8A3A]] of $\mathfrak g$, and its image is a [[subalgebra|WKSSTQ69AK]] of $\mathfrak h$.
