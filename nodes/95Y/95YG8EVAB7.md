---
tag: 95YG8EVAB7
kind: definition
name: Lie ring
msc: [17B60, 17B05]
defines: FZ77E3RWPN
uses: [082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Definition

A *Lie ring* is an [[abelian group|082GHNPJ53]] $(L, +)$ together with a map $[\cdot, \cdot] \colon L \times L \to L$ such that:

1. $[x + y, z] = [x, z] + [y, z]$ and $[x, y + z] = [x, y] + [x, z]$ for all $x, y, z \in L$.
2. $[x, x] = 0$ for all $x \in L$.
3. $[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0$ for all $x, y, z \in L$.

## Remarks

Example: $\Z^3$ with the cross product is a Lie ring.
The cross product of integer vectors has integer coordinates, it is biadditive, $x \times x = 0$, and the Jacobi identity holds because it holds in $\R^3$.

Non-example: a commutative ring $R$ with the bracket $[x, y] = xy$ satisfies clause 1, but it fails clause 2 as soon as some $x \in R$ has $x^2 \ne 0$, such as $x = 1$ in $\Z$.

Clauses 1 and 2 give $[x, y] = -[y, x]$.
A Lie ring is the same as a [[Lie algebra|5JJYBJ6A8K]] over $\Z$.
A Lie algebra over a commutative ring $k$ is a Lie ring that is also a $k$-module, with a $k$-bilinear bracket.
