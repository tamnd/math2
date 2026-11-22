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

1. [[Internal direct sum of subspaces|0XYYT5KNTX]]: how a space splits uniquely into pieces, the test $U \cap W = \{0\}$, the count of dimensions, and why three subspaces need more than pairwise tests.
2. [[External direct sum|0S7W6EG32V]]: how to build the direct sum of spaces that do not live in a common space, and how to define linear maps out of it.
3. [[Direct product of vector spaces|0EX2HPXPJ6]]: the product of a family, why its dimension adds up, and where it differs from the direct sum for infinite families.
4. [[Complementary subspace|0M83V17KHX]]: what a complement is, why a subspace has many of them, and why all of them are isomorphic to $V / U$.
5. [[Existence of a complementary subspace|0P9T8WHNMH]]: why every subspace has a complement, by extending a basis in finite dimension and by Zorn's lemma in general.
6. [[Projection|033DA1WE8Y]]: the idempotent linear maps, how they match direct sum decompositions, and the difference between oblique and orthogonal projections.
7. [[Quotient space|0BR3FY5Q8M]]: cosets $v + U$ as parallel copies of $U$, why the operations on them are well defined, and the quotient map.
8. [[Dimension of a quotient space|0SXDQ6TN00]]: the formula $\dim V / U = \dim V - \dim U$, and a basis of the quotient from a complement.
9. [[Universal property of the quotient space|0ZERJX6PH6]]: how a linear map that vanishes on $U$ passes to $V / U$ in exactly one way.
10. [[First isomorphism theorem for vector spaces|0MTBGVZ4XJ]]: why $V / \ker f$ is isomorphic to the image of $f$, and rank-nullity as a corollary.
11. [[Second isomorphism theorem for vector spaces|0APN65D6Y6]]: the isomorphism $(U + W) / W \cong U / (U \cap W)$, and Grassmann's formula from it.
12. [[Third isomorphism theorem for vector spaces|07RB3EMBWW]]: how to cancel in a quotient of quotients, and the correspondence of subspaces that contain $U$.
13. [[Codimension of a subspace|JJCGJ1EGCQ]]: the size of $V / U$, which still makes sense in infinite dimension, hyperplanes, and the codimension of an intersection.
14. [[Exact sequence of vector spaces|946YAZNYKX]]: chains of linear maps in which each image is the next kernel, why short exact sequences split, and the alternating sum of dimensions.

### Prerequisites

- [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]]: subspaces, sums and intersections of subspaces, bases and dimension.
- [[Linear maps|9080WQTZ3M]]: kernel, image, isomorphisms and the rank-nullity theorem.
