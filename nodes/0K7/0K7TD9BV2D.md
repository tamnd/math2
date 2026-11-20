---
tag: 0K7TD9BV2D
kind: definition
name: Idempotent matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: 0KCE8CG86P
uses: [0CP7YY6NAG, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: lead section
inventory: [DMB0JAP9ZR]
---

## Definition

Let $R$ be a ring and let $P$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The matrix $P$ is *idempotent* when $P^2 = P$, where $P^2 = PP$ is the [[matrix product|076JGP6R3T]].

## Notation

- In Mathlib, `IsIdempotentElem P` means `P * P = P`, for an element of any semigroup.

## Remarks

- The matrices $0$, $I_n$ and $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ are idempotent.
- Over a field, an idempotent matrix is the matrix of a [[projection|033DA1WE8Y]] onto its image along its kernel.
- If $P$ is idempotent, then so is $I - P$.
- Over a field, the eigenvalues of an idempotent matrix are in $\{0, 1\}$, and its rank equals its trace in characteristic $0$.

## Explanations

### L1 human

An idempotent matrix does nothing new when we apply it twice.

### L2 human

Over a field, the only idempotent scalars are $0$ and $1$.
Matrices have many more idempotents, one for each way to split the space into an image and a kernel.
