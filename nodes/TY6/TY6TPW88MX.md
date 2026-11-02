---
tag: TY6TPW88MX
kind: definition
name: Strange attractor
msc: [37D45, 37C70, 34C28]
defines: 9WKCZGG906
uses: [7FWX24X5MW, SSNFTHZ6YJ]
sources:
  - url: https://en.wikipedia.org/wiki/Attractor
    locator: Strange attractor
---

## Definition

Let $f \colon X \to X$ be a continuous map of a metric space, or a flow on a metric space, and let $A$ be an [[attractor|7FWX24X5MW]] of it.
The attractor $A$ is *strange* if it has a fractal structure.
In the most common precise form, this means that the [[Hausdorff dimension|SSNFTHZ6YJ]] of $A$, or its box-counting dimension, is not an integer.

## Remarks

There is no single agreed definition.
Many authors use strange attractor and chaotic attractor as synonyms, and then they ask for sensitive dependence on initial conditions on $A$ instead of, or in addition to, fractal structure.
The two conditions are different: there are chaotic attractors that are not fractal, and there are fractal attractors on which nearby orbits do not separate.

Example: the Smale solenoid map doubles the angle $\theta \mapsto 2\theta$ around a solid torus and contracts strongly in the two transverse directions.
Its attractor is locally the product of an interval and a Cantor set.
So its dimension lies strictly between $1$ and $2$.

Non-example: for the flow of $r' = r(1 - r^2)$, $\theta' = 1$ in polar coordinates in the plane, the unit circle is an attractor.
It is a smooth closed curve of Hausdorff dimension $1$, an integer, so it is not strange.
