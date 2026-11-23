---
tag: SC3MSK6P4Q
kind: example
name: Archimedes' quadrature of the parabola by exhaustion
msc: ["01A20", "51M25", "26A42"]
topics: [DME0TPC348]
audience: ug2
not_instance_of:
  - target: THJV0NFPDQ
    note: the geometric proof uses only properties of the parabola and a geometric series, with no physical law, so it is a mathematical proof and not a physical argument
uses: [THJV0NFPDQ, 04S2GMHX82, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Quadrature_of_the_Parabola
    locator: Geometric proof
  - url: https://en.wikipedia.org/wiki/Method_of_exhaustion
    locator: lead section
---

## Example

The region between the [[parabola|04S2GMHX82]] $y = x^2$ and the line $y = 1$ has area $\tfrac43$, and the triangle with corners $(-1, 1)$, $(1, 1)$ and $(0, 0)$ inside it has area $1$.
Archimedes proved the ratio $\tfrac43$ for every segment of a parabola by geometry alone, and we follow his proof for this segment.

1. The first triangle has base $2$ and height $1$, so its area is $T = 1$.
2. The chords from $(-1, 1)$ to $(0, 0)$ and from $(0, 0)$ to $(1, 1)$ cut off two smaller segments.
   In each, take the point where the tangent is parallel to the chord, which is $(-\tfrac12, \tfrac14)$ or $(\tfrac12, \tfrac14)$.
   Each new triangle has area $\tfrac18$, so together they have area $\tfrac14 T$.
3. Each stage doubles the number of triangles and divides their total area by $4$, so stage $k$ adds triangles of total area $T/4^k$.
4. Each new triangle has more than half the area of its own small segment, because it is half of a parallelogram that contains the segment.
   So after $n$ stages the part of the segment not yet covered has less than $1/2^n$ of the area of the segment, and this becomes as small as we like.
5. For every $n \ge 1$ the finite identity
$$1 + \frac14 + \dots + \frac{1}{4^{n-1}} + \frac13 \cdot \frac{1}{4^{n-1}} = \frac43$$
   holds, as induction on $n$ shows.
   So the triangles of the first $n$ stages have total area $\tfrac43 T - \tfrac13 \cdot T/4^{n-1}$, which is always less than $\tfrac43 T$.
6. Let $K$ be the area of the segment, and suppose $K > \tfrac43 T$.
   Step 4 gives a stage where the uncovered part is smaller than $K - \tfrac43 T$, so the triangles have area more than $\tfrac43 T$, against step 5.
7. Now suppose $K < \tfrac43 T$.
   Step 5 gives a stage where $\tfrac13 \cdot T/4^{n-1}$ is smaller than $\tfrac43 T - K$, so the triangles have area more than $K$, which is impossible inside the segment.
8. Both cases are excluded, so
$$K = \tfrac43 T = \tfrac43.$$

Every step uses a property of the parabola or an identity of numbers, so this is a [[proof|0B94TKFQJX]] and not a [[physical argument|THJV0NFPDQ]].

## Remarks

### Two methods in one work

The work "Quadrature of the Parabola" contains two proofs of the same theorem.
Propositions 6 to 17 give a mechanical argument with a lever, and propositions 18 to 24 give the geometric proof followed here.
So Archimedes himself paired a physical argument with a geometric proof of the same result.
A check by calculus agrees:
$$\int_{-1}^{1} (1 - x^2)\, dx = 2 - \frac23 = \frac43.$$

### Why the double contradiction

Archimedes did not have the sum of an infinite series as a limit.
Steps 6 and 7 replace the limit by two finite arguments: for each wrong value of $K$, some finite stage already gives a contradiction.
This is the method of exhaustion, and it is the ancestor of the definition of a limit by inequalities.

### Watch out

Step 4 is the step that makes the proof work, and it is easy to skip.
Without it we know that the triangles add up to at most $\tfrac43 T$, but not that they fill the segment.
A sequence of shapes inside a region can have total area that approaches a value smaller than the area of the region.

### Try it

What area do the triangles of the first two stages cover?
They cover $1 + \tfrac14 = \tfrac54$, which is $\tfrac{1}{12}$ less than $\tfrac43$, and step 5 gives the same gap, $\tfrac13 \cdot \tfrac14 = \tfrac1{12}$.

## Explanations

### L1 human

Archimedes wanted the area between a parabola and a straight cut across it.
He filled the region with triangles: one big triangle, then two smaller ones, then four smaller still.
Each new layer has a quarter of the area of the layer before.
The layers add up to $1 + \tfrac14 + \tfrac1{16} + \dots = \tfrac43$ times the first triangle.
He proved this with geometry and careful reasoning, without any balance or weights.

### L2 human

We check the area of one triangle in step 2, with corners $(-1, 1)$, $(0, 0)$ and $(-\tfrac12, \tfrac14)$.
A triangle with corners $(x_1, y_1)$, $(x_2, y_2)$ and $(x_3, y_3)$ has area
$$\tfrac12 \left| x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \right|.$$
Substitute the corners:
$$\tfrac12 \left| (-1)\left(0 - \tfrac14\right) + 0 + \left(-\tfrac12\right)(1 - 0) \right| = \tfrac12 \left| \tfrac14 - \tfrac12 \right| = \tfrac18.$$
The typical use of exhaustion is to squeeze the area of a curved region between areas of polygons whose sums are known exactly.
Watch out: a computation of the triangle areas alone is not the proof, because the proof also needs the covering estimate of step 4.
