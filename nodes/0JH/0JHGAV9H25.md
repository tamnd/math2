---
tag: 0JHGAV9H25
kind: statement
role: proposition
name: Orthogonality of eigenspaces
aliases: [eigenspaces-of-self-adjoint-operators-are-orthogonal]
msc: ["47B15", "15A18"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0NEGN5CRSC, 0C8BR8XRTR, 0G0RFPG8HR]
uses: [0MB8HQW495, 0ENZN5G4CV, 0AYEPBQMAW, 0TS7VZJBWD]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: Properties in finite-dimensional case
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Statement

For a normal operator, and so for every self-adjoint operator, eigenvectors that belong to different eigenvalues are perpendicular.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to V$ be a [[normal|0ENZN5G4CV]] operator, for example a [[self-adjoint|0MB8HQW495]] operator.
Let $\lambda \neq \mu$ be eigenvalues of $T$, and let $v$ and $w$ be eigenvectors with $Tv = \lambda v$ and $Tw = \mu w$.
Then $v$ and $w$ are [[orthogonal|0TS7VZJBWD]]:
$$\ip{v}{w} = 0.$$
So the [[eigenspaces|0AYEPBQMAW]] $E_\lambda$ and $E_\mu$ of $T$ for distinct eigenvalues are orthogonal to each other.

## Remarks

### Why each hypothesis is needed

Normality is needed.
[[The upper triangular matrix with diagonal 1, 2|5RQ7EC5RC6]] has the eigenvector $(1, 0)$ for $1$ and the eigenvector $(1, 1)$ for $2$, and
$$(1, 0) \cdot (1, 1) = 1 \neq 0.$$
This matrix is not normal, and its two eigenvectors meet at $45$ degrees.

The eigenvalues must differ.
Inside one eigenspace of dimension at least $2$, two eigenvectors need not be orthogonal: for $T = I$ on $\mathbb{R}^2$, the eigenvectors $(1, 0)$ and $(1, 1)$ are not orthogonal.

### What it gives you

Every self-adjoint, skew-adjoint or unitary operator is normal, so the statement applies to all of them.
If $\lambda_1, \dots, \lambda_k$ are the distinct eigenvalues of a normal $T$, then the sum $E_{\lambda_1} + \dots + E_{\lambda_k}$ is an orthogonal direct sum.
When a normal operator on an $n$-dimensional space has $n$ distinct eigenvalues, its unit eigenvectors already form an orthonormal basis.

For example, the [[symmetric 3 by 3 matrix|2P021RCC4Y]] $\begin{pmatrix} 4 & 0 & -1 \\ 0 & 4 & -1 \\ -1 & -1 & 5 \end{pmatrix}$ has the eigenvalues $3$, $4$ and $6$, with the eigenvectors $(1, 1, 1)$, $(1, -1, 0)$ and $(1, 1, -2)$.
The statement predicts the three dot products before we compute them:
$$(1, 1, 1) \cdot (1, -1, 0) = 0, \qquad (1, 1, 1) \cdot (1, 1, -2) = 0, \qquad (1, -1, 0) \cdot (1, 1, -2) = 0.$$
The [[complex spectral theorem|04CW1P44VD]] and [[the real spectral theorem|06J4PXRG22]] remove the condition of distinct eigenvalues.

### The converse

Orthogonal eigenvectors for distinct eigenvalues do not make $T$ normal.
The matrix $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has the single eigenvalue $0$, so the condition holds with nothing to check, but $N N^{\mathsf{T}} = \operatorname{diag}(1, 0)$ and $N^{\mathsf{T}} N = \operatorname{diag}(0, 1)$.
A true converse is part of the spectral theorems: if $V$ has an orthonormal basis of eigenvectors of $T$, then $T$ is normal.

### Generalizations

The same statement and proof hold for bounded normal operators on a Hilbert space.
For symmetric differential operators, the self-adjoint version of the proof shows that eigenfunctions for different eigenvalues are orthogonal.
Sturm-Liouville theory uses this to explain why the sines in a Fourier series, and many families of orthogonal polynomials, are orthogonal.

## Explanations

### L1 human

For a symmetric matrix, two directions with different stretch factors are always perpendicular.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ stretches $(1, 1)$ by $3$ and $(1, -1)$ by $1$, and these two directions meet at a right angle.
For a matrix that is not symmetric, such as $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, the two special directions $(1, 0)$ and $(1, 1)$ meet at $45$ degrees.

### L2 human

Here is a worked case with a normal matrix that is not Hermitian.
Let $A = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ on $\mathbb{C}^2$, so $A^* = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$.
Multiply in both orders:
$$A A^* = \begin{pmatrix} 1 + 1 & -i + i \\ i - i & 1 + 1 \end{pmatrix} = 2I = A^* A.$$
So $A$ is normal, but $A^* \ne A$.
Next, $A(1, 1) = (1 + i)(1, 1)$ and $A(1, -1) = (1 - i, i - 1) = (1 - i)(1, -1)$, so the eigenvalues $1 + i$ and $1 - i$ differ.
The statement predicts orthogonal eigenvectors, and indeed $\ip{(1, 1)}{(1, -1)} = 1 \cdot 1 + 1 \cdot (-1) = 0$.
This is how one builds an orthonormal eigenbasis in practice: choose an orthonormal basis inside each eigenspace and put them together.
Watch out: inside a single eigenspace, orthogonality is not automatic, and Gram-Schmidt is needed there.

### L3 human

For a normal operator, the eigenspaces are the images of the orthogonal projections in [[the spectral decomposition|D5KVBA1K9R]] $T = \sum_i \lambda_i P_i$.
Orthogonality of the eigenspaces is the statement $P_i P_j = 0$ for $i \neq j$.
In quantum mechanics, the eigenstates of an observable for different measured values are orthogonal, so the outcomes exclude each other.
For orthogonal polynomials and Fourier series, the orthogonality comes from a self-adjoint differential operator with distinct eigenvalues.
