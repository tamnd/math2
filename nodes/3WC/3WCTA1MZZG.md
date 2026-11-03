---
tag: 3WCTA1MZZG
kind: definition
name: Harmonic analysis on homogeneous spaces
msc: ["43A85", "22D10", "43A90"]
defines: 5NVQWPD35X
uses: [AHV05ZBCYW, 85TWR6E75P, AF8V6SMF2H, 74BPYJNZTM, FX3NEFYFFN]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_space
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $H$ be a closed subgroup.
Assume that the [[homogeneous space|85TWR6E75P]] $X = G / H$ carries a nonzero $G$-invariant Radon measure $\mu$.
The *quasi-regular representation* of $G$ on $X$ is the representation $\lambda_X$ on the Hilbert space $L^2(X, \mu)$ given by
$$(\lambda_X(g) f)(x) = f(g^{-1} x), \qquad g \in G, \ f \in L^2(X, \mu), \ x \in X.$$
It is a [[unitary representation|74BPYJNZTM]], because $\mu$ is $G$-invariant.
*Harmonic analysis on the homogeneous space* $X$ is the study of the decomposition of $\lambda_X$ into [[irreducible|FX3NEFYFFN]] unitary representations.
The decomposition is a direct sum or a direct integral, and it gives a corresponding expansion of functions on $X$.

## Remarks

An invariant measure exists, for example, when $G$ and $H$ are both unimodular, or when $H$ is compact; see [[invariant measure on a homogeneous space|AF8V6SMF2H]].

Example: for $G = \R$ and $H = 2\pi\Z$, the space $X$ is the circle.
Then $\lambda_X$ is the direct sum of the characters $x \mapsto e^{i n x}$, $n \in \Z$, each with multiplicity one, and the expansion is the classical Fourier series.

Example: for $G = \mathrm{SO}(3)$ and $H = \mathrm{SO}(2)$, $L^2(S^2)$ is the direct sum of the spaces of spherical harmonics of degree $\ell \ge 0$, each irreducible and occurring once.

Non-example: let $G$ be the affine group $\set{x \mapsto a x + b : a > 0, \ b \in \R}$ and $H$ the stabilizer $\set{x \mapsto a x : a > 0}$ of $0$.
Then $G / H \cong \R$, but there is no nonzero $G$-invariant Radon measure on $\R$: invariance under translations forces a multiple of Lebesgue measure, and dilations change Lebesgue measure.
So the first condition fails, and the formula above does not give a unitary representation.
