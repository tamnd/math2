---
tag: J2Y33XCRH3
kind: definition
name: Left regular representation
msc: ["22D10", "43A65"]
defines: PR8C073VWY
uses: [AHV05ZBCYW, VY0HXD3GC4, SASP14MA1Z, 74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_representation
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]] $m$, and let $L^2(G) = L^2(G, m)$.
For $g \in G$ and $\xi \in L^2(G)$, let
$$(\lambda(g)\xi)(x) = \xi(g^{-1} x), \quad x \in G.$$
The *left regular representation* of $G$ is the map $\lambda$ from $G$ to the unitary operators on $L^2(G)$.

## Remarks

Each $\lambda(g)$ is unitary because $m$ is left invariant, and $\lambda(gh) = \lambda(g)\lambda(h)$ because $(gh)^{-1}x = h^{-1}(g^{-1}x)$.
The map $g \mapsto \lambda(g)\xi$ is continuous for each $\xi$, so $\lambda$ is a [[unitary representation|74BPYJNZTM]].
The right regular representation is $(\rho(g)\xi)(x) = \Delta(g)^{1/2} \xi(xg)$, where $\Delta$ is the modular function; it is unitarily equivalent to $\lambda$.

Example: for a finite group $G$ with counting measure, $L^2(G)$ is the group algebra $\C[G]$ and $\lambda(g)\delta_x = \delta_{gx}$.
Every irreducible representation $\pi$ of $G$ appears in $\lambda$ with multiplicity $\dim \pi$.

Non-example: the formula $(T_g \xi)(x) = \xi(g x)$ does not define a representation when $G$ is not abelian.
Indeed $(T_g T_h \xi)(x) = (T_h \xi)(g x) = \xi(h g x)$, so $T_g T_h = T_{hg}$, and $T_{hg} \ne T_{gh}$ when $gh \ne hg$.

For $f \in L^1(G)$, the integrated operator $\lambda(f) = \int_G f(g)\lambda(g) \, dm(g)$ is convolution by $f$, and the norm closure of these operators is the reduced group C\*-algebra.
