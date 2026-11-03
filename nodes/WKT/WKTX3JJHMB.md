---
tag: WKTX3JJHMB
kind: definition
name: Small oscillations about equilibrium
msc: [70J30, 70J25]
defines: WVRPFFPD0Y
uses: [BCF1EX9W2M, KHT3FBB7NZ, 0693Y2METT, 0QQCG3JWJ4, BEM454AYTT]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_mode
---

## Definition

Let $U \subseteq \R^n$ be open.
Let a mechanical system with [[generalized coordinates|BCF1EX9W2M]] $q \in U$ have the Lagrangian
$$L(q, \dot q) = \frac{1}{2} \dot q^{T} A(q) \, \dot q - V(q),$$
where $V \colon U \to \R$ is smooth.
Here $A$ is smooth, and each $A(q)$ is a symmetric [[positive definite|0QQCG3JWJ4]] $n \times n$ matrix.
Let $q_0 \in U$ be an [[equilibrium|KHT3FBB7NZ]], that is, $\nabla V(q_0) = 0$.
Put $M = A(q_0)$ and let $K$ be the [[Hessian matrix|0693Y2METT]] of $V$ at $q_0$.
The *equations of small oscillations* about $q_0$ are the linear equations
$$M \ddot x + K x = 0, \qquad x \in \R^n,$$
for the displacement $x = q - q_0$, and their solutions are the *small oscillations* about $q_0$.

## Remarks

The equations are the [[Lagrange equations|BEM454AYTT]] of the quadratic Lagrangian $\frac{1}{2} \dot x^T M \dot x - \frac{1}{2} x^T K x$.
This is the second-order Taylor approximation of $L - L(q_0, 0)$ at $(q_0, 0)$.
Equivalently, they are the linearization of the Lagrange equations of $L$ at the equilibrium.
If $K$ is positive definite, $q_0$ is a strict minimum of $V$, every small oscillation is bounded, and it is a sum of normal modes.

Example: the pendulum $L = \frac{1}{2} m \ell^2 \dot \theta^2 + m g \ell \cos \theta$ with $V = -m g \ell \cos \theta$ and $q_0 = 0$.
Here $M = m \ell^2$ and $K = m g \ell$, so the equation is $m \ell^2 \ddot x + m g \ell x = 0$, that is $\ddot x + (g/\ell) x = 0$.

Non-example: at the upright position $q_0 = \pi$ the same formula gives $K = -m g \ell < 0$, so the linear equation $\ddot x = (g/\ell) x$ has exponentially growing solutions; they are not oscillations, and the equilibrium is unstable.
