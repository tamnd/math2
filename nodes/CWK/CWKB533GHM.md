---
tag: CWKB533GHM
kind: example
name: The trace form on 2 by 2 matrices
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [0SQZMXB6GP, 0QK6K857HS, 0AXZNE5XNH, 01NHFZF2SK]
uses: [0P799D6AMN, 0P24YW565F, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Coordinate representation
---

## Example

Let $F$ be a field and let $V = M_2(F)$, the space of $2 \times 2$ matrices over $F$, of dimension $4$.
For $X, Y \in V$ let
$$B(X, Y) = \operatorname{tr}(XY),$$
the [[trace|07PTPSZPME]] of the product.
We use the basis $E_{11}, E_{12}, E_{21}, E_{22}$ in this order, where $E_{ij}$ has the entry $1$ at place $(i, j)$ and $0$ elsewhere.

1. $B$ is a [[bilinear form|0P799D6AMN]]. The product $XY$ is linear in $X$ for fixed $Y$ and linear in $Y$ for fixed $X$, and the trace is linear.
2. $B$ is symmetric, because $\operatorname{tr}(XY) = \operatorname{tr}(YX)$ for all square matrices of one size.
3. We compute the values on basis pairs. The product $E_{ij} E_{kl}$ is $E_{il}$ when $j = k$ and $0$ otherwise, and $\operatorname{tr} E_{il}$ is $1$ when $i = l$ and $0$ otherwise. So $B(E_{ij}, E_{kl}) = 1$ exactly when $j = k$ and $i = l$.
4. The pairs that give $1$ are $(E_{11}, E_{11})$, $(E_{22}, E_{22})$, $(E_{12}, E_{21})$ and $(E_{21}, E_{12})$. All other basis pairs give $0$.
5. So the [[matrix of the form|0P24YW565F]] in this basis is
$$A = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
6. We check one value in two ways. Take $X = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $Y = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$. Then
$$XY = \begin{pmatrix} 1 \cdot 0 + 2 \cdot 1 & 1 \cdot 1 + 2 \cdot 1 \\ 3 \cdot 0 + 4 \cdot 1 & 3 \cdot 1 + 4 \cdot 1 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 4 & 7 \end{pmatrix}, \qquad \operatorname{tr}(XY) = 9.$$
7. The coordinate vectors are $x = (1, 2, 3, 4)$ and $y = (0, 1, 1, 1)$. The matrix $A$ swaps the second and third entries, so $Ay = (0, 1, 1, 1)$, and
$$x^{\mathsf{T}} A y = 1 \cdot 0 + 2 \cdot 1 + 3 \cdot 1 + 4 \cdot 1 = 9.$$
Check: this agrees with step 6.
8. $A$ is a permutation matrix of one swap, so $\det A = -1$. This is not $0$ in any field, so $B$ is [[nondegenerate|01NHFZF2SK]].

## Remarks

The example shows that a natural pairing of matrices has a matrix of its own, here of size $4 \times 4$.
The diagonal units $E_{11}$ and $E_{22}$ pair to $1$ with themselves, while $E_{12}$ and $E_{21}$ pair only with each other.
So the plane spanned by $E_{12}$ and $E_{21}$ has the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, and it is a [[hyperbolic plane|1X5PZSK44P]].
The unit $E_{12}$ is [[isotropic|MZHFGPV1YT]]: $E_{12}^2 = 0$, so $B(E_{12}, E_{12}) = 0$ although $E_{12} \ne 0$.

On $M_n(F)$ the same computation works for every $n$.
The form $\operatorname{tr}(XY)$ has matrix entry $1$ exactly at the pairs $(E_{ij}, E_{ji})$, so its matrix is a permutation matrix and the form is nondegenerate; the [[trace pairing on square matrices|4F7GWKTQ1H]] treats this case.
The trace form of a field extension, $(a, b) \mapsto \operatorname{Tr}(ab)$, is a [[different notion|YWX2R53ED6]] built on the same idea.

## Explanations

### L1 human

Take two small square tables of numbers, multiply them as matrices, and add the two numbers on the diagonal of the result.
This gives one number for each pair of tables.
For the two tables in the example the product has diagonal $2$ and $7$, so the number is $9$.
If you double one table, the number doubles, so the rule is a bilinear form.

### L2 human

Here is the general method to find the matrix of a form: evaluate it on all pairs of basis vectors.
For the trace form, the rule $\operatorname{tr}(E_{ij} E_{kl}) = 1$ when $j = k$ and $i = l$ gives all sixteen values at once.
Write the value $B(e_i, e_j)$ at place $(i, j)$ to get $A$, and then confirm one value in two ways, as in steps 6 and 7.
With $A$ in hand, questions about the form become questions about a matrix: the rank of $A$ is $4$, so the radical is $0$.
Watch out: the matrix depends on the order of the basis.
With the order $E_{11}, E_{22}, E_{12}, E_{21}$ the off-diagonal entries $1$ move to places $(3, 4)$ and $(4, 3)$, and the new matrix is $P^{\mathsf{T}} A P$ for a permutation matrix $P$.
