---
tag: WTXN79ZK76
kind: conjecture
name: MLC conjecture
msc: [37F46, 37F10]
uses: [QSWSVYRCS1, FDVAHRJKF3, WDZFV2ACXR, E6E6DH35Y9]
about: [QSWSVYRCS1]
sources:
  - url: https://en.wikipedia.org/wiki/Mandelbrot_set
    locator: Local connectivity
history:
  posed_by: "Adrien Douady and John H. Hubbard"
---

## Statement

Let $M \subset \C$ be the [[Mandelbrot set|QSWSVYRCS1]] of the [[quadratic family|WDZFV2ACXR]] $f_c(z) = z^2 + c$.
The conjecture states that $M$ is [[locally connected|FDVAHRJKF3]].

## Remarks

The name MLC stands for "Mandelbrot set is locally connected".
The conjecture is open.
Douady and Hubbard proved that $M$ is connected.
Yoccoz proved that $M$ is locally connected at every parameter $c \in M$ for which $f_c$ is at most finitely renormalizable.
Local connectivity has since been proved at many further parameters, but not at all of them.
If $M$ is locally connected, then the external rays of Douady and Hubbard give a complete combinatorial description of $M$.
This description is the "pinched disc" model coming from Thurston's quadratic minor lamination.
MLC would also imply the [[density of hyperbolicity conjecture|E6E6DH35Y9]] for the quadratic family.

## Explanations

### L1 human

A set is locally connected when every point has arbitrarily small neighbourhoods in the set that are each in one piece.
A comb with infinitely many teeth piling up to one limit tooth fails this at the points of the limit tooth away from the spine.
Every small neighbourhood of such a point falls apart into pieces of many teeth.
The Mandelbrot set has infinitely many smaller and smaller bulbs and filaments, so it is not clear that it has no such bad spots.
If it is locally connected, its whole shape can be described exactly by a simple combinatorial rule, and many other questions about the quadratic family would be settled.
