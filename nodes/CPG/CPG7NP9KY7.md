---
tag: CPG7NP9KY7
kind: proof
name: Proof of the inverse in terms of the adjugate
msc: [15A09]
proves: 0ENVM493VK
uses: [0528HKWZ1Z, 0TWTS88TWN, 0GMPYM0NSR, 076JGP6R3T, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Important consequence
---

## Proof

We divide the identity for the adjugate by the unit $\det A$.

1. Let $A$ be an $n \times n$ matrix over $K$ with $n \ge 2$. Let $d = \det A$, and assume that $d$ is a [[unit|019NFGFPR5]] of $K$.
2. Let $B = d^{-1} \operatorname{adj}(A)$, where $\operatorname{adj}(A)$ is the [[adjugate|0GMPYM0NSR]] of $A$.
3. By the definition of the [[matrix product|076JGP6R3T]] and the commutativity of $K$, a scalar factor can be moved out of a product: $A (c M) = c (A M)$ and $(c M) A = c (M A)$.
4. So $A B = d^{-1} (A \operatorname{adj}(A))$ and $B A = d^{-1} (\operatorname{adj}(A) A)$.
5. By the [[product of a matrix and its adjugate|0528HKWZ1Z]], $A \operatorname{adj}(A) = \operatorname{adj}(A) A = d I_n$.
6. By steps 4 and 5, $A B = d^{-1} d I_n = I_n$ and $B A = I_n$.
7. By the definition of an [[invertible matrix|0TWTS88TWN]], $A$ is invertible, and its inverse is unique. So $A^{-1} = B = (\det A)^{-1} \operatorname{adj}(A)$.

## Idea

The adjugate already inverts $A$ up to the scalar factor $\det A$. When this scalar has an inverse in $K$, dividing by it gives the inverse matrix on both sides.
