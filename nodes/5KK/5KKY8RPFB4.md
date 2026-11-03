---
tag: 5KKY8RPFB4
kind: concept
name: Mesh analysis
msc: [94C05, 94C15]
sources:
  - url: https://en.wikipedia.org/wiki/Mesh_analysis
same_as:
  wikidata: Q1852652
  wikipedia: Mesh analysis
---

## Summary

Mesh analysis is a systematic method to compute the currents of a linear circuit drawn in the plane without crossings.
It assigns a circulating current to each mesh, a bounded face of the drawing.
Then it writes the voltage law of [[Kirchhoff's circuit laws|9B0V41V2F8]] around each mesh.
The current law then holds automatically.
It is the dual of [[nodal analysis|9NW7KCBSME]], and for a planar circuit the two methods are exchanged by planar duality.

## Explanations

### L1 human

Draw the circuit on paper so that no wires cross; the wires cut the paper into small windows, the meshes.
Imagine a current running around the edge of each window.
The real current in a wire is the sum of the mesh currents of the one or two windows on its sides, taken with signs.
Walking around each window, the voltage drops must add up to zero, which gives one equation per window.
For one window with a battery $E$ and two resistors $R_1, R_2$, the equation is $(R_1 + R_2) I = E$.
