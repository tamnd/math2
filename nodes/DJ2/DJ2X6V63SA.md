---
tag: DJ2X6V63SA
kind: proof
name: Proof of the dimension criterion for a direct sum
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: P4JG9DJ2HH
methods: [TFQ1845T84, 0NTF6DMVAP]
uses: [20A0K3KBZD, 06HTJNCMPA, 0QW084460E, 05G2G0P224]
sources:
  - book: isbn:9783031410253
    locator: Section 2C
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
---

## Proof

We read off each implication from Grassmann's formula, together with the criteria for two subspaces.
Let $n = \dim V$.
All subspaces of $V$ are finite-dimensional, by the [[dimension of a subspace|0QW084460E]], so [[Grassmann's formula|06HTJNCMPA]] applies:
$$\dim(U + W) + \dim(U \cap W) = \dim U + \dim W. \qquad (*)$$

1. Assume condition 1.
   By the [[criteria for two subspaces|20A0K3KBZD]], $U \cap W = \{0\}$ and $U + W = V$.
2. Then $(*)$ reads $n + 0 = \dim U + \dim W$.
   So conditions 2 and 3 both hold.
3. Assume condition 2.
   Then $\dim(U \cap W) = 0$, and $(*)$ gives $\dim(U + W) = \dim U + \dim W = n$.
4. The subspace $U + W$ of $V$ has the same dimension as $V$, so $U + W = V$, by the [[dimension of a subspace|0QW084460E]].
5. Together with $U \cap W = \{0\}$, the criteria give $V = U \oplus W$, which is condition 1.
6. Assume condition 3.
   Then $\dim(U + W) = n$, and $(*)$ gives $n + \dim(U \cap W) = \dim U + \dim W = n$.
7. So $\dim(U \cap W) = 0$, that is, $U \cap W = \{0\}$.
8. Together with $U + W = V$, the criteria give $V = U \oplus W$, which is condition 1.

## Idea

Grassmann's formula ties together four numbers: the dimensions of $U$, of $W$, of their sum and of their intersection.
When $\dim U + \dim W = \dim V$, the formula says that the intersection has dimension $0$ exactly when the sum has dimension $\dim V$.
So a zero intersection and a full sum become the same condition, and either one gives the direct sum.

## Variants

The step from condition 2 to condition 1 also works without Grassmann's formula.
If $U \cap W = \{0\}$, then a basis of $U$ followed by a basis of $W$ is independent in $V$, by the criteria for two subspaces.
This list has $\dim U + \dim W = \dim V$ vectors, so it is a [[basis|0KCQ9Y3QKA]] of $V$, and therefore $U + W = V$.
A second variant uses the addition map $U \times W \to V$: it is injective exactly when $U \cap W = \{0\}$, and an injective linear map between spaces of the same finite dimension is surjective.
