---
tag: 5WGHAMZTWE
kind: definition
name: Friction
msc: [70F40, 70A05]
defines: 4XE2B2PBGC
uses: [SH7J0X3NCC]
sources:
  - url: https://en.wikipedia.org/wiki/Friction
---

## Definition

Let a particle slide on a fixed surface of class $C^1$ in $\R^3$, in a [[Newtonian system|SH7J0X3NCC]].
Let $N \ge 0$ be the size of the normal force that the surface exerts on the particle.
Let $v$ be the velocity of the particle, which is tangent to the surface.
Let $0 \le \mu_k \le \mu_s$ be constants, the coefficients of kinetic and static friction.
A *Coulomb friction force* is a force $f$ tangent to the surface such that:

1. if $v \ne 0$, then $f = -\mu_k N\, v / \abs{v}$;
2. if $v = 0$, then $\abs{f} \le \mu_s N$.

## Remarks

In case 2 the force is not given by a formula: it takes the value needed to keep the particle at rest, as long as that value satisfies the bound.
Example: a block of mass $m$ at rest on a plane tilted by the angle $\theta$ has $N = m g \cos\theta$ and needs the friction $m g \sin\theta$ along the plane.
It stays at rest exactly when $m g \sin\theta \le \mu_s m g \cos\theta$, that is, $\tan\theta \le \mu_s$.
Non-example: the force $f = -\mu_k N v$ for a sliding particle fails clause 1, since its size grows with the speed; such linear drag is viscous friction, not Coulomb friction.
The model is an empirical law, also called the Amontons–Coulomb law.

## Explanations

### L1 human

Coulomb's model says two things.
A sliding body feels a backward force of fixed size, proportional to how hard it is pressed against the surface.
A body at rest is held by whatever force is needed, up to a limit that is also proportional to the pressing force.
