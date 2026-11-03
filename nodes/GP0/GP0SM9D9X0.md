---
tag: GP0SM9D9X0
kind: definition
name: Hamiltonian mechanics
msc: [70H05, 37J39]
defines: MPM0RHWCN6
uses: [47JMCBM3VJ, BCF1EX9W2M, 0EDKGA2FAK, 0693Y2METT]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_mechanics
---

## Definition

Let $U \subseteq \R^n$ be open, let $I \subseteq \R$ be an open interval, and let $L \colon U \times \R^n \times I \to \R$, $L = L(q, \dot q, t)$, be a Lagrangian of class $C^2$ in [[generalized coordinates|BCF1EX9W2M]] $q$.
The *generalized momenta* are $p_i = \partial L / \partial \dot q_i (q, \dot q, t)$ for $i = 1, \ldots, n$.
Assume that $L$ is *hyperregular*: for each $(q, t)$ the map $\dot q \mapsto p$ is a bijection of $\R^n$ onto an open set.
Assume also that its inverse $\dot q = v(q, p, t)$ is of class $C^1$ jointly in $(q, p, t)$.
The *Hamiltonian* of $L$ is
$$H(q, p, t) = \sum_{i=1}^n p_i \, v_i(q, p, t) - L\big(q, v(q, p, t), t\big).$$
*Hamiltonian mechanics* describes the motion by curves $t \mapsto (q(t), p(t))$ in the phase space of the variables $(q, p)$ that satisfy the [[Hamiltonian system|0EDKGA2FAK]]
$$\dot q_i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q_i}, \qquad i = 1, \ldots, n.$$

## Remarks

The passage from $L$ to $H$ is the Legendre transform in the velocity variables.
Hyperregularity holds when the [[Hessian matrix|0693Y2METT]] $\big(\partial^2 L / \partial \dot q_i \partial \dot q_j\big)$ is positive definite everywhere and $L$ grows faster than linearly in $\dot q$, as for the usual mechanical Lagrangians.

Example: for $L = \frac{1}{2} m \abs{\dot q}^2 - V(q, t)$ with $m > 0$, the momenta are $p = m \dot q$, so $v = p/m$, and
$$H = \frac{\abs{p}^2}{2m} + V(q, t),$$
the kinetic plus the potential energy.

Non-example: $L = \dot q$ for $n = 1$ gives $p = 1$ for every $\dot q$, so $\dot q \mapsto p$ is not injective and no Hamiltonian is defined in this way; such degenerate Lagrangians lead to constrained Hamiltonian systems.

One can also start directly from any function $H(q, p, t)$ of class $C^1$ on an open subset of $\R^{2n} \times \R$ and study its Hamiltonian system, without reference to a Lagrangian.
