---
tag: D5KVBA1K9R
kind: statement
role: theorem
name: Spectral decomposition of a normal operator
aliases: [resolution-of-the-identity, spectral-decomposition]
msc: ["15A18", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0C8BR8XRTR, 0NEGN5CRSC]
uses: [04CW1P44VD, 06J4PXRG22, 0JHGAV9H25, 0Q8HZTJC7G, 0AYEPBQMAW, 0ENZN5G4CV, 0MB8HQW495]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - book: isbn:9780134860244
    locator: Section 6.6
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Statement

The spectral decomposition writes an operator with an orthonormal eigenbasis as a sum of its eigenvalues times the orthogonal projections onto its eigenspaces.

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to V$ be linear, and assume that $V$ has an orthonormal basis of eigenvectors of $T$.
This holds for every [[normal|0ENZN5G4CV]] $T$ when $\mathbb{K} = \mathbb{C}$, and for every [[self-adjoint|0MB8HQW495]] $T$ when $\mathbb{K} = \mathbb{R}$.
Let $\lambda_1, \dots, \lambda_m$ be the distinct eigenvalues of $T$, let $E_i$ be the [[eigenspace|0AYEPBQMAW]] of $\lambda_i$, and let $P_i$ be the [[orthogonal projection|0Q8HZTJC7G]] onto $E_i$.

1. Resolution of the identity. Each $P_i$ is self-adjoint with $P_i^2 = P_i$, we have $P_i P_j = 0$ for $i \neq j$, and $P_1 + \dots + P_m = I$.
2. Spectral decomposition. $T = \lambda_1 P_1 + \dots + \lambda_m P_m$.
3. Polynomials. $p(T) = p(\lambda_1) P_1 + \dots + p(\lambda_m) P_m$ for every polynomial $p$ with coefficients in $\mathbb{K}$.
4. Projections as polynomials. Each $P_i$ is a polynomial in $T$, namely
$$P_i = \prod_{j \neq i} \frac{T - \lambda_j I}{\lambda_i - \lambda_j}.$$
5. The adjoint. $T^* = \overline{\lambda_1} P_1 + \dots + \overline{\lambda_m} P_m$, and $T^*$ is a polynomial in $T$.

## Remarks

### A first decomposition

Take the symmetric matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$, with eigenvalues $6$ and $1$ and eigenvectors $(2, 1)$ and $(1, -2)$.
Part 4 gives the two projections without any normalization:
$$P_1 = \frac{A - I}{6 - 1} = \frac{1}{5} \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}, \qquad P_2 = \frac{A - 6I}{1 - 6} = \frac{1}{5} \begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}.$$
Check: $P_1 + P_2 = I$ and $6 P_1 + P_2 = \tfrac{1}{5} \begin{pmatrix} 25 & 10 \\ 10 & 10 \end{pmatrix} = A$.
The [[worked example|MK4ET9TW4Q]] has the details, and the [[matrix I + J|PAJVDWFC9Q]] shows a repeated eigenvalue, where one projection has rank $2$.

### Why the orthonormal eigenbasis is needed

Without an orthonormal eigenbasis, the projections lose their orthogonality.
The [[matrix with rows (1, 1) and (0, 2)|5RQ7EC5RC6]] is diagonalizable, and the formula of part 4 still gives $A = 1 \cdot P_1 + 2 \cdot P_2$ with $P_1 = 2I - A$ and $P_2 = A - I$.
But $P_2 = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ is not symmetric, so it projects onto its image along a line that is not perpendicular to it.
Without any basis of eigenvectors, part 2 fails outright.
The [[shear|BF9MKKHH4Z]] with rows $(1, 1)$ and $(0, 1)$ has the single eigenvalue $1$ with eigenspace spanned by $e_1$, and $1 \cdot P_1$ is not the shear.

### Functions of an operator

