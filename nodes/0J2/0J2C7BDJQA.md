---
tag: 0J2C7BDJQA
kind: statement
role: theorem
name: Polar decomposition
msc: [15A23]
topics: [SS4EVPKT3A]
audience: ug2
about: [0AR68JTMDT, 01MMVW8CKC]
uses: [0D6RMJ10M9, 0880F9EQCP, EQ98KW1ZN4, 0EX045E2BP]
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

The polar decomposition writes every square matrix as a rigid motion times a stretch along perpendicular axes, just as $z = e^{i\theta} r$ writes a complex number as a unit number times a length.
Let $A$ be an $n \times n$ complex matrix, and let $A^*$ be its [[conjugate transpose|0EX045E2BP]].

1. Existence. There are a [[unitary matrix|0AR68JTMDT]] $U$ and a [[positive semidefinite|01MMVW8CKC]] matrix $P$ with $A = UP$.
2. The stretch is unique. In every such factorization, $P = (A^* A)^{1/2}$, the [[positive semidefinite square root|EQ98KW1ZN4]] of $A^* A$.
3. Invertible case. If $A$ is invertible, then $P$ is positive definite, and $U = A P^{-1}$ is unique.
4. Real case. If $A$ is real, then $P$ is real, and $U$ can be chosen real orthogonal.
5. Left form. With the same $U$, we also have $A = P' U$ with $P' = U P U^* = (A A^*)^{1/2}$.

The [[proof from the square root of A*A|M76S68K6YD]] proves all five parts.

## Remarks

### A first decomposition

Take $A = \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix}$, which is invertible since $\det A = -1 + 4 = 3$.
First form $A^{\mathsf{T}} A$ and take its square root:
$$A^{\mathsf{T}} A = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}, \qquad P = (A^{\mathsf{T}} A)^{1/2} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.$$
Then part 3 gives the rotation:
$$U = A P^{-1} = \tfrac13 \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
Check: $UP = \begin{pmatrix} 0 \cdot 2 - 1 & 0 - 2 \\ 2 + 0 & 1 + 0 \end{pmatrix} = A$.
So $A$ first stretches by $3$ along $(1, 1)$ and by $1$ along $(1, -1)$, and then turns the plane by a quarter turn.
[[The worked example|3PBTVVRPD1]] checks every step and finds the left form as well.

### The complex numbers as the case n = 1

For $n = 1$, a matrix is one complex number $z$, the adjoint is $\bar z$, and $A^* A = \abs{z}^2$.
So $P = \abs z$, and for $z \ne 0$ the unitary factor is $U = z / \abs z = e^{i\theta}$.
This is the [[polar form|0BRXFNQ5JV]] $z = e^{i\theta} r$ with $r = \abs z$, and it gives the theorem its name.
The analogy also predicts what happens at $z = 0$: then $r = 0$, and every angle $\theta$ works, so the unit factor is not unique.

### When is U unique?

The unitary factor is unique exactly when $A$ is invertible.
If $A$ is invertible, part 3 forces $U = A P^{-1}$.
If $A$ is singular, then $P$ is singular too, since $\abs{\det A} = \det P$, so there is a unit vector $v$ with $Pv = 0$.
Let $U' = U (I - 2 v v^*)$, where $I - 2 v v^*$ is the reflection in the hyperplane orthogonal to $v$.
Then $U'$ is unitary, $U' \ne U$, and $U' P = UP - 2 U v (Pv)^* = UP = A$, because $v^* P = (Pv)^*$.
For example, $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ has $P = A$, and $U = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$ works for every real $\theta$.

The factor $P$ needs its positivity to be unique.
Since $A = (-U)(-P)$, dropping the condition $P \succeq 0$ always allows a second factorization.

### Invertible real matrices as a product of two sets

