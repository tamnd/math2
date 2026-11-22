---
tag: E2MNC3W2DM
kind: statement
role: theorem
name: Cartesian decomposition of a complex square matrix
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0P17NGQQMQ]
uses: [0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Skew-Hermitian_matrix
    locator: lead section
---

## Statement

Every complex square matrix has a real part and an imaginary part, both Hermitian, in exactly one way.
Let $A$ be a complex $n \times n$ matrix, and let $A^*$ be its [[conjugate transpose|0EX045E2BP]].
Then there are unique [[Hermitian|0EKZCX4K3P]] $n \times n$ matrices $H$ and $K$ with $A = H + iK$, namely
$$H = \tfrac12 \left(A + A^*\right), \qquad K = \tfrac{1}{2i} \left(A - A^*\right).$$
Equivalently, $A$ is in exactly one way the sum of the Hermitian matrix $H$ and the skew-Hermitian matrix $iK$.

## Remarks

### Why each hypothesis is needed

The matrix must be square, because Hermitian matrices are square by definition, and $A$ and $A^*$ must have the same size for $A + A^*$ to exist.
The scalars must be complex, since the statement uses $i$.
Over $\mathbb{R}$ the role of the theorem goes to the [[decomposition into symmetric and skew-symmetric parts|K284W6D15Z]], $A = \tfrac12(A + A^{\mathsf{T}}) + \tfrac12(A - A^{\mathsf{T}})$.
Uniqueness needs both parts to be Hermitian: without that condition, $A = A + i \cdot 0 = 0 + i(-iA)$ gives many splittings.

### A worked case

For $A = \begin{pmatrix} 1 & 2 \\ 0 & i \end{pmatrix}$, [[the 2 × 2 example|NQBXQ87CXZ]] finds
$$H = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}, \qquad K = \begin{pmatrix} 0 & -i \\ i & 1 \end{pmatrix}.$$
Both are Hermitian, and $H + iK = A$.

### What it gives you

The decomposition turns questions about $A$ into questions about two Hermitian matrices.
The matrix $A$ is Hermitian exactly when $K = 0$, and skew-Hermitian exactly when $H = 0$.
Since $A^* = H - iK$, we get
$$A^* A - A A^* = 2i\,(HK - KH),$$
so $A$ is [[normal|0MR0BYF0K2]] exactly when $H$ and $K$ commute.
For each $x \in \mathbb{C}^n$, $x^* A x = x^* H x + i\, x^* K x$, and both $x^* H x$ and $x^* K x$ are real, so they are the real and imaginary parts of the number $x^* A x$.

### Generalizations

The same formulas work in every complex algebra with an involution $a \mapsto a^*$ that reverses products and conjugates scalars.
For bounded operators on a Hilbert space, every operator is $H + iK$ with $H$ and $K$ self-adjoint, with the same proof.

## Explanations

### L1 human

Each complex number is $a + ib$ with $a$ and $b$ real.
Each complex square matrix is $H + iK$ with $H$ and $K$ Hermitian.
So Hermitian matrices play the part of the real numbers.

### L2 human

The formulas copy $\operatorname{Re} z = (z + \overline{z})/2$ and $\operatorname{Im} z = (z - \overline{z})/(2i)$, with $A^*$ in the part of $\overline{z}$.
To use the theorem, compute $A^*$ once, then add and subtract.
Watch out: $H$ and $K$ are not the entrywise real and imaginary parts of $A$.
For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, a real matrix, the decomposition gives $H = \tfrac12\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $K = \tfrac{1}{2i} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \neq 0$.

### L3 human

The real vector space $M_n(\mathbb{C})$ of dimension $2n^2$ is the direct sum of the Hermitian matrices and the skew-Hermitian matrices, each of real dimension $n^2$.
Multiplication by $i$ maps the first summand onto the second, so $M_n(\mathbb{C})$ is the complexification of the real space of Hermitian matrices.
In the theory of operators, $H$ and $K$ are often written $\operatorname{Re} A$ and $\operatorname{Im} A$, and the numerical range of $A$ projects onto the numerical ranges of $H$ and $K$.
