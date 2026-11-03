---
tag: 924T5SYJGQ
kind: definition
name: Angular acceleration
msc: [70B05, 70B10]
defines: 7M4AZSA2MN
uses: [2FTZ7D8Z0F, 0V1EJCT8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_acceleration
---

## Definition

Let $I \subseteq \R$ be an open interval and let $\omega \colon I \to \R^3$ be the [[angular velocity|2FTZ7D8Z0F]] of a rotating body or frame relative to a fixed frame.
If $\omega$ is differentiable at $t \in I$, the *angular acceleration* at time $t$ is the vector
$$\alpha(t) = \dot\omega(t).$$

## Remarks

Example: rotation about the fixed $z$-axis by the angle $\theta(t)$ has $\omega = (0, 0, \dot\theta)$ and $\alpha = (0, 0, \ddot\theta)$; for $\theta(t) = t^2$ this gives $\alpha = (0, 0, 2)$.
Non-example: uniform rotation with $\theta(t) = \Omega t$ for a constant $\Omega \ne 0$ has nonzero acceleration at each point off the axis, but $\alpha = 0$, so the point accelerations are not the angular acceleration.
For a body turning about a fixed point, a point fixed in the body at position $r(t)$ relative to that fixed point has acceleration $\alpha \times r + \omega \times (\omega \times r)$.
The angular acceleration has the same value whether $\omega$ is differentiated in the fixed frame or in the rotating frame, since $\omega \times \omega = 0$.
