---
tag: C0NQDQAZ2Y
kind: statement
role: theorem
name: Brahmagupta's formula
msc: [51M04, 51M25]
uses: [0RCP929Y1M]
about: [0RCP929Y1M]
sources:
  - url: https://en.wikipedia.org/wiki/Brahmagupta%27s_formula
same_as:
  wikidata: Q1149348
  wikipedia: Brahmagupta's formula
---

## Statement

Let $ABCD$ be a convex [[cyclic quadrilateral|0RCP929Y1M]] in the Euclidean plane with side lengths $a$, $b$, $c$, $d$.
Let $s = \frac{1}{2}(a + b + c + d)$ be its semiperimeter.
Then the area $K$ of $ABCD$ is
$$K = \sqrt{(s - a)(s - b)(s - c)(s - d)}.$$

## Remarks

The diagonal $AC$ splits $ABCD$ into two triangles, and the opposite angles at $B$ and $D$ add up to $\pi$ because $ABCD$ is cyclic.
Computing $AC^2$ by the law of cosines in both triangles and adding the two areas gives the formula after factoring.
Example: a $3 \times 4$ rectangle is cyclic, $s = 7$, and $\sqrt{4 \cdot 3 \cdot 4 \cdot 3} = 12$.
The hypothesis that $ABCD$ is cyclic is needed.
A rhombus with side $1$ and an angle $\theta \ne \pi/2$ has area $\sin \theta < 1$, but the formula would give $1$.
Letting $d = 0$ turns the formula into [[Heron's formula|0FRBZ2X4HJ]] for a triangle.

## Explanations

### L1 human

For a quadrilateral whose corners all lie on one circle, the area depends only on the four side lengths.
Brahmagupta's formula computes it directly from them.
It looks just like Heron's formula for triangles, with one more factor.

### L2 human

For a general quadrilateral the four sides do not fix the area, since the shape can flex.
Among all quadrilaterals with given sides, the cyclic one has the largest area, and Brahmagupta's formula gives that maximum.
Bretschneider's formula extends it to all convex quadrilaterals by an extra term that involves the sum of two opposite angles.
