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

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to V$ be a [[normal|0ENZN5G4CV]] operator, for example a [[self-adjoint|0MB8HQW495]] operator.
Let $\lambda \neq \mu$ be eigenvalues of $T$, and let $v$ and $w$ be eigenvectors with $Tv = \lambda v$ and $Tw = \mu w$.
Then $v$ and $w$ are [[orthogonal|0TS7VZJBWD]]: $\ip{v}{w} = 0$.
So the [[eigenspaces|0AYEPBQMAW]] $E_\lambda$ and $E_\mu$ of $T$ for distinct eigenvalues are orthogonal to each other.

## Remarks

### Why each hypothesis is needed

- Normality is needed. [[The upper triangular matrix with diagonal $1$, $2$|~3859cd16]] has the eigenvectors $(1, 0)$ for $1$ and $(1, 1)$ for $2$, and $(1, 0) \cdot (1, 1) = 1 \neq 0$.
- The eigenvalues must differ. Inside one eigenspace of dimension at least $2$, eigenvectors need not be orthogonal: for $T = I$ on $\mathbb{R}^2$, the eigenvectors $(1, 0)$ and $(1, 1)$ are not orthogonal.

### Consequences

- Every self-adjoint operator is normal, since $T^* T = T^2 = T T^*$. So the statement holds for self-adjoint operators, for skew-adjoint operators and for unitary operators.
- If $T$ is normal with distinct eigenvalues $\lambda_1, \dots, \lambda_k$, then the sum $E_{\lambda_1} + \dots + E_{\lambda_k}$ is an orthogonal direct sum.
- If a normal operator on an $n$-dimensional space has $n$ distinct eigenvalues, then the unit eigenvectors form an orthonormal basis. The [[complex spectral theorem|04CW1P44VD]] and [[the real spectral theorem|06J4PXRG22]] remove the condition on distinct eigenvalues.

### Converse

The converse is false in this form: orthogonality of eigenvectors for distinct eigenvalues does not make $T$ normal.
For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, the only eigenvalue is $0$, so the condition holds with nothing to check, but $A$ is not normal.
A true converse is part of the spectral theorems: if $V$ has an orthonormal basis of eigenvectors of $T$, then $T$ is normal.

### Generalizations

- The same statement and proof hold for bounded normal operators on a Hilbert space.
- For a symmetric operator in the sense of unbounded operators, eigenvectors for distinct eigenvalues are orthogonal by the self-adjoint proof. Sturm-Liouville theory uses this for the orthogonality of eigenfunctions.

## Explanations

### L1 human

For a symmetric matrix, two directions with different stretch factors are always perpendicular.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ stretches $(1, 1)$ by $3$ and $(1, -1)$ by $1$.
These two directions meet at a right angle.
For a matrix that is not symmetric, such as $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, the two special directions $(1, 0)$ and $(1, 1)$ meet at $45$ degrees.

### L2 human

Worked example: a normal matrix that is not Hermitian.

1. Let $A = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ on $\mathbb{C}^2$, so $A^* = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$.
2. Then $A A^* = 2I = A^* A$, so $A$ is normal. It is not Hermitian, because $A^* \neq A$.
3. We get $A(1, 1) = (1 + i, 1 + i)$, so $(1, 1)$ is an eigenvector for $1 + i$.
4. We get $A(1, -1) = (1 - i, i - 1) = (1 - i)(1, -1)$, so $(1, -1)$ is an eigenvector for $1 - i$.
5. The eigenvalues differ, and $\ip{(1, 1)}{(1, -1)} = 1 - 1 = 0$, as the statement predicts.

The typical use is to build an orthonormal eigenbasis: choose an orthonormal basis inside each eigenspace, and put them together.
A trap: inside a single eigenspace, orthogonality is not automatic, and Gram-Schmidt is needed there.

### L3 human

For a normal operator, the eigenspaces are the images of the orthogonal projections in [[the spectral decomposition|~e55cbc04]] $T = \sum \lambda_i P_i$.
The orthogonality of the eigenspaces is the statement $P_i P_j = 0$ for $i \neq j$.
In quantum mechanics, the eigenstates of an observable for different measured values are orthogonal, so the outcomes are mutually exclusive.
For orthogonal polynomials and Fourier series, the orthogonality comes from a self-adjoint differential operator with distinct eigenvalues.
