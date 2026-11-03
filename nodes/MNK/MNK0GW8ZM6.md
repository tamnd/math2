---
tag: MNK0GW8ZM6
kind: statement
role: theorem
name: Stokes' formula of physical geodesy
msc: [86A30, 31B20]
uses: [J6V1B7SP0Q, 999BYZY0ZG, 8GF20Z4KDC, 3F32Y21HP4, QFYGJVA996, 0DEB0JMN0W]
about: [999BYZY0ZG, J6V1B7SP0Q]
sources:
  - url: https://en.wikipedia.org/wiki/Physical_geodesy
---

## Statement

Work in the spherical approximation: the [[geoid|999BYZY0ZG]] is replaced by a sphere $\sigma$ of radius $R$, and normal gravity by a constant $\gamma$.
Let $T$ be the disturbing potential, assumed [[harmonic|0DEB0JMN0W]] outside the sphere, which means that no masses lie outside the geoid.
Assume the reference ellipsoid has the same mass as the Earth and the same potential on its surface as the geoid.
Assume also that its centre is the centre of mass of the Earth.
Let $\Delta g$ be the [[gravity anomaly|J6V1B7SP0Q]], given at every point of $\sigma$.
Let $N(P)$ be the geoid height at a point $P$ of $\sigma$.
Then
$$N(P) = \frac{R}{4\pi\gamma} \int_\sigma \Delta g\, S(\psi)\, d\sigma.$$
Here $\psi$ is the angle at the centre between $P$ and the point of integration, and $d\sigma$ is the area element of the unit sphere.
The Stokes function $S$ is
$$S(\psi) = \frac{1}{\sin(\psi/2)} - 6\sin\frac{\psi}{2} + 1 - 5\cos\psi - 3\cos\psi\,\ln\!\left(\sin\frac{\psi}{2} + \sin^2\frac{\psi}{2}\right).$$

## Remarks

Expand $T$ in [[spherical harmonics|3F32Y21HP4]] as $T = \sum_n (R/r)^{n+1} T_n$, with $T_n$ of degree $n$ on $\sigma$.
The boundary condition $\partial T/\partial r + 2T/R = -\Delta g$ on $\sigma$ gives $\Delta g_n = (n-1) T_n / R$ for each degree $n$.
The hypotheses on mass and potential kill the degree $0$ term, and the hypothesis on the centre kills the degree $1$ term, so $T_n = R\,\Delta g_n/(n-1)$ for $n \ge 2$.
[[Bruns formula|8GF20Z4KDC]] gives $N = T/\gamma$, and the addition theorem turns the sum into the kernel $S(\psi) = \sum_{n \ge 2} \frac{2n+1}{n-1} P_n(\cos\psi)$, with $P_n$ the [[Legendre polynomials|QFYGJVA996]].
Without the hypothesis on mass and potential, a constant $N_0$ must be added to the formula.
The kernel is singular like $1/\sin(\psi/2)$ near $\psi = 0$, but this singularity is integrable, so nearby data matter most while distant data still contribute.
In practice the free-air anomaly is used for $\Delta g$, and global coverage of the data is needed.

## Explanations

### L1 human

Stokes' formula computes the shape of the geoid from gravity measurements all over the Earth.
Where gravity is stronger than the model predicts, the geoid bulges up a little, and the formula adds up these influences with a weight that falls off with distance.
It was published by George Gabriel Stokes in 1849, long before satellites could measure the geoid directly.

### L2 human

The formula is the solution of the spherical Stokes problem, a Robin-type exterior [[geodetic boundary value problem|1F4S3G1R6J]] for the harmonic function $T$.
It is an integral operator whose symbol on degree $n$ spherical harmonics is $R/((n-1)\gamma)$.
Its companion, the Vening Meinesz formula, gives the deflection of the vertical from the same data.
The free boundary version, where the Earth's surface replaces the geoid, is [[Molodensky's problem|PHW0E57MH3]].
