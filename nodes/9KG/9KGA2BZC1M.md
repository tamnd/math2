---
tag: 9KGA2BZC1M
kind: definition
name: Rng
msc: [16B99]
defines: MBK7NFE74S
uses: [071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Rng_(algebra)
---

## Definition

A *rng* is a set $R$ with two binary operations $+$ and $\cdot$ such that:

1. $(R, +)$ is an [[abelian group|071DDFVG4J]];
2. $(ab)c = a(bc)$ for all $a, b, c \in R$;
3. $a(b + c) = ab + ac$ and $(a + b)c = ac + bc$ for all $a, b, c \in R$.

## Remarks

No multiplicative identity is required; a ring is a rng that has one.
Other names are *non-unital ring* and *pseudo-ring*.
Example: the even integers $2\Z$ with the usual operations form a rng; the clauses hold because they hold in $\Z$ and $2\Z$ is closed under both operations.
It has no identity, since $e \cdot 2 = 2$ forces $e = 1 \notin 2\Z$.
Non-example: $\R^3$ with the cross product as multiplication fails clause 2.
With the standard basis $i, j, k$, one has $(i \times i) \times j = 0$ but $i \times (i \times j) = i \times k = -j$.
Every rng $R$ embeds as an ideal in the ring $\Z \times R$ with the product $(m, a)(n, b) = (mn, mb + na + ab)$, whose identity is $(1, 0)$.
