---
tag: T8GV9PYHDQ
kind: proof
name: Proof of the orthogonal decomposition
msc: [46C05]
topics: [8GQVME4SZZ]
audience: ug1
proves: 0SP7P0G7KQ
uses: [0VGSYBWHV2, 079D68S3AW, 041JTZCK9Q, 0EPTJA5QV4, 0Y85GYEGSF, 0FWJ0VW561, 09DZ8CD1AK, T5Q51M5BAK, 06HTJNCMPA]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.49
  - book: isbn:9783031410253
    locator: Section 6C
---

## Proof

We build the part of $v$ in $U$ from an orthonormal basis of $U$, check that the rest is orthogonal to $U$, and then use $U \cap U^\perp = \{0\}$ for uniqueness.

1. Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $U$ be a finite-dimensional [[subspace|0EPTJA5QV4]] of $V$, and let $U^\perp$ be its [[orthogonal complement|079D68S3AW]].
2. For all $x, y \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity in the first argument give $\ip{x}{a y} = \overline{a} \ip{x}{y}$, and in the same way $\ip{x}{y + z} = \ip{x}{y} + \ip{x}{z}$.
3. The set $U^\perp$ is a subspace of $V$, by part 1 of the [[basic properties|T5Q51M5BAK]].
4. The inner product of $V$, restricted to $U$, is an inner product on $U$. So $U$ is a finite-dimensional inner product space, and it has an [[orthonormal basis|0Y85GYEGSF]] $e_1, \dots, e_k$. If $U = \{0\}$, then $k = 0$ and every sum below is $0$.
5. Let $v \in V$. Set $u = \sum_{i=1}^{k} \ip{v}{e_i} e_i$, which lies in $U$ as a combination of the $e_i$, and set $u' = v - u$. Then $v = u + u'$.
6. Fix $j$. Linearity in the first argument, with $\ip{e_i}{e_j} = 0$ for $i \ne j$ and $\ip{e_j}{e_j} = 1$, gives $\ip{u}{e_j} = \ip{v}{e_j}$. So $\ip{u'}{e_j} = \ip{v}{e_j} - \ip{u}{e_j} = 0$.
7. Let $x \in U$. By the [[formula for coordinates|09DZ8CD1AK]] in $U$, $x = \sum_j a_j e_j$ with $a_j \in \mathbb{K}$. By step 2 and step 6, $\ip{u'}{x} = \sum_j \overline{a_j} \ip{u'}{e_j} = 0$.
8. Hence $u' \in U^\perp$. So $V = U + U^\perp$, and the two parts of $v$ are the vectors given in part 2 of the statement.
9. By part 4 of the basic properties, $U \cap U^\perp = \{0\}$.
10. Let $x \in U$ and $x' \in U^\perp$ with $x + x' = 0$. Then $x = -x'$ lies in $U$ and in the subspace $U^\perp$, so $x = 0$ by step 9, and then $x' = 0$.
11. Steps 8 and 10 and the equivalent form of the definition of the [[direct sum|041JTZCK9Q]] give $V = U \oplus U^\perp$. In particular the pair $(u, u')$ of step 5 is the only pair with $v = u + u'$, $u \in U$ and $u' \in U^\perp$. This proves parts 1 and 2.
12. Now let $V$ be finite-dimensional. Then $U$ and $U^\perp$ are finite-dimensional, as subspaces of $V$.
13. The [[dimension formula for sums|06HTJNCMPA]] gives $\dim(U + U^\perp) = \dim U + \dim U^\perp - \dim(U \cap U^\perp)$.
14. By step 8, $U + U^\perp = V$, and by step 9, $\dim(U \cap U^\perp) = 0$. So $\dim V = \dim U + \dim U^\perp$, which is part 3.

## Idea

The vector $\sum_i \ip{v}{e_i} e_i$ is the natural guess for the part of $v$ in $U$, because it has the same inner product as $v$ with each $e_i$.
So the remainder has zero inner product with each $e_i$, and by linearity with every vector of $U$.
Uniqueness holds because a vector that lies in $U$ and is orthogonal to $U$ is orthogonal to itself, hence zero.
The dimension count is then the dimension formula for a direct sum.

## Variants

In $\R^n$ there is a proof by matrices.
If the columns of $A$ form a basis of $U$, then $A^{\mathsf{T}} A$ is invertible, because the columns are independent, and $u = A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} v$ by the [[projection formulas|AK3JJ5HHG2]].
Part 3 in $\R^n$ also follows from rank-nullity: $U^\perp$ is the null space of a $k \times n$ matrix of rank $k$ whose rows form a basis of $U$, so its dimension is $n - k$.
