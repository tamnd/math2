---
tag: SEC5MWF7PB
kind: definition
name: Poinsot's ellipsoid
msc: ["70E15", "70E17"]
defines: FHCJDYE7YF
uses: [WVGTEH6P10, PN15F4ZS8D, C9YCMAPKMT, 7147M98XNR]
sources:
  - url: https://en.wikipedia.org/wiki/Poinsot%27s_ellipsoid
---

## Definition

Let a rigid body move about its centre of mass with no external torque.
Let $I$ be its [[inertia tensor|WVGTEH6P10]] about the centre of mass in a frame attached to the body, and assume $I$ is positive definite.
Let $\omega(t)$ be the angular velocity in this body frame, and let $T = \tfrac12 \omega^T I \omega$ be the rotational [[kinetic energy|C9YCMAPKMT]], which is constant in time.
Assume $T > 0$.
*Poinsot's ellipsoid* of the motion is the ellipsoid
$$\mathcal{E} = \set{ x \in \R^3 : x^T I x = 2T }$$
in the body frame.

## Remarks

In principal axes the equation is $I_1 x_1^2 + I_2 x_2^2 + I_3 x_3^2 = 2T$, so the semi-axes are $\sqrt{2T/I_i}$.
The angular velocity $\omega(t)$ lies on $\mathcal{E}$ for all $t$, because $T$ is conserved by [[Euler's equations|PN15F4ZS8D]] without torque.
The normal to $\mathcal{E}$ at $\omega$ is parallel to $I\omega = L$, the [[angular momentum|7147M98XNR]], which is constant in space.
The tangent plane at $\omega$ has distance $\omega \cdot L / \abs{L} = 2T/\abs{L}$ from the centre, which is constant too.
So, seen from a frame at rest, $\mathcal{E}$ touches a fixed plane perpendicular to $L$, the *invariable plane*, at the tip of $\omega$.
The point of contact lies on the instantaneous axis of rotation, so its velocity is zero, and the ellipsoid rolls on the plane without slipping.

Example: for a body with $I = \operatorname{diag}(1, 2, 3)$ and $\omega = (1, 0, 0)$, one gets $T = \tfrac12$ and $\mathcal{E} = \set{x_1^2 + 2x_2^2 + 3x_3^2 = 1}$, which contains $\omega$.

Non-example: for a body with $T = 0$, that is, at rest, the set $\set{x^T I x = 0}$ is a single point, not an ellipsoid.

## Explanations

### L1 human

Poinsot's ellipsoid is the set of all angular velocities that give the body the same rotational energy as the actual motion.
The actual angular velocity stays on this surface for ever.