For real invertible matrices, parts 3 and 4 say that the map $(U, P) \mapsto UP$ is a bijection from $O(n) \times \{ P : P \text{ positive definite} \}$ onto $GL_n(\R)$, where $O(n)$ is the [[orthogonal group|0TKYAEJ8N7]].
This is a statement about sets, not about groups.
The positive definite matrices are not closed under multiplication, and $GL_n(\R)$ is not the direct product of the two factors as a group.
The same holds over $\C$ with the [[unitary group|0R9R0Y1HDK]] $U(n)$ in place of $O(n)$.

### What it gives you

Taking determinants gives $\abs{\det A} = \det P$, because $\abs{\det U} = 1$, so the volume factor of $A$ lives entirely in $P$.
The eigenvalues of $P$ are the [[singular values|09VMDSRXWJ]] of $A$.
If we diagonalize $P = V \Sigma V^*$, then $A = (U V) \Sigma V^*$, which is the [[singular value decomposition|000NPTMX6J]].
The factors can be chosen to commute, $UP = PU$, exactly when $A$ is [[normal|0MR0BYF0K2]].
For instance, if $UP = PU$, then $A A^* = U P^2 U^* = P^2 = A^* A$.

### Watch out

The factor $P$ comes from $A^* A$, not from $A A^*$.
In the first decomposition, $(A A^{\mathsf{T}})^{1/2} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, and this is the left factor $P'$ in $A = P' U$, not the right factor.
The matrix of absolute values of the entries, $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, is not $P$ either, since it has the eigenvalue $-1$.
For a rectangular $m \times n$ matrix with $m \ge n$, the same proof gives $A = UP$ with $U$ of size $m \times n$ with orthonormal columns, not a unitary matrix.

### Try it

First, find the polar decomposition of $A = \operatorname{diag}(-2, 3)$.
Here $A^{\mathsf{T}} A = \operatorname{diag}(4, 9)$, so $P = \operatorname{diag}(2, 3)$ and $U = \operatorname{diag}(-1, 1)$, a reflection.

Second, decompose $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$.
You get $A^{\mathsf{T}} A = \operatorname{diag}(1, 4)$, $P = \operatorname{diag}(1, 2)$ and $U = A P^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, and $UP = A$.

## History

Léon Autonne studied the polar decomposition of matrices in 1902.

## Explanations

### L1 human

A nonzero complex number is a positive length times a number of size one: $z = r e^{i\theta}$.
A square matrix splits in the same way.
First a stretch $P$ pulls space along perpendicular axes by factors that are not negative.
Then a rigid motion $U$, a rotation or a reflection, moves the result without changing any length.
For $\begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix}$, the stretch has factors $3$ and $1$, and the rigid motion is a quarter turn.

### L2 human

Here is the recipe for an invertible $A$, with $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ as a running case.
Compute $A^* A$, here $\operatorname{diag}(1, 4)$.
Take its square root by diagonalizing, here $P = \operatorname{diag}(1, 2)$.
Finally set $U = A P^{-1}$, here $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, and check that $U^* U = I$ and $UP = A$.
The typical use is to separate the change of shape, $P$, from the rigid motion, $U$, as in continuum mechanics, where a deformation gradient splits into a rotation and a stretch.
The trap is to build $P$ from $A A^*$, which gives the left factor instead.

### L3 human

Part 3 over $\C$ says that $GL_n(\C) = U(n) \cdot \{ \text{positive definite matrices} \}$ with unique factors.
Every positive definite matrix is $e^H$ for exactly one Hermitian $H$, so $GL_n(\C)$ is homeomorphic to $U(n) \times \R^{n^2}$, and $U(n)$ is a deformation retract of $GL_n(\C)$.
This is the prototype of the Cartan decomposition of a reductive Lie group.
The SVD and the polar decomposition carry the same information, since each follows from the other by diagonalizing $P$ or by setting $P = V \Sigma V^*$.
For bounded operators on a Hilbert space, the polar decomposition uses a partial isometry in place of $U$, and that belongs to functional analysis.
