---
tag: YGV5S3MRD6
kind: statement
role: proposition
name: A Dedekind UFD is a PID
msc: [13F05, 13F15, 13F10]
uses: [7NPY2CN5KB, 0W4X9G6263, 0CMD0BCH8T, 00MHHZ9SNE, 0YMT0D2442, 01VH21EV6F, S6PHT75MEK]
about: [7NPY2CN5KB, 0W4X9G6263, 0CMD0BCH8T]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_domain
---

## Statement

Let $R$ be a [[Dedekind domain|7NPY2CN5KB]] that is also a [[unique factorization domain|0W4X9G6263]].
Then $R$ is a [[principal ideal domain|0CMD0BCH8T]].

## Remarks

Let $P$ be a nonzero [[prime ideal|00MHHZ9SNE]] and let $a \in P$ be nonzero.
The element $a$ is not a unit, and one of its [[irreducible|0YMT0D2442]] factors $\pi$ lies in $P$.
In a UFD, $\pi$ is a [[prime element|01VH21EV6F]], so $(\pi)$ is a nonzero prime ideal inside $P$; as nonzero primes of a Dedekind domain are maximal, $(\pi) = P$.
So every nonzero prime is principal, and by the [[unique factorization of ideals|S6PHT75MEK]] every nonzero ideal is a product of principal ideals, hence principal.

Example: $\Z[\sqrt{-5}]$ is a Dedekind domain, but $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ gives two different factorizations into irreducibles, so it is not a UFD; consistent with this, $(2, 1 + \sqrt{-5})$ is not principal.
The Dedekind hypothesis cannot be dropped: $k[x, y]$ for a field $k$ is a UFD, but the ideal $(x, y)$ is not principal.

## Explanations

### L1 human

For rings of algebraic integers, unique factorization of numbers and "every ideal has one generator" are the same property.
One direction holds in every ring: a principal ideal domain always has unique factorization.
This result gives the other direction for Dedekind domains.
So a ring of integers of a number field has unique factorization exactly when its ideals are all principal.

### L2 human

In terms of the [[ideal class group|WQ46BD3ARY]], a Dedekind domain is a UFD exactly when its class group is trivial, and this is the same as being a PID.
The class group thus measures the failure of unique factorization of elements.
For example, the class group of $\Z[\sqrt{-5}]$ has order $2$.
The proof uses only that nonzero primes are maximal and that ideals factor into primes, so it is a good first exercise with the ideal factorization theorem.
