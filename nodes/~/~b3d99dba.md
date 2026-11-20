---
tag: ~b3d99dba
kind: example
name: An eigenspace smaller than the generalized eigenspace
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
instance_of: [0AJ035ZTZE, 01H6QKWGDH]
not_instance_of:
  - target: 07SQCNV233
    note: the only eigenvalue 2 has algebraic multiplicity 2 but geometric multiplicity 1
illustrates: [~b8d53cf6]
uses: [07PNDWA7CE, 0AYEPBQMAW, 0VSSPAFM2C, 0S7A0EMPF4]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Examples
---

## Example

Let $A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$ over $\R$.

1. The trace is $4$ and the determinant is $3 + 1 = 4$. So the [[characteristic polynomial|0VSSPAFM2C]] is $t^2 - 4t + 4 = (t - 2)^2$.
2. So $2$ is the only eigenvalue, with [[algebraic multiplicity|0FY42N02DV]] $2$.
3. $A - 2I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$, with kernel spanned by $(1, -1)$. So the [[eigenspace|0AYEPBQMAW]] is a line.
4. $(A - 2I)^2 = \begin{pmatrix} 1 - 1 & 1 - 1 \\ -1 + 1 & -1 + 1 \end{pmatrix} = 0$.
5. So the [[generalized eigenspace|07PNDWA7CE]] $V_2 = \ker (A - 2I)^2$ is $\R^2$, of dimension $2$.
6. $(A - 2I) e_1 = (1, -1) \ne 0$. So $e_1$ is a generalized eigenvector for $2$ of rank $2$, with chain $e_1 \mapsto (1, -1) \mapsto 0$.

## Remarks

The eigenspace has dimension $1$, while $\dim V_2 = 2$ equals the algebraic multiplicity, as the [[dimension theorem|~b8d53cf6]] says.
So $A$ is not [[diagonalizable|07SQCNV233]], although it has two eigenvalues counted with multiplicity.
In the basis $((1, -1), e_1)$, the matrix of $A$ is $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$, since $A e_1 = (3, -1) = (1, -1) + 2 e_1$.
$A - 2I$ is a nonzero nilpotent matrix of rank $1$.

## Explanations

### L1 human

This matrix has the number $2$ as a double root of its characteristic polynomial.
Yet only one line of vectors is stretched by exactly $2$.
If we allow two steps of $A - 2I$ instead of one, every vector goes to zero.
So the generalized eigenspace is the whole plane.

### L2 human

Check the Jordan form in the basis $P = \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix}$, with columns $(1, -1)$ and $e_1$.

1. $\det P = 0 + 1 = 1$, and $P^{-1} = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}$.
2. $A P = \begin{pmatrix} 2 & 3 \\ -2 & -1 \end{pmatrix}$.
3. $P^{-1} A P = \begin{pmatrix} 0 \cdot 2 - 1 \cdot (-2) & 0 \cdot 3 - 1 \cdot (-1) \\ 2 - 2 & 3 - 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.

The typical use is to find a basis of $V_\lambda$ made of a Jordan chain.
The trap is to count two eigenvalues with multiplicity and conclude that $A$ is diagonalizable.

### L3 human

Every $2 \times 2$ real matrix with a double eigenvalue $\lambda$ is either $\lambda I$ or similar to $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$.
In both cases $V_\lambda = \R^2$, and the eigenspace decides between the two.
