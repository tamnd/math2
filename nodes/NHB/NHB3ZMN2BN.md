---
tag: NHB3ZMN2BN
kind: definition
name: Essential spectrum
msc: [47A53, 47A10]
defines: FRZG0E15SK
uses: [BMKATJ802A, 8HWGKWD6ZM, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_spectrum
---

## Definition

Let $X$ be a complex Banach space with identity map $I$, and let $T \colon X \to X$ be a bounded operator.
The *essential spectrum* of $T$ is the set
$$\sigma_{ess}(T) = \set{\lambda \in \C : T - \lambda I \text{ is not a Fredholm operator}}.$$
Here a bounded operator is [[Fredholm|8HWGKWD6ZM]] when its kernel is finite-dimensional and its image is closed and of finite codimension.

## Remarks

Since every invertible operator is Fredholm, $\sigma_{ess}(T)$ is a subset of the [[spectrum|BMKATJ802A]] $\sigma(T)$; it is compact.
It does not change when a [[compact operator|M2NEP1K5AE]] is added to $T$.
On a Hilbert space, it is the spectrum of the image of $T$ in the quotient algebra of bounded operators by compact operators, by Atkinson's theorem.

Example: if $X$ is infinite-dimensional, then $1 \in \sigma_{ess}(I)$, since $I - I = 0$ has an infinite-dimensional kernel.

Non-example: for $D(x_n) = (x_n / n)$ on $\ell^2$, $1 \in \sigma(D)$ but $1 \notin \sigma_{ess}(D)$.
The kernel of $D - I$ is spanned by $e_1$, and its image is the closed subspace $\set{x : x_1 = 0}$ of codimension $1$, so $D - I$ is Fredholm.
In fact $\sigma_{ess}(D) = \set{0}$.

In Banach spaces several non-equivalent variants of the essential spectrum are in use.
For a self-adjoint operator on a Hilbert space all the usual variants agree.
Then $\lambda \in \sigma_{ess}(T)$ if and only if $\lambda$ is in $\sigma(T)$ and is not an isolated eigenvalue of finite multiplicity.
