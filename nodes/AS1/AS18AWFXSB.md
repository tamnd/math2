---
tag: AS18AWFXSB
kind: statement
role: theorem
name: Halmos–von Neumann theorem
msc: [37A30, 37A35, 37A05]
uses: [QDDRDW9PXS, 556WBDAHNP, AZRPHS478B, 37TRG5DBQC, Z7GZ6SPFA5, 0BQAA2BK3Q, VY0HXD3GC4]
about: [Z7GZ6SPFA5]
sources:
  - url: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
---

## Statement

Let $T$ on $(X, \mu)$ and $S$ on $(Y, \nu)$ be invertible [[ergodic|AZRPHS478B]] [[measure-preserving transformations|556WBDAHNP]] of [[standard probability spaces|QDDRDW9PXS]], with measurable inverses.
Assume both have discrete spectrum, in the sense of the [[spectral theory of dynamical systems|Z7GZ6SPFA5]].
This means that $L^2$ has an orthonormal basis of [[eigenvectors|0BQAA2BK3Q]] of the [[Koopman operator|37TRG5DBQC]].
Let $\Lambda(T) \subseteq \C$ be the set of eigenvalues of the Koopman operator $U_T$ of $T$.

1. $T$ and $S$ are isomorphic if and only if $\Lambda(T) = \Lambda(S)$.
2. $\Lambda(T)$ is a countable subgroup of the unit circle. Moreover, $T$ is isomorphic to a rotation $x \mapsto x + a$ of a compact metrizable abelian group $K$ with its [[Haar measure|VY0HXD3GC4]], where $\set{na : n \in \Z}$ is dense in $K$.

## Remarks

Here isomorphic means conjugate by a measure-preserving bijection defined up to null sets.
For part 1, ergodicity makes every eigenvalue simple and every eigenfunction of constant modulus, so a product of eigenfunctions is again an eigenfunction and $\Lambda(T)$ is a group.
Choose for each $\lambda \in \Lambda(T)$ an eigenfunction $f_\lambda$ of modulus $1$; the products $f_\lambda f_{\lambda'}$ and $f_{\lambda \lambda'}$ differ by constants.
The proof adjusts these constants, which is possible because the circle group is divisible.
It then matches the eigenfunctions of $T$ and $S$ to build a unitary map that preserves products, and such a map comes from an isomorphism of the spaces.
For part 2, $K$ is the Pontryagin dual of $\Lambda(T)$ with the discrete topology, and $a$ is the inclusion character.
Example: for an irrational $\alpha$, the rotation $x \mapsto x + \alpha \bmod 1$ has $\Lambda = \set{e^{2\pi i k \alpha} : k \in \Z}$.
So two irrational rotations by $\alpha$ and $\beta$ are isomorphic exactly when $\beta = \pm \alpha \bmod 1$.
Without the discrete spectrum hypothesis the eigenvalues do not determine the system: all weakly mixing systems have $\Lambda = \set{1}$.

## Explanations

### L1 human

Some systems behave like a collection of clocks running at fixed frequencies, such as rotations of a circle or a torus.
For them, the list of frequencies tells everything: two such systems are the same exactly when they have the same frequencies.
Each of them is in fact a rotation of a compact group.

### L2 human

This is the first complete classification theorem in ergodic theory, obtained by Halmos and von Neumann in 1942.
It shows the power of spectral methods in the class where the spectrum is discrete, and it is the model case for the [[spectral theory of dynamical systems|Z7GZ6SPFA5]].
For systems with continuous spectrum spectral invariants are far from complete, which motivated the search for other invariants such as the Kolmogorov–Sinai entropy.
