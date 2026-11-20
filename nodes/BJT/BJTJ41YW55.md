---
tag: BJTJ41YW55
kind: statement
role: theorem
name: Trace of a projection equals its rank
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
about: [0KZDNGA561, 033DA1WE8Y]
uses: [0RPDTWY2JS, 0JGB7A6GTS, 0RH4E3CAV9]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Properties and classification
---

## Statement

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
Let $P \colon V \to V$ be a [[projection|0RH4E3CAV9]], that is, a linear map with $P \circ P = P$.
Then the [[trace|0RPDTWY2JS]] of $P$ and its [[rank|0JGB7A6GTS]] satisfy
$$\tr P = (\rank P) \cdot 1_F.$$
If $F$ has characteristic $0$, for example $F = \mathbb{Q}$, $\R$ or $\C$, then $\tr P = \rank P$ as integers.
In matrix form: an $n \times n$ matrix $A$ with $A^2 = A$ satisfies $\tr A = (\rank A) \cdot 1_F$.

## Remarks

### Why each hypothesis is needed

- The identity $P \circ P = P$ is needed. The map with matrix $2 I_2$ on $\R^2$ has trace $4$ and rank $2$.
- The characteristic caveat is needed. Over $\mathbb{F}_2$, the identity of $\mathbb{F}_2^2$ is a projection of rank $2$, but its trace is $1 + 1 = 0$. So the trace in $F$ only gives the rank modulo $p$ in characteristic $p$.
- $V$ must be finite-dimensional, so that the trace is defined.

### Consequences

- In characteristic $0$, the trace of an idempotent matrix is a nonnegative integer, at most $n$.
- The rank of an idempotent real matrix can be read from its diagonal, with no row reduction.
- The trace of $\id - P$ is $(\dim V - \rank P) \cdot 1_F$, since $\id - P$ is the projection onto $\ker P$.

### Converse

The converse is false: a matrix with $\tr A = \rank A$ need not be a projection.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $\R$, $\tr A = 2$ and $\rank A = 2$.
But $A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \ne A$, so $A$ is not a projection.

### Generalizations

- For a bounded projection on a Hilbert space of finite rank, the same formula holds with the operator trace.
- If $T^2 = cT$ with $c \ne 0$, then $T/c$ is a projection, and $\tr T = c \cdot (\rank T) \cdot 1_F$.

## History

The result is a standard exercise on the trace and appears in many linear algebra courses.

## Explanations

### L1 human

A projection keeps the vectors of its image and kills the vectors of its kernel.
In a basis made of these two kinds of vectors, its matrix is diagonal with entries $1$ and $0$.
The number of entries $1$ is the rank, and their sum is the trace.

### L2 human

The image and the kernel of a projection give a direct sum $V = \im P \oplus \ker P$.
On the image, $P$ acts as the identity, and on the kernel, $P$ acts as $0$.
So $[P]_B = \operatorname{diag}(1, \dots, 1, 0, \dots, 0)$ in an adapted basis, and the trace counts the entries $1$.

### L3 human

The eigenvalues of a projection are among $0$ and $1$, since $x^2 - x$ annihilates it.
The minimal polynomial divides $x(x - 1)$, which has distinct roots, so $P$ is diagonalizable.
The trace is the sum of the eigenvalues, which is the multiplicity of $1$, that is, the rank.
