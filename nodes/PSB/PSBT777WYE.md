---
tag: PSBT777WYE
kind: concept
name: Slip-line field theory
msc: [74C05, 74G05]
sources:
  - url: https://en.wikipedia.org/wiki/Slip_line_field
same_as:
  wikidata: Q7540843
  wikipedia: Slip line field
---

## Summary

Slip-line field theory is a method for solving plane strain problems of rigid–perfectly plastic bodies, such as metal forming, indentation and cutting.
In the plastic region the directions of maximum shear stress form two orthogonal families of curves, the slip lines.
The stress equations are [[hyperbolic|92C3S03AQZ]] and the slip lines are their characteristics.
So the problem reduces to building a net of curves along which simple relations hold.
These relations are [[Hencky's theorems on slip lines|VB2JS0EM05]], and the theory is a classical part of [[plasticity|K8BBMTN0KV]].

## Explanations

### L1 human

When a metal is pressed hard enough, it flows by sliding along surfaces of greatest shear.
In a flat, two-dimensional flow these surfaces show up as two sets of curves that always cross at right angles, like a bent grid.
If you know the grid, the pressure everywhere follows from the angle through which the grid lines turn.
For example, under a flat punch pressed into a block, the grid consists of straight triangles and fans of lines.
It gives the punch pressure $2k(1 + \pi/2)$, where $k$ is the shear yield stress.
