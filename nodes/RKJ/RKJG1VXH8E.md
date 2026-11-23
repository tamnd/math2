---
tag: RKJG1VXH8E
kind: example
name: Barbara for squares, rectangles and parallelograms
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
instance_of: [AC6XQ4KRNT, MZBNX2T6Q6, S4BTTGFR6J, 1TD6HRM5NG]
uses: [AC6XQ4KRNT, MZBNX2T6Q6, S4BTTGFR6J, 1TD6HRM5NG, KSJ9W29KXQ, 0KCT6DPXJK, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

The argument is: all rectangles are parallelograms, all squares are rectangles, so all squares are parallelograms.
Its form is [[Barbara|AC6XQ4KRNT]]: all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$.
We check that the argument is a categorical syllogism of the first figure and of mood AAA, and then we prove validity in three ways.

1. Each sentence has the form "all $X$ are $Y$", so each is an A proposition, and the mood is AAA.
2. The conclusion "all squares are parallelograms" has subject "squares" and predicate "parallelograms", so $S$ is the squares and $P$ is the parallelograms.
3. "Rectangles" occurs in both premises and not in the conclusion, so it is the middle term $M$, and there are exactly three [[terms|KSJ9W29KXQ]].
4. The middle term is the subject of the major premise and the predicate of the minor premise, which is the scheme of the [[first figure|S4BTTGFR6J]].
5. Validity with sets: the premises say $M \subseteq P$ and $S \subseteq M$.
   Let $x \in S$; then $x \in M$ by the minor premise, and $x \in P$ by the major premise, so $S \subseteq P$.
6. Validity in predicate logic: from $\forall x\,(M(x) \to P(x))$ and $\forall x\,(S(x) \to M(x))$, for an arbitrary object $a$ we get $S(a) \to M(a)$ and $M(a) \to P(a)$, hence $S(a) \to P(a)$, and we generalize.
7. Validity with a [[Venn diagram|0KCT6DPXJK]]: "all $M$ are $P$" shades the regions $SM\bar P$ and $\bar S M \bar P$, and "all $S$ are $M$" shades $S \bar M P$ and $S \bar M \bar P$.
   The conclusion needs $SM\bar P$ and $S\bar M \bar P$ to be empty, and both are shaded.

Step 5 never assumes that $S$, $M$ or $P$ has an element, so the argument is valid in the traditional and in the modern reading.

## Remarks

Barbara is the transitivity of the [[subset|0BJR9QR08E]] relation, written in words.
Change one piece and the result changes.
Weaken the conclusion to "some squares are parallelograms" and you get Barbari (AAI-1), which is valid only when $S$ is not empty; here it is, since the unit square exists.
Make the middle term the predicate of both premises, as in "all squares are parallelograms, all rectangles are parallelograms, so all rectangles are squares", and you get the invalid [[fallacy of the undistributed middle|F8BP8S0RYG]].

The conclusion cannot be turned around.
"All parallelograms are squares" is false: the parallelogram with vertices $(0, 0)$, $(2, 0)$, $(3, 1)$ and $(1, 1)$ has no right angle.
The same figure shows that "all parallelograms are rectangles" is false, so swapping the terms of a premise can turn a true premise into a false one.

## Explanations

### L1 human

Barbara is the simplest correct chain of "all" sentences.
If every square is a rectangle, and every rectangle is a parallelogram, then every square is a parallelogram.
In pictures, the circle of squares lies inside the circle of rectangles, which lies inside the circle of parallelograms.
So the circle of squares lies inside the circle of parallelograms.

### L2 human

We check the side vectors of the parallelogram used above, to be sure it has no right angle.

1. The sides from $(0, 0)$ go to $(2, 0)$ and to $(1, 1)$, so the side vectors are $u = (2, 0)$ and $v = (1, 1)$.
2. The opposite sides are $(3, 1) - (1, 1) = (2, 0)$ and $(3, 1) - (2, 0) = (1, 1)$, so the figure is a parallelogram.
3. The dot product is $u \cdot v = 2 \cdot 1 + 0 \cdot 1 = 2 \neq 0$, so the angle at $(0, 0)$ is not a right angle.
4. So the figure is a parallelogram and not a rectangle, and so not a square.

One such figure refutes both converses at once.
The trap is to think that Barbara with a true conclusion also gives the converse; it gives inclusion in one direction only.
