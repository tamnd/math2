---
tag: HTK0AX3RGC
kind: example
name: A table of polyhedra suggests Euler's formula
msc: ["00A35", "52B10"]
topics: [DME0TPC348]
audience: ug1
instance_of: [8DHD3H1CJ9]
uses: [8DHD3H1CJ9, 09HT3P35YP, 0325SGSJAR]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
    locator: Polyhedra
  - url: https://en.wikipedia.org/wiki/Plausible_reasoning
    locator: "Volume II: Patterns of Plausible Inference"
---

## Example

For a [[polyhedron|0325SGSJAR]], let $V$, $E$ and $F$ be the numbers of vertices, edges and faces.
Count them for a cube: $V = 8$, $E = 12$, $F = 6$, so
$$V - E + F = 8 - 12 + 6 = 2.$$
We collect more data and weigh it with the patterns of [[plausible reasoning|8DHD3H1CJ9]].

| Polyhedron | $V$ | $E$ | $F$ | $V - E + F$ |
|---|---|---|---|---|
| tetrahedron | $4$ | $6$ | $4$ | $2$ |
| cube | $8$ | $12$ | $6$ | $2$ |
| octahedron | $6$ | $12$ | $8$ | $2$ |
| square pyramid | $5$ | $8$ | $5$ | $2$ |
| triangular prism | $6$ | $9$ | $5$ | $2$ |
| pentagonal prism | $10$ | $15$ | $7$ | $2$ |
| dodecahedron | $20$ | $30$ | $12$ | $2$ |
| icosahedron | $12$ | $30$ | $20$ | $2$ |

1. The conjecture $A$ is "$V - E + F = 2$ for every polyhedron".
   Each row is a true consequence of $A$, so $A$ becomes more credible.
2. The rows do not all weigh the same.
   The pyramid and the prisms are new kinds of shape after the regular solids, and a consequence of a new kind adds more credibility than one more regular solid.
3. A test of a new kind is a picture frame: a square slab with a square hole, built from four prisms with trapezoid faces.
   It has $8$ corners on top and $8$ below, so $V = 16$.
   Each of the top and bottom has $4$ outer, $4$ inner and $4$ joining edges, and there are $8$ vertical edges, so $E = 12 + 12 + 8 = 32$.
   The faces are $4$ on top, $4$ below, $4$ outside and $4$ inside, so $F = 16$.
4. The frame gives
   $$V - E + F = 16 - 32 + 16 = 0,$$
   so $A$ is false as stated, by deduction.
5. Every solid in the table is convex, and the frame is not.
   The statement "$V - E + F = 2$ for every convex polyhedron" fits all the data, and it is [[Euler's polyhedron formula|09HT3P35YP]], a theorem.

## Remarks

### Two directions of evidence

Steps 1 and 2 are plausible inferences: they raise confidence and prove nothing.
Step 4 is a deduction: one false consequence ends the conjecture as stated.
Eight rows were not a proof, and a table of a hundred convex solids would not have been one either.
Imre Lakatos built his book *Proofs and Refutations* on the history of this conjecture and its counterexamples.

### What changes with more holes

A frame with $g$ holes gives $V - E + F = 2 - 2g$, which is the [[Euler characteristic|RNDDWDAFJ5]] of a surface of genus $g$.
So the failure is not random: the number $V - E + F$ measures the holes, and the convex case is the case $g = 0$.

### Watch out

A table built only from convex shapes cannot detect that convexity is needed.
The blind spot of the data became a hypothesis of the theorem only after a test of a new kind.

### Try it

Check the square pyramid row.
The base has $4$ corners and the apex adds $1$, so $V = 5$; there are $4$ base edges and $4$ slant edges, so $E = 8$; and $F = 1 + 4 = 5$, so $V - E + F = 2$.

A prism over an $n$-gon has $V = 2n$, $E = 3n$ and $F = n + 2$; what is $V - E + F$?
It is $2n - 3n + n + 2 = 2$ for every $n$, a whole family of checks that all have the same kind.

## Explanations

### L1 human

Count the corners, edges and faces of a cube: $8$, $12$ and $6$.
Corners minus edges plus faces gives $2$.
A pyramid, a prism and other solids give $2$ as well.
After many solids, a person starts to believe that the answer is always $2$.
A picture frame gives $0$, so the rule needs a condition: it works for solids without holes.

### L2 human

We check the triangular prism row.
The two triangles have $3$ corners each, so $V = 6$.
Each triangle has $3$ edges, and $3$ vertical edges join them, so $E = 9$.
There are $2$ triangles and $3$ rectangles, so $F = 5$, and
$$V - E + F = 6 - 9 + 5 = 2.$$
The prisms over all $n$-gons give $2$ as well, but they are consequences of one kind, so together they add less credibility than their number suggests.
The typical use: look for a case that differs from the data in a new way, here a hole, before you trust a pattern.
