---
tag: XJ0JGPBC8R
kind: concept
name: Polyharmonic spline
msc: [41A15, 41A05, 41A63]
sources:
  - url: https://en.wikipedia.org/wiki/Polyharmonic_spline
same_as:
  wikidata: Q7226491
  wikipedia: Polyharmonic spline
---

## Summary

A polyharmonic spline is a sum of translates of one [[radial basis function|ZBSXSTQM2J]] $\varphi(\norm{x})$ on $\R^d$ plus a low degree polynomial.
The radial function is $r^{2m-d}$ or $r^{2m-d} \log r$, a multiple of the [[fundamental solution|K2NK9A8M5F]] of the iterated [[Laplacian|0E0B6RA8K0]] $\Delta^m$ in $\R^d$.
Polyharmonic splines solve scattered data interpolation with minimal "energy", and the [[thin plate spline|P9ZPH7EC8K]] is the best known case.

## Explanations

### L1 human

Data are often measured at scattered points in the plane or in space, not on a grid.
A polyharmonic spline puts a radially symmetric bump at each data point, adds a simple polynomial, and tunes the sizes so that the sum passes through the data.
In one dimension with $m = 2$ the bump is $\abs{x}^3$, and the result is a natural cubic spline.
In the plane with $m = 2$ the bump is $r^2 \log r$, which gives the thin plate spline.
