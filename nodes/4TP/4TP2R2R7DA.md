---
tag: 4TP2R2R7DA
kind: definition
name: Loewner order
msc: [15B57, 47A63]
defines: 9G9S92T1VJ
uses: [0P17NGQQMQ, 01MMVW8CKC, 0KX66CZMBB, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Loewner_order
---

## Definition

Let $n \ge 1$ and let $A$ and $B$ be $n \times n$ [[Hermitian matrices|0P17NGQQMQ]].
Then $A \succeq B$ in the *Loewner order* if $A - B$ is [[positive semidefinite|01MMVW8CKC]].
Also $A \succ B$ if $A - B$ is [[positive definite|0KX66CZMBB]].

## Remarks

The relation $\succeq$ is a [[partial order|0QV2JS9RJ3]].
It is transitive because sums of positive semidefinite matrices are positive semidefinite.
It is antisymmetric because a matrix that is both positive semidefinite and negative semidefinite is $0$.
Example: $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \succeq I$, because the difference $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has eigenvalues $2$ and $0$.
Non-example: $\operatorname{diag}(1, 0) \not\succeq \operatorname{diag}(0, 1)$, because the difference $\operatorname{diag}(1, -1)$ has the eigenvalue $-1$; the converse fails too, so the order is not total.
The order does not respect squares: for $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $A \succeq B$, but $A^2 - B^2 = \begin{pmatrix} 4 & 3 \\ 3 & 2 \end{pmatrix}$ has determinant $-1$.
On the other hand, $A \succeq B \succeq 0$ implies $A^{1/2} \succeq B^{1/2}$.
