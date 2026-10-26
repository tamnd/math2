---
tag: 0AM050KCAW
kind: statement
role: proposition
name: Gram matrices are positive semidefinite
msc: [15B57, 15A63]
uses: [0880F9EQCP, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Decomposition
---

## Statement

Let $B$ be an $m \times n$ complex matrix.
Then the $n \times n$ matrix $B^* B$ is [[positive semidefinite|01MMVW8CKC]], where $B^*$ is the [[conjugate transpose|0DXKE10PHF]].
It is positive definite if and only if the columns of $B$ are linearly independent.

## Remarks

The proof: $x^* B^* B x = (Bx)^* (Bx) = \norm{Bx}^2 \ge 0$.
For a real matrix $B$, the same holds for $B^T B$.
Each [[Gram matrix|00SPJSDT3Z]] has this form, so Gram matrices are positive semidefinite.

## Explanations

### L1 human

Matrices of the form $B^T B$ can never give negative values of $x^T A x$.
The value is the squared length of $Bx$.
It is zero only when $Bx = 0$.
