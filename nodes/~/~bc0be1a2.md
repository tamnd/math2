---
tag: ~bc0be1a2
kind: proof
name: Proof of the rules for inverse matrices
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
proves: ~b26cc133
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0TWTS88TWN, ~139b320d, 0S4WTRE9GG, 09GK5PS824, 06DW9BAWB1, 073E4XC016]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Proof

In each part we exhibit a candidate $B$ with $XB = BX = I_n$ for the matrix $X$ in question.
By the [[uniqueness of the inverse|~139b320d]], $B$ is then the inverse $X^{-1}$.

**Part 1.**

1. By the [[definition of the inverse|0TWTS88TWN]], $A^{-1} A = I_n$ and $A A^{-1} = I_n$.
2. Read with $X = A^{-1}$ and $B = A$, these are the equations $XB = I_n$ and $BX = I_n$.
3. So $A^{-1}$ is invertible and $(A^{-1})^{-1} = A$.

**Part 2.**

4. The [[transpose of a product|09GK5PS824]] is $(XY)^{\mathsf{T}} = Y^{\mathsf{T}} X^{\mathsf{T}}$, for matrices of matching sizes.
5. By step 4, $A^{\mathsf{T}} (A^{-1})^{\mathsf{T}} = (A^{-1} A)^{\mathsf{T}} = I_n^{\mathsf{T}} = I_n$, because the [[identity matrix|06DW9BAWB1]] is symmetric.
6. By step 4, $(A^{-1})^{\mathsf{T}} A^{\mathsf{T}} = (A A^{-1})^{\mathsf{T}} = I_n^{\mathsf{T}} = I_n$.
7. So $A^{\mathsf{T}}$ is invertible and $(A^{\mathsf{T}})^{-1} = (A^{-1})^{\mathsf{T}}$.

**Part 3.**

8. Scalars commute with matrices: $(cX)(dY) = (cd)(XY)$ for $c, d \in R$, because $R$ is commutative.
9. By step 8, $(cA)(c^{-1} A^{-1}) = (c c^{-1})(A A^{-1}) = 1 \cdot I_n = I_n$.
10. By step 8, $(c^{-1} A^{-1})(cA) = (c^{-1} c)(A^{-1} A) = I_n$.
11. So $cA$ is invertible and $(cA)^{-1} = c^{-1} A^{-1}$.

**Part 4.** We use [[induction|0ASJVEFA9J]] on $k$.

12. Base case $k = 0$: $A^0 = I_n$ and $(A^{-1})^0 = I_n$, and $I_n I_n = I_n$. So $(A^0)^{-1} = (A^{-1})^0$.
13. Induction step: assume that $A^k$ is invertible with $(A^k)^{-1} = (A^{-1})^k$.
14. We have $A^{k+1} = A^k A$, a product of two invertible matrices, by step 13 and the hypothesis.
15. By the [[inverse of a product|0S4WTRE9GG]], $A^{k+1}$ is invertible and $(A^{k+1})^{-1} = A^{-1} (A^k)^{-1}$.
16. By step 13, $A^{-1} (A^k)^{-1} = A^{-1} (A^{-1})^k = (A^{-1})^{k+1}$, by [[associativity|073E4XC016]].
17. This proves the statement for $k + 1$, and the induction is complete.

## Idea

Each rule names a candidate inverse, and two multiplications check it.
The transpose rule works because the transpose reverses products, just as the inverse does.

## Variants

Part 4 also follows from part 1 of the inverse of a product applied to $k$ equal factors: $(A \cdots A)^{-1} = A^{-1} \cdots A^{-1}$.
