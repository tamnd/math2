---
tag: KS54E31XWV
kind: proof
name: Proof of the determinant of the inverse
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0783S9D0ZH
methods: [0NTF6DMVAP]
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
5. By the definition of a [[unit|019NFGFPR5]], $\det A$ is a unit of $K$ with inverse $\det(A^{-1})$. This proves part 1.
6. Part 2. By the product rule, $\det(A^{-1} M A) = \det(A^{-1}) \det M \det A$.
7. Since $K$ is commutative, this equals $\det(A^{-1}) \det A \det M$.
8. By step 3, $\det(A^{-1}) \det A = 1$. So $\det(A^{-1} M A) = \det M$.

## Idea

The determinant turns products of matrices into products of ring elements and sends $I_n$ to $1$.
So the equation $A A^{-1} = I_n$ becomes $\det A \cdot \det(A^{-1}) = 1$.
In a conjugate $A^{-1} M A$ the two outer factors cancel after taking determinants.

## Variants

Over a field one can also read part 1 from the [[inverse via the adjugate|0ENVM493VK]]: $\det(\operatorname{adj} A / \det A) = (\det A)^{n-1} / (\det A)^{n}$.
This uses the identity $\det(\operatorname{adj} A) = (\det A)^{n-1}$, which itself rests on the product rule.
