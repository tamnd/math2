---
tag: F9Q17JRV5K
kind: concept
name: Shearlet
msc: [42C40, 42C15, 94A08]
sources:
  - url: https://en.wikipedia.org/wiki/Shearlet
same_as:
  wikidata: Q17018993
  wikipedia: Shearlet
---

## Summary

Shearlets are a multiscale system of functions on $\R^2$ obtained from one generating function by parabolic dilations, shears and translations.
Like [[curvelets|VEVPDJ8S7B]], they resolve directions and represent images with smooth edges sparsely.
Unlike curvelets, they change direction by shearing instead of rotating, and shears with integer parameters preserve the integer lattice.
This makes the passage from the continuous theory to digital algorithms on pixel grids direct.

## Explanations

### L1 human

A shear tilts a picture sideways, as when a deck of cards is pushed so that it leans.
A shearlet is a small thin wave packet that is stretched more in one direction than the other and then tilted by a shear.
Different shears point the packet in different directions, and different scales make it finer.
Since shears with integer amounts move grid points to grid points, the system fits naturally on a grid of pixels.
