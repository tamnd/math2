---
tag: ~e4be5eed
kind: example
name: The diagonal of a rectangular box by the four steps
msc: ["00A35", "51M04"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [~e58f9baf]
uses: [~e58f9baf, 0VP3A1290K]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Four phases
  - book: isbn:9780691164076
---

## Example

Problem: a rectangular box has edges of lengths $a$, $b$ and $c$.
Find the length $d$ of a diagonal of the box, the segment from one corner to the opposite corner.
This is the first example of Pólya's *How to Solve It*, and we solve it with [[Pólya's four steps|~e58f9baf]].

Phase 1: understand the problem.

1. The unknown is the length $d$ of the segment from a corner $A$ to the opposite corner $G$.
2. The data are the lengths $a$, $b$, $c$ of the three edges at $A$.
3. The condition: the box has right angles at every corner, and $G$ is the corner that shares no face with $A$.
4. We draw a figure, with the base $ABCD$, where $AB = a$ and $BC = b$, and the top $EFGH$ above it, where $CG = c$.

Phase 2: devise a plan.

1. A related problem with the same kind of unknown: the diagonal of a rectangle. By the [[Pythagorean theorem|0VP3A1290K]], a rectangle with sides $a$ and $b$ has diagonal $\sqrt{a^2 + b^2}$.
2. To use it, we need a right triangle with the unknown $AG$ as a side.
3. The triangle $ACG$ is a candidate: $AC$ is a diagonal of the base, and $CG$ is a vertical edge.

Phase 3: carry out the plan.

1. In the rectangle $ABCD$, the Pythagorean theorem gives $AC^2 = a^2 + b^2$.
2. The edge $CG$ is perpendicular to the base, so it is perpendicular to every line of the base through $C$, in particular to $AC$. So the angle $ACG$ is a right angle.
3. In the right triangle $ACG$, the Pythagorean theorem gives $AG^2 = AC^2 + CG^2 = a^2 + b^2 + c^2$.
4. So $d = \sqrt{a^2 + b^2 + c^2}$.

Phase 4: look back.

1. Symmetry: the formula is symmetric in $a$, $b$, $c$, as it must be, because the three edges at $A$ play the same role.
2. Special case: for $c = 0$ the box is flat, and the formula gives $\sqrt{a^2 + b^2}$, the diagonal of the rectangle.
3. Units: if $a$, $b$, $c$ are in metres, then $\sqrt{a^2 + b^2 + c^2}$ is in metres.
4. A numerical check: for $a = 3$, $b = 4$, $c = 12$ the base diagonal is $5$, and $d = \sqrt{25 + 144} = 13$.
5. Use for another problem: the same method gives the distance between the points $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ in space.

## Remarks

The example shows how phase 2 works: the solver asks for a solved problem with the same unknown, and the answer, the diagonal of a rectangle, gives the plan.
The auxiliary segment $AC$ is the new element that connects the problem with the known one.
Phase 4 found three independent checks and a new use of the result.

For a box in $n$ dimensions with edges $a_1, \ldots, a_n$, the same steps, repeated $n - 1$ times, give $d = \sqrt{a_1^2 + \cdots + a_n^2}$.

## Explanations

### L1 human

Think of a shoe box, and the longest straight stick that fits inside it, from one bottom corner to the opposite top corner.
First we measure the diagonal of the bottom, with the rule for right triangles.
For a box of $3$ by $4$, the bottom diagonal is $5$.
Then the stick, the bottom diagonal and the height $12$ form another right triangle.
So the stick has length $13$, since $5^2 + 12^2 = 169 = 13^2$.

### L2 human

We use the result of phase 4, item 5, on a new problem: the distance from $P = (1, 2, 3)$ to $Q = (4, 6, 15)$.

1. The segment $PQ$ is the diagonal of a box with edges parallel to the axes.
2. The edges have lengths $|4 - 1| = 3$, $|6 - 2| = 4$ and $|15 - 3| = 12$.
3. So $PQ = \sqrt{9 + 16 + 144} = 13$.

The typical use: a solved problem becomes a method for a family of problems.

A trap: in phase 3, step 2, the right angle at $C$ needs a reason; a figure in perspective can make the angle $ACG$ look acute or obtuse.
