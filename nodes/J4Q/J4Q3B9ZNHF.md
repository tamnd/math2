---
tag: J4Q3B9ZNHF
kind: example
name: Two matrices with the same rank, trace, determinant and characteristic and minimal polynomials that are not similar
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug2
not_instance_of:
  - target: 0E89HQATM8
    note: the 4 x 4 matrices J_2(1) + J_2(1) and J_2(1) + I_2 (block diagonal) share rank 4, trace 4, determinant 1, characteristic polynomial (x - 1)^4 and minimal polynomial (x - 1)^2, but A - I has rank 2 and B - I has rank 1, so they are not similar
illustrates: [191HBJ7PVZ]
uses: [191HBJ7PVZ, 027KDW2K72, 0EWQEYRVA8, 07PTPSZPME, 0C3CFHDN6R, 039HF58KQ5, 0V58FPM3EQ, 0VTAD25A3G, 0PBFS92AJP]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: lead section
---

## Example

The five standard similarity invariants can all agree for two matrices that are not similar, and a sixth invariant tells them apart.
Let $F$ be a field and let $J_2(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ be the [[Jordan block|0PBFS92AJP]] of size $2$ with eigenvalue $1$.
Consider the block diagonal $4 \times 4$ matrices $A = J_2(1) \oplus J_2(1)$ and $B = J_2(1) \oplus I_2$:
$$A = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
They differ only in the entry $(3, 4)$.
We write $E_{ij}$ for the matrix with $1$ in position $(i, j)$ and $0$ elsewhere, so that $E_{ij}E_{kl} = E_{il}$ when $j = k$ and $E_{ij}E_{kl} = 0$ otherwise.

1. [[Determinant|0C3CFHDN6R]].
   Both matrices are upper triangular, so each determinant is the product of the diagonal entries, $1 \cdot 1 \cdot 1 \cdot 1 = 1$.
2. [[Rank|0EWQEYRVA8]].
   Both determinants are nonzero, so both matrices are invertible and both ranks are $4$.
3. [[Trace|07PTPSZPME]].
   Both traces are $1 + 1 + 1 + 1 = 4$.
4. [[Characteristic polynomial|039HF58KQ5]].
   The matrices $xI - A$ and $xI - B$ are upper triangular with all diagonal entries $x - 1$, so both characteristic polynomials are $(x - 1)^4$.
5. The nilpotent parts are $A - I = E_{12} + E_{34}$ and $B - I = E_{12}$.
6. We square $A - I$ term by term:
   $$(A - I)^2 = E_{12}E_{12} + E_{12}E_{34} + E_{34}E_{12} + E_{34}E_{34}.$$
   In each product the two inner indices differ ($2 \ne 1$, $2 \ne 3$, $4 \ne 1$, $4 \ne 3$), so every term is $0$ and $(A - I)^2 = 0$.
7. In the same way $(B - I)^2 = E_{12}E_{12} = 0$, since $2 \ne 1$.
8. [[Minimal polynomial|0V58FPM3EQ]] of $A$.
   By step 6, $(x - 1)^2$ annihilates $A$, so the minimal polynomial [[divides|0VTAD25A3G]] $(x - 1)^2$ and is $1$, $x - 1$ or $(x - 1)^2$.
   It is not $1$, since $I \ne 0$, and it is not $x - 1$, since $A - I \ne 0$, so $m_A = (x - 1)^2$.
9. The same argument with step 7 and $B - I = E_{12} \ne 0$ gives $m_B = (x - 1)^2$.
   So $A$ and $B$ share the rank, trace, determinant and characteristic and minimal polynomials.
10. The sixth invariant.
    The matrix $A - I$ has the two independent nonzero rows $(0, 1, 0, 0)$ and $(0, 0, 0, 1)$, so $\operatorname{rank}(A - I) = 2$.
    The matrix $B - I$ has the single nonzero row $(0, 1, 0, 0)$, so $\operatorname{rank}(B - I) = 1$.
11. If $B$ were [[similar|027KDW2K72]] to $A$, then part 6 of the [[theorem on similarity invariants|191HBJ7PVZ]] with $q = x - 1$ would give $\operatorname{rank}(B - I) = \operatorname{rank}(A - I)$, that is, $1 = 2$.
    So $A$ and $B$ are not similar.

## Remarks

The rank of $A - I$ counts the Jordan blocks.
The number $4 - \operatorname{rank}(A - I)$ is the dimension of the eigenspace $\ker(A - I)$, the geometric multiplicity of the eigenvalue $1$, and it equals the number of Jordan blocks for that eigenvalue.
So $A$ has $4 - 2 = 2$ blocks, both of size $2$, and $B$ has $4 - 1 = 3$ blocks, of sizes $2$, $1$ and $1$.

The size $4$ is the smallest possible for such an example.
In sizes up to $3$, the characteristic and minimal polynomials together decide similarity.
The example works over every field, since only the entries $0$ and $1$ appear.
If we replace $J_2(1) \oplus I_2$ by $J_3(1) \oplus (1)$, the minimal polynomial becomes $(x - 1)^3$, and then the minimal polynomials already differ.

## Explanations

### L1 human

The five standard invariants can agree for two matrices that are not similar.
Both matrices leave some directions fixed, but $B$ fixes a $3$-dimensional space of vectors and $A$ fixes only a $2$-dimensional space.
A change of basis cannot change how many independent vectors a map fixes, so the two matrices are not similar.

### L2 human

Both matrices have only the eigenvalue $1$, and both have largest Jordan block of size $2$.
The characteristic polynomial records the total size $4$, and the minimal polynomial records the largest block size $2$.
Neither records the number of blocks, which is $2$ for $A$ and $3$ for $B$, and the rank of $A - I$ detects exactly that number.
Watch out: to show that two matrices are similar, a list of matching invariants is not enough unless the list is complete, such as the invariant factors or the Jordan form.

### L3 human

The similarity class of a matrix over a field is determined by its invariant factors.
For $A$ they are $(x - 1)^2, (x - 1)^2$, and for $B$ they are $x - 1, x - 1, (x - 1)^2$.
The minimal polynomial is only the last invariant factor, and the characteristic polynomial is only their product, so neither sees the whole list.
