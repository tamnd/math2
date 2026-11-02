---
tag: KBSHB2N0VG
kind: definition
name: Progenerator
msc: [16D90, 16D40]
defines: ZQ9ABBKF1N
uses: [0B1261B5ED, 0NZ8JA25WK, 05QY1VEBYD, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Morita_equivalence
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $P$ be a left $R$-[[module|0NZ8JA25WK]].
The module $P$ is a *generator* if every left $R$-module is a homomorphic image of a direct sum of copies of $P$.
The module $P$ is a *progenerator* if all three of these hold:

1. $P$ is [[finitely generated|05QY1VEBYD]].
2. $P$ is [[projective|BFFA03GE3V]].
3. $P$ is a generator.

## Remarks

A module $P$ is a generator if and only if $R$ is a direct summand of $P^n$ for some $n \ge 1$.
Example: $P = R^n$ with $n \ge 1$ is free of finite rank, hence finitely generated and projective, and $R$ is a direct summand of it, so $P$ is a progenerator.
Non-example: let $k$ be a field, $R = k \times k$ and $P = k \times 0 = R(1, 0)$.
It is finitely generated and projective, as a direct summand of $R$.
It is not a generator: every map $P \to 0 \times k$ is zero, since it sends $(1, 0) = (1, 0)^2$ to $(1, 0) \cdot m = 0$; so $0 \times k$ is not a quotient of a sum of copies of $P$.
Over a commutative ring $R$, a finitely generated projective module is a generator if and only if it is faithful, that is, its rank is positive at every prime ideal.
The ring $\End_R(P)$ of a progenerator $P$ is [[Morita equivalent|RD5WKA1VK7]] to $R$.
