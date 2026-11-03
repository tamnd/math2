---
tag: TWF69TQH3S
kind: concept
name: Optical depth
msc: [85A25, 80A21, 78A40]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_depth
same_as:
  wikidata: Q890809
  wikipedia: Optical depth
---

## Summary

The optical depth measures how much a medium weakens light that passes through it.
It is the integral of the absorption coefficient along the path, a dimensionless number.
Without emission, a beam passing through optical depth $\tau$ keeps the fraction $e^{-\tau}$ of its intensity.
It is the natural length variable in the [[radiative transfer equation|EX9YYRMAJA]] and in models of stellar atmospheres.

## Explanations

### L1 human

Fog, smoke or a stellar atmosphere dims the light that crosses it.
Optical depth counts this dimming on a logarithmic scale: each unit of optical depth cuts the light by a factor $e \approx 2.72$.
A layer with $\tau = 1$ lets through about $37\%$ of the light, and a layer with $\tau = 5$ lets through less than $1\%$.
A medium is called optically thin when $\tau \ll 1$ and optically thick when $\tau \gg 1$.
We see a star down to the depth where the optical depth measured from outside is about $1$.
