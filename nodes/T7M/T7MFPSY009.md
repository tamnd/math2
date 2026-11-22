---
tag: T7MFPSY009
kind: statement
role: theorem
name: Extreme values of the Rayleigh quotient
aliases: [rayleigh-ritz-principle, rayleigh-quotient-bounds]
msc: ["15A18", "15A42"]
topics: [3YM9EK6VMB]
audience: ug1
about: [06WHP8SE98]
uses: [06WHP8SE98, 0MB8HQW495, 0ZND7NQ970, 0B5H4208Z9, 0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
  - url: https://understandinglinearalgebra.org/sec-quadratic-forms.html
    locator: Proposition 7.2.8
---

## Statement

The largest and the smallest eigenvalue of a self-adjoint operator are the largest and the smallest value of its Rayleigh quotient, and they are reached exactly at the matching eigenvectors.
Let $V$ be an inner product space of finite dimension $n \geq 1$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to V$ be [[self-adjoint|0MB8HQW495]], with [[eigenvalues|0ZND7NQ970]] $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$, repeated by multiplicity.
For $v \neq 0$, let $R(v) = \ip{Tv}{v} / \ip{v}{v}$ be the [[Rayleigh quotient|06WHP8SE98]].

1. For every $v \neq 0$,
$$\lambda_n \leq R(v) \leq \lambda_1.$$
2. $R(v) = \lambda_1$ if and only if $v$ is an [[eigenvector|0B5H4208Z9]] for $\lambda_1$, and $R(v) = \lambda_n$ if and only if $v$ is an eigenvector for $\lambda_n$.
3. So the maximum of $R$ is $\lambda_1$, and the minimum of $R$ is $\lambda_n$.

For a [[Hermitian|0EKZCX4K3P]] $n \times n$ matrix $A$, the same holds for $R_A(x) = x^* A x / x^* x$ on $\mathbb{C}^n$, and for a real symmetric matrix on $\mathbb{R}^n$.

## Remarks

### Why each hypothesis is needed

Self-adjointness is needed.
[[The matrix with rows (1, 4) and (0, 1)|39XSQ9MTZ3]] has the single eigenvalue $1$, but its quotient takes the values $R(1, 1) = 3$ and $R(1, -1) = -1$, so part 1 fails.
The vector must be nonzero, because $R(0)$ would be $0 / 0$.
Finite dimension makes the eigenvalues exist and the maximum attained.
On a Hilbert space the supremum of $R$ is the top of the spectrum, which need not be an eigenvalue.

### What it gives you

The theorem turns any test vector into an eigenvalue bound.
For [[the matrix with rows (5, 2) and (2, 2)|3FXAQ6P15S]], with eigenvalues $6$ and $1$, the vector $(3, 1)$ gives
$$\lambda_1 \ge R(3, 1) = \frac{45 + 12 + 2}{10} = 5.9.$$
On the unit sphere, $R$ is the quadratic form $\ip{Tv}{v}$, so the form has the maximum $\lambda_1$ and the minimum $\lambda_n$ there.
For real symmetric matrices this is [[the extreme values of a quadratic form on unit vectors|YS4HT1EYE5]].

Three more facts follow at once.
The operator $T$ is positive definite exactly when $\lambda_n > 0$, because $\ip{Tv}{v} \ge \lambda_n \ip{v}{v}$ with equality at an eigenvector.
The operator norm of $T$ is $\max(\abs{\lambda_1}, \abs{\lambda_n})$.
The other eigenvalues are max-min values of $R$ over subspaces, by the [[Courant-Fischer min-max theorem|CJK2HS2508]].

### The converse

Part 2 is already an equivalence.
Part 1 has a converse: every number in $[\lambda_n, \lambda_1]$ is a value of $R$.
The reason is that $R$ is continuous on the nonzero vectors, which form a connected set when $\dim V \geq 2$ over $\mathbb{R}$ or $\dim V \ge 1$ over $\mathbb{C}$, and it reaches both ends.
For $n = 1$ the interval is the single point $\lambda_1$.

### Generalizations

For a bounded self-adjoint operator on a Hilbert space, the supremum and the infimum of $R$ are the largest and the smallest points of the spectrum.
For an arbitrary operator on a complex space, the set of values of $R$ is the numerical range, which is convex by the Toeplitz-Hausdorff theorem.
For a normal operator in finite dimension, the numerical range is the convex hull of the eigenvalues.

## History

Rayleigh used the quotient in The Theory of Sound (1877) to estimate the frequencies of vibrating systems.

## Explanations

### L1 human

The Rayleigh quotient measures how much $T$ stretches a vector along its own direction.
For a self-adjoint operator, the largest stretch is the largest eigenvalue, and the smallest stretch is the smallest eigenvalue.
For the matrix with rows $(5, 2)$ and $(2, 2)$, no direction is stretched by more than $6$ or by less than $1$.
These extreme stretches happen exactly along the eigenvectors $(2, 1)$ and $(1, -2)$.

### L2 human

Here is a typical use: estimate the smallest eigenvalue of $A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$ from above.
The test vector $x = (1, -1, 1)$ gives
$$Ax = (2 - 1, -1 + 2 - 1, -1 + 2) = (1, 0, 1), \qquad R(x) = \frac{x \cdot Ax}{x \cdot x} = \frac{2}{3}.$$
So $\lambda_3 \le \tfrac{2}{3} \approx 0.667$.
The exact value is $\lambda_3 = 2 - \sqrt{2} \approx 0.586$, with the eigenvector $(1, -\sqrt{2}, 1)$.
Check: $A(1, -\sqrt{2}, 1) = (2 - \sqrt{2}, 2 - 2\sqrt{2}, 2 - \sqrt{2}) = (2 - \sqrt{2})(1, -\sqrt{2}, 1)$.
One test vector gave a bound within $0.09$ of the truth, with no characteristic polynomial.
Watch out: the bounds need a self-adjoint operator, as the matrix with the value $-1$ above shows.

### L3 human

The theorem is the first case of the min-max principle: the extreme eigenvalues are the extreme values of a quadratic form on the sphere.
It holds for bounded self-adjoint operators on Hilbert space, with the ends of the spectrum in place of $\lambda_1$ and $\lambda_n$.
The Courant-Fischer theorem extends it to every $\lambda_k$, and the Rayleigh-Ritz method uses it to approximate eigenvalues from a subspace of trial vectors.
For singular values, the same idea applied to $A^* A$ gives the largest singular value as the maximum of $\norm{Ax} / \norm{x}$.
