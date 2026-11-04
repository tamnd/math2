---
tag: WZF5TT78JV
kind: proof
name: Proof of the rule of Sarrus
msc: [15A15]
proves: 0H8SZFFDXJ
uses: [016PE4VZ8Q, 0FWVRHBRWM, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants
    locator: Formal statement and proof
---

## Proof

1. Write the matrix as $A = (a_{ij})$. Its first row is $a, b, c$, its second row is $d, e, f$ and its third row is $g, h, i$.
2. By the [[Leibniz formula|016PE4VZ8Q]], $\det A = \sum_{\sigma \in S_3} \sgn(\sigma)\, a_{1, \sigma(1)} a_{2, \sigma(2)} a_{3, \sigma(3)}$.
3. The group $S_3$ has six elements. We list each $\sigma$ as $(\sigma(1), \sigma(2), \sigma(3))$.
4. The identity $(1, 2, 3)$ is a product of zero [[transpositions|0FWVRHBRWM]]. By the [[definition of the sign|0SK90238BH]], its sign is $1$, and its term is $aei$.
5. The permutation $(2, 3, 1)$ equals $(1\,3)(1\,2)$, a product of two transpositions. Its sign is $1$, and its term is $a_{12} a_{23} a_{31} = bfg$.
6. The permutation $(3, 1, 2)$ equals $(1\,2)(1\,3)$, a product of two transpositions. Its sign is $1$, and its term is $a_{13} a_{21} a_{32} = cdh$.
7. The permutation $(3, 2, 1)$ is the transposition $(1\,3)$. Its sign is $-1$, and its term is $-a_{13} a_{22} a_{31} = -ceg$.
8. The permutation $(2, 1, 3)$ is the transposition $(1\,2)$. Its sign is $-1$, and its term is $-a_{12} a_{21} a_{33} = -bdi$.
9. The permutation $(1, 3, 2)$ is the transposition $(2\,3)$. Its sign is $-1$, and its term is $-a_{11} a_{23} a_{32} = -afh$.
10. Adding the six terms gives $\det A = aei + bfg + cdh - ceg - bdi - afh$.

## Idea

For $n = 3$ the Leibniz formula has $3! = 6$ terms. The identity and the two cyclic shifts are even and give the three products along the down-right diagonals. The three transpositions are odd and give the other three products with a minus sign.
