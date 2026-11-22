---
tag: BFQQDA489F
kind: statement
role: theorem
name: Simultaneous unitary diagonalization of commuting normal operators
aliases: [simultaneous-unitary-diagonalization, commuting-normal-matrices-are-simultaneously-diagonalizable]
msc: ["15A21", "47B15"]
topics: [3YM9EK6VMB]
audience: ug2
about: [0C8BR8XRTR]
uses: [0ENZN5G4CV, 0MB8HQW495, 0FWJ0VW561, 0B5H4208Z9, 0D6RMJ10M9, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: Consequences
---

## Statement

A family of normal operators can be made diagonal by one orthonormal basis exactly when its members commute with each other.

1. Complex case. Let $V$ be a finite-dimensional complex inner product space, and let $\mathcal{F}$ be a set of [[normal|0ENZN5G4CV]] operators on $V$. Then $V$ has an [[orthonormal basis|0FWJ0VW561]] whose vectors are [[eigenvectors|0B5H4208Z9]] of every member of $\mathcal{F}$ if and only if $S T = T S$ for all $S, T \in \mathcal{F}$.
2. Real case. The same holds for a finite-dimensional real inner product space and a set $\mathcal{F}$ of [[self-adjoint|0MB8HQW495]] operators.
3. Matrix form. Let $A_1, \dots, A_k$ be complex normal $n \times n$ matrices. There is one [[unitary matrix|0D6RMJ10M9]] $U$ such that every $U^* A_j U$ is diagonal if and only if $A_i A_j = A_j A_i$ for all $i$ and $j$. For real symmetric matrices, $U$ can be taken to be a real [[orthogonal matrix|0QRBVFJ50X]].

## Remarks

### A first example

Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Both are symmetric, and $A = 2I + B$, so $AB = 2B + B^2 = BA$.
The vectors $(1, 1)$ and $(1, -1)$ are eigenvectors of both:
$$A(1, 1) = 3(1, 1), \quad A(1, -1) = (1, -1), \quad B(1, 1) = (1, 1), \quad B(1, -1) = -(1, -1).$$
So $Q = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ gives $Q^{\mathsf{T}} A Q = \operatorname{diag}(3, 1)$ and $Q^{\mathsf{T}} B Q = \operatorname{diag}(1, -1)$ at the same time.
The [[pair of symmetric matrices|2YEX40VH77]] works through this case and a pair that does not commute.

### Why each hypothesis is needed

Commuting is needed.
The symmetric matrices $\operatorname{diag}(1, -1)$ and $B$ above do not commute, since their two products are $\pm \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
The eigenvectors of $\operatorname{diag}(1, -1)$ are the multiples of $e_1$ and of $e_2$, and $B$ swaps $e_1$ and $e_2$, so the two matrices have no common eigenvector.

Normality is needed for the basis to be orthonormal.
The single matrix with rows $(1, 1)$ and $(0, 2)$ commutes with itself, but it has [[no orthonormal eigenbasis|5RQ7EC5RC6]].
Commuting diagonalizable matrices always share a basis of eigenvectors, but without normality that basis need not be orthonormal.
Over $\mathbb{R}$, normal operators are not enough: the [[rotation by a right angle|1CF483TZZA]] commutes with itself and has no real eigenvector, so the real case asks for self-adjoint operators.

### What it gives you

Commuting Hermitian matrices have one unitary $U$ that makes them all real diagonal.
If $S$ and $T$ are commuting normal operators, then $S + T$ and $S T$ are normal, because they are diagonal in the common basis.
Every operator is $T = H + iK$ with $H = \tfrac{1}{2}(T + T^*)$ and $K = \tfrac{1}{2i}(T - T^*)$ self-adjoint, and $T$ is normal exactly when $HK = KH$.
For normal $T$, a common eigenbasis of $H$ and $K$ with eigenvalues $\alpha_j$ and $\beta_j$ diagonalizes $T$ with the eigenvalues $\alpha_j + i \beta_j$.
In quantum mechanics, commuting observables have a common basis of eigenstates, which leads to a [[complete set of commuting observables|MHTQ5MFFZG]].

### The converse

The direction "if" is the short one.
In a common orthonormal eigenbasis, every member of $\mathcal{F}$ has a diagonal matrix, and diagonal matrices commute.
The [[proof|NTYR1HB9R3]] of the other direction splits the space into the eigenspaces of one member and uses induction.

### Watch out

When one matrix has a repeated eigenvalue, its eigenspace has many orthonormal bases, and only some of them diagonalize the other matrices.
For example, the identity $I_2$ commutes with $B$, and the standard basis diagonalizes $I_2$ but not $B$.
The correct move is to diagonalize $B$ inside each eigenspace of the first matrix.

### Try it

Do $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ and $C = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ have a common orthonormal eigenbasis?
Yes: $A = I + 2B$ and $C = 3I + B$ with $B$ as above, so they commute, and $\tfrac{1}{\sqrt{2}}(1, 1)$ and $\tfrac{1}{\sqrt{2}}(1, -1)$ diagonalize both, with eigenvalues $3, -1$ for $A$ and $4, 2$ for $C$.

## Explanations

### L1 human

Two symmetric matrices that commute share a set of perpendicular special directions.
Along each of these directions, both matrices just multiply by a number.
So one turn of the coordinate axes makes both matrices diagonal at once.
If the matrices do not commute, no such shared directions exist.

### L2 human

Here is a typical use, with a repeated eigenvalue.
Let $A = \operatorname{diag}(1, 1, 2)$ and $B = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$.
Both products equal $\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 10 \end{pmatrix}$, so $AB = BA$.
The standard basis diagonalizes $A$ but not $B$, so we look inside the eigenspace of $A$ for $1$, the plane spanned by $e_1$ and $e_2$.
There $B$ acts as $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, with the orthonormal eigenvectors $\tfrac{1}{\sqrt{2}}(1, 1, 0)$ and $\tfrac{1}{\sqrt{2}}(1, -1, 0)$ for $1$ and $-1$.
Together with $e_3$ these form the columns of an orthogonal $Q$, and
$$Q^{\mathsf{T}} A Q = \operatorname{diag}(1, 1, 2), \qquad Q^{\mathsf{T}} B Q = \operatorname{diag}(1, -1, 5).$$
This is exactly how the proof works: the eigenspaces of one matrix are invariant under the others, and we diagonalize inside them.

### L3 human

The members of $\mathcal{F}$, their adjoints and $I$ generate a commutative algebra of operators that is closed under taking adjoints.
The theorem says that this algebra is unitarily equivalent to an algebra of diagonal matrices.
In infinite dimension, a commutative [[von Neumann algebra|F12V24NF4R]] plays this role, and the diagonal matrices become multiplication operators on a measure space.
The step that $B^*$ commutes with every operator that commutes with $B$ is the finite-dimensional case of [[Fuglede's theorem|V1C28937NX]].
