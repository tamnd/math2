---
tag: 0PBFS92AJP
kind: definition
name: Jordan block
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
defines: 07PH4RX0X5
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Definition
  - book: isbn:9780135367971
    locator: Section 7.3
---

## Definition

A Jordan block is a square matrix with one scalar on the diagonal, ones just above the diagonal, and zeros elsewhere.
Let $F$ be a field, let $\lambda \in F$, and let $k \ge 1$.
The *Jordan block* $J_k(\lambda)$ is the $k \times k$ [[square matrix|0CP7YY6NAG]] over $F$ with entries
$$(J_k(\lambda))_{ij} = \begin{cases} \lambda & \text{if } j = i, \\ 1 & \text{if } j = i + 1, \\ 0 & \text{otherwise}. \end{cases}$$
The number $k$ is the *size* of the block and $\lambda$ is its *eigenvalue*.
A block diagonal matrix $J_{k_1}(\lambda_1) \oplus \dots \oplus J_{k_s}(\lambda_s)$ of Jordan blocks is a *Jordan matrix*.

## Notation

This is the upper version, with the ones above the diagonal.
Some books use the lower version, the transpose $J_k(\lambda)^{\mathsf T}$, with the ones below the diagonal.
The two versions are similar by the matrix that reverses the order of the basis.

## Remarks

The definition has three parts, and each one matters.
The diagonal carries a single scalar $\lambda$, so the block has only one eigenvalue.
The entries in the positions $(i, i + 1)$ are exactly $1$, which makes the block a normal form rather than a whole family of similar matrices.
All other entries are $0$, so that $J_k(\lambda) - \lambda I$ is the shift with $e_1 \mapsto 0$ and $e_i \mapsto e_{i-1}$ for $2 \le i \le k$.

For example, the block of size $3$ is
$$J_3(\lambda) = \begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{pmatrix},$$
and in the standard basis it acts by $J_3(\lambda) e_1 = \lambda e_1$, $J_3(\lambda) e_2 = e_1 + \lambda e_2$ and $J_3(\lambda) e_3 = e_2 + \lambda e_3$.
A matrix that fails the first condition is $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, whose [[two diagonal entries differ|7YPGG6CK8N]].
The main entry on the [[Jordan block|07PH4RX0X5]] gives its powers, its polynomials and its place in the Jordan normal form.

## Explanations

### L1 human

Write the same number, say $5$, down the diagonal of a square table, put ones just above the diagonal, and fill the rest with zeros.
The $2 \times 2$ result is $\begin{pmatrix} 5 & 1 \\ 0 & 5 \end{pmatrix}$, and that is a Jordan block.
It has only one eigenvalue, $5$, and only one line of eigenvectors.

### L2 human

Take $J = J_2(5)$.
Then $J e_1 = 5 e_1$ and $J e_2 = e_1 + 5 e_2$, so $e_1$ is an eigenvector and $e_2$ is not.
The matrix $J - 5I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has rank $1$, so the eigenspace of $5$ is only the line through $e_1$.
Since $5$ is a double root of $\det(xI - J) = (x - 5)^2$, the block is not diagonalizable.
The trap is the convention: check whether a book puts the ones above or below the diagonal before you read off a chain of vectors.
