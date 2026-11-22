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

We compute the dimension of each side of the second isomorphism theorem and compare the results.
Let $U$ and $W$ be finite-dimensional subspaces of a vector space $V$.

1. The [[sum|0RMKABS2S5]] $U + W$ is finite-dimensional.
   A basis of $U$ together with a basis of $W$ spans $U + W$, and this list is finite.
2. The [[intersection|0V33SPH7RR]] $U \cap W$ is a subspace of the finite-dimensional space $U$, so it is finite-dimensional by the [[dimension of a subspace|0QW084460E]].
3. We apply the [[dimension of a quotient space|0SXDQ6TN00]] to the subspace $U \cap W$ of $U$:
   $$\dim \big(U / (U \cap W)\big) = \dim U - \dim (U \cap W).$$
4. We apply it again to the subspace $W$ of $U + W$:
   $$\dim \big((U + W) / W\big) = \dim (U + W) - \dim W.$$
5. By the [[second isomorphism theorem|0APN65D6Y6]], $U / (U \cap W) \cong (U + W) / W$.
6. Isomorphic finite-dimensional spaces have the same dimension, by the [[classification by dimension|0VJBSK15SN]].
   So the left sides of steps 3 and 4 are equal.
7. Hence $\dim U - \dim (U \cap W) = \dim (U + W) - \dim W$.
8. Adding $\dim W + \dim (U \cap W)$ to both sides gives
   $$\dim (U + W) + \dim (U \cap W) = \dim U + \dim W.$$

## Idea

Both sides of the second isomorphism theorem count the directions that $U$ adds to $W$.
The left side counts them inside $U$, as $\dim U - \dim (U \cap W)$, and the right side counts them inside $U + W$, as $\dim (U + W) - \dim W$.
Setting the two counts equal is Grassmann's formula.
For the $xy$-plane and the $yz$-plane of $\R^3$, both counts give $1$: $2 - 1 = 3 - 2$.

## Variants

The [[proof by extending a basis of the intersection|75VVYAZBK3]] builds an explicit basis of $U + W$ from a basis of $U \cap W$, and it needs no quotients.
A third proof uses the linear map $U \times W \to U + W$, $(u, w) \mapsto u - w$.
It is onto, and its kernel is $\{(x, x) : x \in U \cap W\}$, which is isomorphic to $U \cap W$.
The rank-nullity theorem then gives $\dim U + \dim W = \dim (U + W) + \dim (U \cap W)$.
