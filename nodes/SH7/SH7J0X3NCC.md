---
tag: SH7J0X3NCC
kind: definition
name: Classical mechanics
msc: [70A05, 70F10]
defines: 68W1NWECX8
uses: [0XPR1E85W0, 0NT64JV96A, 0P6KRD5B7A]
sources:
  - url: https://en.wikipedia.org/wiki/Classical_mechanics
---

## Definition

A *Newtonian system of $N$ point particles* consists of the following data.

1. Masses $m_1, \dots, m_N > 0$.
2. For each $i$, a position $x_i(t) \in \R^3$ at time $t$, where $\R^3$ is three-dimensional [[Euclidean space|0XPR1E85W0]].
3. For each $i$, a force law $F_i(t, x, \dot x) \in \R^3$, a function of the time $t$, of all positions $x = (x_1, \dots, x_N)$ and of all velocities $\dot x = (\dot x_1, \dots, \dot x_N)$.

A *motion* of the system is a twice differentiable map $t \mapsto (x_1(t), \dots, x_N(t))$ on an interval that solves the [[ordinary differential equations|0NT64JV96A]]
$$m_i \ddot x_i(t) = F_i\big(t, x(t), \dot x(t)\big), \qquad i = 1, \dots, N.$$
Classical mechanics, in its Newtonian form, is the study of such systems and their motions.

## Remarks

Example: one particle of mass $m$ under the constant force $F = (0, 0, -mg)$ with $g > 0$.
The map $x(t) = (t, 0, -g t^2/2)$ is a motion, since $m \ddot x = (0, 0, -mg) = F$.
Non-example: the map $x(t) = (t, 0, 0)$ is not a motion of this system, since $m \ddot x = 0 \ne F$.
If the force laws are locally Lipschitz, the [[Picard–Lindelöf theorem|0P6KRD5B7A]] shows that the initial positions and velocities determine the motion on some interval.
A dot over a symbol denotes the derivative with respect to time.

## Explanations

### L1 human

The model keeps only what matters for motion: where each particle is, how heavy it is, and which force acts on it.
The equation "mass times acceleration equals force" then decides the whole future from the present positions and velocities.
