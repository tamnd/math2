---
tag: PV2DGD23AY
kind: definition
name: Spectral theory of dynamical systems
msc: [37A30, 37A35, 37A05]
defines: Z7GZ6SPFA5
uses: [0NFPJVJJHX, 556WBDAHNP, 37TRG5DBQC, MM0EJ2GDE4, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Koopman%E2%80%93von_Neumann_classical_mechanics
---

## Definition

Let $(X, \mathcal{B}, \mu)$ and $(Y, \mathcal{C}, \nu)$ be [[probability spaces|0NFPJVJJHX]], and let $T \colon X \to X$ and $S \colon Y \to Y$ be invertible [[measure-preserving transformations|556WBDAHNP]] with measurable measure-preserving inverses.
Let $U_T$ and $U_S$ be their [[Koopman operators|37TRG5DBQC]] on $L^2(\mu)$ and $L^2(\nu)$.

1. $T$ and $S$ are *spectrally isomorphic* if there is a [[unitary operator|MM0EJ2GDE4]] $W \colon L^2(\mu) \to L^2(\nu)$ with $W U_T = U_S W$.
2. A *spectral invariant* is a property of such transformations that holds for $S$ whenever it holds for $T$ and $T$, $S$ are spectrally isomorphic.
3. $T$ has *discrete spectrum* if $L^2(\mu)$ has an orthonormal basis of [[eigenvectors|0BQAA2BK3Q]] of $U_T$.

The spectral theory of dynamical systems is the study of transformations up to spectral isomorphism, through the spectrum and the spectral measures of $U_T$.

## Remarks

Isomorphic transformations are spectrally isomorphic: an isomorphism $\varphi$ with $\varphi \circ T = S \circ \varphi$ gives $W f = f \circ \varphi^{-1}$.

Example of a spectral invariant: ergodicity, since $T$ is ergodic if and only if the eigenvalue $1$ of $U_T$ has multiplicity $1$.
Weak mixing is another: it holds if and only if $1$ is a simple eigenvalue and $U_T$ has no other eigenvalue.
An irrational rotation $x \mapsto x + \alpha \bmod 1$ has discrete spectrum, with basis $e^{2\pi i k x}$ and eigenvalues $e^{2\pi i k \alpha}$, $k \in \Z$.

Non-example: the [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] is not a spectral invariant.
Two Bernoulli shifts with different entropies, such as the $(1/2, 1/2)$ and the $(1/3, 1/3, 1/3)$ shifts, are spectrally isomorphic.
Both Koopman operators have countable Lebesgue spectrum on the orthogonal complement of the constants.
