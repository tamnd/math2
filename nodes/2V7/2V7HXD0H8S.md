---
tag: 2V7HXD0H8S
kind: concept
name: Method of image charges
msc: [78A30, 35J05]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_image_charges
same_as:
  wikidata: Q1372220
  wikipedia: Method of image charges
---

## Summary

The method of image charges solves electrostatic boundary value problems by placing fictitious charges outside the region of interest.
The fictitious charges are chosen so that the total potential meets the boundary condition, such as zero potential on a grounded conductor.
The [[uniqueness theorem for Poisson's equation|CC7NZRPMBB]] then shows that this potential is the true one inside the region.
It gives closed formulas for the [[Green's function|2F6AJ1DM11]] of a half-space and of a ball.

## Explanations

### L1 human

A charge near a flat metal plate behaves as if the plate were a mirror.
Behind the mirror sits an imaginary charge of opposite sign, at the same distance.
The real charge and its mirror image together make the potential zero on the plate.
In front of the plate, this pair gives exactly the true field.
The image charge is only a bookkeeping device: it does not exist, and the formula is valid only on the real side.
