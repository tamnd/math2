---
tag: 8MADRXG8PQ
kind: proof
name: Proof that cyclic groups are abelian
msc: [20A05]
proves: 04RG02S6BA
uses: [0B85Q41RP6, 00DRK90Z6K, 071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Cyclic groups
---

## Proof

1. Let $G$ be a [[cyclic group|0B85Q41RP6]] with generator $g$.
2. Let $x$ and $y$ be elements of $G$. Then there are integers $m$ and $n$ with $x = g^m$ and $y = g^n$.
3. By the [[laws of exponents|00DRK90Z6K]], $xy = g^m g^n = g^{m+n}$.
4. In the same way, $yx = g^n g^m = g^{n+m}$.
5. Since $m + n = n + m$, $xy = yx$. Thus $G$ is [[abelian|071DDFVG4J]].

## Idea

Every element is a power of one generator, and powers of the same element commute.
