---
tag: 7642CPVVSF
kind: example
name: Eight-vertex model
msc: [82B20, 82B23]
instance_of: [PAEME5EQRM]
uses: [45HEVXM7RD]
sources:
  - url: https://en.wikipedia.org/wiki/Eight-vertex_model
same_as:
  wikidata: Q5348943
  wikipedia: Eight-vertex model
---

## Example

Let $\Lambda$ be the $N \times N$ square grid on a torus and let $a, b, c, d \ge 0$.
A configuration orients every edge so that each vertex has an even number of incoming edges: $0$, $2$ or $4$.
There are $8$ such local orientations.
They are the $6$ of the [[six-vertex model|45HEVXM7RD]], and the two in which all four arrows point in or all four point out.
In the symmetric zero-field case the six-vertex pairs get the weights $a$, $b$, $c$, and the new pair gets the weight $d$.
The *eight-vertex model* is the probability measure on these orientations proportional to the product of the vertex weights.

## Remarks

For $d = 0$ it reduces to the six-vertex model.
Baxter computed its free energy exactly in the early 1970s, using commuting transfer matrices built from weights that satisfy the [[Yang–Baxter equation|663BP8ZHS5]].
Its critical exponents vary continuously with the weights, which showed that exponents of a two-dimensional model need not be fixed by dimension and symmetry alone.
The model can be rewritten as two Ising models on the two sublattices of the dual lattice, coupled by a four-spin interaction.
It is the classical counterpart of the XYZ quantum spin chain.

## Explanations

### L1 human

Put arrows on the edges of a square grid so that every vertex has an even number of arrows pointing in.
Compared with ice, two new pictures are allowed: all arrows in and all arrows out.
Baxter's exact solution of this model was a turning point for the theory of solvable models.
