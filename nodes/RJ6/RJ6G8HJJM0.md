---
tag: RJ6G8HJJM0
kind: definition
name: Instant centre of rotation
msc: [70B10, 53A17]
defines: WQT8X3V2JQ
uses: [2FTZ7D8Z0F, K160D2Z0CS]
sources:
  - url: https://en.wikipedia.org/wiki/Instant_centre_of_rotation
---

## Definition

Let $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ be the rotation of $\R^2$ by $\pi/2$.
Let a rigid body move in the plane by $x(t) = R(t) X + b(t)$, where $X \in \R^2$ labels a point of the body.
Here $R(t) \in SO(2)$ and $b(t) \in \R^2$ are differentiable in time $t$.
At time $t$ the [[velocity|K160D2Z0CS]] of the body point located at $x \in \R^2$ is
$$v(x) = \omega\, J\, (x - b(t)) + \dot b(t),$$
where $\omega$ is the [[angular velocity|2FTZ7D8Z0F]], defined by $\dot R(t) R(t)^{-1} = \omega J$.
If $\omega \ne 0$, the *instant centre of rotation* at time $t$ is the unique point $P \in \R^2$ with $v(P) = 0$.

## Remarks

Solving $v(P) = 0$ gives $P = b(t) + \omega^{-1} J \dot b(t)$, using $J^2 = -I$.
Then $v(x) = \omega J (x - P)$ for every $x$: each point moves perpendicular to the segment joining it to $P$, with speed $\abs{\omega}\, \abs{x - P}$.

Example: a wheel of radius $1$ rolling to the right along the line $x_2 = 0$ at unit speed has hub $b(t) = (t, 1)$ and $\omega = -1$.
Then $P = (t, 1) - J (1, 0) = (t, 1) - (0, 1) = (t, 0)$, the contact point with the ground.

Non-example: if $R(t)$ is constant, so $\omega = 0$, and $\dot b \ne 0$, then $v(x) = \dot b$ for all $x$ and no point is at rest; the definition does not apply.
The instant centre is also called the instantaneous centre of rotation or the pole of the motion.
