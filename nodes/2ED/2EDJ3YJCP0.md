---
tag: 2EDJ3YJCP0
kind: definition
name: Lagrangian and Eulerian description
msc: [74A05, 76A02]
defines: 43949CJRF6
uses: [X01DZTS224, E51Y1CMF1Q]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_and_Eulerian_specification_of_the_flow_field
---

## Definition

Let $B \subseteq \R^3$ be the reference configuration of a [[continuum body|X01DZTS224]], and let $\chi \colon B \times I \to \R^3$ be a motion.
So each $\chi(\cdot, t)$ is a [[deformation|E51Y1CMF1Q]] of $B$ onto $\Omega_t = \chi(B, t)$.
A physical quantity of the body can be given in two ways.

1. The *Lagrangian* or *material description* gives it as a function $f_L(X, t)$ of the material point $X \in B$ and the time $t$.
2. The *Eulerian* or *spatial description* gives it as a function $f_E(x, t)$ of the place $x \in \Omega_t$ and the time $t$.

The two describe the same quantity when $f_L(X, t) = f_E(\chi(X, t), t)$ for all $X \in B$ and $t \in I$.

## Remarks

The velocity has the Lagrangian form $V(X, t) = \partial_t \chi(X, t)$ and the Eulerian form $v(x, t) = V(\chi^{-1}(x, t), t)$, where $\chi^{-1}(\cdot, t)$ is the inverse of $\chi(\cdot, t)$.
For the motion $\chi(X, t) = e^t X$ in $\R^3$, one has $V(X, t) = e^t X$ and $v(x, t) = x$: the Eulerian velocity field is steady although every particle other than the one at the origin accelerates.
The time derivative at fixed $X$ is the *material derivative*; in Eulerian terms it is $\partial_t f_E + (v \cdot \nabla) f_E$ by the chain rule.

## Explanations

### L1 human

The Lagrangian description follows the particles; the Eulerian description watches fixed points of space.
The rate of change felt by a moving particle is the local change at its place plus the change caused by moving to a new place.
