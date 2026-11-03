---
tag: PZ5KHM9YEM
kind: concept
name: Vortex lattice method
msc: [76M23, 76G25]
sources:
  - url: https://en.wikipedia.org/wiki/Vortex_lattice_method
same_as:
  wikidata: Q1089893
  wikipedia: Vortex lattice method
---

## Summary

The vortex lattice method is a numerical method that computes the lift and induced drag of wings of almost any planform in incompressible potential flow.
It covers the lifting surface with a grid of panels and puts a horseshoe vortex on each panel.
The vortex strengths are chosen so that the flow does not cross the surface at one control point per panel.
This turns the flow problem into a [[system of linear equations|0GT4WWGWH2]] whose coefficients come from the [[Biot–Savart law|ZXKV1HSQMW]].
It extends [[lifting-line theory|YFM3DBFHWV]] to swept and low aspect ratio wings, and it is still widely used in aircraft design.

## Explanations

### L1 human

Instead of one line of swirling air along the wing, the method uses a whole net of small swirls spread over the wing surface.
Each swirl is shaped like a horseshoe: a short piece across the wing and two long legs trailing back behind it.
The strength of every swirl is unknown, and one condition per panel says that air must not flow through the wing at a chosen point.
With, say, $40$ panels one gets $40$ linear equations for $40$ unknowns, which a computer solves at once.
