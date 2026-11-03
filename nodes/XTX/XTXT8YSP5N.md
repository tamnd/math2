---
tag: XTXT8YSP5N
kind: statement
role: proposition
name: Lambert's cosine law
msc: [80A21, 78A40]
uses: [S6XR2K4N8G, A2RMYX8A65]
about: [S6XR2K4N8G]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert%27s_cosine_law
same_as:
  wikidata: Q1190146
  wikipedia: Lambert's cosine law
---

## Statement

Let a small surface element of area $dA$ emit or reflect radiation with a radiance $L$.
Assume that $L$ is the same in all directions of the hemisphere above the element.
Here radiance is the power per unit area projected normal to the direction and per unit solid angle.
Then:

1. The radiant intensity in a direction at angle $\theta$ from the surface normal is $I(\theta) = L \, dA \cos\theta = I(0) \cos\theta$.
2. The total power leaving the element per unit area, its exitance, is $M = \pi L$.

## Remarks

Proof: seen from a direction at angle $\theta$, the element has projected area $dA \cos\theta$, which gives clause 1.
For clause 2, integrate over the hemisphere with $d\Omega = \sin\theta \, d\theta \, d\phi$:
$$M = \int_0^{2\pi} \int_0^{\pi/2} L \cos\theta \sin\theta \, d\theta \, d\phi = 2\pi L \cdot \tfrac12 = \pi L.$$
The factor is $\pi$, not $2\pi$, because of the cosine.

Example: a [[black body|A2RMYX8A65]] is such a surface, so its exitance is $\pi$ times its radiance, which turns Planck's radiance into the Stefan–Boltzmann exitance.
Matte paper and fresh snow are nearly such surfaces, while a mirror or a glossy surface is not, and for them the cosine law fails.

## Explanations

### L1 human

A matte surface looks equally bright from every angle.
Seen at a slant, it looks smaller, so it sends less total light toward you, in proportion to the cosine of the viewing angle.
These two facts balance: the brightness per visible area is the same.
This is why a sheet of matte paper looks equally bright when you tilt it.

### L2 human

Surfaces that obey the law are called Lambertian, or ideal diffuse.
The law is the assumption behind view factors and radiosity methods, both in heat transfer and in computer graphics.
