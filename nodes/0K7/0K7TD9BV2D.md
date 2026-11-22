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

An idempotent matrix is a square matrix that equals its own square.
Let $R$ be a ring and let $P$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
We call $P$ *idempotent* when $P^2 = P$, where $P^2 = PP$ is the [[matrix product|076JGP6R3T]].

## Notation

Some books say *projection matrix*, and some keep that name for symmetric idempotents.
In Mathlib, `IsIdempotentElem P` means `P * P = P`, for an element of any semigroup.

## Remarks

The matrix must be square so that $PP$ is defined and has the same size as $P$, which the equation $P^2 = P$ needs.
There is only one condition, and it controls all powers: $P^3 = P^2 P = P P = P$, and in the same way $P^k = P$ for every $k \ge 1$.

For example, $P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ is idempotent, and so are $0$ and $I_n$.
In contrast, $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is not, because its square is $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
Among numbers, only $0$ and $1$ satisfy $x^2 = x$, but matrices have many more idempotents.
Over a field there is one for each way to write the space as a direct sum of an image and a kernel, as the concept page on [[idempotent matrices|0KCE8CG86P]] explains.

## Explanations

### L1 human

An idempotent matrix does nothing new when we apply it twice.
Erasing the second coordinate of a point is an example: once it is erased, erasing it again changes nothing.

### L2 human

To test the definition, compute $P^2$ and compare it with $P$ entry by entry.
For $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ the square is $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, so $P$ is idempotent.
Watch out: from $P^2 = P$ we may not cancel a factor $P$ to get $P = I$, because $P$ is usually not invertible.
