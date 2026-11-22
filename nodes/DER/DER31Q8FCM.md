---
tag: DER31Q8FCM
kind: example
name: The general linear group of 2 × 2 real matrices is not abelian
msc: ["20G15", "15A09"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0FCHE902D7]
uses: [0FCHE902D7, 032Q9FB8MT, 0P506SPZP2]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: lead section
---

## Example

Two shears are enough to show that $\mathrm{GL}_2(\mathbb{R})$ is not abelian.
Let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}.$$
Both lie in the [[general linear group|0FCHE902D7]], since $\det A = \det B = 1$, with inverses
$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad B^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}.$$
The two products are
$$AB = \begin{pmatrix} 1 + 1 & 0 + 1 \\ 0 + 1 & 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad BA = \begin{pmatrix} 1 + 0 & 1 + 0 \\ 1 + 0 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}.$$
The $(1, 1)$ entries differ, so $AB \ne BA$.

The same pair works in every size $n \ge 2$.
Put $A$ and $B$ in the top left corner of $I_n$, as the block matrices $\begin{pmatrix} A & 0 \\ 0 & I_{n-2} \end{pmatrix}$ and $\begin{pmatrix} B & 0 \\ 0 & I_{n-2} \end{pmatrix}$.
Block multiplication gives the two products $\begin{pmatrix} AB & 0 \\ 0 & I_{n-2} \end{pmatrix}$ and $\begin{pmatrix} BA & 0 \\ 0 & I_{n-2} \end{pmatrix}$, which differ.

## Remarks

The example uses only the entries $0$ and $1$, so it works over every field and also over $\mathbb{Z}$.
Over $\mathbb{Z}/2$, the products are $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, two different elements of the group $\mathrm{GL}_2(\mathbb{Z}/2)$ of order $6$.
The same matrices show the [[noncommutativity of matrix multiplication|0P506SPZP2]] in the ring $M_2$.
For $n = 1$ the group $\mathrm{GL}_1(F) = F^{\times}$ is abelian, so the condition $n \ge 2$ is needed.

## Explanations

### L1 human

The matrix $A$ shears the plane sideways, sending $(x, y)$ to $(x + y, y)$, and $B$ shears it upward, sending $(x, y)$ to $(x, x + y)$.
Doing the sideways shear first and then the upward one is not the same as the other order.
For example, $AB$ sends $(1, 0)$ to $(2, 1)$, but $BA$ sends it to $(1, 1)$.

### L2 human

The point is that a group of matrices need not be commutative, so in $\mathrm{GL}_n$ you must keep track of the order of the factors.
That is why the inverse of a product is $(AB)^{-1} = B^{-1}A^{-1}$, with the order reversed.
A trap: some pairs do commute, for example two diagonal matrices, so one commuting pair proves nothing.
