---
tag: 581AGFCCRX
kind: concept
name: Robin boundary condition
msc: [34B05, 35J25, 34B24]
sources:
  - url: https://en.wikipedia.org/wiki/Robin_boundary_condition
same_as:
  wikidata: Q748993
  wikipedia: Robin boundary condition
---

## Summary

A Robin boundary condition prescribes a linear combination of the value of the unknown function and its outward normal derivative on the boundary.
It interpolates between the [[Dirichlet condition|EETVA6QYX4]] and the [[Neumann condition|GS3KT2H645]].
It models heat exchange with the surroundings, where the flux through the wall is proportional to the temperature difference.
The separated boundary conditions of [[Sturm–Liouville theory|7WV6B2502K]] are of this type.
See the [[definition|Y19WM1EMS7]].

## Explanations

### L1 human

Think of a hot rod whose ends lose heat to the air.
The heat flowing out of an end is proportional to how much hotter the end is than the air.
This links the slope of the temperature at the end to its value there.
For an end at $x = 1$ with outside temperature $0$, the condition reads $u'(1) = -h\, u(1)$ for a constant $h > 0$.
