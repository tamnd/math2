---
tag: YX9Z3E9SGN
kind: statement
role: proposition
name: A product of symmetric matrices is symmetric if and only if they commute
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0VR671PHE5, 8G3X8MPG7E]
uses: [0N28QN4CYA, MX26N71ZD3, 09GK5PS824]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: Properties
---

## Statement

Let $R$ be a commutative ring, and let $A$ and $B$ be [[symmetric|0N28QN4CYA]] $n \times n$ matrices over $R$.
Then $AB$ is symmetric if and only if $AB = BA$, that is, if and only if $A$ and $B$ [[commute|MX26N71ZD3]].

## Remarks

### Two checks with numbers

The symmetric matrices $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ commute, and both products equal $\begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix}$, which is symmetric.
The symmetric matrices $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ do not commute, and in [[this example|3MD62SJJEP]] their product $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is not symmetric.

### Why each hypothesis is needed

Both factors must be symmetric.
The matrices $I$ and $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ commute, but $IN = N$ is not symmetric, since $N$ is not.

Commutativity of $R$ enters through the [[transpose of a product|09GK5PS824]].
Over the quaternions, the $1 \times 1$ matrices $(i)$ and $(j)$ are symmetric, since every $1 \times 1$ matrix is, and their product $(k)$ is symmetric too, yet $ij = k \neq -k = ji$.
So the direction "symmetric product implies commuting" fails without commutativity of $R$.

### What it gives you

A symmetric matrix commutes with itself, so every power $A^k$ is symmetric, and so is every polynomial $p(A) = c_0 I + c_1 A + \cdots + c_d A^d$.
For any two symmetric matrices, the transpose of $AB$ is $BA$, so $AB + BA$ is symmetric and $AB - BA$ is [[skew-symmetric|0PBY4E9GQF]].
The theorem measures the failure exactly: $AB$ is symmetric when this skew-symmetric part $AB - BA$ is $0$.

### Generalizations

For complex matrices, the same argument with the [[conjugate transpose|0DXKE10PHF]] shows that a product of two [[Hermitian|0P17NGQQMQ]] matrices is Hermitian if and only if they commute.
Over $\mathbb{R}$, two symmetric matrices commute if and only if one orthogonal matrix diagonalizes both at once, so in that case their product is diagonal in the same orthonormal basis.

## Explanations

### L1 human

Two symmetric matrices can have a product that is not symmetric.
The product is symmetric exactly when the order of the two factors does not matter.

### L2 human

The whole theorem is one computation: the transpose of $AB$ is $B^{\mathsf{T}} A^{\mathsf{T}} = BA$.
So the sentence "$AB$ is symmetric" and the sentence "$AB = BA$" are the same equation, and the [[proof|C2VQGVYVE8]] reads it in both directions.
Watch out: this is a common trap in proofs, where one assumes that the product of two symmetric matrices is symmetric and forgets to check that they commute.

### L3 human

Under the transpose, $M_n(R)$ splits outside characteristic $2$ into the symmetric part and the skew-symmetric part.
The symmetric part is closed under the Jordan product $A \circ B = (AB + BA)/2$, and the skew-symmetric part under the commutator $[A, B] = AB - BA$, which makes it the Lie algebra $\mathfrak{so}_n$.
The theorem says that the associative product of two symmetric matrices is $A \circ B + \tfrac{1}{2}[A, B]$, and it stays symmetric exactly when the commutator vanishes.
