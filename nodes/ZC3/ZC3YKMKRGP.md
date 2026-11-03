---
tag: ZC3YKMKRGP
kind: statement
role: theorem
name: Principle of virtual work
msc: [70C20, 70G75, 70F20]
uses: [AXA8HN8Y45, BCF1EX9W2M, 9WQT2RMGTZ, KHT3FBB7NZ, GD776GVZSR]
about: [KHT3FBB7NZ, 9WQT2RMGTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Virtual_work
---

## Statement

Consider $N$ point particles with positions $x_1, \dots, x_N \in \R^3$, subject to time-independent [[holonomic constraints|AXA8HN8Y45]] described by [[generalized coordinates|BCF1EX9W2M]] $q = (q_1, \dots, q_n)$, so that $x_k = x_k(q)$.
Assume the constraints are ideal: the total force of constraint on the system does no work in any virtual displacement $\delta x_k = \sum_i \frac{\partial x_k}{\partial q_i}\, \delta q_i$.
Let $F_k$ be the applied force on particle $k$, a smooth function of the positions.
Call $q^0$ a position of [[equilibrium|KHT3FBB7NZ]] if the system placed at rest at $q^0$ stays at rest.
Then $q^0$ is a position of equilibrium if and only if the virtual work of the applied forces vanishes there:
$$\sum_{k=1}^N F_k \cdot \delta x_k = 0 \quad \text{for all } \delta q \in \R^n.$$
Equivalently, all [[generalized forces|9WQT2RMGTZ]] vanish at $q^0$: $Q_1 = \dots = Q_n = 0$.

## Remarks

For one direction, at rest every particle has zero acceleration, so the applied force and the constraint force on each particle cancel.
Since the constraint forces do no virtual work, neither do the applied forces.
For the other, write Lagrange's equations; when all $Q_i$ vanish at $q^0$, the constant motion $q(t) = q^0$ solves them.
Uniqueness of solutions for smooth equations then shows that the system stays at rest.
Example: a lever with arms $a, b > 0$ carries downward loads of sizes $F_1, F_2$ at its ends.
Turning it by a small angle $\delta\varphi$ lowers one end by $a\,\delta\varphi$ and raises the other by $b\,\delta\varphi$.
So the virtual work is $(F_1 a - F_2 b)\,\delta\varphi$, and equilibrium means $F_1 a = F_2 b$, the law of the lever.
The hypothesis of ideal constraints is necessary: with dry friction, a block can rest on a slope although gravity does nonzero virtual work along the slope.
If the forces derive from a potential $V(q)$, the principle says that the equilibria are the critical points of $V$.

## Explanations

### L1 human

A mechanism is balanced exactly when no small allowed motion would let the forces do any work.
If some small motion lets the forces gain work, the system will start moving that way.
The principle lets one find equilibria without computing the forces in rods, hinges and strings, because those do no work.

### L2 human

The principle is the static case of [[d'Alembert's principle|GD776GVZSR]], which adds the inertial forces $-m_k \ddot x_k$ to the applied forces and gives Lagrange's equations.
In generalized coordinates it reduces statics to the equations $Q_i(q) = 0$.
For conservative forces it reduces statics to finding critical points of the potential energy, and stability of the equilibrium is then studied through the second derivatives of the potential.
