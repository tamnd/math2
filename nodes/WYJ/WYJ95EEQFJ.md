---
tag: WYJ95EEQFJ
kind: example
name: The 1 × 1 matrices behave like their entries
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0JXZKX526R]
uses: [0CP7YY6NAG, 076JGP6R3T, 0BVXADM10P]
sources:
  - url: https://en.wikipedia.org/wiki/Square_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Definition
---

## Example

The smallest [[square matrices|0CP7YY6NAG]] have one row and one column, and they are nothing more than their single entry in brackets.
Let $R$ be a ring, and consider the $1 \times 1$ matrices $\begin{pmatrix} a \end{pmatrix}$ and $\begin{pmatrix} b \end{pmatrix}$ over $R$.

1. The rule for [[matrix addition|0BVXADM10P]] adds the entries in matching positions, and there is only one position:
$$\begin{pmatrix} a \end{pmatrix} + \begin{pmatrix} b \end{pmatrix} = \begin{pmatrix} a + b \end{pmatrix}.$$
2. The rule for [[matrix multiplication|076JGP6R3T]] gives the entry $(1, 1)$ of the product as a sum over $k$ from $1$ to the number of columns of the first factor, which is $1$:
$$\begin{pmatrix} a \end{pmatrix} \begin{pmatrix} b \end{pmatrix} = \begin{pmatrix} \textstyle\sum_{k=1}^{1} a_{1k} b_{k1} \end{pmatrix} = \begin{pmatrix} ab \end{pmatrix}.$$
3. The map $a \mapsto \begin{pmatrix} a \end{pmatrix}$ is a bijection from $R$ to $M_1(R)$, and steps 1 and 2 say that it keeps sums and products. It also sends $1$ to the identity matrix $I_1 = \begin{pmatrix} 1 \end{pmatrix}$. So it is a ring isomorphism.
4. For a concrete case over $\mathbb{Z}$, multiply two $1 \times 1$ matrices:
$$\begin{pmatrix} 3 \end{pmatrix} \begin{pmatrix} -2 \end{pmatrix} = \begin{pmatrix} -6 \end{pmatrix}.$$
Check: $3 \cdot (-2) = -6$, the same as for the numbers.
5. A $1 \times 1$ matrix also appears when a row meets a column. For the column $u = (1, 2)^{\mathsf{T}}$, the product of the $1 \times 2$ matrix $u^{\mathsf{T}}$ with the $2 \times 1$ matrix $u$ is
$$u^{\mathsf{T}} u = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 \end{pmatrix} = \begin{pmatrix} 5 \end{pmatrix},$$
and we read it as the [[dot product|0S52TNNTH9]] $u \cdot u = 5$.

## Remarks

The example shows why books often drop the brackets around a $1 \times 1$ matrix.
Inside $M_1(R)$ nothing is lost, since the matrix and its entry add and multiply in the same way.

Watch out when a $1 \times 1$ matrix meets a larger matrix.
For a $2 \times 2$ matrix $B$, the product $\begin{pmatrix} 2 \end{pmatrix} B$ is not defined, because $\begin{pmatrix} 2 \end{pmatrix}$ has 1 column and $B$ has 2 rows.
The scalar multiple $2B$ is defined, and it is a different operation that multiplies every entry of $B$ by $2$.
So an expression such as $(u^{\mathsf{T}} v) B$ makes sense only when we read $u^{\mathsf{T}} v$ as a number, not as a matrix.

If we pass from order 1 to order 2, the copy of $R$ is lost: $M_2(R)$ is not commutative when $R$ is a nonzero ring, as the [[standard counterexample|0P506SPZP2]] shows.

## Explanations

### L1 human

A $1 \times 1$ matrix is one number in brackets, like $\begin{pmatrix} 7 \end{pmatrix}$.
To add two of them, you add the numbers, and to multiply two of them, you multiply the numbers.
So $\begin{pmatrix} 3 \end{pmatrix}$ times $\begin{pmatrix} 4 \end{pmatrix}$ is $\begin{pmatrix} 12 \end{pmatrix}$, just as $3$ times $4$ is $12$.

### L2 human

The identification of $\begin{pmatrix} a \end{pmatrix}$ with $a$ is what lets us write the dot product of two columns as a matrix product.
For $u = (1, -1, 2)^{\mathsf{T}}$ and $v = (3, 0, 1)^{\mathsf{T}}$ we get
$$u^{\mathsf{T}} v = \begin{pmatrix} 3 + 0 + 2 \end{pmatrix} = \begin{pmatrix} 5 \end{pmatrix},$$
and this is $u \cdot v = 5$.
The typical use is a formula such as the projection $\frac{u^{\mathsf{T}} v}{u^{\mathsf{T}} u}\, u$, where each $1 \times 1$ product is read as a number.
The trap is to keep the matrix reading inside a longer product, where the sizes no longer fit.
