---
tag: H9PVHBV2Y8
kind: proof
name: Proof of the formula for the inverse of a product
msc: [15A09]
topics: [P8J6QR66TJ]
audience: ug1
proves: 0S4WTRE9GG
methods: [0NTF6DMVAP, 0ASJVEFA9J, TFQ1845T84]
uses: [0TWTS88TWN, FMCX4D7RD4, 076JGP6R3T, 073E4XC016, 06DW9BAWB1, 0753Y2X5K6]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Proof

We check the candidate $B^{-1}A^{-1}$ by direct multiplication, extend to $k$ factors by induction, and get the converse over a field from one-sided inverses.

**Part 1.**

1. Since $A$ and $B$ are [[invertible|0TWTS88TWN]], we have $AA^{-1} = A^{-1}A = I_n$ and $BB^{-1} = B^{-1}B = I_n$, where $I_n$ is the [[identity matrix|06DW9BAWB1]].
2. Let $C = B^{-1} A^{-1}$, an $n \times n$ matrix by the definition of the [[product|076JGP6R3T]].
3. By [[associativity|073E4XC016]] and step 1, $(AB)C = A(BB^{-1})A^{-1} = A I_n A^{-1} = AA^{-1} = I_n$.
4. By associativity and step 1, $C(AB) = B^{-1}(A^{-1}A)B = B^{-1} I_n B = B^{-1} B = I_n$.
5. By steps 3 and 4, $AB$ is invertible, and by the [[uniqueness of the inverse|FMCX4D7RD4]], $(AB)^{-1} = C = B^{-1} A^{-1}$.

**Part 2.** We use induction on $k$.

6. For $k = 1$ the claim reads $A_1^{-1} = A_1^{-1}$, which holds.
7. Assume the claim for $k$ factors, and let $P = A_1 \cdots A_k$, so that $P$ is invertible with $P^{-1} = A_k^{-1} \cdots A_1^{-1}$.
8. By part 1 applied to $P$ and $A_{k+1}$, the product $P A_{k+1} = A_1 \cdots A_{k+1}$ is invertible with inverse $A_{k+1}^{-1} P^{-1} = A_{k+1}^{-1} A_k^{-1} \cdots A_1^{-1}$.

**Part 3.** Now the entries lie in a field $F$.

9. If each $A_i$ is invertible, then the product is invertible, by part 2.
10. Conversely, assume that $P = A_1 \cdots A_k$ is invertible, and fix $i$. Write $P = X A_i Y$ with $X = A_1 \cdots A_{i-1}$ and $Y = A_{i+1} \cdots A_k$, where an empty product is $I_n$.
11. By associativity, $X (A_i Y P^{-1}) = P P^{-1} = I_n$, so $X$ has a right inverse.
12. A square matrix over a field with a one-sided inverse is invertible, by [[one-sided inverses of square matrices|0753Y2X5K6]], so $X$ is invertible.
13. By associativity, $(P^{-1} X A_i) Y = P^{-1} P = I_n$, so $Y$ has a left inverse and is invertible by the same theorem.
14. Then $X^{-1} P Y^{-1} = X^{-1} X A_i Y Y^{-1} = A_i$, so $A_i$ is a product of three invertible matrices.
15. By part 2, $A_i$ is invertible, and since $i$ was arbitrary, every factor is invertible.

## Idea

To undo "first $B$, then $A$", undo $A$ first and then undo $B$.
Associativity lets the middle pair $BB^{-1}$ or $A^{-1}A$ collapse to the identity, and then the outer pair collapses too.
For the converse, an invertible product hands each outer block a one-sided inverse.
For square matrices a one-sided inverse is two-sided, and then the middle factor is a product of invertible matrices.

## Variants

Over a field, part 3 also follows from the determinant: $\det(A_1 \cdots A_k) = \det A_1 \cdots \det A_k$ by [[multiplicativity|04CPJ6AF00]].
A product of field elements is nonzero exactly when each factor is nonzero, and a matrix over a field is invertible exactly when its determinant is nonzero.