Part 3 suggests a definition for any function $f$ on the eigenvalues:
$$f(T) = f(\lambda_1) P_1 + \dots + f(\lambda_m) P_m.$$
This agrees with $p(T)$ for every polynomial $p$ with $p(\lambda_i) = f(\lambda_i)$ for all $i$, so it extends the polynomials consistently.
A self-adjoint $T$ with all $\lambda_i \geq 0$ gets the [[square root|0BJVDCF38Y]] $\sqrt{T} = \sum_i \sqrt{\lambda_i}\, P_i$, which is self-adjoint with nonnegative eigenvalues and squares to $T$.
If no $\lambda_i$ is $0$, then $T^{-1} = \sum_i \lambda_i^{-1} P_i$, and in the same way $e^{T} = \sum_i e^{\lambda_i} P_i$ is the [[matrix exponential|0K665H5V1S]].
Part 5 shows that $T^*$ commutes with every operator that commutes with $T$, which drives [[simultaneous unitary diagonalization|BFQQDA489F]].

### The converse

Over $\mathbb{C}$, every operator $T = \sum_i \lambda_i P_i$ is normal when the $P_i$ are self-adjoint projections with $P_i P_j = 0$ for $i \neq j$.
Indeed $T^* = \sum_i \overline{\lambda_i} P_i$, and both $T T^*$ and $T^* T$ equal $\sum_i \abs{\lambda_i}^2 P_i$.
If in addition every $\lambda_i$ is real, then $T^* = T$.

### Watch out

The sum runs over the distinct eigenvalues, and each $P_i$ projects onto the whole eigenspace.
For $I + J$ on $\mathbb{R}^3$, the eigenvalue $1$ has a $2$-dimensional eigenspace, so the decomposition has two terms, not three.
If you write one term for each eigenvector, the terms depend on a choice of basis, while $P_i$ does not.

### Try it

Find the spectral decomposition of $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, and use it to compute $B^{10}$.
Part 4 gives $P_1 = \tfrac{1}{2}(B + I)$ for $\lambda = 1$ and $P_2 = \tfrac{1}{2}(I - B)$ for $\lambda = -1$, so $B = P_1 - P_2$ and $B^{10} = P_1 + P_2 = I$.

## Explanations

### L1 human

A normal operator splits the space into perpendicular eigenspaces.
On each eigenspace it multiplies every vector by one number.
So you can compute $Tv$ in three moves: cast the shadow of $v$ on each eigenspace, multiply each shadow by its eigenvalue, and add the results.
To apply a function to the operator, apply it to each eigenvalue and keep the shadows.

### L2 human

Here is a typical use: compute $A^{n}$ for $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ and every $n \geq 0$.
With the projections of the first remark, part 3 gives
$$A^n = 6^n P_1 + P_2 = \frac{1}{5} \begin{pmatrix} 4 \cdot 6^n + 1 & 2 \cdot 6^n - 2 \\ 2 \cdot 6^n - 2 & 6^n + 4 \end{pmatrix}.$$
Check: for $n = 1$ this is $\tfrac{1}{5} \begin{pmatrix} 25 & 10 \\ 10 & 10 \end{pmatrix} = A$, and for $n = 0$ it is $I$.
For large $n$, the term $6^n P_1$ dominates, so $A^n v$ points almost along $(2, 1)$ for most starting vectors $v$.
This is the idea behind the power method for the largest eigenvalue.
Watch out: the formula needs the distinct eigenvalues and the projections onto whole eigenspaces.

### L3 human

Part 1 says that $E \mapsto \sum_{\lambda_i \in E} P_i$ is a projection-valued measure on the finite set of eigenvalues.
The map $f \mapsto f(T)$ is then an algebra homomorphism from the functions on the spectrum to the operators, and it sends $\overline{f}$ to $f(T)^*$.
For a normal element of a $C^*$-algebra, the [[continuous functional calculus|JB7S6WPZ77]] extends this map to continuous functions on the spectrum.
For bounded normal operators on a Hilbert space, the finite sum becomes an integral against a projection-valued measure, as in the [[spectral theorem for bounded normal operators|X71XRPJR7D]].
