---
tag: 2TRG8VNJ4H
kind: example
name: Proof as discovery in Varignon's theorem
msc: ["00A35", "51M04"]
topics: [N4P3E53HM0]
audience: school
instance_of: [ENY0GKRJS8]
uses: [ENY0GKRJS8, B2ZJW0YBQ7, 0S706JBZBG]
sources:
  - url: https://en.wikipedia.org/wiki/Varignon%27s_theorem
    locator: lead section
---

## Example

[[Varignon's theorem|B2ZJW0YBQ7]] says that the [[midpoints|0S706JBZBG]] of the four sides of a quadrilateral $ABCD$ are the vertices of a parallelogram.
A student who draws only convex quadrilaterals may state it for convex quadrilaterals only.
We give a proof and then read it to see which hypotheses it really uses.

1. Treat points as vectors in the plane.
   The midpoints of $AB$, $BC$, $CD$ and $DA$ are
   $$K = \tfrac{1}{2}(A + B), \quad L = \tfrac{1}{2}(B + C), \quad M = \tfrac{1}{2}(C + D), \quad N = \tfrac{1}{2}(D + A).$$
2. Subtract to get one pair of sides.
   $$L - K = \tfrac{1}{2}(C - A), \qquad M - N = \tfrac{1}{2}(C - A).$$
3. So $L - K = M - N$.
   The sides $KL$ and $NM$ are parallel to the diagonal $AC$, and each is half as long.
4. In the same way $N - K = \tfrac{1}{2}(D - B) = M - L$, so the sides $KN$ and $LM$ are parallel to the diagonal $BD$.
5. A quadrilateral $KLMN$ with $L - K = M - N$ is a parallelogram, provided that its four vertices do not lie on one line.

Steps 1 to 5 use only the midpoint formula and vector arithmetic.
No step uses that $ABCD$ is convex, so the proof gives more than the student stated: the theorem holds for non-convex quadrilaterals too.

We check this on a non-convex quadrilateral.

6. Let $A = (0, 0)$, $B = (4, 0)$, $C = (1, 1)$ and $D = (0, 4)$.
   The point $C$ lies inside the triangle $ABD$, so the angle at $C$ is greater than $180°$ and $ABCD$ is not convex.
7. The midpoints are $K = (2, 0)$, $L = (2.5, 0.5)$, $M = (0.5, 2.5)$ and $N = (0, 2)$.
8. Compare opposite sides.
   $$L - K = (0.5, 0.5) = M - N, \qquad N - K = (-2, 2) = M - L.$$
   Check: $\tfrac{1}{2}(C - A) = (0.5, 0.5)$ and $\tfrac{1}{2}(D - B) = (-2, 2)$, as steps 2 and 4 predict.
9. So $KLMN$ is a parallelogram.

## Remarks

The example shows the function of discovery: reading a proof for the hypotheses it really uses can give a more general theorem.
The figure suggested convexity, but the proof never needed it.
The proof also gave facts that nobody asked for, namely that the sides of $KLMN$ are parallel to the diagonals of $ABCD$ and half as long.

Step 5 is where care is needed.
The four midpoints lie on one line when the diagonals $AC$ and $BD$ are parallel, and that can happen for a self-crossing quadrilateral.
For $A = (0, 0)$, $B = (0, 1)$, $C = (2, 0)$ and $D = (2, 1)$ the midpoints are $(0, 0.5)$, $(1, 0.5)$, $(2, 0.5)$ and $(1, 0.5)$, all on the line $y = 0.5$.
So the general theorem needs "the diagonals are not parallel", and the proof told us exactly that.

## Explanations

### L1 human

Draw a four-sided shape and mark the middle of each side.
Join the four middle points in order, and you get a parallelogram.
Most people first try a nice shape, such as a kite or a rectangle.
The proof never uses the fact that the shape bulges outward.
So the same thing happens for a dented shape like an arrowhead, and a quick drawing confirms it.

### L2 human

Here is a second test of the general claim, with $A = (0, 0)$, $B = (6, 0)$, $C = (2, 2)$ and $D = (0, 6)$, where again $C$ lies inside the triangle $ABD$.
The midpoints are
$$K = (3, 0), \quad L = (4, 1), \quad M = (1, 4), \quad N = (0, 3).$$
Opposite sides agree:
$$L - K = (1, 1) = M - N, \qquad N - K = (-3, 3) = M - L.$$
So $KLMN$ is a parallelogram, as the proof predicts.
This is how a proof strengthens a theorem: list the hypotheses that the proof uses, and drop the rest.
Watch out: the two numerical checks only illustrate the claim.
The vector proof is what covers every quadrilateral.
