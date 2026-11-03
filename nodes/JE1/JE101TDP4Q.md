---
tag: JE101TDP4Q
kind: definition
name: Physical optics
msc: [78A10, 78A45]
defines: FSCTVTQQF2
uses: [5EHD2XBQDG, MNXKTXJ35G, 9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Physical_optics
---

## Definition

Let $\Omega \subseteq \R^3$ be a region with [[refractive index|9VGK0SP6EQ]] $n$.
Let $c$ be the speed of light in vacuum.
*Physical optics* (scalar wave optics) describes light in $\Omega$ by a real field $U(x, t)$ that solves the [[wave equation|5EHD2XBQDG]]
$$\frac{n(x)^2}{c^2} \frac{\partial^2 U}{\partial t^2} = \Delta U.$$
A *monochromatic* field of angular frequency $\omega$ has the form $U(x, t) = \operatorname{Re}\left(u(x) e^{-i \omega t}\right)$.
Its complex amplitude $u$ solves the [[Helmholtz equation|MNXKTXJ35G]]
$$\Delta u + k^2 n(x)^2 u = 0, \qquad k = \frac{\omega}{c} = \frac{2\pi}{\lambda},$$
and $\lambda$ is the vacuum wavelength.
The observable *intensity* is $I(x) = \abs{u(x)}^2$, up to a constant factor.

## Remarks

Because the equations are linear, fields add, and intensities do not: for $u = u_1 + u_2$ one gets $I = \abs{u_1}^2 + \abs{u_2}^2 + 2 \operatorname{Re}(u_1 \overline{u_2})$, and the last term produces interference fringes.
Example: two plane waves $e^{i k x \sin\alpha}$ and $e^{-i k x \sin\alpha}$ in vacuum give $I = 4 \cos^2(k x \sin\alpha)$, a pattern of fringes with spacing $\lambda / (2 \sin\alpha)$.
Geometrical optics is the limit $k \to \infty$, where $u \approx A e^{i k L}$ and $L$ solves the eikonal equation.
The scalar model ignores polarisation; the vector theory uses Maxwell's equations for the electric and magnetic fields.

## Explanations

### L1 human

Physical optics represents light by a wave amplitude at each point.
The squared size of the amplitude is the brightness, and the phase of the amplitude decides how waves from different paths combine.
