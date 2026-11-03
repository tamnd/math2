---
tag: 5DK9SWGZFC
kind: definition
name: Semisimple Lie algebra
msc: [17B20]
defines: EY9DN7QAX1
uses: [5JJYBJ6A8K, JWMTXQ8A3A, W7A2R0GR3T, N43CM5H99K, 1ZAT1Z967A, G8FEGYDSNE, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_Lie_algebra
---

## Definition

Let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
The Lie algebra $\mathfrak g$ is *semisimple* if its only [[solvable|W7A2R0GR3T]] [[ideal|JWMTXQ8A3A]] is $0$.

## Remarks

Equivalently, $\mathfrak g$ has no nonzero [[abelian|N43CM5H99K]] ideal.
Indeed, if $\mathfrak a$ is a nonzero solvable ideal, the last nonzero term of its derived series is an abelian ideal of $\mathfrak g$.
Equivalently again, the radical of $\mathfrak g$, its largest solvable ideal, is $0$.
By convention the zero Lie algebra is semisimple.

Example: the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$ is simple, so its only ideals are $0$ and itself.
It is not solvable, since $[\mathfrak{sl}_2, \mathfrak{sl}_2] = \mathfrak{sl}_2$, so its only solvable ideal is $0$.

Non-example: the [[general linear Lie algebra|G8FEGYDSNE]] $\mathfrak{gl}_n(k)$ with $n \ge 1$ is not semisimple, since the scalar matrices form a nonzero abelian ideal.

Let $k$ have [[characteristic|1ZB13N78XW]] $0$.
Then $\mathfrak g$ is semisimple if and only if it is a direct sum of simple ideals.
It is semisimple if and only if its Killing form is nondegenerate.
