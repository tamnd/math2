---
tag: 29PHKDB4PT
kind: statement
role: theorem
name: Gelfand spectrum of L1(G)
msc: [43A20, 46J20, 43A25]
uses: [ZR09S9R3AW, VY0HXD3GC4, 6GD25S53ND, FMW57WNPDB, VHN5VW5Q92, M7JVFJ3MMX, VWNSHKJT92]
about: [6GD25S53ND, M7JVFJ3MMX]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand_representation
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with a [[Haar measure|VY0HXD3GC4]], and let $L^1(G)$ be its [[group algebra|6GD25S53ND]], a commutative Banach algebra under convolution.
Let $\widehat{G}$ be the [[Pontryagin dual|FMW57WNPDB]] of $G$, and let $\widehat{f}$ be the [[Fourier transform|VHN5VW5Q92]] of $f \in L^1(G)$.
For $\chi \in \widehat{G}$ let $h_\chi(f) = \widehat{f}(\chi)$.
Then the following hold.

1. Each $h_\chi$ is a nonzero multiplicative linear functional on $L^1(G)$.
2. Every nonzero multiplicative linear functional on $L^1(G)$ equals $h_\chi$ for exactly one $\chi \in \widehat{G}$.
3. The map $\chi \mapsto h_\chi$ is a homeomorphism from $\widehat{G}$ onto the [[character space|M7JVFJ3MMX]] of $L^1(G)$ with its weak-* topology.
4. Under this identification, the [[Gelfand transform|VWNSHKJT92]] of $f$ is $\widehat{f}$.

## Remarks

Proof idea: $h_\chi$ is multiplicative because the Fourier transform turns convolution into products.
Conversely, a nonzero multiplicative linear functional $h$ has norm at most $1$, so $h(f) = \int_G f \varphi$ for some $\varphi \in L^\infty(G)$.
Multiplicativity gives $\varphi(x + y) = \varphi(x)\varphi(y)$ almost everywhere, and one shows that $\varphi$ agrees almost everywhere with $\overline{\chi}$ for a continuous character $\chi$.
The comparison of topologies uses the uniform continuity of translation in $L^1(G)$.

Example: for $G = \Z$ the algebra is $\ell^1(\Z)$ and $\widehat{\Z} = \mathbb{T}$.
The functional for $z \in \mathbb{T}$ is $a \mapsto \sum_n a_n z^{-n}$, so the Gelfand transform is an absolutely convergent Fourier series.
Gelfand's theory then gives Wiener's lemma: if such a series has no zero on $\mathbb{T}$, then its reciprocal is again an absolutely convergent Fourier series.

## Explanations

### L1 human

The integrable functions on an abelian group form an algebra where the product is convolution.
The theorem says that the ways to map this algebra to the complex numbers, keeping products, are exactly the evaluations of the Fourier transform at one character.
So the abstract theory of commutative Banach algebras, applied to $L^1(G)$, gives back the dual group and the Fourier transform.

### L2 human

This is the bridge between Gelfand theory and harmonic analysis.
It shows at once that $\widehat{f}$ is continuous and vanishes at infinity, because all Gelfand transforms do.
It also turns questions about closed ideals of $L^1(G)$ into questions about sets of characters, as in Wiener's Tauberian theorem and in spectral synthesis.
The maximal regular ideals of $L^1(G)$ are the kernels of the functionals $h_\chi$.
