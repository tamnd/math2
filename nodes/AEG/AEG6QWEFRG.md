---
tag: AEG6QWEFRG
kind: problem
name: Minimal surface of revolution
msc: [49Q05, 49K05, 53A10]
uses: [JRQZ803Q5Y, F7EKTEESQ5, 0S29Y4ZW0Y, NE09EDK19V, 6NN1HP54GB]
about: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_surface_of_revolution
same_as:
  wikidata: Q6865337
  wikipedia: Minimal surface of revolution
history:
  posed_by: "Leonhard Euler"
  first_stated: "1744"
---

## Problem

Let $a < b$ and $A, B > 0$.
Among curves $y \in C^1([a, b])$ with $y > 0$, $y(a) = A$ and $y(b) = B$, find one whose [[surface of revolution|NE09EDK19V]] about the $x$-axis has the least [[surface area|0S29Y4ZW0Y]]
$$S(y) = 2\pi \int_a^b y(x) \sqrt{1 + y'(x)^2} \, dx.$$

## Remarks

The Lagrangian $y\sqrt{1 + y'^2}$ does not depend on $x$, so the [[Beltrami identity|F7EKTEESQ5]] gives $y / \sqrt{1 + y'^2} = c$ for a constant $c > 0$.
The solutions are the catenaries $y(x) = c \cosh\big((x - d)/c\big)$, and their surfaces of revolution are [[catenoids|6NN1HP54GB]].
Depending on the positions of the two end points, there are two, one or no catenaries through them.
When the end circles are far apart compared with their radii, no catenary joins the points and there is no minimiser among such smooth curves.
Then the infimum of $S$ is $\pi(A^2 + B^2)$, the area of the two end discs, approached by curves that run close to the axis; this limit is the Goldschmidt solution.
For some positions where catenaries do exist, the two discs still have smaller total area than every catenoid through the points, and again no smooth curve attains the infimum.

## Explanations

### L1 human

Dip two parallel rings into soapy water and pull them apart a little.
The soap film between them takes the shape of a catenoid, a surface of revolution whose area cannot be lowered by small changes.
If the rings are pulled too far apart, the film breaks and leaves a flat film on each ring.
