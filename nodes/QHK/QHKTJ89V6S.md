---
tag: QHKTJ89V6S
kind: topic
name: Direct sums, complements and quotient spaces
msc: ["15A03", "15A04"]
topics: [GN8GYSDZFX]
---

## Summary

This part of [[linear algebra|GN8GYSDZFX]] is about two ways to break a vector space into simpler spaces.
The first way is to cut it into pieces: a direct sum $V = U \oplus W$ writes every vector as one part from $U$ plus one part from $W$, in exactly one way.
It starts inside one space with subspaces, then builds new spaces from old ones as external direct sums and products, and asks which subspaces can serve as the other piece of a cut, the complements.
Every subspace has a complement, but complements are far from unique, and the projections are the linear maps that record a choice of complement.
The second way is to divide: the quotient $V / U$ forgets everything inside $U$ and keeps only what is left over.
Quotients need no choice, and a complement of $U$ turns out to be a copy of $V / U$ placed inside $V$.
The isomorphism theorems then compare quotients with images of linear maps, with each other and with sums of subspaces, which gives rank-nullity and Grassmann's formula again.
The story ends with codimension, which measures the size of a quotient, and with exact sequences, the language in which all of these facts are later stated in algebra and topology.

## Remarks

### Reading order

1. [[Internal direct sum of subspaces|0XYYT5KNTX]]: unique splitting into pieces, and why three subspaces need more than pairwise tests.
2. [[External direct sum|0S7W6EG32V]]: the direct sum of unrelated spaces, and linear maps out of it.
3. [[Direct product of vector spaces|0EX2HPXPJ6]]: products of families, and where they differ from direct sums.
4. [[Complementary subspace|0M83V17KHX]]: why a subspace has many complements, all isomorphic to $V / U$.
5. [[Existence of a complementary subspace|0P9T8WHNMH]]: complements by extending a basis, and by Zorn's lemma.
6. [[Projection|033DA1WE8Y]]: idempotent maps as direct sum decompositions, oblique and orthogonal.
7. [[Quotient space|0BR3FY5Q8M]]: cosets $v + U$ as parallel copies of $U$, and the quotient map.
8. [[Dimension of a quotient space|0SXDQ6TN00]]: $\dim V / U = \dim V - \dim U$, and a basis of the quotient.
9. [[Universal property of the quotient space|0ZERJX6PH6]]: how a map that vanishes on $U$ passes to $V / U$.
10. [[First isomorphism theorem for vector spaces|0MTBGVZ4XJ]]: $V / \ker f$ is the image of $f$, and rank-nullity follows.
11. [[Second isomorphism theorem for vector spaces|0APN65D6Y6]]: $(U + W) / W \cong U / (U \cap W)$, and Grassmann's formula.
12. [[Third isomorphism theorem for vector spaces|07RB3EMBWW]]: cancelling in a quotient of quotients.
13. [[Codimension of a subspace|JJCGJ1EGCQ]]: the size of a quotient, hyperplanes, and intersections.
14. [[Exact sequence of vector spaces|946YAZNYKX]]: why short exact sequences split, and the alternating sum of dimensions.

### Prerequisites

- [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]]: subspaces, sums and intersections of subspaces, bases and dimension.
- [[Linear maps|9080WQTZ3M]]: kernel, image, isomorphisms and the rank-nullity theorem.
