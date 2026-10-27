---
tag: 0EKZW08FQ5
kind: definition
name: Orientable surface
msc: [53A05]
defines: 0TD904MG06
uses: [0BJDQ2HBH1, 05788J51WZ, 0DQ8ERJZNS]
sources:
  - url: https://en.wikipedia.org/wiki/Orientability
    locator: Orientable surfaces
  - url: https://en.wikipedia.org/wiki/Orientability
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: Orientation
inventory: [CW3MVTV0FC]
---

## Definition

Let $S \subseteq \mathbb{R}^3$ be a surface that has a tangent plane at each point.
The surface $S$ is orientable if there is a continuous map $n \colon S \to \mathbb{R}^3$ with the following property. For each $p \in S$, $n(p)$ is a [[unit normal vector|0BJDQ2HBH1]] of $S$ at $p$.
Such a map $n$ is an orientation of $S$, and $S$ together with $n$ is an oriented surface.

## Remarks

If $S$ is connected and orientable, then it has exactly two orientations, $n$ and $-n$.
A regular injective [[parametrisation|05788J51WZ]] $r$ gives the orientation $n = (r_u \times r_v) / \| r_u \times r_v \|$. Swapping $u$ and $v$ gives the opposite orientation.
Spheres, planes and tori are orientable. The boundary of a bounded region in $\mathbb{R}^3$ has the outward normal as its standard orientation. The Möbius strip is not orientable.
Integrals of vector fields across a surface, such as flux, need an orientation. Reversing the orientation changes their sign. [[Integrals of scalar functions|0DQ8ERJZNS]] do not need one.

## Explanations

### L1 human

An orientable surface has two sides, an inside and an outside, or a top and a bottom.
On a Möbius strip, an ant can walk from one side to the other without crossing an edge. So there is no consistent choice of side.
