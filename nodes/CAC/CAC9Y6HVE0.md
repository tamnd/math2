---
tag: CAC9Y6HVE0
kind: definition
name: Modular Lie algebra
msc: [17B50]
defines: HKYYR1SZQW
uses: [5JJYBJ6A8K, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_Lie_algebra
---

## Definition

Let $F$ be a field of [[characteristic|1ZB13N78XW]] $p > 0$.
A *modular Lie algebra* is a [[Lie algebra|5JJYBJ6A8K]] over $F$.

## Remarks

Example: $\mathfrak{sl}_2(\F_p)$, the $2 \times 2$ matrices of trace zero over $\F_p$ with bracket $[x, y] = xy - yx$, is a modular Lie algebra, since $\F_p$ has characteristic $p$.
Non-example: $\mathfrak{sl}_2(\C)$ is a Lie algebra over a field of characteristic $0$, so it is not modular.
Many authors also require the Lie algebra to be finite-dimensional.
Lie's theorem fails in characteristic $p$.
Let $V = F[t]/(t^p)$ and let the Heisenberg algebra with basis $x, y, z$, $[x, y] = z$, act by $x \mapsto d/dt$, $y \mapsto$ multiplication by $t$, $z \mapsto \id$.
This is well defined because the derivative of $t^p$ is $0$, and $V$ is an irreducible module of dimension $p$ of a nilpotent Lie algebra.
Over an algebraically closed field of characteristic $0$, finite-dimensional irreducible modules of solvable Lie algebras are one-dimensional.
Let $F$ be algebraically closed of characteristic $p > 3$.
By work of Block, Wilson, Premet and Strade, each finite-dimensional simple Lie algebra over $F$ is of classical type, of Cartan type, or of Melikian type.
The Melikian type occurs only for $p = 5$.
