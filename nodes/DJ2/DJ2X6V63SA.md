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

Let $n = \dim V$.
All subspaces of $V$ are finite-dimensional, by the [[dimension of a subspace|0QW084460E]].
By [[Grassmann's formula|06HTJNCMPA]],
$$\dim(U + W) + \dim(U \cap W) = \dim U + \dim W. \qquad (*)$$

1. Assume condition 1. By the [[criteria for two subspaces|20A0K3KBZD]], $U \cap W = \{0\}$ and $U + W = V$.
2. Then $(*)$ gives $n + 0 = \dim U + \dim W$. So conditions 2 and 3 hold.
3. Assume condition 2. Then $(*)$ gives $\dim(U + W) = \dim U + \dim W = n$.
4. The subspace $U + W$ of $V$ has the same dimension as $V$. By the [[dimension of a subspace|0QW084460E]], $U + W = V$.
5. With $U \cap W = \{0\}$ and the criteria, $V = U \oplus W$. This is condition 1.
6. Assume condition 3. Then $(*)$ gives $n + \dim(U \cap W) = \dim U + \dim W = n$.
7. So $\dim(U \cap W) = 0$, that is, $U \cap W = \{0\}$.
8. With $U + W = V$ and the criteria, $V = U \oplus W$. This is condition 1.

## Idea

Grassmann's formula ties together the four numbers $\dim(U + W)$, $\dim(U \cap W)$, $\dim U$ and $\dim W$.
If $\dim U + \dim W = \dim V$, then the intersection is zero exactly when the sum is everything.

## Variants

- Without Grassmann's formula: if $U \cap W = \{0\}$, then a basis of $U$ followed by a basis of $W$ is independent in $V$ by the criteria. It has $\dim V$ vectors, so it is a [[basis|0KCQ9Y3QKA]] of $V$, and $U + W = V$.
- The criterion also follows from injectivity of the addition map $U \times W \to V$ and the equivalence of injective and surjective maps between spaces of the same finite dimension.
