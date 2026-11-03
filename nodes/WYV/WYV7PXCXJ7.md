---
tag: WYV7PXCXJ7
kind: example
name: Oppenheimer–Snyder model of collapse
msc: [83C57, 83C15, 83C75]
illustrates: [YHJ0PDNY8T, 26AVAT8306]
uses: [VEFN58C4D0, ECJMS4VDTF, 6Y50T68WKY]
sources:
  - url: https://en.wikipedia.org/wiki/Oppenheimer–Snyder_model
same_as:
  wikidata: Q121493524
  wikipedia: Oppenheimer–Snyder model
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Fix $a_m > 0$ and an angle $\chi_0 \in (0, \pi/2)$.
Inside, take the closed dust [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]]
$$g = -d\tau^2 + a(\tau)^2\left(d\chi^2 + \sin^2\chi\, d\Omega^2\right), \qquad 0 \le \chi \le \chi_0,$$
where the scale factor is the cycloid given in terms of a parameter $\eta \in [0, \pi]$ by
$$a = \frac{a_m}{2}(1 + \cos\eta), \qquad \tau = \frac{a_m}{2}(\eta + \sin\eta).$$
Outside the ball, take the [[Schwarzschild metric|6Y50T68WKY]] of mass
$$M = \frac{a_m}{2}\sin^3\chi_0.$$
The surface of the ball is $\chi = \chi_0$, with areal radius $R(\tau) = a(\tau)\sin\chi_0$.
Along it the induced metrics and the extrinsic curvatures of the two sides agree, so the glued metric solves the Einstein equations across the surface.
This is the *Oppenheimer–Snyder model*: a uniform ball of pressureless dust, at rest at $\tau = 0$, collapsing under its own gravity.

Check of the mass: for closed dust, $\rho a^3$ is constant and the Friedmann equation $\dot a^2 = \frac{8\pi}{3}\rho a^2 - 1$ with $\dot a = 0$ at $a = a_m$ gives $\frac{4\pi}{3}\rho a^3 = \frac{a_m}{2}$.
The mass inside areal radius $R = a\sin\chi_0$ is $\frac{4\pi}{3}\rho R^3 = \frac{a_m}{2}\sin^3\chi_0 = M$.
The model is the special case of the [[Lemaître–Tolman metric|VEFN58C4D0]] with uniform density inside and no dust outside.

The surface reaches $R = 0$ at $\eta = \pi$, after the finite proper time $\tau = \pi a_m / 2$.
It crosses $R = 2M$ before that, and from then on the surface of the ball is a [[trapped surface|26AVAT8306]].
A [[black hole|YHJ0PDNY8T]] forms, and the collapse ends in a curvature singularity.
Distant observers never see the surface cross $r = 2M$: its light reaches them more and more redshifted.

## Explanations

### L1 human

Oppenheimer and Snyder published this model in 1939.
It describes a perfectly round, uniform cloud of dust with no pressure that falls in on itself.
Inside, the cloud behaves like a small closed universe running backwards towards a big crunch; outside, spacetime is the Schwarzschild solution.
The model was the first exact demonstration in general relativity that gravitational collapse can produce what is now called a black hole.
