---
tag: X71XRPJR7D
kind: statement
role: theorem
name: Spectral theorem for bounded normal operators
msc: [47B15, 47A60]
uses: [HM2HHE3J51, 6HSJBJ8TTQ, BMKATJ802A, 0WQXY32Q8D, ATGT25E5FF, 04CW1P44VD, JB7S6WPZ77]
about: [ATGT25E5FF, BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $N$ be a bounded operator on $H$.
Assume that $N$ is normal: $N N^* = N^* N$, where $N^*$ is the [[adjoint|6HSJBJ8TTQ]] of $N$.
Let $\sigma(N) \subseteq \C$ be the [[spectrum|BMKATJ802A]] of $N$.
Then there is a unique [[projection-valued measure|ATGT25E5FF]] $E$ on the [[Borel sets|0WQXY32Q8D]] of $\sigma(N)$ such that
$$\ip{N x}{y} = \int_{\sigma(N)} \lambda \, d E_{x,y}(\lambda) \quad \text{for all } x, y \in H,$$
where $E_{x,y}(B) = \ip{E(B) x}{y}$.
In short, $N = \int_{\sigma(N)} \lambda \, dE(\lambda)$.

## Remarks

One proof starts from the [[continuous functional calculus|JB7S6WPZ77]] $f \mapsto f(N)$ on $C(\sigma(N))$.
For fixed $x, y$, the map $f \mapsto \ip{f(N) x}{y}$ is a bounded linear functional on $C(\sigma(N))$, so by the Riesz–Markov theorem it is integration against a complex measure $E_{x,y}$.
One then defines $E(B)$ by $\ip{E(B) x}{y} = E_{x,y}(B)$ and checks that it is a projection-valued measure.
The projections $E(B)$ commute with every bounded operator that commutes with $N$.
An equivalent form holds when $H$ is separable.
Then there are a $\sigma$-finite measure space $(\Omega, \mu)$, a bounded measurable function $\varphi$ on $\Omega$ and a unitary map $U \colon H \to L^2(\Omega, \mu)$ with $U N U^{-1} f = \varphi f$ for all $f \in L^2(\Omega, \mu)$.
Example: on $L^2([0,1])$, the operator $(Nf)(t) = t f(t)$ is self-adjoint with spectrum $[0,1]$, and $E(B)$ is multiplication by the indicator function of $B$.
In finite dimension, $E(B)$ is the orthogonal projection onto the sum of the eigenspaces for the eigenvalues in $B$, and the theorem is the [[spectral theorem for normal matrices|04CW1P44VD]].
Normality is necessary: the right shift on $\ell^2$ is not normal, and it is not of this form.

## Explanations

### L1 human

A normal matrix is diagonal in a suitable orthonormal basis.
An operator on an infinite-dimensional space may have no eigenvectors, so a basis of eigenvectors may not exist.
The spectral theorem replaces the list of eigenvalues by a measure on the spectrum, whose values are projections.
In this sense, every normal operator is a continuous version of a diagonal matrix: it is multiplication by a function.

### L2 human

The theorem makes it possible to define $f(N) = \int f(\lambda) \, dE(\lambda)$ for every bounded Borel function $f$ on $\sigma(N)$, the Borel functional calculus.
With $f$ an indicator function, this gives the spectral projections of $N$, which split $H$ into pieces where $N$ acts with spectrum in a given set.
The self-adjoint case covers the observables of quantum mechanics with bounded values; the unitary case gives the spectral analysis of unitary operators, used in ergodic theory.
For unbounded self-adjoint operators, a similar theorem holds with a projection-valued measure on $\R$.
