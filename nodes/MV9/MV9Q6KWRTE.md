---
tag: MV9Q6KWRTE
kind: definition
name: Abraham–Lorentz–Dirac equation
msc: [78A35, 83A05, 70H40]
defines: GDMRN1NBGE
uses: [TC04HE7BDQ, WRZJRJS44W, 6XPSV47R56]
sources:
  - url: https://en.wikipedia.org/wiki/Abraham%E2%80%93Lorentz_force
---

## Definition

Use Minkowski space with the metric $\eta = \mathrm{diag}(1, -1, -1, -1)$ and the speed of light $c$, and let $\mu_0 > 0$ be the vacuum permeability.
Let a point [[charge|6XPSV47R56]] $q$ of mass $m > 0$ have worldline $x^\mu(\tau)$ parametrized by proper time $\tau$, with four-velocity $u^\mu = dx^\mu / d\tau$, so that $u_\mu u^\mu = c^2$.
Let $F^\mu_{\mathrm{ext}}$ be an external four-force, for example $q F^{\mu\nu} u_\nu$ for an external [[electromagnetic tensor|WRZJRJS44W]] $F^{\mu\nu}$.
The *Abraham–Lorentz–Dirac equation* is
$$m \frac{du^\mu}{d\tau} = F^\mu_{\mathrm{ext}} + \frac{\mu_0 q^2}{6 \pi c} \left( \frac{d^2 u^\mu}{d\tau^2} + \frac{1}{c^2} \frac{du_\nu}{d\tau} \frac{du^\nu}{d\tau} \, u^\mu \right).$$

## Remarks

The last term on the right is the radiation reaction four-force, and $\frac{\mu_0 q^2}{6 \pi c} = \frac{q^2}{6 \pi \varepsilon_0 c^3}$.
Since $u_\mu u^\mu = c^2$, one has $u_\mu \dot u^\mu = 0$ and $u_\mu \ddot u^\mu = -\dot u_\mu \dot u^\mu$, with dots for $d/d\tau$.
So the radiation reaction force is orthogonal to $u$, as every four-force on a particle of constant mass must be.
In the rest frame at an instant, the space part of the radiation reaction force reduces to the [[Abraham–Lorentz force|TC04HE7BDQ]] $\frac{q^2}{6 \pi \varepsilon_0 c^3} \dot a$.

Example: a charge in uniform motion, $u^\mu$ constant, with $F_{\mathrm{ext}} = 0$, solves the equation, since both sides vanish.

Non-example: the equation $m \dot u^\mu = F^\mu_{\mathrm{ext}} + \frac{\mu_0 q^2}{6 \pi c} \ddot u^\mu$ without the term in $u^\mu$ is not the Abraham–Lorentz–Dirac equation.
Its force has component $\frac{\mu_0 q^2}{6 \pi c} u_\mu \ddot u^\mu = -\frac{\mu_0 q^2}{6 \pi c} \dot u_\mu \dot u^\mu$ along $u$, which is nonzero for accelerated motion, so it would not preserve $u_\mu u^\mu = c^2$.

## Explanations

### L1 human

The equation says: mass times four-acceleration equals the external force plus a self-force from radiation.
The self-force has two parts: the relativistic analog of the Abraham–Lorentz force, and a term that accounts for the four-momentum carried off by the radiation.
The second term is exactly what is needed to keep the particle on the mass shell.
