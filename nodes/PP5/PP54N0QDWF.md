---
tag: PP54N0QDWF
kind: definition
name: Lagrange multipliers for constraints
msc: [70H03, 70F20, 70H45]
defines: XADAEPN54D
uses: [BCF1EX9W2M, AXA8HN8Y45, BEM454AYTT, 0VKKP8X6Q6, 0NS2QYVC4Y, PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_multiplier
  - url: https://en.wikipedia.org/wiki/Lagrangian_mechanics
---

## Definition

Let $U \subseteq \R^N$ be open, let $q = (q_1, \ldots, q_N)$ be [[coordinates|BCF1EX9W2M]] on $U$, and let $L(q, \dot q, t)$ be a Lagrangian of class $C^2$.
Let $m < N$ and let $f_1, \ldots, f_m \colon U \times \R \to \R$ be [[holonomic constraints|AXA8HN8Y45]] of class $C^2$.
Assume that the [[gradients|0NS2QYVC4Y]] $\nabla_q f_1, \ldots, \nabla_q f_m$ are linearly independent at each point of the constraint set.
*Lagrange's equations with multipliers* (of the first kind) for $q(t)$ and unknown functions $\lambda_1(t), \ldots, \lambda_m(t)$ are
$$\frac{d}{dt} \frac{\partial L}{\partial \dot q_i} - \frac{\partial L}{\partial q_i} = \sum_{a=1}^m \lambda_a(t) \, \frac{\partial f_a}{\partial q_i}(q, t), \qquad i = 1, \ldots, N,$$
$$f_a(q(t), t) = 0, \qquad a = 1, \ldots, m.$$
The functions $\lambda_a$ are the *Lagrange multipliers* of the constraints.

## Remarks

The vector $\sum_a \lambda_a \nabla_q f_a$ is the generalized constraint force; it is normal to the constraint set, so ideal constraints do no virtual work.
The same equations are the [[Euler–Lagrange equations|PS0VV149ET]] of the action of $L + \sum_a \lambda_a f_a$, varied in both $q$ and $\lambda$.
This is the dynamical analogue of the [[Lagrange multiplier theorem|0VKKP8X6Q6]] for constrained extrema.
Eliminating $\lambda$ with coordinates adapted to the constraints gives the [[Lagrange equations|BEM454AYTT]] of the second kind.

Example: a planar pendulum of mass $m$ and length $\ell$ in Cartesian coordinates, with $L = \frac{1}{2} m (\dot x^2 + \dot y^2) - m g y$ and $f = x^2 + y^2 - \ell^2$.
The equations are $m \ddot x = 2 \lambda x$, $m \ddot y + m g = 2 \lambda y$ and $x^2 + y^2 = \ell^2$.
The force $2 \lambda (x, y)$ points along the rod, and its magnitude $2 \abs{\lambda} \ell$ is the tension.

Non-example: the constraints $f_1 = x^2 + y^2 - \ell^2$ and $f_2 = 2 f_1$ describe the same set, but their gradients are dependent.
Then only $\lambda_1 + 2 \lambda_2$ is determined, so the multipliers are not unique.
