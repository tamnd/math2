---
tag: JSHFXYCSSK
kind: proof
name: Proof of the formula for the dimension of the orthogonal complement
msc: [15A03, 46C05]
proves: 0E2NYPVSP9
uses: [079D68S3AW, 0QW084460E, 0SP7P0G7KQ, 041JTZCK9Q, 06HTJNCMPA, 05G2G0P224]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.51
---

## Proof

We combine the orthogonal decomposition with Grassmann's formula.

1. Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$. Let $W$ be a subspace of $V$, and let $W^\perp$ be its [[orthogonal complement|079D68S3AW]].
2. The subspace $W$ is [[finite-dimensional|0QW084460E]], since $V$ is. So [[$V = W \oplus W^\perp$|0SP7P0G7KQ]].
3. By the definition of the [[direct sum|041JTZCK9Q]], $W + W^\perp = V$ and the only way to write $0 = u + u'$ with $u \in W$, $u' \in W^\perp$ is $u = u' = 0$.
4. Let $x \in W \cap W^\perp$. Then $x + (-x) = 0$ with $x \in W$ and $-x \in W^\perp$. By step 3, $x = 0$. So $W \cap W^\perp = \set{0}$.
5. The set $W^\perp$ contains $0$ and is closed under linear combinations, by linearity of the inner product in the first argument. So $W^\perp$ is a subspace, and it is finite-dimensional by the same result as in step 2.
6. By [[Grassmann's formula|06HTJNCMPA]], $\dim(W + W^\perp) + \dim(W \cap W^\perp) = \dim W + \dim W^\perp$, where $\dim$ is the [[dimension|05G2G0P224]].
7. By steps 3 and 4, the left side is $\dim V + 0$. Hence $\dim W + \dim W^\perp = \dim V$.

## Idea

The space splits as $W \oplus W^\perp$, and the two parts meet only in $0$. Dimensions add over such a splitting, as Grassmann's formula shows.
