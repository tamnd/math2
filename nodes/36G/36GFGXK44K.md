---
tag: 36GFGXK44K
kind: example
name: The columns of the 3 × 3 identity matrix are the standard basis vectors
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [06DW9BAWB1]
uses: [6NHZRCKJNW, 0CCQV3884B, 0V7ZD6P7RK]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Standard_basis
    locator: lead section
---

## Example

The identity matrix of order 3 is built from the three unit vectors along the axes, and this explains why it fixes every vector.
Let
$$I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad x = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}.$$

1. By the [[definition|6NHZRCKJNW]], the entry $(i, j)$ of $I_3$ is $\delta_{ij}$. So column $j$ has the entry $1$ in row $j$ and $0$ in the other two rows.
2. The three columns are therefore
$$e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \qquad e_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \qquad e_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix},$$
the [[standard basis vectors|0V7ZD6P7RK]] of $\mathbb{R}^3$.
3. The column view of the [[matrix-vector product|0CCQV3884B]] says that $I_3 x$ is the combination of the columns with weights $x_1, x_2, x_3$:
$$I_3 x = x_1 e_1 + x_2 e_2 + x_3 e_3.$$
4. Adding the three vectors entry by entry gives $(x_1, x_2, x_3)^{\mathsf{T}} = x$. So $I_3 x = x$ for every $x \in \mathbb{R}^3$.
5. For instance, with $x = (2, -1, 7)^{\mathsf{T}}$:
$$I_3 x = 2 e_1 - e_2 + 7 e_3 = \begin{pmatrix} 2 \\ -1 \\ 7 \end{pmatrix}.$$

## Remarks

The rows of $I_3$ are $e_1^{\mathsf{T}}, e_2^{\mathsf{T}}, e_3^{\mathsf{T}}$, the same vectors laid flat, so $I_3$ equals its transpose and is [[symmetric|0VR671PHE5]].

The example also explains the right identity law.
For any matrix $A$ with 3 columns, the product $A e_j$ is column $j$ of $A$, so $A I_3$ has the same columns as $A$ and $A I_3 = A$.
Nothing depends on the number $3$: for every $n$ the columns of $I_n$ are $e_1, \dots, e_n$.

If we swap two columns of $I_3$, for example the first two, the columns are still the standard basis vectors, but in the order $e_2, e_1, e_3$.
The result is a permutation matrix, which sends $x$ to $(x_2, x_1, x_3)^{\mathsf{T}}$, so it is no longer the identity.

## Explanations

### L1 human

The identity matrix of order 3 is made of three arrows of length one, one along each axis.
To multiply it by a vector, take $x_1$ steps along the first arrow, $x_2$ steps along the second and $x_3$ steps along the third.
You land exactly at the point $x$, so the vector does not change.

### L2 human

A matrix is fixed by what it does to $e_1, e_2, e_3$, since column $j$ of any matrix $A$ is $A e_j$.
The identity map sends each $e_j$ to itself, so its matrix has the columns $e_1, e_2, e_3$, which is $I_3$.
The typical use is to build the matrix of a linear map column by column: write the image of each $e_j$ as column $j$.
The trap is to write the images as rows instead, which gives the transpose of the correct matrix.
