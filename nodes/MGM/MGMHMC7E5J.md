---
tag: MGMHMC7E5J
kind: statement
role: proposition
name: Dynamical friction
msc: [85A05, 70F10]
uses: [29WRN5J730, 3QSVWQJX11, 7Y56QCZSZJ, 4V8BT1ZD00]
about: [4V8BT1ZD00]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_friction
---

## Statement

Let a body of mass $M$ move with velocity $v_M$ through an infinite, homogeneous background of stars of mass $m \ll M$.
The bodies interact by [[Newtonian gravity|29WRN5J730]] with gravitational constant $G$.
Let the background have an isotropic velocity distribution $f(v)$, normalized so that $4\pi \int_0^\infty f(v) v^2 \, dv = n$ is the number density, and let $\rho = n m$ be its mass density.
Treat the encounters as independent two-body encounters with impact parameters up to a maximum $b_{\max}$, and let $\ln \Lambda$ be the Coulomb logarithm, with $\Lambda \approx b_{\max} v_M^2 / (G M)$.
Then, up to terms smaller by a factor $1/\ln \Lambda$, the body decelerates according to *Chandrasekhar's dynamical friction formula*
$$\frac{d v_M}{dt} = -16 \pi^2 G^2 M m \ln \Lambda \left( \int_0^{\abs{v_M}} f(v) v^2 \, dv \right) \frac{v_M}{\abs{v_M}^3}.$$
For a [[Maxwellian|3QSVWQJX11]] background with one-dimensional dispersion $\sigma$, and $X = \abs{v_M}/(\sqrt{2} \sigma)$, this becomes
$$\frac{d v_M}{dt} = -\frac{4 \pi G^2 M \rho \ln \Lambda}{\abs{v_M}^3} \left( \operatorname{erf}(X) - \frac{2X}{\sqrt{\pi}} e^{-X^2} \right) v_M,$$
where $\operatorname{erf}$ is the [[error function|7Y56QCZSZJ]].

## Remarks

Each encounter deflects a background star and slightly changes the velocity of $M$; averaging over impact parameters and over the background velocities gives a mean change opposite to $v_M$.
Only stars slower than $M$ contribute to the leading term, as for the gravitational field of a uniform spherical shell, which pulls only on points outside it.
In another picture, $M$ focuses the background stars into a denser wake behind it, and the wake pulls $M$ back.

The drag is proportional to $M$, not to $m$, so heavy bodies sink fastest.
For a slow body, $X \ll 1$, the drag is linear in $v_M$; for a fast body, $X \gg 1$, it falls like $\abs{v_M}^{-2}$.
This sets the time in which globular clusters and satellite galaxies spiral into the centre of their host galaxy.
It also sets the time in which massive black holes sink to the centre of a merged galaxy.

## Explanations

### L1 human

A heavy object moving through a crowd of stars pulls the stars toward itself.
By the time they have gathered, the object has moved on, so the crowd is denser behind it than in front.
This extra crowd behind it pulls it backward, so it slows down even though it never touches a star.
Heavier objects create bigger wakes and are slowed down more.

### L2 human

The formula comes from the theory of two-body encounters that also gives the relaxation time in [[stellar dynamics|4V8BT1ZD00]].
It assumes an infinite uniform medium.
In a real galaxy $b_{\max}$ is of the order of the size of the orbit, and the result is accurate only up to the uncertainty in $\ln \Lambda$.
Apply it to a body on a circular orbit in a singular isothermal sphere.
It gives an inspiral time proportional to the square of the initial radius and inversely proportional to $M$.
