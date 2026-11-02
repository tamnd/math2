---
tag: QHPXB39SN7
kind: statement
role: theorem
name: Rogers' bound
msc: [52C17, 11H31]
uses: [HF32CBN5MA, 4P5PSWADJD]
about: [4P5PSWADJD]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_packing
---

## Statement

Let $n \ge 1$.
Let $T$ be a regular simplex in $\R^n$ with edge length $2$.
Let $\sigma_n$ be the fraction of the volume of $T$ covered by the $n + 1$ unit balls centred at the vertices of $T$.
Then every [[sphere packing|HF32CBN5MA]] of unit balls in $\R^n$ has upper [[packing density|4P5PSWADJD]] at most $\sigma_n$.

## Remarks

C. A. Rogers proved the bound in 1958.
The proof splits space into the Voronoi cells of the centres, and splits each cell further into simplices.
A local volume argument shows that the balls fill at most the fraction $\sigma_n$ of each Voronoi cell.
For $n = 2$, the triangle of side $2$ has area $\sqrt 3$, and the three discs cover three sectors of angle $\pi/3$, of total area $\pi/2$.
So $\sigma_2 = \pi/\sqrt{12}$, and the bound is sharp by [[Thue's theorem|3P246RHXMF]].
For $n = 3$ one gets $\sigma_3 \approx 0.7797$, a little above the true optimum $\pi/\sqrt{18} \approx 0.7405$ of the [[Kepler conjecture|AFMBQT06ZV]].

## Explanations

### L1 human

In the plane, the best packing of coins puts every three neighbouring coins at the corners of an equilateral triangle.
Rogers' bound says that in any dimension, a packing of balls cannot be denser than the share of a regular simplex filled by balls at its corners.
In dimension $3$ this simplex is a regular tetrahedron, and the bound is close to, but above, the true answer.

### L2 human

Rogers' bound was the best general upper bound on sphere packing density for about twenty years.
For large $n$ it is roughly $\tfrac{n}{e} 2^{-n/2}$, and the Kabatiansky–Levenshtein bound improved it exponentially in 1978 by a method based on linear programming.
In dimensions $4$ to $36$ the Cohn–Elkies linear programming bound is better, and it is sharp in dimensions $8$ and $24$.
