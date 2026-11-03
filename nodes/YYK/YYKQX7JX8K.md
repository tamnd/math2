---
tag: YYKQX7JX8K
kind: object
name: Okubo algebra
msc: [17A75, 17A20]
instance_of: [1Q9G6AST10, R1Z4P70285]
uses: [0P17NGQQMQ, 8H3JKHAAHE]
sources:
  - url: https://en.wikipedia.org/wiki/Okubo_algebra
same_as:
  wikidata: Q17099522
  wikipedia: Okubo algebra
---

## Description

Let $V$ be the real vector space of $3 \times 3$ complex [[Hermitian matrices|0P17NGQQMQ]] of trace $0$; it has dimension $8$.
Let $\mu = \frac{3 + \sqrt{3}\, i}{6}$, so that $\bar{\mu} = 1 - \mu$.
The *Okubo algebra* is $V$ with the product
$$x * y = \mu\, xy + \bar{\mu}\, yx - \tfrac{1}{3} \tr(xy)\, I,$$
where $xy$ is the matrix product and $I$ is the identity matrix.

## Remarks

The product stays in $V$: the adjoint of $\mu xy + \bar{\mu} yx$ is $\bar{\mu} yx + \mu xy$, and the trace of $x * y$ is $(\mu + \bar{\mu} - 1)\tr(xy) = 0$.
The algebra is [[flexible|R1Z4P70285]] but not unital, not associative and not alternative.
There is a norm $N$ on $V$, a positive multiple of $x \mapsto \tr(x^2)$, with $N(x * y) = N(x)N(y)$ and $(x * y) * x = x * (y * x) = N(x)\,y$.
So it is a [[composition algebra|1Q9G6AST10]] without a unit.
Since $N$ is positive definite, $x * y = 0$ forces $x = 0$ or $y = 0$, so the Okubo algebra is an $8$-dimensional real [[division algebra|8H3JKHAAHE]] that is not isomorphic to the octonions.

## Explanations

### L1 human

The Okubo algebra is an eight-dimensional real algebra built from $3 \times 3$ matrices with a twisted product.
Like the octonions, it has a length that respects multiplication, and one can divide by nonzero elements.
Unlike the octonions, it has no element that acts as $1$.
