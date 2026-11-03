---
tag: W178NQAYS9
kind: statement
role: theorem
name: Kirchhoff's diffraction formula
msc: [78A45, 35J05]
uses: [MNXKTXJ35G, SH6JY9RN2E, JE101TDP4Q]
about: [FSCTVTQQF2]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchhoff%27s_diffraction_formula
same_as:
  wikidata: Q7408338
  wikipedia: Kirchhoff's diffraction formula
---

## Statement

1. (Kirchhoff's integral theorem.) Let $V \subset \R^3$ be a bounded domain with smooth boundary $S$ and outward unit normal $\nu$, and let $k > 0$.
Let $u \in C^2(\overline V)$ solve the [[Helmholtz equation|MNXKTXJ35G]] $\Delta u + k^2 u = 0$ in $V$.
For $P \in V$ and $Q \in S$, let $s = \abs{Q - P}$.
Then
$$u(P) = \frac{1}{4\pi} \int_S \left( \frac{e^{i k s}}{s} \frac{\partial u}{\partial \nu}(Q) - u(Q) \frac{\partial}{\partial \nu_Q} \frac{e^{i k s}}{s} \right) dS(Q).$$
2. (Fresnel–Kirchhoff diffraction formula.) Let an opaque plane screen have an aperture $A$.
Let a point source at $P_0$ send the wave $a e^{i k r}/r$ onto it, with $r = \abs{Q - P_0}$, and let $P$ lie on the other side.
Assume Kirchhoff's boundary conditions.
On $A$ the field and its normal derivative equal those of the incident wave, and on the dark side of the screen both vanish.
Assume also that $r$ and $s = \abs{Q - P}$ are large compared with the wavelength $\lambda = 2\pi/k$.
Let $\nu$ be the unit normal of the screen that points toward $P$.
Let $\theta_0$ and $\theta$ be the angles that the directions from $P_0$ to $Q$ and from $Q$ to $P$ make with $\nu$.
Then
$$u(P) = \frac{a}{i \lambda} \int_A \frac{e^{i k (r + s)}}{r s} \, \frac{\cos\theta_0 + \cos\theta}{2} \, dA(Q).$$

## Remarks

Part 1 is Green's representation formula with the outgoing [[Green's function|SH6JY9RN2E]] $e^{i k s}/(4\pi s)$ of the Helmholtz operator.
To prove it, apply Green's second identity on $V$ minus a small ball around $P$, and let the radius of the ball tend to $0$.
Part 2 applies part 1 to a large region on the side of $P$.
The boundary conditions keep only the aperture, and terms of relative order $1/(k r)$ and $1/(k s)$ are dropped.
For normal incidence and a point $P$ straight ahead, both cosines are $1$ and the formula becomes the [[Huygens–Fresnel principle|HE51RF4XB9]] with obliquity factor $1$.
Kirchhoff's boundary conditions are mathematically inconsistent: a solution of the Helmholtz equation whose value and normal derivative both vanish on a piece of surface vanishes identically.
The formula is nevertheless very accurate when the aperture is large compared with $\lambda$; the [[Rayleigh–Sommerfeld formulas|3B5D567BEK]] remove the inconsistency.

## Explanations

### L1 human

Kirchhoff's formula computes the light behind a hole in a screen.
It adds up waves coming from every point of the hole, each weighted by a factor that depends on the angles.
This is a precise version of Huygens' idea of secondary wavelets.

### L2 human

Part 1 says that a solution of the Helmholtz equation inside a region is determined by its values and normal derivatives on the boundary.
Part 2 is the workhorse of scalar diffraction theory: the Fresnel and Fraunhofer approximations simplify its phase $k(r + s)$.
It is an approximation based on a guess of the field on the aperture.
So it is reliable only for apertures much larger than the wavelength and for points not too close to the screen.
