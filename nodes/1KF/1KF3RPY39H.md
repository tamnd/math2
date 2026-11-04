---
tag: 1KF3RPY39H
kind: proof
name: Proof that Gram matrices are positive semidefinite
msc: [15B57, 15A63]
proves: 0AM050KCAW
uses: [0880F9EQCP, 0QQCG3JWJ4, 0EKZCX4K3P, 0EX045E2BP, 09GK5PS824, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Decomposition
---

## Proof

1. Let $B$ be an $m \times n$ complex matrix, and let $A = B^* B$, where $^*$ is the [[conjugate transpose|0EX045E2BP]]. Then $A$ is $n \times n$.
2. For matrices $X$ and $Y$ with $XY$ defined, $(XY)^* = Y^* X^*$. This is the [[transpose of a product|09GK5PS824]] with all entries conjugated.
3. By step 2, $A^* = B^* (B^*)^* = B^* B = A$. So $A$ is [[Hermitian|0EKZCX4K3P]].
4. For a vector $y \in \C^m$, we have $y^* y = \sum_{i=1}^m \abs{y_i}^2 \ge 0$, with equality only if $y = 0$.
5. Let $x \in \C^n$. By step 2, $x^* A x = x^* B^* B x = (Bx)^* (Bx)$.
6. By steps 4 and 5 with $y = Bx$, we get $x^* A x \ge 0$. So $A$ is [[positive semidefinite|0880F9EQCP]].
7. Let $b_1, \dots, b_n$ be the columns of $B$. Then $Bx = x_1 b_1 + \cdots + x_n b_n$.
8. By steps 4 and 5, $x^* A x = 0$ holds if and only if $Bx = 0$.
9. Suppose the columns are [[linearly independent|0EVHJFTG9Z]], and let $x \ne 0$. By step 7, $Bx \ne 0$. By step 8, $x^* A x > 0$. So $A$ is [[positive definite|0QQCG3JWJ4]].
10. Conversely, suppose the columns are linearly dependent. Then there is $x \ne 0$ with $x_1 b_1 + \cdots + x_n b_n = 0$, that is, $Bx = 0$.
11. By step 8, $x^* A x = 0$ for this $x \ne 0$. So $A$ is not positive definite.
12. By steps 9 to 11, $B^* B$ is positive definite if and only if the columns of $B$ are linearly independent.

## Idea

The number $x^* B^* B x$ is the squared length of the vector $Bx$. A squared length is never negative, and it is zero only for the zero vector. The vector $Bx$ is a combination of the columns of $B$, so it vanishes for some $x \ne 0$ exactly when the columns are dependent.
