---
tag: YY46TGRVBG
kind: concept
name: Analysis on fractals
msc: ["31E05", "28A80"]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_on_fractals
same_as:
  wikidata: Q4751108
  wikipedia: Analysis on fractals
---

## Summary

Analysis on fractals builds Laplacians, energies, harmonic functions, heat equations and diffusion processes on fractal sets such as the Sierpiński gasket.
On such sets there are no smooth curves or tangent vectors, so the [[Laplacian|0E0B6RA8K0]] cannot be defined by derivatives.
Instead one takes limits of renormalized energies and [[Laplacian matrices|TN6M6DVZRP]] of finite graphs that approximate the fractal, as in [[Kigami's construction|VXB4G47Z3T]].
Another route builds Brownian motion on the fractal as a limit of random walks on these graphs.
The key tools are [[Dirichlet forms|MH20Q2N1AH]] and [[resistance forms|THCM7DWHNY]].
The results show new features, such as a spectral dimension that differs from the [[Hausdorff dimension|SSNFTHZ6YJ]].

## Explanations

### L1 human

Imagine a triangle from which the middle triangle is removed, and then the middle of each smaller triangle, forever: this is the Sierpiński gasket.
Heat cannot flow along straight lines in it, because almost every line segment hits a hole.
But one can model the gasket by a finite network of resistors, one network for each level of detail, and compute how heat or current flows in each network.
When the networks are rescaled in the right way, these computations converge, and the limit is a Laplacian on the gasket itself.
For the [[Laplacian on the Sierpiński gasket|W9V9JSAWYK]], the right scaling multiplies energies by $5/3$ at each level, a number that comes from a small computation on a triangle.
