---
tag: DK0A24WJKF
kind: concept
name: Discrete differential geometry
msc: [53A70, 52C26, 52B70]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_differential_geometry
same_as:
  wikidata: Q958922
  wikipedia: Discrete differential geometry
---

## Summary

Discrete differential geometry builds discrete counterparts of notions of differential geometry, such as curvature, geodesics and conformal maps.
It works with polyhedral surfaces, meshes and other finite structures.
A good discrete notion keeps the key theorems of the smooth theory exactly, not only in the limit.
The angle defect at a vertex of a [[polyhedron|0325SGSJAR]] plays the role of [[Gaussian curvature|SQVQ5DQT6W]], and [[circle packings|S360JBEYKD]] serve as discrete conformal maps.
The field supplies the mathematics behind computer graphics, geometry processing and architectural design.

## Explanations

### L1 human

Smooth surfaces are approximated on computers by surfaces made of flat triangles.
Discrete differential geometry asks how to define curvature and related ideas directly on such triangle meshes.
At a vertex of a polyhedral surface, the curvature is measured by how much the angles around the vertex fall short of a full turn $2\pi$.
At a corner of a cube three right angles meet, so the defect is $2\pi - 3 \cdot \frac{\pi}{2} = \frac{\pi}{2}$.
The eight corners give a total of $4\pi$, exactly as the Gauss–Bonnet theorem predicts for a sphere; this is [[Descartes's theorem|PT67C5ANSD]].
