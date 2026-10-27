---
tag: 0K7TD9BV2D
kind: definition
name: Idempotent matrix
msc: [15A99]
defines: 0KCE8CG86P
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: lead section
inventory: [DMB0JAP9ZR]
---

## Definition

Let $R$ be a ring and let $P$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $P$ is *idempotent* when $P^2 = P$.

## Remarks

The matrices $0$, $I_n$ and $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ are idempotent.
Over a field, an idempotent matrix is the matrix of a [[projection|033DA1WE8Y]] onto its image along its kernel.
If $P$ is idempotent, then so is $I - P$.
Over a field, the eigenvalues of an idempotent matrix are in $\{0, 1\}$, and its rank equals its trace in characteristic $0$.

## Explanations

### L1 human

An idempotent matrix does nothing new when we apply it twice.
A projection onto a line is the main example: once a point is on the line, projecting again keeps it there.
So $P^2 = P$.
