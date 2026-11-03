---
tag: JSYMQ9C0G0
kind: definition
name: Fictitious force
msc: [70A05, 70B05]
defines: ZN2Z2HJY9Z
uses: [Q05G0NZDNB, HNXK6CJ5B2, KNBP19FG6K, 2FTZ7D8Z0F]
sources:
  - url: https://en.wikipedia.org/wiki/Fictitious_force
---

## Definition

Fix an [[inertial frame|Q05G0NZDNB]] with coordinates $x \in \R^3$.
Let $o$ be a twice differentiable curve in $\R^3$ and $R$ a twice differentiable curve in $SO(3)$.
A second frame has coordinates $X$ given by $x = o(t) + R(t) X$.
Let $\Omega(t) = R(t)^T \omega(t)$ be the [[angular velocity|2FTZ7D8Z0F]] of the frame expressed in its own axes.
Consider a particle of mass $m > 0$ with position $X(t)$ in the second frame, acted on by a total force with components $F$ in that frame.
The *fictitious force* on the particle in the second frame is
$$F_{\mathrm{fict}} = -m\, R^T \ddot o - m\, \dot\Omega \times X - 2m\, \Omega \times \dot X - m\, \Omega \times (\Omega \times X).$$
With it, [[Newton's second law|KNBP19FG6K]] in the second frame reads $m \ddot X = F + F_{\mathrm{fict}}$.

## Remarks

The formula comes from differentiating $x = o + R X$ twice: with $\dot R = R\, [\Omega]_\times$ one gets $\ddot x = \ddot o + R\big(\ddot X + 2\,\Omega \times \dot X + \dot\Omega \times X + \Omega \times (\Omega \times X)\big)$, and $m\ddot x$ is the force in the inertial frame.
The four terms are the translational force $-m R^T \ddot o$, the Euler force $-m\,\dot\Omega \times X$, the Coriolis force $-2m\,\Omega \times \dot X$ and the centrifugal force $-m\,\Omega \times (\Omega \times X)$.
Example: in a car moving in a straight line with constant acceleration vector $A$, $R$ is constant and $\ddot o = A$, so a passenger feels $F_{\mathrm{fict}} = -m R^T A$, a push backward.
Non-example: the gravitational force on the passenger is not fictitious, because it is exerted by another body and is present in every frame.
For a frame moving at constant velocity without rotation, $F_{\mathrm{fict}} = 0$, in agreement with Galilean invariance.
