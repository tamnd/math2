---
tag: S0GB8AZT9W
kind: proof
name: Proof that orthogonal projections are the self-adjoint idempotents
msc: [15A04, 47A05]
topics: [8GQVME4SZZ]
audience: ug1
proves: ZJRJNWJ8V1
uses: [0Q8HZTJC7G, AK3JJ5HHG2, 0SP7P0G7KQ, 0EX045E2BP]
methods: [TFQ1845T84, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Orthogonal projections
  - book: isbn:9783031410253
    locator: Section 6C
---

## Proof

We prove that 1 implies 2, then that 2 implies 1, and finally we translate condition 2 into matrices.

1. Assume 1, so $P = P_U$ for a subspace $U$; by part 1 of the [[formulas for the orthogonal projection|AK3JJ5HHG2]], $P^2 = P$.
2. Let $v, w \in V$, and write $v = Pv + v'$ and $w = Pw + w'$, where $v' = v - Pv$ and $w' = w - Pw$ lie in $U^\perp$ by the [[definition|0Q8HZTJC7G]].
3. Since $Pv \in U$ and $w' \in U^\perp$, we have $\ip{Pv}{w'} = 0$, and so
$$\ip{Pv}{w} = \ip{Pv}{Pw} + \ip{Pv}{w'} = \ip{Pv}{Pw}.$$
4. Since $Pw \in U$ and $v' \in U^\perp$, we have $\ip{v'}{Pw} = 0$, and so
$$\ip{v}{Pw} = \ip{Pv}{Pw} + \ip{v'}{Pw} = \ip{Pv}{Pw}.$$
5. Steps 3 and 4 give $\ip{Pv}{w} = \ip{v}{Pw}$, so 1 implies 2.
6. Now assume 2, and let $U$ be the image of $P$; it is a subspace of the finite-dimensional space $V$, so $U$ is finite-dimensional and $P_U$ is defined.
7. Each $u \in U$ is $u = Px$ for some $x$, so $Pu = P^2 x = Px = u$.
8. Let $v \in V$, so that $Pv \in U$; for every $u \in U$, step 7 and the self-adjointness in condition 2 give
$$\ip{v - Pv}{u} = \ip{v - Pv}{Pu} = \ip{P(v - Pv)}{u} = \ip{Pv - P^2 v}{u} = 0.$$
9. So $v = Pv + (v - Pv)$ with $Pv \in U$ and $v - Pv \in U^\perp$, and the uniqueness in the [[orthogonal decomposition|0SP7P0G7KQ]] gives $P_U v = Pv$; hence 2 implies 1, with $U = \im P$.
10. For the matrix form, take the standard inner product $\ip{x}{y} = y^* x$; the rule $(BC)^* = C^* B^*$ for the [[conjugate transpose|0EX045E2BP]] gives
$$\ip{Pv}{w} = w^* P v, \qquad \ip{v}{Pw} = (Pw)^* v = w^* P^* v.$$
11. So condition 2 holds for all $v, w$ exactly when $w^* (P - P^*) v = 0$ for all $v, w$.
12. Taking $v = e_j$ and $w = e_i$ picks out entry $(i, j)$ of $P - P^*$, so this holds exactly when $P^* = P$, and over $\R$ exactly when $P^{\mathsf{T}} = P$.

## Idea

An orthogonal projection splits each vector into a part in $U$ and a part in $U^\perp$.
In both inner products $\ip{Pv}{w}$ and $\ip{v}{Pw}$, the cross terms between the two kinds of parts vanish, and what is left is $\ip{Pv}{Pw}$ both times.
For the converse, self-adjointness lets us move $P$ across the inner product, and idempotence then kills the error term $v - Pv$.

## Variants

The [[real spectral theorem|06J4PXRG22]], or its [[complex form|04CW1P44VD]], gives a second proof of the converse.
A self-adjoint $P$ has an orthonormal basis of eigenvectors, and $P^2 = P$ forces each eigenvalue $\lambda$ to satisfy $\lambda^2 = \lambda$, so $\lambda$ is $0$ or $1$.
Then $P$ keeps the eigenvectors with eigenvalue $1$ and kills the others, which is the orthogonal projection onto the span of the first group.
