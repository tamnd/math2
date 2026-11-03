---
tag: AF8V6SMF2H
kind: statement
role: theorem
name: Invariant measure on a homogeneous space
msc: [28C10, 43A85, 22D05]
uses: [AHV05ZBCYW, 417ZRDCHY6, 85TWR6E75P, VY0HXD3GC4, 63TX60RTRQ, HZNEQQBCW4]
about: [85TWR6E75P, VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $H$ be a closed subgroup of $G$.
Let $\Delta_G$ and $\Delta_H$ be the [[modular functions|63TX60RTRQ]] of $G$ and of $H$.
Let $G/H$ be the space of left cosets $xH$ with the [[quotient topology|417ZRDCHY6]], on which $G$ acts by $g \cdot xH = gxH$.
Then the following are equivalent.

1. There is a nonzero [[Radon measure|HZNEQQBCW4]] $\nu$ on $G/H$ that is $G$-invariant: $\nu(gE) = \nu(E)$ for every $g \in G$ and every Borel set $E \subseteq G/H$.
2. $\Delta_G(h) = \Delta_H(h)$ for every $h \in H$.

When these hold, such a measure $\nu$ is unique up to a positive constant factor.

## Remarks

The idea of the proof: the map $P \colon C_c(G) \to C_c(G/H)$, $(Pf)(xH) = \int_H f(xh) \, dh$, is onto.
Under condition 2 the functional $Pf \mapsto \int_G f(x) \, dx$ is well defined on $C_c(G/H)$, and the Riesz representation theorem turns it into the measure $\nu$.
Conversely, an invariant $\nu$ gives the functional $f \mapsto \int_{G/H} Pf \, d\nu$, which is a left Haar integral on $G$.
Comparing how both sides change under right translation by $h \in H$ forces $\Delta_G(h) = \Delta_H(h)$.

Example: if $H$ is compact, then $\Delta_H$ and $\Delta_G|_H$ are continuous homomorphisms from a compact group into $(0, \infty)$, so both are identically $1$.
Thus $G/H$ has an invariant measure; for instance the sphere $S^{n-1} = SO(n)/SO(n-1)$ carries the rotation-invariant surface measure.
The same holds when $G$ and $H$ are both unimodular, for instance when $H$ is discrete and $G$ is unimodular.

Non-example: let $G$ be the group of maps $x \mapsto ax + b$ of $\R$ with $a > 0$, and let $H = \set{x \mapsto ax}$.
Then $H \cong (0, \infty)$ is abelian, so $\Delta_H = 1$, but $\Delta_G$ is not identically $1$ on $H$.
Here $G/H$ is identified with $\R$, and there is no nonzero $G$-invariant Radon measure on $\R$: it would be invariant under translations and dilations at once.

## Explanations

### L1 human

A homogeneous space is a space on which a group acts so that every point can be moved to every other point, such as the sphere under rotations.
One would like a way to measure areas on it that the group does not change.
The theorem says when this is possible: a certain balance between how the group and the stabilizer of a point distort volumes must hold.
When it holds, the invariant measure is unique apart from the choice of unit.

### L2 human

The theorem reduces the existence of invariant measures to a computation with modular functions, which are often explicit.
It applies whenever $H$ is compact, which gives invariant measures on spheres, Grassmannians and Riemannian symmetric spaces.
It also applies to lattices $\Gamma$ in unimodular groups, which gives the invariant measure on $G/\Gamma$ used in the theory of automorphic forms.
When the condition fails, $G/H$ still has quasi-invariant measures, which change under the action only by a density.
The invariant measure is linked to the Haar measures of $G$ and $H$ by [[Weil's quotient integral formula|NW3R4Q6WN9]].
