---
tag: RTJQPZC0VY
kind: definition
name: Atomic domain
msc: [13F15, 13G05]
defines: F37JBGAA1S
uses: [09S3PFBEPM, 052SDEPZH7, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_domain
---

## Definition

Let $R$ be an [[integral domain|09S3PFBEPM]].
$R$ is *atomic* if every nonzero element $r$ of $R$ that is not a [[unit|019NFGFPR5]] has a factorization into irreducibles.
That is, $r = a_1 a_2 \cdots a_n$ for some $n \ge 1$ and some [[irreducible elements|052SDEPZH7]] $a_1, \ldots, a_n$ of $R$.

## Remarks

Example: $\Z[\sqrt{-5}]$ is atomic, because it is Noetherian.
In a Noetherian domain, a nonzero nonunit without a factorization would give an infinite strictly ascending chain of principal ideals.
Non-example: the ring $\overline{\Z}$ of all algebraic integers is not atomic.
For a nonzero nonunit $\alpha$, a square root $\beta$ of $\alpha$ is an algebraic integer and a nonunit, and $\alpha = \beta^2$.
So no element of $\overline{\Z}$ is irreducible, and $2$ has no factorization.
A domain that satisfies the ascending chain condition on principal ideals is atomic; the converse is false.
The factorization is not required to be unique; uniqueness up to order and units is what makes $R$ a [[unique factorisation domain|06YMXJMXYS]].
