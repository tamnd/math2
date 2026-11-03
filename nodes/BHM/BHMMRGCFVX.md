---
tag: BHMMRGCFVX
kind: definition
name: Group von Neumann algebra
msc: ["22D25", "46L10"]
defines: 2N7CR03Q1X
uses: [AHV05ZBCYW, VY0HXD3GC4, PSFWQVZ0FS, 1VC7EJ1ZBZ, KHJ2G2R5G7]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_algebra
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]] $\mu$.
For $g \in G$, let $\lambda(g)$ be the unitary operator on $L^2(G, \mu)$ given by $(\lambda(g)\xi)(x) = \xi(g^{-1}x)$, the [[left regular representation|PR8C073VWY]].
The *group von Neumann algebra* of $G$ is
$$L(G) = \set{\lambda(g) : g \in G}'',$$
the double [[commutant|1VC7EJ1ZBZ]] of the set of operators $\lambda(g)$ in the bounded operators on $L^2(G)$.

## Remarks

By the von Neumann bicommutant theorem, $L(G)$ is the closure in the [[strong operator topology|KHJ2G2R5G7]] of the linear span of the operators $\lambda(g)$, and it is a [[von Neumann algebra|PSFWQVZ0FS]].

Example: $G = \Z$.
Fourier series identify $\ell^2(\Z)$ with $L^2(\mathbb{T})$, and $\lambda(n)$ with multiplication by $z^n$.
The commutant of these multiplications is the algebra of multiplications by functions in $L^\infty(\mathbb{T})$, which is its own commutant, so $L(\Z) \cong L^\infty(\mathbb{T})$.

Non-example: the reduced group C\*-algebra $C^*_r(\Z) \cong C(\mathbb{T})$, acting by multiplication on $L^2(\mathbb{T})$, is not a von Neumann algebra.
Its double commutant is $L^\infty(\mathbb{T})$, which is strictly larger than $C(\mathbb{T})$.

For a discrete group $G$, the vector $\delta_e$ gives a faithful normal trace $\tau(a) = \ip{a\delta_e}{\delta_e}$ on $L(G)$.
If $G$ is a nontrivial discrete group and every conjugacy class of $G$ other than $\set{e}$ is infinite, then $L(G)$ is a factor of type $\mathrm{II}_1$.
