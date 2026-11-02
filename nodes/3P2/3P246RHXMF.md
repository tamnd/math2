---
tag: 3P246RHXMF
kind: statement
role: theorem
name: Thue's theorem
msc: [52C15, 05B40]
uses: [S360JBEYKD, 4P5PSWADJD]
about: [S360JBEYKD]
sources:
  - url: https://en.wikipedia.org/wiki/Circle_packing
---

## Statement

Every packing of equal circles in the plane $\R^2$ has upper [[packing density|4P5PSWADJD]] at most
$$\frac{\pi}{\sqrt{12}} = \frac{\pi}{2\sqrt 3} \approx 0.9069.$$
The hexagonal [[circle packing|S360JBEYKD]], in which the centres form a triangular lattice and each circle touches six others, has density exactly $\pi/\sqrt{12}$.

## Remarks

For the hexagonal packing with radius $1$, the centres form a lattice whose fundamental parallelogram has area $2\sqrt 3$.
Each cell carries one disc of area $\pi$, and this gives the density.
For the upper bound, one standard proof joins the centres of a saturated packing into a Delaunay triangulation.
Each triangle has sides at least $2$.
One shows that the discs cover at most the fraction $\pi/\sqrt{12}$ of each triangle, with equality for the equilateral triangle of side $2$.
Lagrange proved the bound for lattice packings in 1773.
Axel Thue gave proofs for general packings in 1890 and 1910, and László Fejes Tóth gave the first proof regarded as complete in 1940.

## Explanations

### L1 human

Pack equal coins on a big table as tightly as possible.
The best you can do is the honeycomb pattern, where each coin touches six others, and it covers about $90.7\%$ of the table.
The theorem says that no clever irregular arrangement can beat it.

### L2 human

Thue's theorem is the two-dimensional case of the sphere packing problem; its three-dimensional case is the [[Kepler conjecture|AFMBQT06ZV]].
The local argument works in the plane because the densest local arrangement, six circles around one, fits together into a global tiling.
In three dimensions this fails, which is one reason why the Kepler conjecture is so much harder.
