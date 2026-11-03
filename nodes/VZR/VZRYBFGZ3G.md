---
tag: VZRYBFGZ3G
kind: statement
role: theorem
name: Uniqueness theorem for Fourier–Stieltjes transforms
msc: [43A25, 43A10]
uses: [ZR09S9R3AW, FMW57WNPDB, 8E2CDA2WSV, FZQ7MVMPTN, 0T8BYAFEXX]
about: [FZQ7MVMPTN]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with [[Pontryagin dual|FMW57WNPDB]] $\widehat{G}$.
Let $\mu$ be a measure in the [[measure algebra|8E2CDA2WSV]] $M(G)$ of finite complex Radon measures on $G$.
If its [[Fourier–Stieltjes transform|FZQ7MVMPTN]] $\widehat{\mu}(\chi) = \int_G \overline{\chi(x)}\, d\mu(x)$ is $0$ for every $\chi \in \widehat{G}$, then $\mu = 0$.

## Remarks

Equivalently, two measures in $M(G)$ with the same transform are equal.

Proof idea: fix a Haar measure $\nu$ on $\widehat{G}$, and for $\varphi \in L^1(\widehat{G})$ let $\check{\varphi}(x) = \int_{\widehat{G}} \varphi(\chi) \chi(x)\, d\nu(\chi)$.
By Fubini's theorem, $\int_G \check{\varphi}\, d\mu = \int_{\widehat{G}} \varphi(\chi)\, \widehat{\mu}(\overline{\chi}) \, d\nu(\chi) = 0$.
The functions $\check{\varphi}$ form a dense subspace of $C_0(G)$, by the Stone–Weierstrass theorem.
By the Riesz representation theorem, a measure that integrates every function of $C_0(G)$ to $0$ is the zero measure.

Example: for $G = \R$ and a probability measure $\mu$, $\widehat{\mu}$ is the characteristic function of $\mu$ up to a change of variable.
So the theorem says that the [[characteristic function determines the distribution|0T8BYAFEXX]].
For $G = \mathbb{T}$ it says that a measure on the circle with all Fourier coefficients $0$ is zero.

## Explanations

### L1 human

A measure on an abelian group cannot hide from all the waves at once.
If every wave integrates to zero against it, then the measure itself is zero.
So the list of numbers $\widehat{\mu}(\chi)$ carries all the information about $\mu$.

### L2 human

The theorem makes the Fourier–Stieltjes transform an injective algebra homomorphism from $M(G)$ into the bounded continuous functions on $\widehat{G}$.
It contains the injectivity of the Fourier transform on $L^1(G)$ as the case $d\mu = f\, dx$.
In probability it is the reason why characteristic functions identify distributions, which is the first step of the Lévy continuity theorem and of the proof of the central limit theorem.
