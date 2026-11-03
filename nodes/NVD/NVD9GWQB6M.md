---
tag: NVD9GWQB6M
kind: definition
name: Kirillov orbit method
msc: ["22E27", "22E45", 22D10]
defines: G9AW6R1D2F
uses: [DK87YN458D, 07JBSZE0V4, P6ZP0TE07M, 0YQPZB5Q1G, H3QX1ZFC8K, 6Q7AHAZ6Q4, 95Q8WZMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Orbit_method
---

## Definition

Let $G$ be a connected and simply connected [[nilpotent Lie group|DK87YN458D]] with [[Lie algebra|5JJYBJ6A8K]] $\mathfrak g$ and [[exponential map|H3QX1ZFC8K]] $\exp \colon \mathfrak g \to G$.
Let $\mathfrak g^*$ be the [[dual space|07JBSZE0V4]] of $\mathfrak g$, with the coadjoint action $(g \cdot \ell)(X) = \ell(\mathrm{Ad}(g^{-1}) X)$, where $\mathrm{Ad}$ is the [[adjoint representation|P6ZP0TE07M]].
For $\ell \in \mathfrak g^*$, a *polarization* at $\ell$ is a Lie subalgebra $\mathfrak h \subseteq \mathfrak g$ such that $\ell([\mathfrak h, \mathfrak h]) = 0$ and $\mathfrak h$ is a maximal subspace with this property.
For such $\mathfrak h$, let $H = \exp \mathfrak h$ and let $\chi_\ell$ be the unitary character $\chi_\ell(\exp Y) = e^{i \ell(Y)}$ of $H$.
The *Kirillov orbit method* assigns to $\ell$ the [[induced representation|6Q7AHAZ6Q4]]
$$\pi_\ell = \mathrm{Ind}_H^G \chi_\ell.$$
By Kirillov's theorem, $\pi_\ell$ is irreducible, and its class depends only on the [[orbit|0YQPZB5Q1G]] $G \cdot \ell$, not on the choice of $\mathfrak h$.
The map $G \cdot \ell \mapsto \pi_\ell$ is a bijection from the set of coadjoint orbits onto the [[unitary dual|95Q8WZMN0W]] of $G$.

## Remarks

A polarization always exists for nilpotent $\mathfrak g$, and its dimension is $\tfrac12 (\dim \mathfrak g + \dim \mathfrak g_\ell)$, where $\mathfrak g_\ell = \set{X : \ell([X, \mathfrak g]) = 0}$.

Example: let $\mathfrak g$ have basis $X, Y, Z$ with $[X, Y] = Z$ and $Z$ central, the Lie algebra of the Heisenberg group.
For $\ell$ with $\ell(Z) = \lambda \ne 0$, the coadjoint orbit is the plane $\set{\ell' : \ell'(Z) = \lambda}$.
The subalgebra $\mathfrak h = \operatorname{span}(Y, Z)$ is abelian, so $\ell([\mathfrak h, \mathfrak h]) = 0$, and it is maximal with this property since $\ell([X, Y]) = \lambda \ne 0$.
The induced representation $\pi_\ell$ is the Schrödinger representation with central character $e^{i \lambda z}$.
For $\ell(Z) = 0$ the orbit is the single point $\ell$, and $\pi_\ell$ is the one-dimensional character $\exp(aX + bY + cZ) \mapsto e^{i(a \ell(X) + b \ell(Y))}$.

Non-example: for $\ell(Z) = \lambda \ne 0$, the center $\mathfrak h = \operatorname{span}(Z)$ satisfies $\ell([\mathfrak h, \mathfrak h]) = 0$ but is not maximal.
The induced representation $\mathrm{Ind}_H^G \chi_\ell$ acts on $L^2(\R^2)$ and is a direct sum of infinitely many copies of the Schrödinger representation, so it is reducible.
