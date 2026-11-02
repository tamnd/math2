---
tag: 6AT64EQEJQ
kind: definition
name: Free product of algebras
msc: [08B25, "20E06"]
defines: HHNWHS1XTN
uses: [AJNZJD8442, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Free_product
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras and let $(A_i)_{i \in I}$ be a family of algebras in $\mathcal{V}$.
A *free product* of the family in $\mathcal{V}$ is an algebra $A$ in $\mathcal{V}$ with [[homomorphisms|KBXSZC6BV1]] $\iota_i \colon A_i \to A$ such that the following holds.
For every algebra $B$ in $\mathcal{V}$ and all homomorphisms $f_i \colon A_i \to B$, there is a unique homomorphism $f \colon A \to B$ with $f \circ \iota_i = f_i$ for all $i \in I$.

## Remarks

The free product exists for every family in a variety, and it is unique up to a unique isomorphism compatible with the maps $\iota_i$.
It is the coproduct of the family in the category of algebras of $\mathcal{V}$.
Some authors require in addition that every $\iota_i$ be injective.

Example: in the variety of abelian groups, $A_1 \times A_2$ with $\iota_1(a) = (a, 0)$ and $\iota_2(b) = (0, b)$ is a free product.
Given $f_1, f_2$ into an abelian group $B$, the map $f(a, b) = f_1(a) + f_2(b)$ is a homomorphism because $B$ is abelian, it satisfies $f \circ \iota_k = f_k$, and it is the only such map since $(a, b) = \iota_1(a) + \iota_2(b)$.

Non-example: in the variety of all groups, $\Z \times \Z$ with the two coordinate inclusions is not a free product of $\Z$ and $\Z$.
Take $f_1, f_2 \colon \Z \to S_3$ sending $1$ to the transpositions $(1\,2)$ and $(2\,3)$.
A homomorphism $f$ with $f \circ \iota_k = f_k$ would send the commuting elements $(1, 0)$ and $(0, 1)$ to these two transpositions, which do not commute.

In the variety of groups, the free product of a family is the group of reduced words in the factors.
