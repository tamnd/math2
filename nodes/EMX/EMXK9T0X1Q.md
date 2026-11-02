---
tag: EMXK9T0X1Q
kind: definition
name: Hamilton–Jacobi theory of the calculus of variations
msc: [49L99, 70H20, 49K05]
defines: 6JGM1K39FB
uses: [PQ25NHV0KS, PS0VV149ET, 5TRXQKP7DY, K4DFT3H9BJ]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton–Jacobi_equation
---

## Definition

Let $I \subseteq \R$ be an open interval and let $L \colon I \times \R^n \times \R^n \to \R$, $(t, q, v) \mapsto L(t, q, v)$, be of class $C^2$.
Assume that for each $(t, q)$ the map $v \mapsto \partial L / \partial v (t, q, v)$ is a diffeomorphism of $\R^n$ and $\partial^2 L / \partial v^2$ is positive definite.
The variational problem is to find extremals of $\int L(t, q, q') \, dt$, the solutions of the [[Euler–Lagrange equation|PS0VV149ET]].
Its Hamiltonian is $H(t, q, p) = p \cdot v - L(t, q, v)$, where $v$ is the unique vector with $p = \partial L / \partial v(t, q, v)$.
The *Hamilton–Jacobi equation* of the problem is the [[partial differential equation|5TRXQKP7DY]]
$$\frac{\partial S}{\partial t} + H\Big(t, q, \frac{\partial S}{\partial q}\Big) = 0$$
for a function $S$ of class $C^2$ on an open set $G \subseteq I \times \R^n$.
*Hamilton–Jacobi theory* is the study of the variational problem through the solutions $S$ of this equation and the curves $q$ in $G$ with
$$q'(t) = \frac{\partial H}{\partial p}\Big(t, q(t), \frac{\partial S}{\partial q}(t, q(t))\Big).$$

## Remarks

The basic fact is that each such curve is an extremal, with momentum $p(t) = \partial S / \partial q(t, q(t))$ solving Hamilton's canonical equations.
These curves fill $G$ and form a [[field of extremals|K4DFT3H9BJ]], and $S$ is the action along them.
Example: $L = \frac12 \abs{v}^2$, so $H = \frac12 \abs{p}^2$, on $G = \set{(t, q) : t > t_0}$.
The function $S(t, q) = \abs{q - a}^2 / (2(t - t_0))$ solves the equation, since $S_t = -\abs{q - a}^2 / (2 (t - t_0)^2)$ and $\frac12 \abs{\nabla_q S}^2 = \abs{q - a}^2 / (2 (t - t_0)^2)$.
The curves solve $q' = (q - a)/(t - t_0)$, so they are the straight lines through $a$ at time $t_0$, which are the extremals of $L$.
Non-example: for $L = \frac12 \abs{v}^2$ the function $S(t, q) = \abs{q}^2$ does not solve the equation, since $S_t + \frac12 \abs{\nabla S}^2 = 2 \abs{q}^2 \ne 0$ for $q \ne 0$.
Jacobi's theorem completes the theory: from a family $S(t, q, a)$ of solutions with $\det(\partial^2 S / \partial q \, \partial a) \ne 0$, the equations $\partial S / \partial a = b$ define all solutions of Hamilton's equations near a point.
