---
tag: C8JXVEFWRE
kind: definition
name: Dipole model of the Earth's magnetic field
msc: [86A25, 78A25]
defines: 2KPTTBM584
uses: [NDPHH8SR3E, SSAWJ3JF5Y, 0H7C3T1GJY]
sources:
  - url: https://en.wikipedia.org/wiki/Dipole_model_of_the_Earth%27s_magnetic_field
---

## Definition

Let $a$ be the Earth's radius, and let $(r, \theta, \phi)$ be spherical coordinates centred at the Earth's centre.
The *dipole model* of [[Earth's magnetic field|NDPHH8SR3E]] is the field $B = -\nabla V$ with the [[scalar potential|0H7C3T1GJY]]
$$V = \frac{a^3}{r^2} \bigl( g_1^0 \cos\theta + (g_1^1 \cos\phi + h_1^1 \sin\phi) \sin\theta \bigr),$$
for real constants $g_1^0, g_1^1, h_1^1$, not all zero.
This is the field of a [[magnetic dipole|SSAWJ3JF5Y]] at the centre, with moment of magnitude $\abs{m} = 4\pi a^3 B_0 / \mu_0$.
Here $B_0 = \sqrt{(g_1^0)^2 + (g_1^1)^2 + (h_1^1)^2}$, and $\mu_0$ is the magnetic permeability of free space.

## Remarks

In coordinates whose axis is the dipole axis, with geomagnetic colatitude $\theta$ and $g_1^0 = -B_0$ as for the present field, the components are
$$B_r = -2 B_0 \Bigl(\frac{a}{r}\Bigr)^3 \cos\theta, \qquad B_\theta = -B_0 \Bigl(\frac{a}{r}\Bigr)^3 \sin\theta.$$
So the intensity is $F = B_0 (a/r)^3 \sqrt{1 + 3\cos^2\theta}$, twice as large at the poles as at the equator.
The inclination $I$ at the surface satisfies $\tan I = -B_r / \abs{B_\theta} = 2 \cot\theta = 2 \tan\lambda$, where $\lambda = 90^\circ - \theta$ is the magnetic latitude.
Example: at $\lambda = 45^\circ$, $\tan I = 2$, so $I \approx 63.4^\circ$.
Non-example: the full field with all degrees $n \ge 2$ is not a dipole field, and its inclination does not follow $\tan I = 2 \tan\lambda$ exactly.
A field line satisfies $r = L \sin^2\theta$ for a constant $L$, the distance at which it crosses the magnetic equator.
Paleomagnetism inverts the formula $\tan I = 2\tan\lambda$ to find the ancient latitude of a rock from its remanent inclination.

## Explanations

### L1 human

The dipole model keeps only the three largest Gauss coefficients.
It describes a centred, tilted bar magnet, and gives simple rules for how steep and how strong the field is at each magnetic latitude.
