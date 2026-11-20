---
tag: ~1fa1acd5
kind: proof
name: Proof that row rank equals column rank by row reduction
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 0TZAG60ZYT
uses: [FCM29NQ6DN, 0NNR68BFRY, 0BCMGDHZGR, 11CSKXQNG3, E4GKK727ZM, ~b802c546, 0EWQEYRVA8, 0W809K6AW0]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proof using row reduction
  - book: isbn:9780321982384
    locator: Section 4.6
---

## Proof

1. Let $A$ be an $m \times n$ matrix over $F$. By the [[existence of the reduced form|FCM29NQ6DN]], $A$ is row equivalent to a [[reduced row echelon form|0NNR68BFRY]] $R$.
2. Let $p$ be the number of [[pivots|0BCMGDHZGR]] of $R$.
3. By the [[theorem on the column space|11CSKXQNG3]], part 3, $\dim \operatorname{Col}(A) = p$.
4. By the [[theorem on row equivalence|E4GKK727ZM]], part 3, $\operatorname{Row}(A) = \operatorname{Row}(R)$.
5. By the definition of the reduced form, each nonzero row of $R$ has exactly one leading entry, and each pivot lies in one nonzero row. So $R$ has exactly $p$ nonzero rows.
6. By the [[theorem on echelon rows|~b802c546]], the nonzero rows of $R$ form a basis of $\operatorname{Row}(R)$. So $\dim \operatorname{Row}(A) = p$, by steps 4 and 5.
7. By steps 3 and 6, $\dim \operatorname{Row}(A) = \dim \operatorname{Col}(A)$.
8. The columns of the [[transpose|0W809K6AW0]] $A^\top$ are the rows of $A$, so $\operatorname{Col}(A^\top) = \operatorname{Row}(A)$.
9. By the [[definition of rank|0EWQEYRVA8]] and steps 7 and 8, $\rank A^\top = \dim \operatorname{Row}(A) = \dim \operatorname{Col}(A) = \rank A$.

## Idea

Row operations change the column space but keep its dimension, and they keep the row space.
In the reduced form, the pivots count both the independent columns and the nonzero rows.
So both dimensions equal the number of pivots.

## Variants

- [[By a rank factorization|S1C1ATEFW1]]: this proof uses no row reduction and works for any basis of the column space.
- [[By orthogonality over the real numbers|~53093409]]: this proof works only over $\R$, or over an ordered field.
- By duality: see the [[matrix of the dual map|0ZPB3180AY]] and the [[dimension of the annihilator|06Q1EFVH0Q]].
