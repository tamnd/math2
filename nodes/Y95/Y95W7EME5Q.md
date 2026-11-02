---
tag: Y95W7EME5Q
kind: definition
name: Continuous and residual spectrum
msc: [47A10]
defines: YVH149HCAG
uses: [BMKATJ802A, 7FNVA0Q6YQ, 0BSJSX7ME2, 0WSFKKT6FF]
sources:
  - url: https://en.wikipedia.org/wiki/Decomposition_of_spectrum_(functional_analysis)
---

## Definition

Let $X$ be a complex Banach space with identity map $I$, and let $T \colon X \to X$ be a bounded operator with [[spectrum|BMKATJ802A]] $\sigma(T)$ and [[point spectrum|7FNVA0Q6YQ]] $\sigma_p(T)$.
For $\lambda \in \sigma(T) \setminus \sigma_p(T)$, the operator $T - \lambda I$ is injective.

1. The *continuous spectrum* $\sigma_c(T)$ is the set of $\lambda \in \sigma(T) \setminus \sigma_p(T)$ such that the [[image|0WSFKKT6FF]] of $T - \lambda I$ is [[dense|0BSJSX7ME2]] in $X$.
2. The *residual spectrum* $\sigma_r(T)$ is the set of $\lambda \in \sigma(T) \setminus \sigma_p(T)$ such that the image of $T - \lambda I$ is not dense in $X$.

## Remarks

By construction, $\sigma(T)$ is the disjoint union $\sigma_p(T) \cup \sigma_c(T) \cup \sigma_r(T)$.
For $\lambda \in \sigma_c(T)$, the image of $T - \lambda I$ is dense but not all of $X$, since a bounded bijection between Banach spaces has a bounded inverse.

Example: for $D(x_n) = (x_n / n)$ on $\ell^2$, $0 \in \sigma_c(D)$.
Indeed $D$ is injective, it is not surjective, and its image contains every finitely supported sequence, a dense set.

Non-example: for the right shift $S(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$ on $\ell^2$, $0$ is not in $\sigma_c(S)$.
The image of $S$ is the closed subspace $\set{x : x_1 = 0}$, which is not dense, so $0 \in \sigma_r(S)$.

For the right shift, $\sigma_p(S) = \emptyset$, $\sigma_r(S)$ is the open unit disc and $\sigma_c(S)$ is the unit circle.
A self-adjoint operator on a Hilbert space has empty residual spectrum.
