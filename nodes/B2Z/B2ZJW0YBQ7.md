---
tag: B2ZJW0YBQ7
kind: statement
role: theorem
name: Varignon's theorem
msc: [51M04]
uses: [8VEFWD3EJB, 0S706JBZBG]
about: [8VEFWD3EJB]
sources:
  - url: https://en.wikipedia.org/wiki/Varignon%27s_theorem
same_as:
  wikidata: Q1896455
  wikipedia: Varignon's theorem
---

## Statement

Let $ABCD$ be a simple quadrilateral, that is a simple [[polygon|8VEFWD3EJB]] with four vertices, in the Euclidean plane.
Let $K$, $L$, $M$, $N$ be the [[midpoints|0S706JBZBG]] of $AB$, $BC$, $CD$, $DA$.
Then $KLMN$ is a parallelogram.
Its sides are parallel to the diagonals $AC$ and $BD$ and half as long, and its area is half the area of $ABCD$.

## Remarks

With vectors, $L - K = \frac{1}{2}(C - A) = M - N$, so $KL$ and $NM$ are parallel and equal, which makes $KLMN$ a parallelogram.
In the same way $KN$ and $LM$ equal $\frac{1}{2}(D - B)$.
The area of $ABCD$ is $\frac{1}{2}\abs{(C - A) \times (D - B)}$, and the area of $KLMN$ is $\abs{\frac{1}{2}(C - A) \times \frac{1}{2}(D - B)}$, which is half of it.
Example: for the square with vertices $(0, 0), (2, 0), (2, 2), (0, 2)$, the midpoints form a square of side $\sqrt 2$ and area $2$, half of $4$.
The parallelogram part needs no simplicity; for a self-crossing quadrilateral the area relation fails, and the parallelogram can even degenerate.

## Explanations

### L1 human

Draw any four-sided figure and mark the middle of each side.
Joining these four midpoints always gives a parallelogram.
This works even for very irregular quadrilaterals, and the parallelogram covers exactly half of the area.

### L2 human

The proof is the midpoint theorem for triangles applied twice, once in each triangle cut off by a diagonal.
It is a good first example of how vectors turn a geometric statement into one line of algebra.
