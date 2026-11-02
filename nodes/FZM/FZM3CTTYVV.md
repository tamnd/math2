---
tag: FZM3CTTYVV
kind: example
name: Peridynamics
msc: [74A70, 45K05]
instance_of: [YRKW2KX2CW]
sources:
  - url: https://en.wikipedia.org/wiki/Peridynamics
same_as:
  wikidata: Q4351291
  wikipedia: Peridynamics
---

## Example

Peridynamics is a nonlocal model of continuum mechanics.
Let a body occupy a region $B \subseteq \R^3$ in its reference configuration, with mass density $\rho(x)$.
Let $u(x, t)$ be the displacement of the point $x$ at time $t$.
Fix a horizon $\delta > 0$ and let $H_x = \set{x' \in B : \abs{x' - x} \le \delta}$.
In the bond-based theory the equation of motion is
$$\rho(x) \, \frac{\partial^2 u}{\partial t^2}(x, t) = \int_{H_x} f\big(u(x', t) - u(x, t), \, x' - x\big) \, dx' + b(x, t).$$
Here $b$ is a given body force density.
The pairwise force function $f(\eta, \xi)$ gives the force per unit volume squared that $x'$ exerts on $x$.
Its arguments are the relative position $\xi = x' - x$ and the relative displacement $\eta$.
It satisfies $f(-\eta, -\xi) = -f(\eta, \xi)$, so that action equals reaction.
The equation contains a time derivative of $u$ and a space integral of $u$, but no space derivative: it is an [[integro-differential equation|YRKW2KX2CW]].

Check: in the prototype microelastic brittle model, $f(\eta, \xi) = c \, s \, \frac{\xi + \eta}{\abs{\xi + \eta}}$ for $\abs{\xi} \le \delta$, where $s = \frac{\abs{\xi + \eta} - \abs{\xi}}{\abs{\xi}}$ is the bond stretch and $c > 0$ is a constant.
A rigid translation $u(x, t) = a$ gives $\eta = 0$ and $s = 0$, so the integral vanishes, and with $b = 0$ the equation reduces to $\ddot u = 0$, which a constant $u$ satisfies.

## Remarks

Since no spatial derivatives of $u$ appear, the equation makes sense for displacements with jumps, so cracks can form and grow without a separate rule for fracture.
In the model above a bond breaks for good once its stretch exceeds a critical value.
When $\delta \to 0$, for smooth displacements and suitable force functions, the model approaches classical linear elasticity.

## Explanations

### L1 human

In classical elasticity a point of a solid feels only its immediate neighbours, through derivatives of the displacement.
In peridynamics each point is linked by springs, called bonds, to all points within a fixed distance.
The force on a point is then an integral over all its bonds, and cracks are simply regions where bonds have broken.
