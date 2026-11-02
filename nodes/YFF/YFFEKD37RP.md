---
tag: YFFEKD37RP
kind: definition
name: Order of a PDE
msc: [35A99]
defines: E7JDFDPM1X
uses: [GC5BDZ6QBC, 0PJXBR6QA3, 0XK0G19SK8]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_differential_equation
---

## Definition

Let $F\left(D^k u, \dots, D u, u, x\right) = 0$ be a [[partial differential equation|GC5BDZ6QBC]] in an open set $\Omega \subseteq \R^n$.
Here $D^j u$ is the collection of the partial derivatives $\partial^\alpha u$ with $\abs{\alpha} = j$, in [[multi-index notation|0PJXBR6QA3]].
Its *order* is the largest integer $m$ such that $F$ actually depends on some derivative $\partial^\alpha u$ with $\abs{\alpha} = m$.
For a system of equations, the order is the largest order of a derivative that occurs in some equation of the system.

## Remarks

Example: the [[minimal surface equation|3GV2E2YTZX]] in two variables involves $\partial_x^2 u$, $\partial_x \partial_y u$ and $\partial_y^2 u$ but no third derivatives, so it has order $2$.
Non-example of a misreading: $(\partial_x u)^2 + (\partial_y u)^2 = 1$ has order $1$, not $2$, because the square is a power of a first derivative and not a second derivative.
This is the same notion as the [[order of a differential equation|0XK0G19SK8]], applied to equations in several variables.
A mixed derivative $\partial^\alpha u$ counts with its total order $\abs{\alpha} = \alpha_1 + \dots + \alpha_n$.

## Explanations

### L1 human

The order of a PDE is the largest total number of differentiations applied to the unknown in any term.
