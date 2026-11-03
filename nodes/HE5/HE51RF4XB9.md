---
tag: HE51RF4XB9
kind: statement
role: fact
name: Huygens–Fresnel principle
msc: [78A45, 78A10]
uses: [JE101TDP4Q, MNXKTXJ35G]
about: [FSCTVTQQF2]
sources:
  - url: https://en.wikipedia.org/wiki/Huygens%E2%80%93Fresnel_principle
same_as:
  wikidata: Q188321
  wikipedia: Huygens–Fresnel principle
---

## Statement

Let $u$ be the complex amplitude of a monochromatic scalar wave of wavelength $\lambda$ and wavenumber $k = 2\pi/\lambda$ in a homogeneous medium.
Let $S$ be a surface that separates the sources of the wave from a point $P$, for example a wavefront.
For $Q \in S$, let $r = \abs{P - Q}$ and let $\chi$ be the angle between the normal of $S$ at $Q$ and the direction from $Q$ to $P$.
Assume all distances $r$ are large compared with $\lambda$.
Then every point of $S$ acts as a source of a secondary spherical wave, and
$$u(P) = \frac{1}{i \lambda} \int_S u(Q) \, \frac{e^{i k r}}{r} \, K(\chi) \, dS(Q),$$
where the obliquity factor $K$ satisfies $K(0) = 1$.

## Remarks

Huygens proposed that each point of a wavefront emits a wavelet and that the new wavefront is their envelope.
Fresnel added that the wavelets interfere, with their phases $k r$, and this explains diffraction fringes.
The principle in this form is heuristic; [[Kirchhoff's diffraction formula|W178NQAYS9]] derives it from the [[Helmholtz equation|MNXKTXJ35G]] and gives $K(\chi) = (1 + \cos\chi)/2$ when $S$ is a spherical wavefront from a point source.
The factor $1/(i\lambda)$ makes the formula consistent: applied to a plane wave and a plane $S$, it reproduces the plane wave at $P$, by the method of stationary phase.
For the sharp form of Huygens' principle for the wave equation in odd dimensions, see [[Huygens principle|1SH2WZVZ66]].

## Explanations

### L1 human

Every point reached by a wave behaves like a tiny new source that sends out its own round ripple.
The wave further on is the sum of all these ripples, each with its own delay.
Where the ripples arrive in step they add up, and where they arrive out of step they cancel.

### L2 human

In diffraction problems one takes $S$ to be the plane of an aperture and assumes that $u$ on the aperture equals the incident wave.
The integral then becomes the starting point of the Fresnel and Fraunhofer approximations, which simplify the phase $k r$ for distant observation points.
Kirchhoff's integral theorem and the Rayleigh–Sommerfeld formulas are the rigorous versions of the principle.
