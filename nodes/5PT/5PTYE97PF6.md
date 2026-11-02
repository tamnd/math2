---
tag: 5PTYE97PF6
kind: object
name: Siegel upper half-space
msc: [32M15, 11F46]
instance_of: [NT4797Z9H8]
uses: [NT4797Z9H8, X6XGGH5FPW, X12FS2JAP0, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Siegel_upper_half-space
same_as:
  wikidata: Q2283003
  wikipedia: Siegel upper half-space
---

## Description

Let $g \ge 1$ be an integer.
The *Siegel upper half-space* of degree $g$ is
$$\mathbb{H}_g = \set{Z \in M_{g \times g}(\C) : Z^T = Z,\ \operatorname{Im} Z \text{ is positive definite}}.$$
It is an open subset of the space of complex symmetric $g \times g$ matrices, so it is a complex manifold of dimension $g(g+1)/2$.
For $g = 1$ it is the [[upper half-plane|X6XGGH5FPW]].

The real [[symplectic group|X12FS2JAP0]] $Sp(2g, \R)$, the group of real $2g \times 2g$ matrices $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ with $M^T J M = J$ for $J = \begin{pmatrix} 0 & I_g \\ -I_g & 0 \end{pmatrix}$, acts on $\mathbb{H}_g$ by
$$M \cdot Z = (AZ + B)(CZ + D)^{-1}.$$
For $Z = X + iY \in \mathbb{H}_g$, the matrix $\begin{pmatrix} Y^{1/2} & X Y^{-1/2} \\ 0 & Y^{-1/2} \end{pmatrix}$ is symplectic and sends $iI_g$ to $Z$, so the action is transitive.
The stabilizer of $iI_g$ is the subgroup with $A = D$ and $C = -B$, which is isomorphic to the unitary group $U(g)$ via $A + iB$.
Hence $\mathbb{H}_g \cong Sp(2g, \R)/U(g)$.

## Remarks

The Siegel upper half-space is a [[Hermitian symmetric space|NT4797Z9H8]] of noncompact type, the type $III_g$ in Cartan's list.
The Cayley transform $Z \mapsto (Z - iI)(Z + iI)^{-1}$ maps it biholomorphically onto the bounded domain $\set{W : W^T = W,\ I - W^* W > 0}$.
The quotient $Sp(2g, \Z) \backslash \mathbb{H}_g$ is the moduli space of principally polarized abelian varieties of dimension $g$: the point $Z$ corresponds to the complex torus $\C^g / (\Z^g + Z \Z^g)$.
Siegel modular forms are functions on $\mathbb{H}_g$ with a transformation law under $Sp(2g, \Z)$.

## Explanations

### L1 human

The upper half-plane is the set of complex numbers with positive imaginary part.
The Siegel upper half-space replaces the number by a symmetric matrix and "positive" by "positive definite".
Just as the upper half-plane parametrizes elliptic curves, the Siegel space parametrizes higher-dimensional complex tori with a polarization, through their period matrices.
