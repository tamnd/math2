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

A linear map is an orthogonal projection exactly when applying it twice changes nothing and it can be moved across the inner product.

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $P \colon V \to V$ be linear.
Then the following are equivalent.

1. $P = P_U$ is the [[orthogonal projection|0Q8HZTJC7G]] onto some subspace $U$ of $V$.
2. $P^2 = P$, and $\ip{Pv}{w} = \ip{v}{Pw}$ for all $v, w \in V$.

When they hold, $U$ is the image of $P$.
For an $n \times n$ matrix $P$ with the standard inner product on $\mathbb{K}^n$, condition 2 reads $P^2 = P$ and $P^* = P$, where $P^*$ is the [[conjugate transpose|0EX045E2BP]]; over $\R$ it reads $P^2 = P$ and $P^{\mathsf{T}} = P$.

The [[proof|S0GB8AZT9W]] checks the error condition $v - Pv \perp U$ in one direction and computes inner products in the other.

## Remarks

### Why each hypothesis is needed

Idempotence alone is not enough.
The matrix $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ has $P^2 = P$, since its first row $(1, 1)$ times its columns gives $(1, 1)$ again and its second row is zero.
But $P^{\mathsf{T}} \ne P$, and its kernel is the line $x + y = 0$, which is not perpendicular to its image, the $x$-axis.
So it is [[an oblique projection|DZXTTHGFQD]], a [[projection|0RH4E3CAV9]] that is not orthogonal.

Symmetry alone is not enough either.
The matrix $2I$ is symmetric, but $(2I)^2 = 4I \ne 2I$, so it is not a projection of any kind.

Finite dimension of $V$ makes the image $U = \im P$ finite-dimensional, so that $P_U$ is defined by our [[definition|0Q8HZTJC7G]].
In a Hilbert space the theorem survives with closed subspaces, as described below.

### What it gives you

The theorem gives a test that needs no picture: a matrix is an orthogonal projection exactly when it is symmetric and idempotent.
It also gives quick consequences.
The map $I - P$ is again an orthogonal projection, since $(I - P)^2 = I - 2P + P^2 = I - P$ and $I - P$ is self-adjoint.
The eigenvalues of $P$ lie in $\{0, 1\}$, with eigenspaces $\ker P = U^\perp$ and $\im P = U$, and these are orthogonal.
An orthogonal projection never increases length, because
$$\norm{Pv}^2 = \norm{v}^2 - \norm{v - Pv}^2 \le \norm{v}^2.$$

### A test by length

The last property has a converse: an idempotent $P$ with $\norm{Pv} \le \norm{v}$ for every $v$ is an orthogonal projection.
Here is the reason in outline.
Take $u \in \im P$ and $w \in \ker P$; then $P(u + tw) = u$ for every scalar $t$, so $\norm{u} \le \norm{u + tw}$.
So $0$ is the closest point of the line $\mathbb{K} w$ to $u$, and the [[best approximation theorem|0MCDDSCB9Z]] gives $\ip{u}{w} = 0$.
Hence $\ker P \perp \im P$, and $P$ is the orthogonal projection onto its image.
The oblique projection above fails the length test: it sends $(1, 1)$, of length $\sqrt{2}$, to $(2, 0)$, of length $2$.

### Generalizations

The condition $\ip{Pv}{w} = \ip{v}{Pw}$ says that $P$ is [[self-adjoint|0NEGN5CRSC]].
In a Hilbert space, the orthogonal projections onto closed subspaces are exactly the bounded linear maps with $P^2 = P$ and $P^* = P$, where $P^*$ is the [[adjoint|0R9NMSM1ZP]].
In a C*-algebra, an element $p$ with $p = p^2 = p^*$ is called a projection, and the theorem explains that name.

## Explanations

### L1 human

A projection is a map that does nothing the second time you apply it.
Among the projections, the orthogonal ones are those whose matrix is symmetric, the same when you flip it across the diagonal.
For example, the shadow map onto the floor sends $(x, y, z)$ to $(x, y, 0)$, and its matrix has $1, 1, 0$ on the diagonal and zeros elsewhere, which is symmetric.

### L2 human

Here is a typical check: is $P = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ an orthogonal projection?
The matrix equals its transpose, so it is symmetric.
Square it:
$$P^2 = \frac{1}{4} \begin{pmatrix} 1 + 1 & 1 + 1 \\ 1 + 1 & 1 + 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = P.$$
So $P$ is the orthogonal projection onto its image, the line $\R(1, 1)$, as in [[the projection onto the line spanned by (1, 1)|MAP4F54GJW]].
The same two checks catch arithmetic mistakes when you compute a projection matrix by hand.
Watch out: one check alone proves nothing, as the two examples above show.

### L3 human

On a finite-dimensional space, the orthogonal projections correspond one to one with the subspaces, and the order $P \le Q$ given by $PQ = P$ matches the inclusion of images.
Two orthogonal projections commute exactly when their product is again an orthogonal projection, and then the product projects onto the intersection of the two images.
In the spectral theorems of the sub-area on [[operators on inner product spaces|3YM9EK6VMB]], every self-adjoint operator becomes a combination $\sum_i \lambda_i P_i$ of such projections.
