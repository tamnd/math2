---
tag: FZEF1XYTVB
kind: proof
name: Proof that the orthogonal complement of the orthogonal complement is the subspace
msc: [46C05]
proves: 0PXN9G4MX1
uses: [0VGSYBWHV2, 079D68S3AW, 0E2NYPVSP9, 0WGAXEK99E, 0QW084460E]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.52
---

## Proof

We show one inclusion, and then compare dimensions.

1. Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $W$ be a subspace of $V$ and $W^\perp$ its [[orthogonal complement|079D68S3AW]]. Set $n = \dim V$.
2. Let $w \in W$ and $x \in W^\perp$. By conjugate symmetry, $\ip{w}{x} = \overline{\ip{x}{w}} = \overline{0} = 0$.
3. So $w$ is orthogonal to every vector of $W^\perp$, that is, $w \in (W^\perp)^\perp$. Hence $W \subseteq (W^\perp)^\perp$.
4. The set $W^\perp$ contains $0$ and is closed under linear combinations, by linearity in the first argument. So it is a subspace of $V$. By the [[dimension formula|0E2NYPVSP9]], $\dim W^\perp = n - \dim W$.
5. The same formula for the subspace $W^\perp$ gives $\dim (W^\perp)^\perp = n - \dim W^\perp = \dim W$.
6. By step 3, $W$ is a subspace of the [[finite-dimensional|0QW084460E]] space $(W^\perp)^\perp$, and by step 5 it has the same dimension.
7. A [[subspace of full dimension is the whole space|0WGAXEK99E]]. Hence $W = (W^\perp)^\perp$.

## Idea

Each vector of $W$ is orthogonal to each vector of $W^\perp$, so $W$ lies inside $(W^\perp)^\perp$. Taking the complement twice brings the dimension back to $\dim W$. A subspace inside another one of the same finite dimension is equal to it.
