---
tag: GCPWX48XRD
kind: example
name: Singular isothermal sphere
msc: [85A05, 85A15]
illustrates: [XSVHFDJHRJ, V4FYBDSGMT]
uses: [XSVHFDJHRJ, V4FYBDSGMT, 3XQ8W7ZKMB]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_isothermal_sphere_profile
same_as:
  wikidata: Q7524245
  wikipedia: Singular isothermal sphere profile
---

## Example

Let $\sigma > 0$ be a velocity dispersion and $G$ the gravitational constant.
The *singular isothermal sphere* is the spherical mass distribution with density
$$\rho(r) = \frac{\sigma^2}{2 \pi G r^2},$$
whose mass inside radius $r$ is $M(r) = \int_0^r 4\pi s^2 \rho(s) \, ds = 2 \sigma^2 r / G$.

Check of the spherical isotropic [[Jeans equation|XSVHFDJHRJ]] $\frac{d(\rho \sigma^2)}{dr} = -\rho \frac{G M(r)}{r^2}$ with constant $\sigma$: the left side is $\sigma^2 \rho'(r) = -2 \sigma^2 \rho / r$, and the right side is $-\rho \cdot 2 \sigma^2 r / r^2 = -2 \sigma^2 \rho / r$.
So stars with the same isotropic dispersion $\sigma$ everywhere are in equilibrium in this mass distribution.

The circular speed is $v_c(r) = \sqrt{G M(r)/r} = \sqrt{2} \, \sigma$, independent of $r$, so the model has a flat [[rotation curve|V4FYBDSGMT]].

## Remarks

The potential is $\Phi(r) = 2 \sigma^2 \ln(r/r_0)$ for any reference radius $r_0$.
By [[Jeans's theorem|3XQ8W7ZKMB]], the distribution function $f(E) \propto e^{-E/\sigma^2}$, with $E = \frac{1}{2} v^2 + \Phi$, gives a Maxwellian velocity distribution of dispersion $\sigma$ at every point and density $\propto r^{-2}$.
The density diverges at the centre and the total mass is infinite, so the model describes the middle range of radii of real systems.
It is a standard simple model for the dark halos of galaxies and for gravitational lenses.

## Explanations

### L1 human

The singular isothermal sphere is a ball of stars, or of dark matter, whose density falls like one over the square of the distance.
Its stars all have the same spread of speeds, like the molecules of a gas at one temperature, which is where the name comes from.
Remarkably, an orbiting body would have the same speed at every distance, which is what is observed in the outer parts of many spiral galaxies.
