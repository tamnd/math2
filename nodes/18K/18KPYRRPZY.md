---
tag: 18KPYRRPZY
kind: statement
role: theorem
name: Spectral theorem for unbounded self-adjoint operators
msc: [47B25, 47B15, 81Q10]
uses: [HM2HHE3J51, KRJX5RA0PW, BCJHNHKQFG, 86B7HF79PQ, BMKATJ802A, 0WQXY32Q8D, ATGT25E5FF, X71XRPJR7D]
about: [ATGT25E5FF, 86B7HF79PQ]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $A$ be a [[densely defined operator|BCJHNHKQFG]] on $H$ with domain $D(A)$.
Assume that $A$ is self-adjoint: $A = A^*$, with equal domains, where $A^*$ is the [[adjoint|86B7HF79PQ]] of $A$.
Then there is a unique [[projection-valued measure|ATGT25E5FF]] $E$ on the [[Borel sets|0WQXY32Q8D]] of $\R$ such that, with $E_{x,y}(B) = \ip{E(B) x}{y}$:

1. $D(A) = \set{x \in H : \int_{\R} \lambda^2 \, d E_{x,x}(\lambda) < \infty}$;
2. $\ip{A x}{y} = \int_{\R} \lambda \, d E_{x,y}(\lambda)$ for all $x \in D(A)$ and $y \in H$.

Moreover, $E(\R \setminus \sigma(A)) = 0$, where $\sigma(A) \subseteq \R$ is the [[spectrum|BMKATJ802A]] of $A$.

## Remarks

One proof uses the Cayley transform $U = (A - iI)(A + iI)^{-1}$, a unitary operator for which $1$ is not an eigenvalue.
The [[spectral theorem for bounded normal operators|X71XRPJR7D]] applied to $U$ gives a projection-valued measure on the unit circle.
It is carried over to $\R$ by the inverse of the map $\lambda \mapsto (\lambda - i)/(\lambda + i)$.
Equivalently, if $H$ is separable, $A$ is unitarily equivalent to the multiplication by a real measurable function $\varphi$ on some $L^2(\Omega, \mu)$, on the domain of all $f$ with $\varphi f \in L^2(\Omega, \mu)$.
Example: on $L^2(\R)$, the momentum operator $-i \, d/dx$ on the Sobolev space $H^1(\R)$ is self-adjoint; the Fourier transform turns it into multiplication by the variable $\xi$, with spectrum $\R$.
Self-adjointness, not mere symmetry, is needed.
The operator $-i \, d/dx$ on smooth functions with compact support in $(0, \infty)$ is symmetric, but it has no self-adjoint extension and no spectral resolution of this form.

## Explanations

### L1 human

Many important operators, such as derivatives, are unbounded: they can make vectors arbitrarily long.
The theorem says that a self-adjoint unbounded operator is still, in a precise sense, a real diagonal operator.
Its eigenvalues are replaced by a measure on the real line whose values are projections.

### L2 human

The theorem is the mathematical basis of quantum mechanics, where observables such as position, momentum and energy are unbounded self-adjoint operators.
It defines $f(A) = \int f(\lambda) \, dE(\lambda)$ for Borel functions $f$, in particular the unitary group $e^{itA}$ that gives the time evolution of a quantum system.
The probability that a measurement of $A$ in the unit state $x$ gives a value in $B$ is $\ip{E(B) x}{x}$.
Stone's theorem gives the converse correspondence between strongly continuous one-parameter unitary groups and self-adjoint operators.
