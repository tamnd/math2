---
tag: F46ASFTAVG
kind: definition
name: Born rigidity
msc: [83A05, 74A05]
defines: J7FVATX80A
uses: [G49G4R1K04, Z788G6MJ9E, Y59V040THG, TWXJH5ZEHA]
sources:
  - url: https://en.wikipedia.org/wiki/Born_rigidity
---

## Definition

Let $M$ be [[Minkowski space|G49G4R1K04]] with inertial coordinates $(x^0, x^1, x^2, x^3)$ and metric $\eta_{\mu\nu} = \operatorname{diag}(-1, 1, 1, 1)$, and let $D \subseteq M$ be an open set.
A *motion* of a body in $D$ is a smooth vector field $u$ on $D$ with $\eta_{\mu\nu} u^\mu u^\nu = -c^2$.
Its integral curves are timelike [[world lines|Z788G6MJ9E]] parametrised by proper time, and $u$ is their [[four-velocity|Y59V040THG]] field.
Let $u_\mu = \sum_\nu \eta_{\mu\nu} u^\nu$ and let
$$h_{\mu\nu} = \eta_{\mu\nu} + \frac{u_\mu u_\nu}{c^2}$$
be the projection onto the rest space orthogonal to $u$.
The motion is *Born rigid* if
$$\sum_{\alpha, \beta} h_\mu{}^\alpha h_\nu{}^\beta \left( \partial_\alpha u_\beta + \partial_\beta u_\alpha \right) = 0 \quad \text{on } D \text{ for all } \mu, \nu,$$
where $h_\mu{}^\alpha = \sum_\beta h_{\mu\beta} \eta^{\beta\alpha}$.

## Remarks

The condition says that the distance between infinitesimally close world lines, measured orthogonally to $u$, does not change along the motion.
Equivalently, the expansion and the shear of $u$ vanish, or the Lie derivative of $h$ along $u$ vanishes.
Example: uniform motion $u = \gamma (c, v, 0, 0)$ with constant $v$ is Born rigid, since $\partial_\alpha u_\beta = 0$.
Example: the world lines of fixed $\rho$ in [[Rindler coordinates|TWXJH5ZEHA]] form a Born rigid motion.
Each is a hyperbolic motion with proper acceleration $c^2/\rho$.
The metric $-\rho^2 d\eta^2 + d\rho^2 + dy^2 + dz^2$ does not depend on $\eta$, so the rest-space distances between these observers are constant.
Non-example: a family of world lines that all have the same constant proper acceleration $\alpha$ along $x$, starting at rest at different points $x_0$, is not Born rigid.
Their coordinate distance stays constant in the original frame, so the distance measured in their rest frames is $\gamma$ times it, which grows with the speed.
The Rindler example shows that in a Born rigid accelerated rod the rear end must accelerate harder than the front.
