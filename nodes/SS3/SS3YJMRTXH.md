---
tag: SS3YJMRTXH
kind: definition
name: Rigid body dynamics
msc: ["70E15", "70E17"]
defines: NKYMS899KM
uses: [EZ9P9ERKNE, 0HNK6KT05K, 7147M98XNR, 9636MFFSGC, 2FTZ7D8Z0F, KNBP19FG6K, Q05G0NZDNB]
sources:
  - url: https://en.wikipedia.org/wiki/Rigid_body_dynamics
---

## Definition

*Rigid body dynamics* is the part of mechanics that determines the motion of [[rigid bodies|EZ9P9ERKNE]] under given forces and torques, in an [[inertial frame|Q05G0NZDNB]].
For a rigid body made of particles of masses $m_i > 0$ at positions $x_i(t) \in \R^3$, let:

1. $m = \sum_i m_i$ be the total mass and $c(t) = \frac{1}{m}\sum_i m_i x_i(t)$ the [[centre of mass|0HNK6KT05K]];
2. $\omega(t)$ be the [[angular velocity|2FTZ7D8Z0F]], so that $\dot x_i = \dot c + \omega \times (x_i - c)$;
3. $I_c(t) = \sum_i m_i \big( \abs{r_i}^2 \, \mathrm{I}_3 - r_i r_i^T \big)$, with $r_i = x_i - c$ and $\mathrm{I}_3$ the identity matrix, be the inertia tensor about $c$;
4. $L_c = I_c\, \omega$ be the [[angular momentum|7147M98XNR]] about $c$.

Let external forces $F_k$ act at points $p_k$.
The equations of motion are the following *Newton–Euler equations*.
$$m\, \ddot c = \sum_k F_k, \qquad \frac{d L_c}{dt} = \sum_k (p_k - c) \times F_k$$
The second sum is the total [[torque|9636MFFSGC]] about $c$.

## Remarks

Both equations follow from [[Newton's laws|KNBP19FG6K]] for the particles.
One assumes that the internal forces between two particles are equal, opposite and along the line joining them, so their forces and torques cancel in pairs.
Clause 4 agrees with the general definition $L_c = \sum_i m_i\, r_i \times \dot r_i$, by the identity $r \times (\omega \times r) = \abs{r}^2 \omega - (r \cdot \omega) r$.

Example: a body falling freely under gravity $g$ has total force $m g$ and zero torque about $c$, since gravity acts at the centre of mass.
So $c$ follows a parabola and $L_c$ is constant.

Non-example: a system whose particles move apart, such as an exploding shell, is not a rigid body.
The first equation still holds for its centre of mass, but $L_c = I_c \omega$ makes no sense because there is no common angular velocity.
In body-fixed principal axes the second equation becomes Euler's equations of rigid body motion.
