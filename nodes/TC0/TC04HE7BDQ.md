---
tag: TC04HE7BDQ
kind: statement
role: fact
name: Abraham–Lorentz force
msc: [78A35, 78A40]
uses: [EHYKJXF899, 6XPSV47R56, S3RZRCH0T5]
about: [6XPSV47R56]
sources:
  - url: https://en.wikipedia.org/wiki/Abraham%E2%80%93Lorentz_force
same_as:
  wikidata: Q253011
  wikipedia: Abraham–Lorentz force
---

## Statement

Let $\varepsilon_0 > 0$ be the vacuum permittivity and $c$ the speed of light.
In non-relativistic classical electrodynamics, let a point [[charge|6XPSV47R56]] $q$ of mass $m$ move with speed much smaller than $c$ and acceleration $a(t)$.
Besides the external force $F_{\mathrm{ext}}$, it feels the radiation reaction force
$$F_{\mathrm{rad}} = \frac{q^2}{6 \pi \varepsilon_0 c^3} \, \dot a.$$
Its equation of motion is the Abraham–Lorentz equation
$$m a = F_{\mathrm{ext}} + m \tau \dot a, \qquad \tau = \frac{q^2}{6 \pi \varepsilon_0 m c^3}.$$

## Remarks

The force is fixed by energy balance with the [[Larmor formula|EHYKJXF899]].
If the motion is periodic, or the acceleration vanishes at the start and at the end, an integration by parts gives $\int F_{\mathrm{rad}} \cdot v \, dt = -\frac{q^2}{6 \pi \varepsilon_0 c^3} \int \abs{a}^2 \, dt$.
So the work done by $F_{\mathrm{rad}}$ is minus the energy radiated according to the Larmor formula.

The equation is of third order in the position and has unphysical solutions.
With $F_{\mathrm{ext}} = 0$ it has the runaway solutions $a(t) = a(0) e^{t/\tau}$, whose acceleration grows without bound.
Excluding them by a condition at $t \to \infty$ leads to pre-acceleration: the charge starts to accelerate a time of order $\tau$ before the external force acts.
For an electron, $\tau$ is about $6 \times 10^{-24}$ seconds, so these effects lie far below the scales where classical electrodynamics applies.

## Explanations

### L1 human

An accelerated charge radiates and so loses energy.
That energy has to come from somewhere, so the charge must feel a braking force from its own field.
The Abraham–Lorentz force is this self-force, and it is proportional to the rate of change of the acceleration.

### L2 human

The Abraham–Lorentz equation is a standard example of the difficulties of point particles in classical field theory.
In practice one uses it in reduced form, replacing $\dot a$ by the derivative of $F_{\mathrm{ext}} / m$, which removes runaways and is accurate when the radiation force is small.
Its relativistic generalization is the Abraham–Lorentz–Dirac equation.
