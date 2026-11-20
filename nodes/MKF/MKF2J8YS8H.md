---
tag: MKF2J8YS8H
kind: proof
name: Proof of Grassmann's formula by the second isomorphism theorem
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: 06HTJNCMPA
methods: [0NTF6DMVAP]
uses: [0APN65D6Y6, 0SXDQ6TN00, 0VJBSK15SN, 0QW084460E, 0RMKABS2S5, 0V33SPH7RR]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem B (modules)
  - book: isbn:9783031410253
    locator: Section 3E
---

## Proof

Let $U$ and $W$ be finite-dimensional subspaces of $V$.

1. The [[sum|0RMKABS2S5]] $U + W$ is spanned by the union of a basis of $U$ and a basis of $W$. So it is finite-dimensional.
2. The [[intersection|0V33SPH7RR]] $U \cap W$ is a subspace of $U$. By the [[dimension of a subspace|0QW084460E]], it is finite-dimensional.
3. Apply the [[dimension of a quotient|0SXDQ6TN00]] to the subspace $U \cap W$ of the finite-dimensional space $U$: $\dim\big(U / (U \cap W)\big) = \dim U - \dim(U \cap W)$.
4. Apply it again to the subspace $W$ of the finite-dimensional space $U + W$: $\dim\big((U + W)/W\big) = \dim(U + W) - \dim W$.
5. By the [[second isomorphism theorem|0APN65D6Y6]], $U / (U \cap W) \cong (U + W)/W$.
6. Isomorphic finite-dimensional spaces have the same dimension, by the [[classification by dimension|0VJBSK15SN]].
7. So $\dim U - \dim(U \cap W) = \dim(U + W) - \dim W$, by steps 3 to 6.
8. Rearranging gives $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$.

## Idea

Both sides of Grassmann's formula count the directions that $U$ adds to $W$.
The second isomorphism theorem identifies these directions, once as $U / (U \cap W)$ and once as $(U + W)/W$.

## Variants

- The [[proof by extending a basis of the intersection|75VVYAZBK3]] builds an explicit basis of $U + W$.
- One can also apply the first isomorphism theorem to the map $U \times W \to U + W$, $(u, w) \mapsto u - w$, whose kernel $\{(x, x) : x \in U \cap W\}$ is isomorphic to $U \cap W$.
