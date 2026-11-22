---
tag: 9HYGNPKP1G
kind: proof
name: Proof of the rules for inverse matrices
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
proves: 2ZH4X4Q99D
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0TWTS88TWN, FMCX4D7RD4, 0S4WTRE9GG, 09GK5PS824, 06DW9BAWB1, 073E4XC016]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Proof

In each part we name a candidate $Y$ for the inverse of a matrix $X$ and check $XY = YX = I_n$.
By the [[definition of the inverse|0TWTS88TWN]] and the [[uniqueness of the inverse|FMCX4D7RD4]], $Y$ is then $X^{-1}$.

**Part 1.**

1. By the definition, $A^{-1} A = I_n$ and $A A^{-1} = I_n$.
2. Read with $X = A^{-1}$ and $Y = A$, these two equations say $XY = I_n$ and $YX = I_n$.
3. So $A^{-1}$ is invertible and $(A^{-1})^{-1} = A$.

**Part 2.**

4. The [[transpose of a product|09GK5PS824]] reverses the order: $(XY)^{\mathsf{T}} = Y^{\mathsf{T}} X^{\mathsf{T}}$ for matrices of matching sizes.
5. By step 4, $A^{\mathsf{T}} (A^{-1})^{\mathsf{T}} = (A^{-1} A)^{\mathsf{T}} = I_n^{\mathsf{T}} = I_n$, because the [[identity matrix|06DW9BAWB1]] is symmetric.
6. By step 4 again, $(A^{-1})^{\mathsf{T}} A^{\mathsf{T}} = (A A^{-1})^{\mathsf{T}} = I_n^{\mathsf{T}} = I_n$.
7. So $A^{\mathsf{T}}$ is invertible and $(A^{\mathsf{T}})^{-1} = (A^{-1})^{\mathsf{T}}$.

**Part 3.**

8. For $c, d \in R$ we have $(cX)(dY) = (cd)(XY)$, because each entry of the product is a sum of terms $c x_{ij} \, d y_{jk}$ and $R$ is commutative.
9. By step 8, $(cA)(c^{-1} A^{-1}) = (c c^{-1})(A A^{-1}) = 1 \cdot I_n = I_n$.
10. By step 8, $(c^{-1} A^{-1})(cA) = (c^{-1} c)(A^{-1} A) = I_n$.
11. So $cA$ is invertible and $(cA)^{-1} = c^{-1} A^{-1}$.

**Part 4.** We use [[induction|0ASJVEFA9J]] on $k$.

12. Base case $k = 0$: $A^0 = I_n$ and $(A^{-1})^0 = I_n$, and $I_n I_n = I_n$, so $(A^0)^{-1} = (A^{-1})^0$.
13. Induction step: assume that $A^k$ is invertible with $(A^k)^{-1} = (A^{-1})^k$.
14. Then $A^{k+1} = A^k A$ is a product of two invertible matrices, by step 13 and the hypothesis on $A$.
15. By the [[inverse of a product|0S4WTRE9GG]], $A^{k+1}$ is invertible and $(A^{k+1})^{-1} = A^{-1} (A^k)^{-1}$.
16. By step 13 and [[associativity|073E4XC016]], $A^{-1} (A^k)^{-1} = A^{-1} (A^{-1})^k = (A^{-1})^{k+1}$.
17. This is the statement for $k + 1$, and the induction is complete.

## Idea

Every rule comes with its own candidate, so nothing has to be solved.
We only multiply the matrix by the candidate on both sides and watch the identity appear.
The transpose rule works because the transpose reverses products, just as the inverse does, so the two reversals fit together.

## Variants

Part 4 also follows from the inverse of a product applied to $k$ equal factors: $(A \cdots A)^{-1} = A^{-1} \cdots A^{-1}$, with the order reversed, which makes no difference here because all factors are equal.
Over a field, one product in each part is enough, by the theorem on [[one-sided inverses of square matrices|0753Y2X5K6]], but the two-sided check is just as short.
