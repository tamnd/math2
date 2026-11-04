---
tag: T8GV9PYHDQ
kind: proof
name: Proof that a space is the direct sum of a finite-dimensional subspace and its orthogonal complement
msc: [46C05]
proves: 0SP7P0G7KQ
uses: [0VGSYBWHV2, 079D68S3AW, 041JTZCK9Q, 0EPTJA5QV4, 0Y85GYEGSF, 0FWJ0VW561, 09DZ8CD1AK]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.49
---

## Proof

We use an orthonormal basis of $W$ to split each vector, and then show that $W \cap W^\perp = \set{0}$.

1. Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $W$ be a finite-dimensional [[subspace|0EPTJA5QV4]] of $V$, and let $W^\perp$ be its [[orthogonal complement|079D68S3AW]].
2. For all $u, w \in V$ and $a \in \mathbb{K}$, conjugate symmetry and linearity in the first argument give $\ip{u}{a w} = \overline{a} \ip{u}{w}$. In the same way, $\ip{u}{\cdot}$ is additive.
3. $W^\perp$ is a subspace. Indeed, $\ip{0}{w} = 0$ for all $w$. If $x, y \in W^\perp$ and $a, b \in \mathbb{K}$, then $\ip{a x + b y}{w} = a \ip{x}{w} + b \ip{y}{w} = 0$ for all $w \in W$.
4. The restriction of $\ip{\cdot}{\cdot}$ to $W$ is an inner product on $W$. So $W$ is a finite-dimensional inner product space, and it has an [[orthonormal basis|0Y85GYEGSF]] $e_1, \dots, e_k$.
5. Let $v \in V$. Set $w = \sum_{i=1}^{k} \ip{v}{e_i} e_i$, which lies in $W$, and $w' = v - w$. Then $v = w + w'$.
6. For each $j$, linearity in the first argument and orthonormality give $\ip{w}{e_j} = \ip{v}{e_j}$. So $\ip{w'}{e_j} = 0$.
7. Let $u \in W$. By the [[formula for coordinates|09DZ8CD1AK]] in $W$, $u = \sum_j a_j e_j$ with $a_j \in \mathbb{K}$. By step 2, $\ip{w'}{u} = \sum_j \overline{a_j} \ip{w'}{e_j} = 0$.
8. Hence $w' \in W^\perp$. So $V = W + W^\perp$.
9. Let $x \in W \cap W^\perp$. Since $x \in W^\perp$ and $x \in W$, we get $\ip{x}{x} = 0$. By positivity of the inner product, $x = 0$.
10. Let $u \in W$ and $u' \in W^\perp$ with $u + u' = 0$. Then $u = -u'$ lies in $W$ and in the subspace $W^\perp$. By step 9, $u = 0$, and so $u' = 0$.
11. By steps 8 and 10 and the equivalent form of the definition of the [[direct sum|041JTZCK9Q]], $V = W \oplus W^\perp$.

## Idea

For an orthonormal basis $e_1, \dots, e_k$ of $W$, the vector $\sum_i \ip{v}{e_i} e_i$ is the part of $v$ in $W$. The remainder has zero inner product with each $e_i$, so it lies in $W^\perp$. Uniqueness holds because a vector orthogonal to itself is zero.
