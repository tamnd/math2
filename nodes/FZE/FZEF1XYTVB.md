---
tag: FZEF1XYTVB
kind: proof
name: Proof of the double orthogonal complement theorem
msc: [46C05]
topics: [8GQVME4SZZ]
audience: ug1
proves: 0PXN9G4MX1
uses: [0VGSYBWHV2, 079D68S3AW, T5Q51M5BAK, 0E2NYPVSP9, 0WGAXEK99E, 0QW084460E]
methods: [0NTF6DMVAP]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.52
  - book: isbn:9783031410253
    locator: Section 6C
---

## Proof

We prove the inclusion $U \subseteq (U^\perp)^\perp$ directly, and then show that both sides have the same dimension.

1. Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $U$ be a subspace of $V$, let $U^\perp$ be its [[orthogonal complement|079D68S3AW]], and set $n = \dim V$.
2. Let $u \in U$ and $x \in U^\perp$. By conjugate symmetry and the definition of $U^\perp$, $\ip{u}{x} = \overline{\ip{x}{u}} = \overline{0} = 0$.
3. So $u$ is orthogonal to every vector of $U^\perp$, which means $u \in (U^\perp)^\perp$. Hence $U \subseteq (U^\perp)^\perp$, and this step does not use finite dimension.
4. The set $U^\perp$ is a subspace of $V$, by part 1 of the [[basic properties|T5Q51M5BAK]]. The [[dimension formula|0E2NYPVSP9]] gives $\dim U^\perp = n - \dim U$.
5. The same formula for the subspace $U^\perp$ gives $\dim (U^\perp)^\perp = n - \dim U^\perp = n - (n - \dim U) = \dim U$.
6. By step 3, $U$ is a subspace of the [[finite-dimensional|0QW084460E]] space $(U^\perp)^\perp$, and by step 5 the two have the same dimension.
7. A [[subspace of full dimension is the whole space|0WGAXEK99E]], so $U = (U^\perp)^\perp$.

## Idea

Every vector of $U$ is orthogonal to every vector of $U^\perp$, so $U$ sits inside $(U^\perp)^\perp$ for free.
Each complement subtracts the dimension from $n$, so two complements bring the dimension back to $\dim U$.
A subspace inside another one of the same finite dimension is equal to it.

## Variants

A proof without counting dimensions uses the [[orthogonal decomposition|0SP7P0G7KQ]].
Let $x \in (U^\perp)^\perp$ and write $x = u + u'$ with $u \in U$ and $u' \in U^\perp$.
Then $u' = x - u$ lies in $(U^\perp)^\perp$, by step 3, and also in $U^\perp$, so $\ip{u'}{u'} = 0$ and $u' = 0$.
This version needs only that $U$ is finite-dimensional, so $V$ may be infinite-dimensional.
