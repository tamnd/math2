---
tag: ~1d5e4bea
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

Let $F$ be a field and let $V = M_2(F)$, the space of $2 \times 2$ matrices over $F$.
For $X, Y \in V$ let $B(X, Y) = \tr(XY)$, the [[trace|07PTPSZPME]] of the product.
We use the basis $E_{11}, E_{12}, E_{21}, E_{22}$, where $E_{ij}$ has the entry $1$ at place $(i, j)$ and $0$ elsewhere.

1. $B$ is a [[bilinear form|0P799D6AMN]]. The product $XY$ is linear in $X$ and in $Y$, and the trace is linear.
2. $B$ is symmetric, because $\tr(XY) = \tr(YX)$ for all square matrices.
3. We compute the values on the basis. The product $E_{ij}E_{kl}$ is $E_{il}$ when $j = k$ and $0$ otherwise. Its trace is $1$ exactly when $j = k$ and $i = l$.
4. So $B(E_{11}, E_{11}) = 1$, $B(E_{22}, E_{22}) = 1$, $B(E_{12}, E_{21}) = 1$ and $B(E_{21}, E_{12}) = 1$. All other values on basis pairs are $0$.
5. The [[matrix of the form|0P24YW565F]] in this basis is
$$A = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
6. A check: $X = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $Y = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ give $XY = \begin{pmatrix} 2 & 3 \\ 4 & 7 \end{pmatrix}$, so $\tr(XY) = 9$.
7. The coordinate vectors are $x = (1, 2, 3, 4)$ and $y = (0, 1, 1, 1)$. Then $Ay = (0, 1, 1, 1)$ and $x^T A y = 0 + 2 + 3 + 4 = 9$, as in step 6.
8. $\det A = -1 \neq 0$, so $B$ is [[nondegenerate|01NHFZF2SK]].

## Remarks

The example shows that a natural form on matrices has a matrix of its own, of size $4 \times 4$.
The diagonal matrices $E_{11}$ and $E_{22}$ give squares $1$, and the plane spanned by $E_{12}$ and $E_{21}$ is a [[hyperbolic plane|~70f96526]].
The matrix $E_{12}$ is [[isotropic|~0d389e21]], since $E_{12}^2 = 0$ gives $B(E_{12}, E_{12}) = 0$.
On $M_n(F)$ the same computation gives a nondegenerate symmetric form for every $n$, with matrix entries $1$ at the pairs $(E_{ij}, E_{ji})$.
The trace form of a field extension, $(a, b) \mapsto \operatorname{Tr}(ab)$, is a [[different notion|YWX2R53ED6]] with the same idea.

## Explanations

### L1 human

Take two small square tables of numbers, multiply them as matrices, and add the two numbers on the diagonal of the result.
This gives one number for each pair of tables.
For the tables in the example the number is $9$.
If we double one table, the number doubles, so the rule is a bilinear form.

### L2 human

To find the matrix of a form, evaluate it on all pairs of basis vectors.

1. List the basis $E_{11}, E_{12}, E_{21}, E_{22}$.
2. Use $\tr(E_{ij}E_{kl}) = 1$ when $j = k$ and $i = l$, and $0$ otherwise.
3. Write the value $B(e_i, e_j)$ at place $(i, j)$. This gives the matrix $A$ above.
4. Check one value of $B$ in two ways, as in steps 6 and 7.

The typical use is to compute the radical, the rank or the isotropic vectors from the matrix.
A trap: the matrix depends on the order of the basis.
With the order $E_{11}, E_{22}, E_{12}, E_{21}$ the $1$s off the diagonal move to places $(3, 4)$ and $(4, 3)$.
