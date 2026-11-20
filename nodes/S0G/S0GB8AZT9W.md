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

We prove both directions, and then the matrix form.

1. Assume 1, so $P = P_U$ for a subspace $U$. By part 1 of the [[formulas for the orthogonal projection|AK3JJ5HHG2]], $P^2 = P$.
2. Let $v, w \in V$. Write $v = Pv + v'$ and $w = Pw + w'$, where $v' = v - Pv$ and $w' = w - Pw$ lie in $U^\perp$ by the [[definition|0Q8HZTJC7G]].
3. $Pv \in U$ and $w' \in U^\perp$, so $\ip{Pv}{w'} = 0$. Hence $\ip{Pv}{w} = \ip{Pv}{Pw} + \ip{Pv}{w'} = \ip{Pv}{Pw}$.
4. $Pw \in U$ and $v' \in U^\perp$, so $\ip{v'}{Pw} = 0$. Hence $\ip{v}{Pw} = \ip{Pv}{Pw} + \ip{v'}{Pw} = \ip{Pv}{Pw}$.
5. Steps 3 and 4 give $\ip{Pv}{w} = \ip{v}{Pw}$. So 1 implies 2.
6. Assume 2, and let $U$ be the image of $P$. It is a subspace of the finite-dimensional space $V$, so $U$ is finite-dimensional and $P_U$ is defined.
7. For $u \in U$, write $u = Px$. Then $Pu = P^2 x = Px = u$.
8. Let $v \in V$. Then $Pv \in U$. For $u \in U$, steps 7 and 2 give $\ip{v - Pv}{u} = \ip{v - Pv}{Pu} = \ip{P(v - Pv)}{u} = \ip{Pv - P^2 v}{u} = 0$.
9. So $v = Pv + (v - Pv)$ with $Pv \in U$ and $v - Pv \in U^\perp$. By the uniqueness in the [[orthogonal decomposition|0SP7P0G7KQ]], $P_U v = Pv$. So 2 implies 1, with $U = \im P$.
10. Matrix form: for the standard inner product, $\ip{Pv}{w} = w^* P v$ and $\ip{v}{Pw} = (Pw)^* v = w^* P^* v$, by the rule $(BC)^* = C^* B^*$ for the [[conjugate transpose|0EX045E2BP]].
11. So condition 2 holds for all $v, w$ exactly when $w^* (P - P^*) v = 0$ for all $v, w$. Taking $v = e_j$ and $w = e_i$ gives entry $(i, j)$ of $P - P^*$, so this holds exactly when $P^* = P$.

## Idea

An orthogonal projection splits each vector into two orthogonal parts, and the cross terms vanish in both inner products.
Conversely, self-adjointness moves $P$ across the inner product, and idempotence then kills the error term.

## Variants

With the [[spectral theorem|06J4PXRG22]], a self-adjoint $P$ has an orthonormal basis of eigenvectors, and $P^2 = P$ forces each eigenvalue to be $0$ or $1$.
Then $P$ is the projection onto the span of the eigenvectors with eigenvalue $1$.
