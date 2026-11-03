---
tag: GFMTB5RE1H
kind: definition
name: Velocity
msc: [70B05]
defines: K160D2Z0CS
uses: [0V1EJCT8G6, 0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Velocity
---

## Definition

Let $I \subseteq \R$ be an open interval of times, and let $x \colon I \to \R^3$ give the position of a point particle in a fixed frame of reference.
If $x$ is differentiable at $t \in I$, the *velocity* of the particle at time $t$ is the vector
$$v(t) = \dot x(t) = \lim_{h \to 0} \frac{x(t + h) - x(t)}{h},$$
the [[derivative|0V1EJCT8G6]] of $x$ at $t$.
The *speed* at time $t$ is the length $\abs{v(t)}$ of this [[vector|0QN3D80AWP]].

## Remarks

Example: for uniform circular motion $x(t) = (R\cos(\omega t), R\sin(\omega t), 0)$ with $R > 0$ and $\omega \in \R$, the velocity is $v(t) = (-R\omega\sin(\omega t), R\omega\cos(\omega t), 0)$ and the speed is $R\abs{\omega}$, constant although the velocity turns.
Non-example: the average velocity $(x(t_2) - x(t_1))/(t_2 - t_1)$ over an interval is not the velocity at an instant.
For the circular motion over one full period it is $0$, while the speed is $R\abs\omega$.
Common notations are $v$, $\dot x$ and $dx/dt$.
Velocity depends on the frame of reference: in a frame moving with constant velocity $u$, the velocity of the particle is $v - u$.
