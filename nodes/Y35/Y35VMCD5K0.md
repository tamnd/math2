---
tag: Y35VMCD5K0
kind: statement
role: theorem
name: Normal gravity and Somigliana's formula
msc: [86A30, 86A20]
uses: [R9XX7TNJCH, 5Y2BWNY6MF, 6QBV95NG6E, 0HVX863SAJ]
about: [R9XX7TNJCH, 5Y2BWNY6MF]
sources:
  - url: https://en.wikipedia.org/wiki/Theoretical_gravity
    locator: Somigliana equation
---

## Statement

Let $\mathcal{E}$ be an ellipsoid of revolution with semi-axes $a > b > 0$, rotating with constant angular velocity $\omega$ about its minor axis.
Let $U$ be a normal potential for $\mathcal{E}$.
This is the sum of a gravitational potential of masses inside $\mathcal{E}$ and the centrifugal potential $\tfrac12\omega^2(x^2 + y^2)$, and it is constant on $\mathcal{E}$.
The *normal gravity* is $\gamma = \norm{\nabla U}$ on $\mathcal{E}$.
Let $\gamma_a$ and $\gamma_b$ be its values at the equator and at the poles.
Then at each point of $\mathcal{E}$ with [[geodetic latitude|6QBV95NG6E]] $\varphi$,
$$\gamma(\varphi) = \frac{a\gamma_a \cos^2\varphi + b\gamma_b \sin^2\varphi}{\sqrt{a^2\cos^2\varphi + b^2\sin^2\varphi}}.$$

## Remarks

The formula is due to Somigliana (1929).
Outside $\mathcal{E}$ the gravitational part of $U$ is harmonic and is fixed by its boundary values on $\mathcal{E}$.
So it has a closed form in ellipsoidal coordinates.
Differentiating along the ellipsoid normal and simplifying gives the formula.
An equivalent form is $\gamma(\varphi) = \gamma_a (1 + k\sin^2\varphi)/\sqrt{1 - e^2\sin^2\varphi}$, with $k = b\gamma_b/(a\gamma_a) - 1$ and $e^2 = 1 - b^2/a^2$, where $e$ is the [[eccentricity|0HVX863SAJ]].
For the GRS 80 ellipsoid, $\gamma_a = 9.7803267715$ m/s$^2$ and $\gamma_b = 9.8321863685$ m/s$^2$.
At $\varphi = 0$ the formula gives $a\gamma_a/a = \gamma_a$, and at $\varphi = \pm\pi/2$ it gives $\gamma_b$, as it must.

## Explanations

### L1 human

Gravity at sea level is about $0.5\%$ stronger at the poles than at the equator.
Somigliana's formula gives the exact value at each latitude for an idealised Earth: a spinning ellipsoid whose surface is level.
It only needs the two axes of the ellipsoid and the gravity values at the equator and at the poles.
Geodesists subtract this normal gravity from measured gravity to see the effect of the real, uneven Earth.

### L2 human

The level ellipsoid of a geodetic reference system, such as GRS 80, is determined by four constants: $a$, $f$, $GM$ and $\omega$.
Its exterior potential is unique, and Somigliana's formula is the closed form of its gravity on the surface.
Expanding it in powers of the flattening recovers, to first order, [[Clairaut's theorem|J3EFPYR841]].
The difference between observed gravity and normal gravity is the gravity anomaly, the main data of [[physical geodesy|PK0J9TCYYF]].
