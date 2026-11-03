---
tag: AV2WRWW1TN
kind: statement
role: theorem
name: Conservation of energy
msc: [70A05, 70F10]
uses: [KNBP19FG6K, 4NMMPYCK2C, 5T5GAKQD3S, SNB562CJDB]
about: [C9YCMAPKMT, DF7DKHTQ7A]
sources:
  - url: https://en.wikipedia.org/wiki/Conservation_of_energy
---

## Statement

Let $N$ point particles have masses $m_i > 0$ and positions $x_i(t) \in \R^3$.
Let $U \subseteq \R^{3N}$ be open and let $V \colon U \to \R$ be of class $C^1$.
Suppose that the motion $x = (x_1, \dots, x_N)$ takes values in $U$ and obeys [[Newton's second law|KNBP19FG6K]] with the forces $F_i = -\nabla_{x_i} V$, that is,
$$m_i \ddot x_i(t) = -\nabla_{x_i} V\big(x(t)\big), \qquad i = 1, \dots, N.$$
Then the total mechanical energy
$$E(t) = \sum_{i=1}^{N} \tfrac12 m_i \abs{\dot x_i(t)}^2 + V\big(x(t)\big),$$
the sum of the [[kinetic energy|4NMMPYCK2C]] and the [[potential energy|5T5GAKQD3S]], is constant in $t$.

## Remarks

By the chain rule, $\dot E = \sum_i m_i \ddot x_i \cdot \dot x_i + \sum_i \nabla_{x_i} V \cdot \dot x_i = \sum_i (m_i \ddot x_i + \nabla_{x_i} V) \cdot \dot x_i = 0$.
Equivalently, by the [[work–energy theorem|SNB562CJDB]], the gain of kinetic energy equals the work of the forces, which equals the loss of potential energy.
Example: a stone thrown upward at speed $v_0$ with $V = m g z$ reaches its greatest height $h$, where it is at rest, with $\frac12 m v_0^2 = m g h$, that is, $h = v_0^2/(2g)$.
The hypothesis that the forces come from a time-independent potential is needed: friction, or a potential that depends explicitly on time, can change $E$.
In physics, conservation of energy is a wider principle that also counts heat and other forms of energy; this statement is its mechanical part.

## Explanations

### L1 human

When only forces such as gravity or springs act, energy just changes form between motion and position.
A swinging pendulum is fastest at the bottom and stops for an instant at the top, but the sum of the two energies never changes.

### L2 human

Energy is a first integral of the equations of motion, which reduces their order.
For one degree of freedom, $\frac12 m \dot q^2 + V(q) = E$ can be solved for $\dot q$ and integrated by quadrature.
In Lagrangian mechanics this conservation follows from the invariance of the Lagrangian under time shifts, an instance of Noether's theorem.
