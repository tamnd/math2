---
tag: WR4RSD9NTK
kind: definition
name: Screw theory
msc: [70B10, 53A17]
defines: NVBD7Y86ES
uses: [0N5N15HWZ7, 0S52TNNTH9, 0H3YY8CPKH]
sources:
  - url: https://en.wikipedia.org/wiki/Screw_theory
---

## Definition

Work in $\R^3$ with the [[dot product|0S52TNNTH9]] $\cdot$ and the [[cross product|0N5N15HWZ7]] $\times$.

1. A *screw* is a pair $S = (\omega, v)$ of vectors of $\R^3$, an element of $\R^6$.
2. A *twist* is a screw read as the velocity field $u(x) = v + \omega \times x$ of a moving rigid body. Here $\omega$ is the angular velocity and $v$ is the velocity of the body point at the origin.
3. A *wrench* is a screw $(f, m)$ read as a system of forces with resultant force $f$ and moment $m$ about the origin.
4. If $\omega \ne 0$, the *pitch* of $(\omega, v)$ is $h = \omega \cdot v / \abs{\omega}^2$, and its *axis* is the line $\set{\omega \times v / \abs{\omega}^2 + t \omega : t \in \R}$.

The *reciprocal product* of a twist $(\omega, v)$ and a wrench $(f, m)$ is $\omega \cdot m + v \cdot f$, the power of the wrench on the motion.
*Screw theory* is the study of screws, twists and wrenches with these operations.

## Remarks

On the axis, the velocity is parallel to $\omega$: for $p = \omega \times v / \abs{\omega}^2$ one finds $\omega \times p = \omega (\omega \cdot v)/\abs{\omega}^2 - v$, so $u(p) = h \omega$.
So the body turns about the axis and slides along it with speed $h \abs{\omega}$, which is the infinitesimal form of Chasles' theorem.
Example: for $\omega = (0, 0, 1)$ and $v = (0, -1, 2)$, the pitch is $h = 2$ and $p = \omega \times v = (1, 0, 0)$.
Check: $u(p) = (0, -1, 2) + (0, 0, 1) \times (1, 0, 0) = (0, -1, 2) + (0, 1, 0) = (0, 0, 2) = 2\omega$; the axis is the vertical line through $(1, 0, 0)$.
If $\omega = 0$, the twist is a pure translation with velocity $v$, a screw of infinite pitch.
Non-example: the field $u(x) = A x$ with $A = \operatorname{diag}(1, 0, 0)$ is not a twist, since $A$ is not skew-symmetric; it stretches the body along the first axis instead of moving it rigidly.
The twists form the Lie algebra of the [[Euclidean group|0H3YY8CPKH]], with bracket $[(\omega_1, v_1), (\omega_2, v_2)] = (\omega_1 \times \omega_2, \omega_1 \times v_2 - \omega_2 \times v_1)$.
