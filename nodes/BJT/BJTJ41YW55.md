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

The trace of a projection counts the dimension of its image.
Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
Let $P \colon V \to V$ be a [[projection|0RH4E3CAV9]], that is, a linear map with $P \circ P = P$.
Then the [[trace|0RPDTWY2JS]] of $P$ and its [[rank|0JGB7A6GTS]] satisfy
$$\tr P = (\rank P) \cdot 1_F.$$
If $F$ has characteristic $0$, for example $F = \mathbb{Q}$, $\mathbb{R}$ or $\mathbb{C}$, then $\tr P = \rank P$ as integers.
In matrix form, an $n \times n$ matrix $A$ with $A^2 = A$ satisfies $\tr A = (\rank A) \cdot 1_F$.

## Remarks

### What it gives you

In characteristic $0$, the trace of an idempotent matrix is a nonnegative integer, at most $n$.
The rank of an idempotent real matrix can be read from its diagonal, with no row reduction.
For example, $A = \tfrac{1}{5}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ satisfies $A^2 = \tfrac{1}{25}\begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix} = A$, so its rank is $\tr A = \tfrac{1}{5} + \tfrac{4}{5} = 1$.
The map $\mathrm{id} - P$ is the projection onto $\ker P$, so $\tr(\mathrm{id} - P) = (\dim V - \rank P) \cdot 1_F$.

### Why each hypothesis is needed

The identity $P \circ P = P$ is needed.
The map with matrix $2 I_2$ on $\mathbb{R}^2$ has trace $4$ and rank $2$.

The characteristic matters for the equality of integers.
Over $\mathbb{F}_2$, the identity of $\mathbb{F}_2^2$ is a projection of rank $2$, but its trace is $1 + 1 = 0$, as the [[worked example|BJ3ZVHZ6VF]] shows.
In characteristic $p$ the trace only gives the rank modulo $p$.

The space $V$ must be finite-dimensional, so that the trace is defined.

### The converse

The converse is false: a matrix with $\tr A = \rank A$ need not be a projection.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{R}$, $\tr A = 2$ and $\rank A = 2$.
But $A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \ne A$, so $A$ is not a projection.

### Generalizations

If $T^2 = cT$ with $c \ne 0$, then $(T/c)^2 = T/c$, so $T/c$ is a projection, and $\tr T = c \cdot (\rank T) \cdot 1_F$.
For a bounded projection of finite rank on a Hilbert space, the same formula holds with the operator trace.
The [[proof|NXAVS73SDP]] splits $V$ into the image and the kernel of $P$.

## Explanations

### L1 human

A projection keeps the vectors of its image and sends the vectors of its kernel to $0$.
In a basis made of these two kinds of vectors, its matrix is diagonal with entries $1$ and $0$.
The number of entries $1$ is the rank, and their sum is the trace.

### L2 human

The image and the kernel of a projection give a direct sum $V = \operatorname{im} P \oplus \ker P$.
On the image $P$ acts as the identity, and on the kernel $P$ acts as $0$.
So $[P]_B = \operatorname{diag}(1, \dots, 1, 0, \dots, 0)$ in an adapted basis, and the trace counts the entries $1$.
Watch out: over a field of characteristic $p$, the count is only seen modulo $p$.

### L3 human

The polynomial $x^2 - x$ annihilates a projection, so its eigenvalues lie among $0$ and $1$.
The minimal polynomial divides $x(x - 1)$, which has distinct roots, so $P$ is diagonalizable.
The trace is the sum of the eigenvalues, which is the multiplicity of $1$ times $1_F$, and that multiplicity is $\dim \operatorname{im} P$, the rank.
