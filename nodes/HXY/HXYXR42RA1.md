---
tag: HXYXR42RA1
kind: example
name: A 2 × 2 matrix written in the basis of matrix units
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [A4HTT7JFD1]
uses: [4H93XF4RVH, 0V7ZD6P7RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Standard_basis
    locator: lead section
---

## Example

Let
$$A = \begin{pmatrix} 3 & -1 \\ 4 & 7 \end{pmatrix}$$
over $\mathbb{R}$.
We write $A$ as a combination of the four [[matrix units|4H93XF4RVH]] and see that they form a basis.

1. Scale each matrix unit by the entry in its place:
$$3E_{11} = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}, \quad -E_{12} = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix}, \quad 4E_{21} = \begin{pmatrix} 0 & 0 \\ 4 & 0 \end{pmatrix}, \quad 7E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 7 \end{pmatrix}.$$
2. Add the four matrices place by place; each place gets exactly one nonzero term:
$$3E_{11} - E_{12} + 4E_{21} + 7E_{22} = \begin{pmatrix} 3 & -1 \\ 4 & 7 \end{pmatrix} = A.$$
3. The same works for any matrix, so the four matrix units span the space of $2 \times 2$ matrices.
4. If $aE_{11} + bE_{12} + cE_{21} + dE_{22} = 0$, then $\begin{pmatrix} a & b \\ c & d \end{pmatrix} = 0$, so $a = b = c = d = 0$, and the four matrix units are linearly independent.
5. By steps 3 and 4 they form a basis, the [[standard basis|0V7ZD6P7RK]] of $M_2(\mathbb{R})$, and $\dim M_2(\mathbb{R}) = 4$.

## Remarks

The coordinates of a matrix in this basis are its entries, so no computation is needed to find them.
If the entries are listed row by row, this basis identifies $M_2(\mathbb{R})$ with $\mathbb{R}^4$, and $A$ corresponds to $(3, -1, 4, 7)$.
The [[trace|07PTPSZPME]] of $A$ is the sum of the coordinates on $E_{11}$ and $E_{22}$, here $3 + 7 = 10$.

Other bases are possible, and in them the coordinates are not the entries.
For example, $I$, $E_{12}$, $E_{21}$ and $E_{11} - E_{22}$ also form a basis, and in it
$$A = 5I - E_{12} + 4E_{21} - 2(E_{11} - E_{22}).$$
Check: the diagonal entries are $5 - 2 = 3$ and $5 + 2 = 7$.

## Explanations

### L1 human

Each entry of a matrix tells how much of one matrix unit the matrix contains.
Here $A$ contains $3$ copies of $E_{11}$, $-1$ of $E_{12}$, $4$ of $E_{21}$ and $7$ of $E_{22}$.

### L2 human

The same argument shows that the $mn$ matrix units of size $m \times n$ form a basis of $M_{m \times n}(F)$, for each field $F$, so this space has dimension $mn$.
Watch out: in step 4, linear independence holds because different matrix units have their $1$ in different places, so no cancellation between them is possible.
