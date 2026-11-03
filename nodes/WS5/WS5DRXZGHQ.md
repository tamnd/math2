---
tag: WS5DRXZGHQ
kind: definition
name: Fracture mechanics
msc: [74R10, 74A45, 74G70]
defines: SNRXGRZWR5
uses: [JRD6BDKT1X, 6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Fracture_mechanics
---

## Definition

Let $\Omega \subset \R^3$ be the reference configuration of a deformable body.
A *crack* in $\Omega$ is a closed set $\Gamma \subset \overline{\Omega}$, usually a surface with boundary, across which the displacement may jump.
Unless stated otherwise, its two faces are free of tractions.
The boundary curve of $\Gamma$ inside $\Omega$ is the *crack front*.
*Fracture mechanics* is the theory of the equilibrium and motion of bodies $\Omega \setminus \Gamma$ with cracks.
It consists of:

1. the solution of boundary value problems on $\Omega \setminus \Gamma$, in [[linear elasticity|6W00ZECYT0]] or another material model, near the crack front;
2. a criterion that decides, from quantities computed in 1, whether the crack $\Gamma$ stays as it is or grows;
3. a law for the direction and speed of crack growth.

*Linear elastic fracture mechanics* is the case in which the material in 1 is linear elastic.

## Remarks

Example: a plate in plane stress with a straight through crack of length $2a$ under remote tension $\sigma$ is a problem of linear elastic fracture mechanics.
The crack-tip stresses behave like $\sigma \sqrt{a / (2r)}$ at distance $r$ from a tip.
The Griffith criterion decides when the crack grows.
Non-example: the theory of the strength of an uncracked bar, which compares the stress with a yield or tensile strength, has no crack and no crack growth criterion.
Fracture mechanics with plastic zones much smaller than the crack is still treated by linear elastic theory (small-scale yielding); larger plastic zones require elastic–plastic fracture mechanics.

## Explanations

### L1 human

Fracture mechanics starts from a body that already has a crack.
It computes how the loads are concentrated at the crack front, and then decides whether the crack stays put or grows.
