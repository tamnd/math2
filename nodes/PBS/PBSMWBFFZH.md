---
tag: PBSMWBFFZH
kind: definition
name: Discrete spectrum
msc: [47A10]
defines: PJWY3JJQQ7
uses: [BMKATJ802A, HNW4WRSEEX, FRZG0E15SK, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_spectrum_(mathematics)
---

## Definition

Let $X$ be a complex Banach space, and let $T \colon X \to X$ be a bounded operator with [[spectrum|BMKATJ802A]] $\sigma(T)$.
A point $\lambda \in \sigma(T)$ is a *normal eigenvalue* of $T$ if:

1. $\lambda$ is an isolated point of $\sigma(T)$, and
2. the [[Riesz projector|HNW4WRSEEX]] $P_{\set{\lambda}}$ of $T$ for $\set{\lambda}$ has finite rank.

The *discrete spectrum* $\sigma_{disc}(T)$ is the set of normal eigenvalues of $T$.

## Remarks

A normal eigenvalue is an eigenvalue, and its algebraic multiplicity, the rank of $P_{\set{\lambda}}$, is finite.

Example: if $T$ is a [[compact operator|M2NEP1K5AE]], then every nonzero point of $\sigma(T)$ is a normal eigenvalue.
For $D(x_n) = (x_n / n)$ on $\ell^2$, each $1/n$ is isolated in $\sigma(D)$, and $P_{\set{1/n}}$ is the projection onto the span of $e_n$, of rank $1$.

Non-example: if $X$ is infinite-dimensional, then $\sigma(I) = \set{1}$ and $1$ is isolated, but $P_{\set{1}} = I$ has infinite rank, so clause 2 fails.
For $D$ above, $0$ fails clause 1, since $1/n \to 0$.

For a self-adjoint operator $T$ on a Hilbert space, $\sigma_{disc}(T)$ is the set of isolated eigenvalues of finite multiplicity.
Then $\sigma(T)$ is the disjoint union of $\sigma_{disc}(T)$ and the [[essential spectrum|FRZG0E15SK]].
