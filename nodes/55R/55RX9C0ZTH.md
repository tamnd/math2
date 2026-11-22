---
tag: 55RX9C0ZTH
kind: statement
role: proposition
name: Skew-symmetric matrices of odd size are singular
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
uses: [0C3CFHDN6R, 03RNVFDEAN]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
---

## Statement

A matrix that changes sign under transposition and has odd size always has determinant $0$, as long as $2$ can be cancelled or the diagonal is $0$.

Let $K$ be a commutative ring, let $n$ be odd, and let $A$ be an $n \times n$ matrix over $K$.

1. If $A^{\mathsf{T}} = -A$ and $2$ is not a zero divisor in $K$, then $\det A = 0$, where $\det$ is the [[determinant|0C3CFHDN6R]].
2. If $A$ is alternating, that is $A^{\mathsf{T}} = -A$ and $a_{ii} = 0$ for all $i$, then $\det A = 0$ for every commutative ring $K$.

In particular, a [[skew-symmetric matrix|03RNVFDEAN]] of odd size over a field of characteristic other than $2$ is singular.

## Remarks

### A three by three check

Take
$$A = \begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 2 \\ 1 & -2 & 0 \end{pmatrix}.$$
The rule of Sarrus adds the three products along the diagonals and subtracts the three products along the antidiagonals:
$$\det A = (0 \cdot 0 \cdot 0) + (1 \cdot 2 \cdot 1) + ((-1) \cdot (-1) \cdot (-2)) - ((-1) \cdot 0 \cdot 1) - (0 \cdot 2 \cdot (-2)) - (1 \cdot (-1) \cdot 0) = 0 + 2 - 2 - 0 - 0 - 0 = 0.$$
A nonzero vector in the kernel is $(2, 1, 1)$: the three rows give $1 - 1 = 0$, $-2 + 2 = 0$ and $2 - 2 = 0$.
The [[proof|CMZNSAXRCR]] explains why the answer is always $0$.

### Why each hypothesis is needed

The size must be odd.
The $2 \times 2$ matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is skew-symmetric, and its determinant is $0 \cdot 0 - 1 \cdot (-1) = 1$.

Part 1 needs that $2$ is not a zero divisor.
Over $\mathbb{F}_2$ we have $-1 = 1$, so the $1 \times 1$ matrix $(1)$ satisfies $A^{\mathsf{T}} = -A$, but its determinant is $1$.
That matrix is not alternating, since its diagonal entry is $1$, so it does not contradict part 2.
So in characteristic $2$ the condition $a_{ii} = 0$ is what saves the statement.

### What it gives you

A real skew-symmetric matrix of odd size has the eigenvalue $0$, so it has a nonzero kernel.
For example, the matrix of $v \mapsto a \times v$ on $\mathbb{R}^3$ is skew-symmetric of size $3$, so it is singular, and in fact it sends $a$ to $a \times a = 0$.

The statement also explains the convention for the [[Pfaffian|NH5HWBPWS9]].
An alternating matrix of odd size has no perfect matchings, so its Pfaffian is set to $0$, and then the [[square rule|473MBZST4D]] $\operatorname{pf}(A)^2 = \det A$ holds in odd size too.

### The converse

The converse is false.
The matrix $\operatorname{diag}(1, 0, 0)$ has odd size and determinant $0$, but it is not skew-symmetric.
In even size a skew-symmetric matrix can be singular, such as the zero matrix, or invertible, such as the $2 \times 2$ matrix above.

### Generalizations

Over a field, the rank of every alternating matrix is even, whatever its size.
In odd size an even rank is less than $n$, so this gives part 2 again over a field.

## Explanations

### L1 human

A skew-symmetric matrix turns into its own negative when you flip it over its diagonal.
Flipping does not change the determinant.
Changing the sign of every entry of an odd-size matrix changes the sign of its determinant.
So the determinant equals its own negative, and the only such number is $0$.

### L2 human

Here is a typical use: does the system $A x = 0$ with the matrix $A$ of the check above have a nonzero solution?
The matrix is skew-symmetric of size $3$, so $\det A = 0$ without any computation, and a nonzero solution exists.
To find one, look for $x = (x_1, x_2, x_3)$ with $x_2 - x_3 = 0$ from row 1 and $-x_1 + 2x_3 = 0$ from row 2.
Taking $x_3 = 1$ gives $x = (2, 1, 1)$, and row 3 gives $2 - 2 + 0 = 0$, as it must.
Watch out: in characteristic $2$, skew-symmetric means symmetric, and the statement needs the diagonal to be $0$.

### L3 human

An alternating matrix is the Gram matrix of an [[alternating bilinear form|0DGDS5XY84]].
Over a field, such a form has a basis in which its matrix is made of blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and zeros, so its rank is even.
For a real skew-symmetric matrix the eigenvalues are purely imaginary and come in pairs $\pm i\lambda$, so in odd size at least one eigenvalue is $0$.
