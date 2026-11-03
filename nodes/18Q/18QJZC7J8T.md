---
tag: 18QJZC7J8T
kind: definition
name: Nonimaging optics
msc: [78A05, 78A55]
defines: 8QZN1EN3EB
uses: [90F3NWRHVD, M8FEBN0QSE, 9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Nonimaging_optics
---

## Definition

In [[geometrical optics|90F3NWRHVD]], let a source and a target be given as sets of rays, each ray described by a point and a direction.
*Nonimaging optics* is the design of optical systems that send the rays of the source to the target with optimal transfer of light.
The quantity to optimise is the fraction of the source light reaching the target, or the distribution of light over the target.
No condition is imposed that rays from one source point meet at one image point.
The *geometric concentration* of a concentrator is $C = A_{\mathrm{in}} / A_{\mathrm{out}}$, the ratio of the area of its entrance aperture to the area of its exit aperture.

## Remarks

Conservation of [[etendue|M8FEBN0QSE]] bounds the concentration.
Let a three-dimensional concentrator accept all rays within a half-angle $\theta$ and deliver them into a medium of [[refractive index|9VGK0SP6EQ]] $n$.
Then $C \le n^2 / \sin^2 \theta$; in two dimensions the bound is $C \le n / \sin \theta$.
Example: the two-dimensional compound parabolic concentrator, made of two tilted parabolic arcs, accepts all rays within $\theta$ of its axis and attains $C = 1 / \sin\theta$ in air.
Non-example: a camera lens is designed so that the rays from each object point meet at one image point; this imaging condition is exactly what nonimaging design drops.

## Explanations

### L1 human

Nonimaging optics asks how to move light, not how to copy a picture.
The figure of merit is how much light gets from the source to the target, or how evenly it lands there.
