---
tag: D72KEW2MFT
kind: definition
name: Rotating reference frame
msc: [70B05, 70A05]
defines: HNXK6CJ5B2
uses: [Q05G0NZDNB, 2FTZ7D8Z0F, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/Rotating_reference_frame
---

## Definition

Fix an [[inertial frame|Q05G0NZDNB]] with position coordinates $x \in \R^3$ and time $t$ in an interval $I$.
A *rotating reference frame* with the same origin is given by a differentiable curve $R \colon I \to SO(3)$.
Here $SO(3)$ is the [[special orthogonal group|0CGYNDCWRR]], and the coordinates $X \in \R^3$ of the frame satisfy
$$x = R(t)\, X.$$
The frame is genuinely rotating when its [[angular velocity|2FTZ7D8Z0F]] $\omega(t)$, defined by $\dot R R^T y = \omega \times y$, is not identically zero.
It rotates uniformly when $\omega$ is constant and nonzero.

## Remarks

Example: a frame turning with constant angular speed $\Omega \ne 0$ about the $z$-axis has $R(t)$ equal to the rotation by the angle $\Omega t$ about that axis, and $\omega = (0, 0, \Omega)$.
Non-example: a frame with $R(t) = R_0$ constant is not rotating, since $\omega = 0$; it is an inertial frame with tilted axes.
Differentiating $x = R X$ gives $\dot x = R \dot X + \omega \times x$: the inertial velocity is the velocity seen in the rotating frame, turned back to the inertial axes, plus the velocity $\omega \times x$ due to the rotation.
A frame whose origin also moves along a curve $o(t)$ is given by $x = o(t) + R(t) X$.
