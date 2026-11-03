---
tag: NW3R4Q6WN9
kind: statement
role: theorem
name: Weil's quotient integral formula
msc: [28C10, 43A85, 22D05]
uses: [AHV05ZBCYW, 417ZRDCHY6, VY0HXD3GC4, 63TX60RTRQ, AF8V6SMF2H]
about: [VY0HXD3GC4, 85TWR6E75P]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $H$ be a closed subgroup of $G$.
Let $dx$ and $dh$ be left [[Haar measures|VY0HXD3GC4]] on $G$ and on $H$.
Assume that the [[modular functions|63TX60RTRQ]] satisfy $\Delta_G(h) = \Delta_H(h)$ for every $h \in H$.
Then there is a unique $G$-invariant Radon measure $d\dot{x}$ on the [[quotient space|417ZRDCHY6]] $G/H$ such that
$$\int_G f(x) \, dx = \int_{G/H} \left( \int_H f(xh) \, dh \right) d\dot{x}$$
for every continuous function $f \colon G \to \C$ with compact support.

## Remarks

The inner integral depends only on the coset $xH$, by left invariance of $dh$, so the right side makes sense.
The proof is the construction in the theorem on the [[invariant measure on a homogeneous space|AF8V6SMF2H]].
The formula is taken as the definition of a functional on $C_c(G/H)$, and the hypothesis on the modular functions shows that it is well defined.
Uniqueness holds because every function in $C_c(G/H)$ has the form $xH \mapsto \int_H f(xh) \, dh$ for some $f \in C_c(G)$.
The formula then extends to all $f \in L^1(G)$, with the inner integral defined for almost every coset.

Example: $G = \R$, $H = \Z$, with Lebesgue measure on $\R$ and counting measure on $\Z$.
Then $G/H$ is the circle $\R/\Z$, the invariant measure is Lebesgue measure on $[0, 1)$, and the formula reads
$$\int_\R f(x) \, dx = \int_0^1 \sum_{n \in \Z} f(x + n) \, dx.$$
This is the identity behind periodization and the Poisson summation formula.

Without the hypothesis on the modular functions, $G/H$ has no nonzero $G$-invariant Radon measure.
The formula then holds only in a modified form, with a quasi-invariant measure and a correcting density.

## Explanations

### L1 human

To integrate over a group, one can first integrate along each coset of a subgroup and then integrate the results over the space of cosets.
This is like computing the area of a region by first integrating along vertical lines and then over the horizontal axis.
Weil's formula says that this works for groups, with the right choice of measure on the space of cosets.

### L2 human

The formula is a Fubini theorem for the fibration $G \to G/H$ with fibres the cosets $xH$.
It is used to normalize measures on homogeneous spaces compatibly with Haar measures, for instance to compute the volume of $SL_n(\R)/SL_n(\Z)$.
For a lattice $\Gamma$ in $G$, it relates integrals over $G$ to integrals over a fundamental domain, which is basic in the theory of automorphic forms.
For abelian $G$, combined with Pontryagin duality, it gives the Poisson summation formula for a closed subgroup and its annihilator.
