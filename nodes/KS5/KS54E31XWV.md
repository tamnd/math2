---
tag: KS54E31XWV
kind: proof
name: Proof of the determinant of the inverse
msc: [15A15]
proves: 0783S9D0ZH
uses: [0TWTS88TWN, 04CPJ6AF00, 0Z4BWARC38, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Other properties
---

## Proof

1. Since $A$ is [[invertible|0TWTS88TWN]], there is an $n \times n$ matrix $A^{-1}$ with $A A^{-1} = A^{-1} A = I_n$.
2. By the [[product rule|04CPJ6AF00]], $\det A \cdot \det(A^{-1}) = \det(A A^{-1}) = \det I_n$.
3. By the [[determinant of the identity|0Z4BWARC38]], $\det I_n = 1$. So $\det A \cdot \det(A^{-1}) = 1$.
4. Since $K$ is commutative, also $\det(A^{-1}) \cdot \det A = 1$.
5. By the definition of a [[unit|019NFGFPR5]], steps 3 and 4 show that $\det A$ is a unit of $K$ with inverse $\det(A^{-1})$.
6. So $\det(A^{-1}) = (\det A)^{-1}$.

## Idea

The determinant turns products of matrices into products of ring elements and sends $I_n$ to $1$. So the equation $A A^{-1} = I_n$ becomes $\det A \cdot \det(A^{-1}) = 1$.
