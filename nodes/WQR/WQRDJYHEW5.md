---
tag: WQRDJYHEW5
kind: definition
name: Parker spiral
msc: [85A30, 76W05]
defines: HK345QKE6Y
uses: [3C3BXAPJQA, GMWEA8Q83B]
sources:
  - url: https://en.wikipedia.org/wiki/Heliospheric_current_sheet
---

## Definition

Let a star rotate with constant angular velocity $\Omega > 0$ about the $z$-axis, and use spherical coordinates $(r, \theta, \phi)$ in an inertial frame centred on the star.
Assume that beyond a sphere of radius $r_0$ the plasma moves radially with a constant speed $v > 0$, as in the [[Parker solar wind model|GMWEA8Q83B]].
Assume that the magnetic field is [[frozen into the plasma|3C3BXAPJQA]].
Let a field line be anchored at the point of the sphere $r = r_0$ with colatitude $\theta_0$ that has longitude $\phi_0 + \Omega t$ at time $t$.
The *Parker spiral* through this footpoint at time $t$ is the curve
$$\theta = \theta_0, \qquad \phi = \phi_0 + \Omega t - \frac{\Omega}{v} (r - r_0), \qquad r \ge r_0.$$

## Remarks

The plasma that sits at radius $r$ at time $t$ left the footpoint at time $t' = t - (r - r_0)/v$, when the footpoint had longitude $\phi_0 + \Omega t'$; this gives the formula.
At fixed $t$, $r$ is an affine function of $\phi$, so the curve is an Archimedean spiral, and its turns are spaced by $2\pi v/\Omega$ in $r$.
The field components are $B_r = B_0 (r_0/r)^2$ and $B_\phi = -B_r \, \Omega (r - r_0) \sin\theta / v$, so the angle $\psi$ between the field and the radial direction satisfies $\tan\psi = \Omega (r - r_0) \sin\theta / v$.

Example: for the Sun, $\Omega \approx 2.7 \times 10^{-6}$ per second, and at the Earth $r \approx 1.5 \times 10^{8}$ kilometres with $v \approx 400$ kilometres per second.
Then $\Omega r / v \approx 1$, so $\psi \approx 45$ degrees in the equatorial plane.

Non-example: a logarithmic spiral $r = r_0 e^{b\phi}$ is not a Parker spiral, because the distance between its successive turns grows with $r$ instead of staying equal to $2\pi v/\Omega$.
