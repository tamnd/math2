---
tag: CVTKSCP55A
kind: problem
name: Kelvin problem
msc: [49Q10, 52C22, 49Q20]
uses: [HTJ03RFKFH, 0S29Y4ZW0Y, 381RB634WS, 3JST9B967R]
about: [HTJ03RFKFH]
sources:
  - url: https://en.wikipedia.org/wiki/Weaire%E2%80%93Phelan_structure
history:
  posed_by: "William Thomson (Lord Kelvin)"
  first_stated: "1887"
---

## Problem

Among all partitions of $\R^3$ into cells of equal volume, find one whose interfaces have the least [[surface area|0S29Y4ZW0Y]] per cell.

To make the question precise, fix the cell volume to $1$.
Then ask for the least value of the quantity
$$\limsup_{R \to \infty} \frac{\mathcal{H}^2(\Sigma \cap B_R)}{\abs{B_R}}.$$
Here $\Sigma$ is the union of the cell boundaries, $\mathcal{H}^2$ is area, and $B_R$ is the ball of radius $R$ about the origin.

## Remarks

Kelvin proposed as the answer a partition into congruent cells shaped like truncated octahedra, arranged as in the bitruncated cubic [[honeycomb|HTJ03RFKFH]].
His cells are not exactly polyhedra: their hexagonal faces are slightly curved, so that they satisfy [[Plateau's laws|381RB634WS]].
In 1993 Denis Weaire and Robert Phelan found a partition into two kinds of cells of equal volume with about $0.3\%$ less area than Kelvin's.
So Kelvin's proposal is not optimal.
The problem is open: no partition is known to be optimal, and it is not known whether the Weaire–Phelan structure is.
The two-dimensional analogue is solved: by the [[honeycomb theorem|3JST9B967R]] of Thomas Hales, the regular hexagonal tiling is optimal in the plane.

## Explanations

### L1 human

How should one divide space into bubbles of the same size, so that the soap film needed is as small as possible?
Kelvin suggested a pattern of identical fourteen-faced cells.
A century later, a better foam was found with two kinds of cells, and nobody yet knows the best one.
