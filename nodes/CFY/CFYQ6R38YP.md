---
tag: CFYQ6R38YP
kind: statement
role: theorem
name: Hamilton's equations
msc: [70H05, 70H03]
uses: [MPM0RHWCN6, PS0VV149ET, 0EDKGA2FAK, 47JMCBM3VJ]
about: [MPM0RHWCN6, 0EDKGA2FAK]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_mechanics
---

## Statement

Let $U \subseteq \R^n$ and $I \subseteq \R$ be open, and let $L(q, \dot q, t)$ be a hyperregular Lagrangian of class $C^2$ on $U \times \R^n \times I$, with [[Hamiltonian|MPM0RHWCN6]] $H(q, p, t)$ and momenta $p = \partial L / \partial \dot q$.
Let $J \subseteq I$ be an open interval, let $q \colon J \to U$ be of class $C^2$, and let $p(t) = \frac{\partial L}{\partial \dot q}\big(q(t), \dot q(t), t\big)$.
Then $q$ satisfies the [[Euler–Lagrange equations|PS0VV149ET]]
$$\frac{d}{dt} \frac{\partial L}{\partial \dot q_i} - \frac{\partial L}{\partial q_i} = 0, \qquad i = 1, \ldots, n,$$
if and only if $(q, p)$ satisfies Hamilton's equations
$$\dot q_i = \frac{\partial H}{\partial p_i}(q, p, t), \qquad \dot p_i = -\frac{\partial H}{\partial q_i}(q, p, t), \qquad i = 1, \ldots, n.$$
Moreover $\partial H / \partial t = -\partial L / \partial t$, so along such a solution $\frac{d}{dt} H(q, p, t) = \frac{\partial H}{\partial t}$.

## Remarks

The proof is a computation of partial derivatives of $H = p \cdot v - L(q, v, t)$, where $v(q, p, t)$ is the inverse of $\dot q \mapsto \partial L / \partial \dot q$.
Since $\partial L / \partial \dot q (q, v, t) = p$, the terms with derivatives of $v$ cancel, which gives $\partial H / \partial p = v$, $\partial H / \partial q = -\partial L / \partial q$ and $\partial H / \partial t = -\partial L / \partial t$.
The first equation $\dot q = \partial H / \partial p$ is then the definition of $p$, and the second is the Euler–Lagrange equation $\dot p = \partial L / \partial q$.

Example: for $L = \frac{1}{2} m \dot q^2 - \frac{1}{2} k q^2$, $H = p^2/(2m) + k q^2/2$, and Hamilton's equations $\dot q = p/m$, $\dot p = -k q$ combine to $m \ddot q = -k q$.

Without hyperregularity, $H$ need not be defined: for $L = \frac{1}{2} (\dot q_1 - q_2)^2$ the momentum $p_2$ is identically $0$, and the Legendre transform is not invertible; such systems need the theory of constraints.

## Explanations

### L1 human

Newton's or Lagrange's equations are second order: they give the acceleration.
Hamilton's equations rewrite them as twice as many first-order equations, one for the position and one for the momentum.
Both forms describe exactly the same motions.
In the new form, $\frac{d}{dt} H = \partial H / \partial t$, so energy is conserved when $H$ does not depend on time.

### L2 human

Hamilton's equations say that the velocity in phase space is the [[Hamiltonian vector field|C5EH3B4BEP]] of $H$.
This form is the starting point for [[Liouville's theorem|9T7D9ZRWYY]] on the conservation of phase-space volume, for [[canonical transformations|AGA36YKX4F]], and for the [[Hamilton–Jacobi equation|5TRXQKP7DY]].
A quantity $f(q, p)$ evolves by $\dot f = \{f, H\} + \partial f / \partial t$, with the [[Poisson bracket|2S0MXDT4YH]].
In [[canonical coordinates|XKDVF07R1Q]] the equations keep the same form, which is why changes of variables that preserve this form are so useful.
