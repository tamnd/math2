---
tag: ~eb8f8d7d
kind: example
name: Archimedes' quadrature of the parabola by exhaustion
msc: ["01A20", "51M25", "26A42"]
topics: [DME0TPC348]
audience: ug2
not_instance_of:
  - target: ~eff91bdf
    note: the geometric proof uses only properties of the parabola and a geometric series, with no physical law, so it is a mathematical proof and not a physical argument
uses: [~eff91bdf, 04S2GMHX82, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Quadrature_of_the_Parabola
    locator: Geometric proof
  - url: https://en.wikipedia.org/wiki/Method_of_exhaustion
    locator: lead section
---

## Example

We find the area of the segment of the [[parabola|04S2GMHX82]] $y = x^2$ cut off by the chord from $(-1, 1)$ to $(1, 1)$, following the geometric proof of Archimedes.
The answer is $\frac43$ times the area of the inscribed triangle.

1. The first triangle. The triangle with vertices $(-1, 1)$, $(1, 1)$ and $(0, 0)$ has base $2$ and height $1$, so area $T = 1$.
2. The next triangles. The chords from $(-1,1)$ to $(0,0)$ and from $(0,0)$ to $(1,1)$ cut off two smaller segments. In each, take the point where the tangent is parallel to the chord: $(-\frac12, \frac14)$ and $(\frac12, \frac14)$. The triangle $(-1,1), (0,0), (-\frac12, \frac14)$ has area $\frac18$, and so has the other one. Together they have area $\frac14 T$.
3. The pattern. Each stage doubles the number of triangles and divides their total area by $4$. Stage $k$ adds triangles of total area $T/4^k$.
4. The exhaustion. Each new triangle has more than half the area of its own small segment, because it is half of a parallelogram that contains the segment. So after $n$ stages the uncovered part has area less than $1/2^n$ times the area of the segment, which becomes as small as we like.
5. The finite identity. $1 + \frac14 + \cdots + \frac{1}{4^{n-1}} + \frac13 \cdot \frac{1}{4^{n-1}} = \frac43$ for every $n \geq 1$, as induction on $n$ shows.
6. The double contradiction. Let $K$ be the area of the segment. If $K > \frac43 T$, step 4 gives a stage whose triangles exceed $\frac43 T$, against step 5. If $K < \frac43 T$, step 5 gives a stage whose triangles exceed $K$, which is impossible inside the segment.
7. The conclusion. $K = \frac43 T = \frac43$.

Every step uses a geometric property of the parabola or an identity of numbers.
No law of physics is assumed, so this is a [[proof|0B94TKFQJX]] and not a [[physical argument|~eff91bdf]].

## Remarks

The work "Quadrature of the Parabola" contains two proofs of the theorem.
Propositions 6 to 17 give a mechanical proof with a lever, and propositions 18 to 24 give the geometric proof followed here.
So Archimedes himself paired a physical argument with a geometric proof of the same result.
A check by calculus: $\int_{-1}^{1} (1 - x^2)\, dx = 2 - \frac23 = \frac43$.

## Explanations

### L1 human

Archimedes wanted the area between a parabola and a straight cut across it.
He filled the region with triangles: one big triangle, then two smaller ones, then four smaller still.
Each new layer has a quarter of the area of the layer before.
The layers add up to $1 + \frac14 + \frac1{16} + \cdots = \frac43$ times the first triangle.
He proved this with geometry and careful reasoning, without any balance or weights.

### L2 human

We check the area of the triangle in step 2.

1. The vertices are $(-1, 1)$, $(0, 0)$ and $(-\frac12, \frac14)$.
2. The area of a triangle with vertices $(x_1,y_1), (x_2,y_2), (x_3,y_3)$ is $\frac12 |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$.
3. Here it is $\frac12 |(-1)(0 - \frac14) + 0 + (-\frac12)(1 - 0)| = \frac12 |\frac14 - \frac12| = \frac18$.

The typical use: the area of a curved region is squeezed between areas of polygons whose sums are known exactly.
A trap: the sum of an infinite series was not available to Archimedes as a limit, so step 6 replaces it by two finite contradictions.
