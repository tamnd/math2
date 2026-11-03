---
tag: N20ZKQ5P2J
kind: definition
name: Lagrangian mechanics
msc: [70H03, 70G45]
defines: 47JMCBM3VJ
uses: [MGYKGP7PW3, F45VQ47GPV, WY6K3P4YCG, PS0VV149ET, C9YCMAPKMT, DF7DKHTQ7A]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_mechanics
---

## Definition

A *Lagrangian system* is a pair $(Q, L)$ of the following kind.
The [[configuration space|MGYKGP7PW3]] $Q$ is a [[smooth manifold|F45VQ47GPV]] of dimension $n$.
The *Lagrangian* $L \colon \R \times TQ \to \R$ is a smooth function on the product of the time axis with the [[tangent bundle|WY6K3P4YCG]] of $Q$.
A *motion* of the system is a $C^2$ curve $q \colon [t_0, t_1] \to Q$ that satisfies, in every local chart with coordinates $q_1, \ldots, q_n$, the [[Euler–Lagrange equations|PS0VV149ET]]
$$\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}\big(t, q(t), \dot q(t)\big) = \frac{\partial L}{\partial q_i}\big(t, q(t), \dot q(t)\big), \qquad i = 1, \ldots, n.$$
*Lagrangian mechanics* is the study of Lagrangian systems.

## Remarks

The Euler–Lagrange equations have the same form in every chart, so the definition does not depend on the choice of coordinates.
The *natural* systems are those with $L = T - V$, where the [[kinetic energy|C9YCMAPKMT]] $T(q, v) = \tfrac12 g_q(v, v)$ comes from a Riemannian metric $g$ and the [[potential energy|DF7DKHTQ7A]] $V$ is a function on $Q$.
The quantities $p_i = \partial L / \partial \dot q_i$ are the generalized momenta.

Example: a particle of mass $m$ in $\R^3$ with potential $V$ has $Q = \R^3$ and $L = \tfrac12 m\abs{\dot q}^2 - V(q)$.
Then $\partial L/\partial \dot q_i = m\dot q_i$ and $\partial L/\partial q_i = -\partial V/\partial q_i$, so the equations are Newton's law $m\ddot q = -\nabla V(q)$.

Non-example: the damped oscillator $m\ddot x + b\dot x + kx = 0$ with $b > 0$ has no Lagrangian $L(x, \dot x)$ that is independent of time, smooth on the whole plane and has $\partial^2 L / \partial \dot x^2 \ne 0$.
Such a Lagrangian would make the energy $E = \dot x\, \partial L/\partial \dot x - L$ constant along motions, and $E$ is not a constant function since $\partial E/\partial \dot x = \dot x\, \partial^2 L/\partial \dot x^2$.
But every solution of the damped equation tends to $(x, \dot x) = (0, 0)$, so a continuous function constant along motions is constant on the whole plane, a contradiction.
The time-dependent Lagrangian $e^{bt/m}\big(\tfrac12 m\dot x^2 - \tfrac12 k x^2\big)$ does give this equation.

## Explanations

### L1 human

A Lagrangian system is given by a space of positions and one function of position, velocity and time.
Its motions are the curves that satisfy the Euler–Lagrange equations of this function.
