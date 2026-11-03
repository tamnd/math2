---
tag: VKJBAB97CP
kind: definition
name: Beam theory
msc: [74K10, 74B05]
defines: GDM0J9ZCBT
uses: [6W00ZECYT0, Q6XAPXMGH0]
sources:
  - url: https://en.wikipedia.org/wiki/Euler–Bernoulli_beam_theory
---

## Definition

Let a straight body occupy $\set{(x, y, z) : 0 < x < L, \ (y, z) \in A}$, where the cross-section $A \subset \R^2$ has a diameter much smaller than the length $L$.
Let the body be made of a [[linear elastic|6W00ZECYT0]] material and carry a transverse load $q(x)$ per unit length.
A *beam theory* is a model of this body in which:

1. The unknowns are functions of $x$ alone, such as the transverse deflection $w(x)$ of the axis and the rotation $\varphi(x)$ of the cross-section.
2. The displacement of the body is given in terms of these unknowns by an assumption on the kinematics of the cross-sections.
3. The internal forces are the shear force $V(x)$ and the [[bending moment|Q6XAPXMGH0]] $M(x)$.
   With $q$ and $w$ measured in the same direction they satisfy the equilibrium equations $V' = -q$ and $M' = V$.
4. A constitutive law, derived from the elastic law and the assumption of clause 2, expresses $M$ and $V$ through the unknowns.

## Remarks

Example: Euler–Bernoulli theory assumes that cross-sections stay plane and normal to the deformed axis, so $\varphi = w'$, and it takes $M = -EI w''$ with Young's modulus $E$ and second moment of area $I$.
Then the equilibrium equations give $(EI w'')'' = q$, the [[Euler–Bernoulli beam equation|13FGKM7NQ0]].

Non-example: a model in which the body is described by the full displacement field $u(x, y, z)$ is three-dimensional elasticity and fails clause 1.

The sign conventions for $M$ and $V$ differ between texts; the ones here make a sagging moment positive when $w$ and $q$ point downwards.
