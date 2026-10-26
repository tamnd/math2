---
tag: ~d5c71ccc
kind: definition
name: Idempotent matrix
msc: [15A99]
defines: ~84784214
uses: [~c4555ee3]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: lead section
---

## Definition

Let $R$ be a ring and let $P$ be an $n \times n$ [[square matrix|~92565f6b]] over $R$.
The matrix $P$ is *idempotent* when $P^2 = P$.

## Remarks

The matrices $0$, $I_n$ and $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ are idempotent.
Over a field, an idempotent matrix is the matrix of a [[projection|~7de9f341]] onto its image along its kernel.
If $P$ is idempotent, then so is $I - P$.
Over a field, the eigenvalues of an idempotent matrix are in $\{0, 1\}$, and its rank equals its trace in characteristic $0$.

## Explanations

### L1 human

An idempotent matrix does nothing new when we apply it twice.
A projection onto a line is the main example: once a point is on the line, projecting again keeps it there.
So $P^2 = P$.
