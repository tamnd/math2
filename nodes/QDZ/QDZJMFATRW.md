---
tag: QDZJMFATRW
kind: statement
role: theorem
name: Determinant and eigenvalues of an orthogonal matrix
aliases: [orthogonal-matrix-determinant-plus-or-minus-one, eigenvalues-of-orthogonal-matrix-on-unit-circle]
msc: ["15B10", "15A18"]
topics: [AZS5BPF5H3]
audience: ug1
about: [0W02QESPJQ, 00KDZRW4C0, 0BQAA2BK3Q]
uses: [0QRBVFJ50X, 0C3CFHDN6R, 0ZND7NQ970, 039HF58KQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Matrix properties
  - book: isbn:9780134860244
    locator: Section 6.5
---

## Statement

A matrix that keeps all lengths can neither change volumes nor stretch any eigenvector, so its determinant is $\pm 1$ and its eigenvalues lie on the unit circle.
Let $Q$ be a real $n \times n$ [[orthogonal matrix|0QRBVFJ50X]].

1. The [[determinant|0C3CFHDN6R]] of $Q$ is $1$ or $-1$.
2. Every complex root $\lambda$ of the [[characteristic polynomial|039HF58KQ5]] of $Q$ has $\abs{\lambda} = 1$. In particular, every real [[eigenvalue|0ZND7NQ970]] of $Q$ is $1$ or $-1$.
3. The non-real roots come in pairs $\lambda$, $\bar\lambda$ with the same multiplicity, and $\bar\lambda = \lambda^{-1}$.

## Remarks

### Why each hypothesis is needed

Without orthogonality, part 1 fails: $\operatorname{diag}(2, 1)$ has determinant $2$.
Part 2 can fail even when part 1 holds.
The matrix $\operatorname{diag}(2, \frac{1}{2})$ has determinant $1$, but its eigenvalues $2$ and $\frac{1}{2}$ are off the unit circle, and it is not orthogonal.

Part 3 needs a real matrix.
The unitary matrix $\operatorname{diag}(i, 1)$ has the eigenvalue $i$ but not $-i$, and its determinant $i$ is neither $1$ nor $-1$.
For complex unitary matrices only $\abs{\det U} = 1$ survives.

### What it gives you

The determinant splits the orthogonal matrices into two classes.
Those with $\det Q = 1$ are the rotations, and they form the [[special orthogonal group|6WBVP2PB1Y]].
Those with $\det Q = -1$ include the [[reflections|06BRDF3F0E]].

In odd dimension, every rotation fixes a line.
Indeed, let $n$ be odd and $\det Q = 1$.
The non-real roots pair up with products $\lambda\bar\lambda = 1$, so the real roots are an odd number of values $\pm 1$ whose product is $\det Q = 1$.
An odd number of signs with product $1$ cannot all be $-1$, so $1$ is an eigenvalue, and in dimension $3$ this is [[Euler's rotation theorem|2ZVG43GSKA]].

The trace of $Q$ is a sum of $n$ numbers of absolute value $1$, so $\abs{\tr Q} \le n$.
For a rotation of $\R^3$ by the angle $\theta$, the roots are $1, e^{i\theta}, e^{-i\theta}$, and the trace is $1 + 2\cos\theta$.

### The converse

The converse is false.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$ and the single eigenvalue $1$, on the unit circle.
It is not orthogonal, because its second column $(1, 1)$ has length $\sqrt{2}$.
The converse holds for [[normal matrices|0MR0BYF0K2]]: a real normal matrix with all eigenvalues on the unit circle is orthogonal, by the [[real normal form|G6T1FNE3JC]].

### Generalizations

For a unitary matrix $U$, every eigenvalue has absolute value $1$ and $\abs{\det U} = 1$, by the [[properties of unitary matrices|GZ7NG7J3J8]].
For a linear isometry $T$ of a finite-dimensional inner product space, the same reason works without matrices: $Tv = \lambda v$ with $v \ne 0$ gives $\norm{v} = \norm{Tv} = \abs{\lambda}\norm{v}$.

## Explanations

### L1 human

An orthogonal matrix turns or mirrors space, and it keeps all lengths.
The determinant measures how volumes change, with a minus sign for mirror images.
Volumes do not change, so the determinant is $1$ or $-1$.
An eigenvector is an arrow that the matrix only stretches, and the stretch factor must be $1$ or $-1$ because the length stays the same.

### L2 human

Here is the theorem on the quarter turn $Q = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
First we check that $Q$ is orthogonal and compute its determinant:
$$Q^TQ = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \det Q = 0 \cdot 0 - (-1) \cdot 1 = 1.$$
The characteristic polynomial is $\det(tI - Q) = t^2 + 1$, with the roots $i$ and $-i$.
Both roots have absolute value $1$, and they are conjugate, as parts 2 and 3 say.
There is no real eigenvalue, which fits the picture: a quarter turn fixes no direction.
The theorem is a quick test in the other direction too, since a real matrix with an eigenvalue $2$ or with determinant $3$ cannot be orthogonal.
Watch out: passing the test does not prove orthogonality, as the shear shows.

### L3 human

The determinant is a [[group homomorphism|0JYTG5K9Y4]] from the orthogonal group onto $\{1, -1\}$, and its kernel is the special orthogonal group.
The eigenvalues on the unit circle reflect the compactness of $O(n)$: the powers $Q^k$ and $Q^{-k} = (Q^T)^k$ stay bounded, so no eigenvalue can have absolute value other than $1$.
The same argument works for every compact group of matrices.
The [[normal form of orthogonal matrices|QTY3VMFGY1]] shows how the eigenvalues $e^{\pm i\theta}$ come from rotations in perpendicular planes.
