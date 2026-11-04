---
tag: BTTJMY7FJ0
kind: proof
name: Proof of Euler's four-square identity by expansion
msc: ["11E25"]
proves: 08WTN6SCQ6
uses: [0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_four-square_identity
---

## Proof

We expand both sides, using the laws of a [[commutative ring|0GYGHKX834]].

1. Call the four expressions on the right $z_1, z_2, z_3, z_4$, in the order written. Each $z_k$ is a sum of four terms $\pm a_i b_j$.
2. The index pairs $(i, j)$ in the terms are: in $z_1$, $(1,1), (2,2), (3,3), (4,4)$; in $z_2$, $(1,2), (2,1), (3,4), (4,3)$; in $z_3$, $(1,3), (2,4), (3,1), (4,2)$; in $z_4$, $(1,4), (2,3), (3,2), (4,1)$.
3. So each of the $16$ pairs $(i, j)$ occurs in exactly one $z_k$, and in exactly one term.
4. For $t_1, \dots, t_4$ in a commutative ring, $(t_1 + t_2 + t_3 + t_4)^2 = \sum_i t_i^2 + 2\sum_{i < l} t_i t_l$.
5. By steps 3 and 4, the squares of the terms add up to $\sum_{i, j} a_i^2 b_j^2$. This is the left side $(\sum_i a_i^2)(\sum_j b_j^2)$.
6. It remains to show that the cross terms $2 t_i t_l$ cancel. Each cross term is $\pm 2\, a_i a_l b_j b_r$ with $i \ne l$ and $j \ne r$. We list the coefficients of each such monomial, without the factor $2$.
7. $a_1a_2b_1b_2$: $-1$ from $z_1$ and $+1$ from $z_2$. $a_1a_2b_3b_4$: $-1$ from $z_3$ and $+1$ from $z_4$.
8. $a_1a_3b_1b_3$: $-1$ from $z_1$ and $+1$ from $z_3$. $a_1a_3b_2b_4$: $+1$ from $z_2$ and $-1$ from $z_4$.
9. $a_1a_4b_1b_4$: $-1$ from $z_1$ and $+1$ from $z_4$. $a_1a_4b_2b_3$: $-1$ from $z_2$ and $+1$ from $z_3$.
10. $a_2a_3b_2b_3$: $+1$ from $z_1$ and $-1$ from $z_4$. $a_2a_3b_1b_4$: $+1$ from $z_2$ and $-1$ from $z_3$.
11. $a_2a_4b_2b_4$: $+1$ from $z_1$ and $-1$ from $z_3$. $a_2a_4b_1b_3$: $-1$ from $z_2$ and $+1$ from $z_4$.
12. $a_3a_4b_3b_4$: $+1$ from $z_1$ and $-1$ from $z_2$. $a_3a_4b_1b_2$: $+1$ from $z_3$ and $-1$ from $z_4$.
13. Each $z_k$ has $6$ cross terms, so there are $24$ in all. Steps 7 to 12 account for all $24$, in $12$ pairs with opposite signs.
14. For example, in $z_1$ the terms $a_1b_1$ and $-a_2b_2$ give $-2a_1a_2b_1b_2$. In $z_2$ the terms $a_1b_2$ and $a_2b_1$ give $+2a_1a_2b_1b_2$. The other lines are read off in the same way.
15. So all cross terms cancel, and $z_1^2 + z_2^2 + z_3^2 + z_4^2$ equals the left side.

## Idea

Each product $a_i b_j$ appears in exactly one of the four squares, so the squared terms give the product of the two sums. The signs are arranged, as in the multiplication of quaternions, so that the cross terms cancel in pairs.
