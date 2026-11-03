---
tag: YV2XRKXHEV
kind: definition
name: Euler free nutation
msc: ["70E15", 86A30]
defines: 9HF39441Y0
uses: [EZ9P9ERKNE, WVGTEH6P10, PN15F4ZS8D, 2FTZ7D8Z0F]
sources:
  - url: https://en.wikipedia.org/wiki/Chandler_wobble
---

## Definition

Let a [[rigid body|EZ9P9ERKNE]] have [[principal moments of inertia|WVGTEH6P10]] $A = B < C$ about body axes $e_1, e_2, e_3$, and let no external torque act on it.
Write its [[angular velocity|2FTZ7D8Z0F]] in the body frame as $\omega = (\omega_1, \omega_2, \omega_3)$.
By [[Euler's equations|PN15F4ZS8D]], $\omega_3$ is constant and
$$\omega_1(t) + i\,\omega_2(t) = m\, e^{i \sigma_E t}, \qquad \sigma_E = \frac{C - A}{A}\,\omega_3,$$
for a complex constant $m$.
If $m \ne 0$, this motion of $\omega$ around $e_3$ in the body frame is the *Euler free nutation*, and $2\pi/\sigma_E$ is the Euler period.

## Remarks

Check: Euler's equations with $A = B$ read $A\dot\omega_1 = -(C - A)\omega_2\omega_3$, $A\dot\omega_2 = (C - A)\omega_3\omega_1$ and $C\dot\omega_3 = 0$, so $\frac{d}{dt}(\omega_1 + i\omega_2) = i\sigma_E(\omega_1 + i\omega_2)$.
Example: for the Earth $(C - A)/A \approx 1/305$, so the Euler period is about $305$ sidereal days.
Non-example: if $m = 0$, the body spins steadily about its symmetry axis and there is no nutation.
The word "nutation" here refers to a motion relative to the body.
Seen from space, the same motion is a small free precession of the symmetry axis around the fixed angular momentum vector.
