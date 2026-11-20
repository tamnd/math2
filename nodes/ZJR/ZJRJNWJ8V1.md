---
tag: ZJRJNWJ8V1
kind: statement
role: theorem
name: Orthogonal projections are the self-adjoint idempotents
msc: [15A04, 47A05]
topics: [8GQVME4SZZ]
audience: ug1
about: [0B8KZRT28M]
uses: [0Q8HZTJC7G, 0RH4E3CAV9, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Orthogonal projections
  - book: isbn:9783031410253
    locator: Section 6C
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $P \colon V \to V$ be linear.
Then the following are equivalent:

1. $P = P_U$ is the [[orthogonal projection|0Q8HZTJC7G]] onto some subspace $U$ of $V$.
2. $P^2 = P$, and $\ip{Pv}{w} = \ip{v}{Pw}$ for all $v, w \in V$.

When they hold, $U$ is the image of $P$.
For an $n \times n$ matrix $P$ with the standard inner product on $\mathbb{K}^n$, condition 2 reads $P^2 = P$ and $P^* = P$, where $P^*$ is the [[conjugate transpose|0EX045E2BP]]; over $\R$ it reads $P^2 = P$ and $P^{\mathsf{T}} = P$.

The [[proof|S0GB8AZT9W]] checks the error condition $v - Pv \perp U$ in one direction and computes inner products in the other.

## Remarks

### Why each hypothesis is needed

- The idempotent condition alone is not enough: $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ satisfies $P^2 = P$ but $P^{\mathsf{T}} \ne P$. It is [[an oblique projection|DZXTTHGFQD]] onto the $x$-axis along the line $\R(1, -1)$.
- The symmetry condition alone is not enough: $P = 2I$ is symmetric, but $P^2 = 4I \ne P$.
- Finite dimension of $V$ makes $U = \im P$ finite-dimensional, so $P_U$ is defined by our [[definition|0Q8HZTJC7G]].

### Consequences

- An orthogonal projection does not increase length: $\norm{Pv}^2 = \norm{v}^2 - \norm{v - Pv}^2 \le \norm{v}^2$.
- The eigenvalues of an orthogonal projection are among $0$ and $1$. The eigenspaces are $\ker P = U^\perp$ and $\im P = U$, and they are orthogonal.
- If $P$ is an orthogonal projection, then so is $I - P$, since $(I - P)^2 = I - 2P + P^2 = I - P$ and $I - P$ is self-adjoint.

### Converse

The statement is an equivalence.
A related fact replaces symmetry by a norm condition: an idempotent $P$ with $\norm{Pv} \le \norm{v}$ for all $v$ is an orthogonal projection.
We do not prove that fact here.
The oblique projection above fails it: it maps $(1, 1)$, of norm $\sqrt{2}$, to $(2, 0)$, of norm $2$.

### Generalizations

In a Hilbert space, the orthogonal projections onto closed subspaces are exactly the bounded linear maps $P$ with $P^2 = P$ and $P^* = P$, where $P^*$ is the [[adjoint|0R9NMSM1ZP]].
The condition $\ip{Pv}{w} = \ip{v}{Pw}$ says that $P$ is [[self-adjoint|0NEGN5CRSC]].

## Explanations

### L1 human

A projection is a map that does nothing the second time you apply it.
It is orthogonal exactly when its matrix is symmetric.
A symmetric matrix that does nothing the second time is a perpendicular shadow onto its image.

### L2 human

We test $P = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

1. $P^{\mathsf{T}} = P$, because the matrix is symmetric.
2. $P^2 = \frac{1}{4} \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = P$.
3. So $P$ is the orthogonal projection onto its image $\R(1, 1)$, as in [[the projection onto the line spanned by (1, 1)|MAP4F54GJW]].

The typical use is to check a computed projection matrix: it must be symmetric and idempotent.
The trap is to check only one of the two conditions.

### L3 human

In a C*-algebra, an element $p$ with $p = p^2 = p^*$ is called a projection, and this theorem explains the name.
The orthogonal projections of a finite-dimensional space form a lattice isomorphic to the lattice of subspaces.
Two orthogonal projections commute exactly when their product is again an orthogonal projection, onto the intersection of their images.
