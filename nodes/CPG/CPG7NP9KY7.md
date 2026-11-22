---
tag: CPG7NP9KY7
kind: proof
name: Proof of the inverse in terms of the adjugate
msc: ["15A09"]
topics: [DTBK11SR77]
audience: ug1
proves: 0ENVM493VK
methods: [0NTF6DMVAP]
uses: [0528HKWZ1Z, 0TWTS88TWN, 0GMPYM0NSR, 076JGP6R3T, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Important consequence
---

## Proof

We divide the adjugate identity by the unit $\det A$ and check that the result is a two-sided inverse.

1. Let $A$ be an $n \times n$ matrix over a commutative ring $K$ with $n \ge 1$.
   Let $d = \det A$, and assume that $d$ is a [[unit|019NFGFPR5]] of $K$, with inverse $d^{-1}$.
2. Let $B = d^{-1} \operatorname{adj}(A)$, where $\operatorname{adj}(A)$ is the [[adjugate|0GMPYM0NSR]] of $A$.
3. For a scalar $c \in K$ and matrices $M$ and $N$, the definition of the [[matrix product|076JGP6R3T]] gives $(MN)_{ik} = \sum_j m_{ij} n_{jk}$.
   Since $K$ is commutative, $m_{ij} (c\, n_{jk}) = c\, (m_{ij} n_{jk})$, so $M (cN) = c (MN)$, and in the same way $(cM) N = c (MN)$.
4. By step 3,
$$A B = d^{-1} \big(A \operatorname{adj}(A)\big), \qquad B A = d^{-1} \big(\operatorname{adj}(A) A\big).$$
5. By the [[adjugate identity|0528HKWZ1Z]], $A \operatorname{adj}(A) = \operatorname{adj}(A) A = d\, I_n$.
6. By steps 4 and 5, $A B = d^{-1} d\, I_n = I_n$, and in the same way $B A = I_n$.
7. By the definition of an [[invertible matrix|0TWTS88TWN]], $A$ is invertible with inverse $B$.
   The inverse is unique, since $AB' = I_n$ gives $B' = (BA) B' = B (A B') = B$.
   So $A^{-1} = B = (\det A)^{-1} \operatorname{adj}(A)$.

## Idea

The adjugate already inverts $A$ up to the scalar factor $\det A$, from both sides.
When this scalar has an inverse in $K$, multiplying by it turns the adjugate into the inverse matrix.

## Variants

Over a field, [[Gaussian elimination|0JVJ2WCXZH]] on $(A \mid I_n)$ gives another route to $A^{-1}$, and since the inverse is unique it gives the same matrix.
That route does not give the formula, though, and it does not work over rings such as $\mathbb{Z}$, where the pivots cannot always be divided by.
