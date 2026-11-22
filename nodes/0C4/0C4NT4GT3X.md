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

A self-adjoint operator has only real eigenvalues, and on a nonzero space it has at least one, found as the maximum of its quadratic form on the unit sphere.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be a [[self-adjoint|0MB8HQW495]] operator.

1. Every [[eigenvalue|0ZND7NQ970]] of $T$ is a real number.
2. If $V \neq 0$, then the function $v \mapsto \ip{Tv}{v}$ attains a maximum $\lambda$ on the unit sphere $\{v \in V : \norm{v} = 1\}$, and every point $u$ of the sphere where it attains $\lambda$ satisfies $Tu = \lambda u$. In particular, $T$ has an eigenvalue.

So every real [[symmetric|0N28QN4CYA]] $n \times n$ matrix with $n \geq 1$ has a real eigenvalue with a real eigenvector.

## Remarks

### Why each hypothesis is needed

Without self-adjointness both parts fail.
The rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has the characteristic polynomial $t^2 + 1$.
Over $\mathbb{C}$ its eigenvalues are $i$ and $-i$, which are not real, and over $\mathbb{R}$ it has no eigenvalue at all; [[the rotation by a right angle|1CF483TZZA]] works this out.

Over $\mathbb{C}$, the right condition is $A^* = A$ and not $A^{\mathsf{T}} = A$.
The matrix $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ equals its transpose, but its eigenvalues are $1 + i$ and $1 - i$, with the eigenvectors $(1, 1)$ and $(1, -1)$.
[[The complex symmetric matrix|DAZBNZXZK7]] shows the same failure.

Part 2 needs finite dimension.
On the Hilbert space $L^2[0, 1]$, multiplication by $x$ is a bounded self-adjoint operator with no eigenvalue, because $x f(x) = \lambda f(x)$ forces $f = 0$ away from the point $\lambda$.
There the unit sphere is not compact, and the supremum of $\ip{Tf}{f}$ is not attained.

### What it gives you

Part 1 says that the characteristic polynomial of a Hermitian matrix has only real roots, so its determinant and its trace are real.
Part 2 goes further over $\mathbb{R}$: it gives a real eigenvector without the fundamental theorem of algebra, by compactness of the sphere.
Together with induction, part 2 is the first step of [[the real spectral theorem|06J4PXRG22]].

The maximum $\lambda$ in part 2 is the largest eigenvalue of $T$, by [[the extreme values of the Rayleigh quotient|T7MFPSY009]].
For $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ and $v = (\cos \theta, \sin \theta)$, the double-angle formulas give
$$v^{\mathsf{T}} A v = 5 \cos^2 \theta + 4 \sin \theta \cos \theta + 2 \sin^2 \theta = \tfrac{7}{2} + \tfrac{3}{2} \cos 2\theta + 2 \sin 2\theta.$$
The largest value of $\tfrac{3}{2} \cos 2\theta + 2 \sin 2\theta$ is $\sqrt{9/4 + 4} = \tfrac{5}{2}$, so $\lambda = 6$.
It is attained at $u = \tfrac{1}{\sqrt{5}}(2, 1)$.
Check: $Au = \tfrac{1}{\sqrt{5}}(12, 6) = 6u$.

### The converse

Real eigenvalues do not make an operator self-adjoint.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the single eigenvalue $1$, but it is not symmetric.
For [[normal operators|0C8BR8XRTR]] on a complex space the converse holds.
By [[the complex spectral theorem|04CW1P44VD]], $T = U D U^*$ with $U$ unitary and $D$ diagonal, and real entries in $D$ give $T^* = U \overline{D} U^* = T$.

### Generalizations

Every point of the spectrum of a bounded self-adjoint operator on a Hilbert space is real, by [[the real spectrum of self-adjoint operators|NXV8S3145K]].
For a compact self-adjoint operator, the maximum of $\abs{\ip{Tv}{v}}$ on the unit sphere is attained and gives an eigenvalue.
That is the first step of [[the spectral theorem for compact self-adjoint operators|A1G25R99PY]].

## History

Cauchy proved in 1829 that the eigenvalues of a real symmetric matrix are real.
Hermitian matrices carry the name of Hermite, who showed in 1855 that their eigenvalues are real as well.

## Explanations

### L1 human

A symmetric matrix can only stretch or flip directions by real factors.
It never turns a direction by a complex factor such as $i$.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the eigenvalues $1$ and $-1$, while the quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is not symmetric and has the eigenvalues $\pm i$.
Part 2 says more: a symmetric matrix always has a real direction that it only stretches.
The direction in which it stretches the most is such a direction.

### L2 human

Here is a typical use: show that $A = \begin{pmatrix} 3 & 2 & 0 \\ 2 & 3 & 0 \\ 0 & 0 & 7 \end{pmatrix}$ has only real eigenvalues, and find the largest.
The matrix is real and symmetric, so part 1 says that every root of its characteristic polynomial is real before we compute anything.
The block structure gives the polynomial
$$\det(A - tI) = \big((3 - t)^2 - 4\big)(7 - t) = (t - 1)(t - 5)(7 - t).$$
So the eigenvalues are $1$, $5$ and $7$, all real, and the largest is $7$, with the unit eigenvector $e_3$.
Check by part 2: $e_3^{\mathsf{T}} A e_3 = 7$, and for $v = \tfrac{1}{\sqrt{2}}(1, 1, 0)$ we get $v^{\mathsf{T}} A v = \tfrac{1}{2}(3 + 2 + 2 + 3) = 5$, which is smaller.
Watch out: part 1 alone does not give a real eigenvector of a real symmetric matrix; for that you need part 2, or a null vector of the real matrix $A - \lambda I$.

### L3 human

Part 1 is the finite-dimensional case of the fact that self-adjoint elements of a $C^*$-algebra have real spectrum.
Part 2 is a variational principle: the eigenvalues are critical values of the quadratic form on the sphere, and the eigenvectors are its critical points.
With Lagrange multipliers, the gradient of $v^{\mathsf{T}} A v$ is $2Av$ and the gradient of $v^{\mathsf{T}} v$ is $2v$, so a critical point satisfies $Av = \lambda v$.
The proof of part 2 uses only the compactness of the sphere.
This makes it the model for the variational proofs of Sturm-Liouville theory and of the [[Courant-Fischer min-max theorem|CJK2HS2508]].
