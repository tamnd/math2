---
tag: P2NS0V36TH
kind: definition
name: Operator monotone function
msc: [47A63, 15A45, 26A48]
defines: N155BSJ2DN
uses: [0Q1D85B8G6, 0P17NGQQMQ, 9G9S92T1VJ, W7MPTRPXYD, 01MMVW8CKC, 0DGZBQWZWN, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_monotone_function
---

## Definition

Let $I \subseteq \R$ be an [[interval|0Q1D85B8G6]] and let $f \colon I \to \R$.
Let $A$ be an $n \times n$ [[Hermitian matrix|0P17NGQQMQ]] with all eigenvalues in $I$.
By the [[spectral theorem|0DGZBQWZWN]], $A = U \operatorname{diag}(\lambda_1, \dots, \lambda_n) U^*$ with $U$ unitary.
The [[matrix function|W7MPTRPXYD]] $f(A)$ is $U \operatorname{diag}(f(\lambda_1), \dots, f(\lambda_n)) U^*$; it does not depend on the choice of $U$.
For Hermitian matrices $A$ and $B$ of the same size, $A \le B$ in the [[Loewner order|9G9S92T1VJ]] means that $B - A$ is [[positive semidefinite|01MMVW8CKC]].
The function $f$ is *operator monotone* on $I$ if the following holds for every $n \ge 1$.
For all $n \times n$ Hermitian matrices $A$ and $B$ with eigenvalues in $I$, if $A \le B$, then $f(A) \le f(B)$.

## Remarks

For $n = 1$ the condition says that $f$ is nondecreasing, so an operator monotone function is a [[monotone function|0A7KV2WB7A]].
Example: $f(t) = -1/t$ on $(0, \infty)$.
If $0 < A \le B$, then $B^{-1/2} A B^{-1/2} \le I$, so its eigenvalues lie in $(0, 1]$, so $B^{1/2} A^{-1} B^{1/2} \ge I$, which gives $A^{-1} \ge B^{-1}$, that is, $-A^{-1} \le -B^{-1}$.
Non-example: $f(t) = t^2$ on $[0, \infty)$.
Take $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, both positive semidefinite, with $B - A = \operatorname{diag}(1, 0) \ge 0$.
Then $B^2 - A^2 = \begin{pmatrix} 3 & 1 \\ 1 & 0 \end{pmatrix}$ has determinant $-1$, so it has a negative eigenvalue and $A^2 \le B^2$ fails.
The same definition with self-adjoint operators on a Hilbert space gives the same class of functions.

## Explanations

### L1 human

The definition asks that $f$ keep the order of Hermitian matrices of all sizes, not only the order of numbers.
The size-two example with $t^2$ shows that this is a real restriction.
