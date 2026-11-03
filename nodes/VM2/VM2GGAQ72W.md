---
tag: VM2GGAQ72W
kind: definition
name: Acceleration
msc: [70B05]
defines: Q8D2JWY8G6
uses: [K160D2Z0CS, 0Q4QJWEHW3]
sources:
  - url: https://en.wikipedia.org/wiki/Acceleration
---

## Definition

Let $I \subseteq \R$ be an open interval of times, and let $x \colon I \to \R^3$ give the position of a point particle in a fixed frame of reference.
Assume $x$ is differentiable on $I$, with [[velocity|K160D2Z0CS]] $v = \dot x$, and that $v$ is differentiable at $t \in I$.
The *acceleration* of the particle at time $t$ is the vector
$$a(t) = \dot v(t) = \ddot x(t),$$
the [[second derivative|0Q4QJWEHW3]] of the position.

## Remarks

Example: for uniform circular motion $x(t) = (R\cos(\omega t), R\sin(\omega t), 0)$ with $R > 0$, the acceleration is $a(t) = -\omega^2 x(t)$: it points to the centre and has size $R\omega^2$.
Non-example: the rate of change of the speed, $\frac{d}{dt}\abs{v(t)}$, is not the acceleration; for the circular motion it is $0$, while $a(t) \ne 0$ when $\omega \ne 0$.
When $v(t) \ne 0$, the acceleration splits into a tangential part $\frac{d}{dt}\abs{v}$ along the direction of motion and a normal part of size $\abs{v}^2 \kappa$, where $\kappa$ is the curvature of the path.
Frames of reference that move with constant velocity relative to each other give the same acceleration.
