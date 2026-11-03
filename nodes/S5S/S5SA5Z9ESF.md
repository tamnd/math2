---
tag: S5SA5Z9ESF
kind: statement
role: theorem
name: Tolman surface brightness test
msc: [85A40, 83F05]
uses: [ECJMS4VDTF, 8K69WPX4GS]
about: [8K69WPX4GS]
sources:
  - url: https://en.wikipedia.org/wiki/Tolman_surface_brightness_test
same_as:
  wikidata: Q7814443
  wikipedia: Tolman surface brightness test
---

## Statement

Assume that spacetime has a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]].
Assume that light travels along null geodesics and that the number of photons is conserved.
Let a source at [[cosmological redshift|8K69WPX4GS]] $z$ have bolometric surface brightness $B_0$ in its rest frame.
This is the total emitted power per unit area per unit solid angle.
Then the bolometric surface brightness $B$ measured by a comoving observer is
$$B = \frac{B_0}{(1 + z)^4} ,$$
whatever the curvature and the matter content of the model.

## Remarks

Proof idea: the luminosity distance $d_L$ and the angular diameter distance $d_A$ satisfy Etherington's reciprocity relation $d_L = (1+z)^2 d_A$.
The received flux is $L/(4\pi d_L^2)$ and the solid angle of a patch of area $A$ is $A/d_A^2$, so the surface brightness scales as $(d_A/d_L)^2 = (1+z)^{-4}$.
One factor of $1+z$ comes from the energy loss of each photon.
One factor comes from the lower arrival rate of photons.
Two factors come from the apparent enlargement of the source.

Example: a galaxy at $z = 1$ appears $2^4 = 16$ times dimmer per unit solid angle than an identical galaxy nearby, which is $3$ magnitudes per square arcsecond.

In a static universe where redshift comes from a "tired light" mechanism, only the energy loss acts and the dimming is $(1+z)^{-1}$.
Richard Tolman proposed comparing the two exponents as a test of the expansion.
In practice the test is difficult because galaxies were intrinsically brighter in the past, so the evolution of their luminosity must be modelled.

## Explanations

### L1 human

In an expanding universe, distant galaxies look much fainter per patch of sky than nearby ones, by the factor $(1+z)^4$.
In a non-expanding universe the surface brightness would hardly change with distance.
So measuring how the surface brightness of similar galaxies falls with redshift tests whether the universe really expands.

### L2 human

The result is purely kinematic: it uses only the metric and photon conservation, not the Friedmann equations.
It is equivalent to the reciprocity relation $d_L = (1+z)^2 d_A$, so a measured violation would point to photon loss or to physics beyond a metric theory.
For a surface brightness per unit frequency, the exponent depends on the spectral shape of the source.
Observers correct for this shift of the band by the K-correction.
