---
tag: WK6YWCWJD0
kind: proof
name: Proof that row rank equals column rank by row reduction
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 0TZAG60ZYT
uses: [FCM29NQ6DN, 0NNR68BFRY, 0BCMGDHZGR, 11CSKXQNG3, E4GKK727ZM, 1JGMW9DM4Z, 0EWQEYRVA8, 0W809K6AW0]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proof using row reduction
  - book: isbn:9780321982384
    locator: Section 4.6
---

## Proof

We show that the row rank and the column rank both equal the number of pivots of the reduced row echelon form.
Let $A$ be an $m \times n$ matrix over a field $F$.

1. By the [[existence of the reduced form|FCM29NQ6DN]], $A$ is row equivalent to a matrix $R$ in [[reduced row echelon form|0NNR68BFRY]].
Let $p$ be the number of [[pivots|0BCMGDHZGR]] of $R$.
2. By the [[theorem on the column space|11CSKXQNG3]], the pivot columns of $A$ form a basis of $\operatorname{Col}(A)$, so $\dim \operatorname{Col}(A) = p$.
3. Row operations do not change the row space, by the [[theorem on row equivalence|E4GKK727ZM]], so $\operatorname{Row}(A) = \operatorname{Row}(R)$.
4. In the reduced form, each nonzero row has exactly one leading entry, and that entry is a pivot.
Each pivot lies in exactly one row, so $R$ has exactly $p$ nonzero rows.
5. The nonzero rows of $R$ form a basis of $\operatorname{Row}(R)$, by the [[theorem on echelon rows|1JGMW9DM4Z]].
With steps 3 and 4, this gives $\dim \operatorname{Row}(A) = p$.
6. Steps 2 and 5 give $\dim \operatorname{Row}(A) = p = \dim \operatorname{Col}(A)$.
7. The columns of the [[transpose|0W809K6AW0]] $A^{\mathsf{T}}$ are the rows of $A$, written as columns, so $\dim \operatorname{Col}(A^{\mathsf{T}}) = \dim \operatorname{Row}(A)$.
8. By the [[definition of rank|0EWQEYRVA8]] and steps 6 and 7, $\rank A^{\mathsf{T}} = \dim \operatorname{Row}(A) = \dim \operatorname{Col}(A) = \rank A$.

## Idea

Row operations keep the row space, and they change the column space but keep every linear relation among the columns.
So both dimensions can be read from the reduced form.
There, the pivots count the independent columns, and they also count the nonzero rows.
For example, the reduced form of the matrix with rows $(1, 2, 3)$ and $(2, 4, 6)$ has rows $(1, 2, 3)$ and $(0, 0, 0)$, with one pivot, one nonzero row and one independent column.

## Variants

The [[proof by a factorization A = CR|S1C1ATEFW1]] uses no row reduction, and it works with any basis of the column space.
The [[proof by orthogonality|4JYHHBC6J7]] works only over $\mathbb{R}$ or another ordered field, but it shows more: $A$ is injective on its row space.
The [[proof by duality|7DQXA4AY1D]] uses the [[matrix of the dual map|0ZPB3180AY]] and the [[dimension of the annihilator|06Q1EFVH0Q]], and it proves the statement for linear maps without coordinates.
