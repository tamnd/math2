---
tag: HWA3DABX59
kind: statement
role: proposition
name: Babinet's principle
msc: [78A45, 78A10]
uses: [W178NQAYS9]
about: [W178NQAYS9]
sources:
  - url: https://en.wikipedia.org/wiki/Babinet%27s_principle
same_as:
  wikidata: Q369535
  wikipedia: Babinet's principle
---

## Statement

Let a monochromatic scalar wave fall on a plane screen, and compute the diffracted field behind it with [[Kirchhoff's diffraction formula|W178NQAYS9]].
Let $S_1$ and $S_2$ be complementary screens: the open part of $S_1$ is the opaque part of $S_2$, and conversely.
Let $U_1$ and $U_2$ be the diffracted fields behind $S_1$ and $S_2$, and let $U_0$ be the field with no screen.
Then, at every point behind the screen plane,
$$U_1 + U_2 = U_0.$$
In particular, at every point where $U_0 = 0$, the intensities agree: $\abs{U_1}^2 = \abs{U_2}^2$.

## Remarks

In Kirchhoff's approximation, the field behind the screen is an integral of the incident field over the openings.
The openings of $S_1$ and $S_2$ together make up the whole plane, and the integral over the whole plane gives the unobstructed field $U_0$.
So the identity is the additivity of the integral.

Example: a laser beam focused by a lens gives $U_0 = 0$ away from the focal spot in the focal plane.
There, the Fraunhofer pattern of a thin wire equals the pattern of a slit of the same width, which is how the width of a hair can be measured.

The identity holds for Kirchhoff's approximate theory.
For electromagnetic waves and thin, perfectly conducting screens there is an exact version due to Booker.
In it, the complementary screen is lit by the wave with the electric and magnetic fields exchanged.

## Explanations

### L1 human

Take a card with a small hole, and a small disc of the same shape as the hole.
Babinet's principle says that, away from the direct beam, they spread light into the same pattern.
The light through the hole plus the light around the disc must add up to the light with nothing in the way.
Where nothing in the way gives darkness, the two waves are equal and opposite, so they are equally bright.

### L2 human

The principle halves the work in diffraction: the pattern of an obstacle follows from the pattern of an aperture.
It explains why a thin fibre and a slit give the same Fraunhofer fringes.
In antenna theory, its electromagnetic form relates a slot antenna to the complementary strip dipole, and their impedances satisfy Booker's relation.
