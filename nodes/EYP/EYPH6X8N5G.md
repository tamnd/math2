---
tag: EYPH6X8N5G
kind: example
name: A factorization PA = LU with one row exchange
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0RKG5YW66Y]
uses: [0RKG5YW66Y, 08SP3DF8NB, 3PPBWG0B96, 032Q9FB8MT]
sources:
  - book: isbn:9780321982384
    locator: Section 2.5
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: LU factorization with partial pivoting
---

## Example

A zero in the corner blocks the factorization $A = LU$, and one row exchange at the start repairs it.
Let
$$A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 7 & 9 \end{pmatrix}$$
over $\mathbb{Q}$.
The entry $a_{11}$ is $0$, so $\Delta_1 = 0$, and by the theorem on [[existence of the LU decomposition|3PPBWG0B96]] the invertible matrix $A$ has no factorization $A = LU$ with $L$ unit lower triangular.

1. Exchange rows 1 and 2. This is left multiplication by the [[permutation matrix|08SP3DF8NB]] $P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, and $PA = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 2 & 7 & 9 \end{pmatrix}$.
2. Row 2 already has $0$ in column 1, so $\ell_{21} = 0$.
3. The step $R_3 \to R_3 - 2R_1$ turns row 3 into $(0, 3, 7)$, so $\ell_{31} = 2$.
4. The step $R_3 \to R_3 - 3R_2$ turns row 3 into $(0, 0, 4)$, so $\ell_{32} = 3$.

So $PA = LU$ with
$$L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 3 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 4 \end{pmatrix}.$$
Check: rows 1 and 2 of $LU$ are $(1, 2, 1)$ and $(0, 1, 1)$, and row 3 is $2(1, 2, 1) + 3(0, 1, 1) + (0, 0, 4) = (2, 7, 9)$, which are the rows of $PA$.
Since $P^{-1} = P$, also $A = PLU$, and $\det A = \det P \det U = (-1) \cdot 4 = -4$.

## Remarks

### Why the exchange works

The leading principal minors of $PA$ are $1$, $\det \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = 1$ and $4$.
All are nonzero, so the existence theorem applies to $PA$, and by the [[uniqueness theorem|R424G32KFA]] the factors $L$ and $U$ are the only ones for this $P$.

### Watch out

The factorization depends on the choice of $P$.
Exchanging rows 1 and 3 instead gives a matrix with corner minors $2$ and $2 \cdot 2 - 7 \cdot 1 = -3$, so it also has an LU decomposition, with other factors.
Numerical programs choose the row with the largest entry in the pivot column; this partial pivoting belongs to numerical analysis.

### Try it

Factor $PA = LU$ for $A = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix}$ with $P$ the exchange of rows 1 and 2.
Answer: $PA$ has rows $(1, 1, 1)$, $(0, 1, 2)$ and $(1, 2, 4)$.
The steps $R_3 \to R_3 - R_1$ and $R_3 \to R_3 - R_2$ give
$$L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}.$$
Check: row 3 of $LU$ is $(1, 1, 1) + (0, 1, 2) + (0, 0, 1) = (1, 2, 4)$, and $\det A = -\det U = -1$.

## Explanations

### L1 human

If a pivot is zero, swap in a lower row first.
Do all the swaps at the start, as a permutation matrix $P$, and then eliminate as usual.
The result is $PA = LU$.

### L2 human

The determinant gives a useful check on the work.
Expansion of $\det A$ along the first column gives $-1 \cdot (1 \cdot 9 - 1 \cdot 7) + 2 \cdot (1 \cdot 1 - 1 \cdot 2) = -2 - 2 = -4$.
This agrees with $\det P \det U = -4$ from the factorization.
A trap: when you write $A = PLU$, remember that $P$ appears on the other side, and it is $P^{-1}$ in general; here $P^{-1} = P$ because $P$ is a single exchange.
