---
tag: 0J2C7BDJQA
kind: statement
role: theorem
name: Polar decomposition
msc: [15A23]
topics: [SS4EVPKT3A]
audience: ug2
about: [0AR68JTMDT, 01MMVW8CKC]
uses: [0D6RMJ10M9, 0880F9EQCP, ~21ece919, 0EX045E2BP]
proofs: [M76S68K6YD]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_decomposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Polar_decomposition
    locator: General derivation
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780521839402
    locator: Chapter 7
same_as:
  wikidata: Q2101158
  wikipedia: Polar decomposition
---

## Statement

Let $A$ be an $n \times n$ complex matrix.

1. There are a [[unitary matrix|0AR68JTMDT]] $U$ and a [[positive semidefinite|01MMVW8CKC]] matrix $P$ with
$$A = UP.$$
2. The factor $P$ is unique: $P = (A^* A)^{1/2}$, the [[positive semidefinite square root|~21ece919]] of $A^* A$.
3. If $A$ is invertible, then $P$ is positive definite, and $U = A P^{-1}$ is unique.
4. If $A$ is real, then $U$ can be chosen real orthogonal, and $P$ is real.
5. With the same $U$, $A = P' U$ with $P' = U P U^* = (A A^*)^{1/2}$. This is the *left polar decomposition*.

## Remarks

### Why each hypothesis is needed

- For a singular $A$, the unitary factor is not unique. For $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, we have $P = A$, and $U = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$ works for every real $\theta$.
- The condition $P \succeq 0$ is needed for uniqueness of $P$. Since $A = (-U)(-P)$, dropping it allows the second factor $-P$.
- $A$ must be square for $U$ to be unitary. For an $m \times n$ matrix the same proof gives $U$ with orthonormal columns when $m \ge n$.

### Consequences

- [[The $2 \times 2$ example|~532a4bf7]] writes $\begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix}$ as a rotation by $90^\circ$ times $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
- For real invertible matrices, $(U, P) \mapsto UP$ is a bijection from $O(n) \times \set{\text{positive definite } P}$ onto $GL_n(\R)$. The [[orthogonal group|0TKYAEJ8N7]] is the first factor.
- $\abs{\det A} = \det P$, since $\abs{\det U} = 1$.
- The eigenvalues of $P$ are the [[singular values|09VMDSRXWJ]] of $A$.

### Converse

If $U$ is unitary and $P$ is positive semidefinite, then $UP$ is some $n \times n$ matrix; there is no condition to check.
The content of the theorem is that every square matrix arises, and that $P$ is determined by $A$.

### Generalizations

- For $n = 1$, it is the [[polar form|0BRXFNQ5JV]] $z = e^{i\theta} r$ of a complex number, with $r = \abs z = (\bar z z)^{1/2}$.
- $A$ is [[normal|0MR0BYF0K2]] if and only if $U$ and $P$ can be chosen to commute.
- Bounded operators on a Hilbert space have a polar decomposition with a partial isometry in place of $U$; this belongs to functional analysis.

## History

The polar decomposition of matrices was introduced by Léon Autonne in 1902, according to the Wikipedia article on the polar decomposition.

## Explanations

### L1 human

A nonzero complex number is a positive length times a unit number: $z = r e^{i\theta}$.
A square matrix is in the same way a stretch times a rotation, possibly with a reflection.
The stretch $P$ pulls space along perpendicular axes by nonnegative factors.
The rotation $U$ keeps all lengths.
The stretch is always unique.

### L2 human

Recipe for an invertible $A$:

1. Compute $A^* A$.
2. Compute its square root $P = (A^* A)^{1/2}$, by diagonalizing $A^* A$.
3. Compute $U = A P^{-1}$.

[[The $2 \times 2$ example|~532a4bf7]] follows this recipe.
A trap: $P$ comes from $A^* A$ and not from $A A^*$.
The matrix $(A A^*)^{1/2}$ is the factor of the left decomposition $A = P' U$.

### L3 human

In group terms, part 3 says $GL_n(\C) = U(n) \cdot \set{\text{positive definite}}$, with unique factors.
The positive definite matrices are $\exp$ of the Hermitian matrices, so $GL_n(\C)$ is homeomorphic to $U(n) \times \R^{n^2}$, and $U(n)$ is a deformation retract of $GL_n(\C)$.
This is the prototype of the Cartan decomposition of a reductive Lie group.
The [[singular value decomposition|000NPTMX6J]] follows from the polar decomposition by diagonalizing $P$, and the converse also holds.
