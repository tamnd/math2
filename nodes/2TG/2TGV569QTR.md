---
tag: 2TGV569QTR
kind: definition
name: Seismic migration
msc: [86A22, 35R30, 35L05]
defines: BVS01HTGNS
uses: [5EHD2XBQDG, 3Y0VBDXHJD, 0WN5G117YC]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_migration
---

## Definition

Let reflection data $d(s, r, t)$ be recorded at the surface for sources $s$, receivers $r$ and times $t$.
Let $c(x)$ be a given model of the wave speed in the subsurface.
In the [[Born approximation|3Y0VBDXHJD]] the data depend linearly on a reflectivity $R(x)$, so $d \approx F R$.
The linear operator $F$ is built from solutions of the [[wave equation|5EHD2XBQDG]] with speed $c$.
*Seismic migration* is the map from $d$ to an image $I(x)$ of the subsurface given by the adjoint operator, or an approximation of it:
$$I = F^{*} d.$$
Equivalently, the recorded wavefield is propagated backward in time into the model, and an imaging condition is applied at each point $x$.

## Remarks

Example: take zero-offset data over a medium with constant speed $c$.
A point scatterer at $(x_0, z_0)$ produces an event at two-way time
$$t(x) = \frac{2}{c} \sqrt{(x - x_0)^2 + z_0^2}.$$
This is a branch of a [[hyperbola|0WN5G117YC]] in the $(x, t)$ plane.
Migration sums the data along such curves, so the energy of this event focuses at $(x_0, z_0)$.
Non-example: the unmigrated section, which plots each reflection at depth $c\, t/2$ directly below the recording point, is not migrated; it places the scatterer energy on the whole hyperbola.
The image $F^{*} d$ has correct positions but distorted amplitudes, because $F^{*}$ is not the inverse of $F$; least-squares migration solves $\min_R \norm{F R - d}^2$ instead.
Common methods are Kirchhoff migration, which sums along travel-time curves, and wave-equation methods such as reverse time migration.

## Explanations

### L1 human

Migration takes the recorded echoes and the wave speeds, and sends each echo back to the place underground that could have produced it.
Where many echoes agree, the image becomes bright, and this marks a reflector.
