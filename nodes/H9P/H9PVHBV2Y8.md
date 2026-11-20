---
tag: H9PVHBV2Y8
kind: proof
name: Proof of the formula for the inverse of a product
msc: [15A09]
topics: [P8J6QR66TJ]
audience: ug1
proves: 0S4WTRE9GG
methods: [0NTF6DMVAP, 0ASJVEFA9J, TFQ1845T84]
uses: [0TWTS88TWN, ~139b320d, 076JGP6R3T, 073E4XC016, 06DW9BAWB1, 0753Y2X5K6]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Proof

**Part 1.**

1. Since $A$ and $B$ are [[invertible|0TWTS88TWN]], they have inverses $A^{-1}$ and $B^{-1}$. These satisfy $AA^{-1} = A^{-1}A = I_n$ and $BB^{-1} = B^{-1}B = I_n$, where $I_n$ is the [[identity matrix|06DW9BAWB1]].
2. Let $C = B^{-1} A^{-1}$. It is an $n \times n$ matrix by the definition of the [[product|076JGP6R3T]].
3. By [[associativity|073E4XC016]], $(AB)C = A(BB^{-1})A^{-1} = A I_n A^{-1}$.
4. Since $A I_n = A$, step 3 gives $(AB)C = AA^{-1} = I_n$.
5. By associativity, $C(AB) = B^{-1}(A^{-1}A)B = B^{-1} I_n B = B^{-1} B = I_n$.
6. By steps 4 and 5, $(AB)C = C(AB) = I_n$. So $AB$ is invertible by definition.
7. The inverse is unique, by the [[uniqueness of the inverse|~139b320d]]. So $(AB)^{-1} = C = B^{-1} A^{-1}$.

**Part 2.** We use induction on $k$.

8. For $k = 1$ the claim is $A_1^{-1} = A_1^{-1}$.
9. Assume the claim for $k$ factors, and let $P = A_1 \cdots A_k$. By this assumption, $P$ is invertible with $P^{-1} = A_k^{-1} \cdots A_1^{-1}$.
10. By part 1 applied to $P$ and $A_{k+1}$, the product $P A_{k+1} = A_1 \cdots A_{k+1}$ is invertible with inverse $A_{k+1}^{-1} P^{-1} = A_{k+1}^{-1} A_k^{-1} \cdots A_1^{-1}$.

**Part 3.** Now the entries lie in a field $F$.

11. If each $A_i$ is invertible, then the product is invertible, by part 2.
12. Conversely, assume that $P = A_1 \cdots A_k$ is invertible, and fix $i$. Write $P = X A_i Y$ with $X = A_1 \cdots A_{i-1}$ and $Y = A_{i+1} \cdots A_k$, where an empty product is $I_n$.
13. By [[associativity|073E4XC016]], $X (A_i Y P^{-1}) = P P^{-1} = I_n$. So $X$ has a right inverse.
14. A square matrix over a field with a one-sided inverse is invertible, by [[one-sided inverses of square matrices|0753Y2X5K6]]. So $X$ is invertible.
15. By associativity, $(P^{-1} X A_i) Y = P^{-1} P = I_n$. So $Y$ has a left inverse, and $Y$ is invertible by the same theorem.
16. Then $X^{-1} P Y^{-1} = X^{-1} X A_i Y Y^{-1} = A_i$.
17. So $A_i$ is a product of three invertible matrices, and $A_i$ is invertible by part 2.
18. Since $i$ was arbitrary, each factor is invertible.

## Idea

To undo "first $B$, then $A$", undo $A$ first and then undo $B$.
Associativity lets the middle factors $B B^{-1}$ or $A^{-1} A$ cancel to the identity.
For the converse over a field, an invertible product gives a one-sided inverse to each part, and for square matrices one-sided inverses are two-sided.

## Variants

Over a field, part 3 also follows from the determinant: $\det(A_1 \cdots A_k) = \det A_1 \cdots \det A_k$ by [[multiplicativity|04CPJ6AF00]].
A product of field elements is nonzero if and only if each factor is nonzero.
