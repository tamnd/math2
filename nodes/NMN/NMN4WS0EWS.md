---
tag: NMN4WS0EWS
kind: definition
name: Radical of a Lie algebra
msc: [17B05, 17B30]
defines: 33MD21KMNP
uses: [5JJYBJ6A8K, JWMTXQ8A3A, W7A2R0GR3T, G8FEGYDSNE, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_of_a_Lie_algebra
---

## Definition

Let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
The *radical* of $\mathfrak g$, written $\operatorname{rad}(\mathfrak g)$, is the sum of all [[solvable|W7A2R0GR3T]] [[ideals|JWMTXQ8A3A]] of $\mathfrak g$.
It is itself a solvable ideal, so it is the unique largest solvable ideal of $\mathfrak g$.

## Remarks

The sum is solvable because, for solvable ideals $\mathfrak a$ and $\mathfrak b$, the quotient $(\mathfrak a + \mathfrak b) / \mathfrak b \cong \mathfrak a / (\mathfrak a \cap \mathfrak b)$ is solvable, and an extension of solvable Lie algebras is solvable.
By finite dimension, the radical is the sum of finitely many solvable ideals.
The quotient $\mathfrak g / \operatorname{rad}(\mathfrak g)$ has no nonzero solvable ideals.

Example: let $k$ have [[characteristic|1ZB13N78XW]] $0$ and let $\mathfrak g = \mathfrak{gl}_n(k)$ be the [[general linear Lie algebra|G8FEGYDSNE]] with $n \ge 2$.
The scalar matrices $kI$ form an abelian, hence solvable, ideal.
The quotient $\mathfrak{gl}_n(k) / kI$ is isomorphic to $\mathfrak{sl}_n(k)$, which has no nonzero solvable ideals, so $\operatorname{rad}(\mathfrak{gl}_n(k)) = kI$.

Non-example: in the two-dimensional Lie algebra with basis $x, y$ and $[x, y] = y$, the line $ky$ is a solvable ideal, but it is not the radical.
The whole algebra is solvable, so the radical is the whole algebra.
