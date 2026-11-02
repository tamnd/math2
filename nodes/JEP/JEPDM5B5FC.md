---
tag: JEPDM5B5FC
kind: statement
role: theorem
name: Spectral theory of compact operators
msc: [47B07, 47A10]
uses: [06GZ956657, M2NEP1K5AE, BMKATJ802A, 0BQAA2BK3Q, 0S23E6YE83, 0WSFKKT6FF]
about: [M2NEP1K5AE, BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theory_of_compact_operators
same_as:
  wikidata: Q7575213
  wikipedia: Spectral theory of compact operators
---

## Statement

Let $X$ be a complex [[Banach space|06GZ956657]], let $T \colon X \to X$ be a [[compact operator|M2NEP1K5AE]], and let $\sigma(T)$ be its [[spectrum|BMKATJ802A]].
Then the following hold.

1. Every $\lambda \in \sigma(T)$ with $\lambda \ne 0$ is an [[eigenvalue|0BQAA2BK3Q]] of $T$, and its eigenspace $\ker(T - \lambda I)$ is finite-dimensional.
2. For $\lambda \ne 0$, the [[image|0WSFKKT6FF]] of $T - \lambda I$ is closed, and its codimension in $X$ equals $\dim \ker(T - \lambda I)$.
3. The set $\sigma(T)$ is finite or countable, and $0$ is its only possible accumulation point.
4. If $X$ is infinite-dimensional, then $0 \in \sigma(T)$.

## Remarks

The key tool is the Riesz lemma: in an infinite-dimensional normed space, the unit ball contains a sequence of unit vectors at mutual distance at least $1/2$.
If $\ker(T - \lambda I)$ were infinite-dimensional for some $\lambda \ne 0$, such a sequence in it would be mapped to $\lambda$ times itself, which has no convergent subsequence, against compactness.
A similar argument shows that, for each $\varepsilon > 0$, only finitely many eigenvalues satisfy $\abs{\lambda} \ge \varepsilon$, which gives part 3.
Part 2 is the Fredholm alternative: for $\lambda \ne 0$, the equation $Tx - \lambda x = y$ is solvable for every $y$ as soon as the homogeneous equation has only the solution $x = 0$.
Part 4 holds because a compact operator on an infinite-dimensional space cannot have a bounded inverse.
Example: on $\ell^2$, the diagonal operator $T(x_n) = (x_n / n)$ is compact, and $\sigma(T) = \set{1/n : n \ge 1} \cup \set{0}$, where $0$ is not an eigenvalue.
The compactness hypothesis matters: the identity on an infinite-dimensional space has the eigenvalue $1$ with infinite-dimensional eigenspace.

## Explanations

### L1 human

Compact operators are the infinite-dimensional operators that behave most like matrices.
This theorem says that their spectrum looks like that of a matrix, apart from the point $0$.
Away from $0$, the spectrum consists of eigenvalues with finitely many independent eigenvectors each, and these eigenvalues can only pile up at $0$.

### L2 human

This is the Riesz–Schauder theory, the abstract form of Fredholm's results on integral equations.
It applies to integral operators with continuous kernels, which are compact on spaces of continuous or square-integrable functions.
For compact self-adjoint operators on a Hilbert space, it combines with orthogonality to give the spectral theorem for compact self-adjoint operators.
In the language of Fredholm theory, part 2 says that $T - \lambda I$ is a Fredholm operator of index $0$ for each $\lambda \ne 0$.
