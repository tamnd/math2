---
tag: 0C4NT4GT3X
kind: statement
role: theorem
name: Eigenvalues of a self-adjoint operator are real
msc: ["47B15", "15A18"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0NEGN5CRSC, 0BQAA2BK3Q]
uses: [0MB8HQW495, 0ZND7NQ970, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be a [[self-adjoint|0MB8HQW495]] operator.

1. Every [[eigenvalue|0ZND7NQ970]] of $T$ is a real number.
2. If $V \neq 0$, then $T$ has an eigenvalue. More precisely, the function $v \mapsto \ip{Tv}{v}$ attains a maximum $\lambda$ on the unit sphere $\set{v \in V : \norm{v} = 1}$, and every point $u$ where it attains $\lambda$ satisfies $Tu = \lambda u$.

In particular, every real [[symmetric|0N28QN4CYA]] $n \times n$ matrix with $n \geq 1$ has a real eigenvalue and a real eigenvector.

## Remarks

### Why each hypothesis is needed

- Self-adjointness is needed in both parts. [[The rotation by a right angle|~369bb802]] has the eigenvalues $\pm i$ over $\mathbb{C}$, and over $\mathbb{R}$ it has no eigenvalue at all.
- A real matrix with $A^T = A$ needs the real field. [[The complex symmetric matrix|DAZBNZXZK7]] has $A^T = A$ but is not Hermitian, and it can have eigenvalues that are not real.
- Part 2 needs finite dimension. On the Hilbert space $L^2[0, 1]$, multiplication by $x$ is a bounded self-adjoint operator with no eigenvalue, as the Wikipedia article on the spectral theorem explains in "Possible absence of eigenvectors". The unit sphere there is not compact.

### Consequences

- The characteristic polynomial of a self-adjoint operator splits into real linear factors. Over $\mathbb{C}$ this follows from part 1. Over $\mathbb{R}$ it follows by induction from part 2, or from part 1 applied to the complexification.
- Part 2 is the first step of the inductive proof of [[the real spectral theorem|06J4PXRG22]].
- The maximum $\lambda$ in part 2 is the largest eigenvalue of $T$. This is [[the extreme value statement for the Rayleigh quotient|~5c6d5f8a]].
- The eigenvalues of a [[Hermitian matrix|0P17NGQQMQ]] are real, and its determinant and trace are real.

### Converse

Part 1 has no converse.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the real eigenvalue $1$ only, but it is not self-adjoint.
For [[normal operators|0C8BR8XRTR]] there is a converse over $\mathbb{C}$: a normal operator with only real eigenvalues is self-adjoint.
The reason: by [[the complex spectral theorem|04CW1P44VD]], $T = U D U^*$ with real diagonal $D$, so $T^* = U \overline{D} U^* = T$.

### Generalizations

- Every point of the spectrum of a bounded self-adjoint operator on a Hilbert space is real. This is [[the real spectrum of self-adjoint operators|NXV8S3145K]].
- For a compact self-adjoint operator, the maximum of $\abs{\ip{Tv}{v}}$ on the unit sphere is attained and gives an eigenvalue. This is the first step of [[the spectral theorem for compact self-adjoint operators|A1G25R99PY]].

### History

Hermitian matrices are named after Hermite, who showed in 1855 that they have real eigenvalues, like real symmetric matrices.
This fact is from the Wikipedia article on Hermitian matrices.

## Explanations

### L1 human

A symmetric matrix can only stretch or flip directions by real factors.
It never turns a direction by a complex factor such as $i$.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the eigenvalues $1$ and $-1$.
By contrast, the quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is not symmetric, and its eigenvalues are $\pm i$.
Part 2 says more: a symmetric matrix always has at least one real direction that it stretches.
The direction where the matrix stretches most is such a direction.

### L2 human

Worked example: we find the maximum of the quadratic form for a symmetric $2 \times 2$ matrix.

1. Let $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ and $q(v) = v^T A v$ on the unit circle.
2. Write $v = (\cos \theta, \sin \theta)$. Then $q(v) = 5 \cos^2 \theta + 4 \sin \theta \cos \theta + 2 \sin^2 \theta = \tfrac{7}{2} + \tfrac{3}{2} \cos 2\theta + 2 \sin 2\theta$.
3. The maximum of $\tfrac{3}{2} \cos 2\theta + 2 \sin 2\theta$ is $\sqrt{9/4 + 4} = \tfrac{5}{2}$. So $\lambda = 6$.
4. It is attained at $u = \tfrac{1}{\sqrt{5}}(2, 1)$, and indeed $Au = \tfrac{1}{\sqrt{5}}(12, 6) = 6u$.

The typical use of part 1 is to know in advance that all roots of a characteristic polynomial are real.
A trap: part 1 alone does not show that a real symmetric matrix has a real eigenvector.
Part 2, or the complexification, is needed.

### L3 human

Part 1 is the finite-dimensional case of the fact that self-adjoint elements of a $C^*$-algebra have real spectrum.
Part 2 is a variational principle: eigenvalues are critical values of the quadratic form on the sphere, and eigenvectors are critical points.
In the language of Lagrange multipliers, the gradient of $v^T A v$ is $2Av$, and the gradient of $v^T v$ is $2v$, so a critical point satisfies $Av = \lambda v$.
The proof of part 2 uses compactness of the sphere and no fundamental theorem of algebra.
This makes it the model for the variational proofs in Sturm-Liouville theory and for compact operators.
