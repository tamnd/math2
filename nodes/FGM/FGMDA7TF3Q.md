---
tag: FGMDA7TF3Q
kind: example
name: The diagonal of a rectangular box by the four steps
msc: ["00A35", "51M04"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [DYD57G2Y5Z]
uses: [DYD57G2Y5Z, 0VP3A1290K]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Four phases
  - book: isbn:9780691164076
---

## Example

A rectangular box has edges of lengths $a$, $b$ and $c$.
We want the length $d$ of a diagonal, the segment from one corner to the opposite corner.
This is the first example in Pólya's *How to Solve It*, and we follow [[Pólya's four steps|DYD57G2Y5Z]].

In phase 1 we understand the problem.
The unknown is the length $d$ of the segment from a corner $A$ to the opposite corner $G$.
The data are the lengths $a$, $b$ and $c$ of the three edges at $A$.
The condition is that the box has right angles at every corner, and that $G$ shares no face with $A$.
We draw the base $ABCD$ with $AB = a$ and $BC = b$, and the top $EFGH$ above it with $CG = c$.

In phase 2 we devise a plan.
We ask for a solved problem with the same kind of unknown, and the diagonal of a rectangle comes to mind.
By the [[Pythagorean theorem|0VP3A1290K]], a rectangle with sides $a$ and $b$ has diagonal $\sqrt{a^2 + b^2}$.
To use that result, we need a right triangle that has the unknown $AG$ as a side.
The triangle $ACG$ is a candidate, since $AC$ is a diagonal of the base and $CG$ is a vertical edge.

In phase 3 we carry out the plan.

1. In the rectangle $ABCD$, the Pythagorean theorem gives $AC^2 = a^2 + b^2$.
2. The edge $CG$ is perpendicular to the base, so it is perpendicular to every line in the base through $C$, and in particular to $AC$.
   So the angle $ACG$ is a right angle.
3. In the right triangle $ACG$, the Pythagorean theorem gives
   $$AG^2 = AC^2 + CG^2 = a^2 + b^2 + c^2.$$
4. So $d = \sqrt{a^2 + b^2 + c^2}$.

In phase 4 we look back.
The formula is symmetric in $a$, $b$ and $c$, as it must be, because the three edges at $A$ play the same role.
For $c = 0$ the box is flat, and the formula gives $\sqrt{a^2 + b^2}$, the diagonal of the rectangle.
If $a$, $b$ and $c$ are in meters, then $\sqrt{a^2 + b^2 + c^2}$ is in meters too.
For $a = 3$, $b = 4$ and $c = 12$, the base diagonal is $5$ and $d = \sqrt{25 + 144} = 13$.
The same method gives the distance between two points $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ in space.

## Remarks

The example shows how phase 2 works.
The question "do you know a problem with the same unknown?" brought up the diagonal of a rectangle, and that problem gave the plan.
The segment $AC$ is an [[auxiliary element|8TKKRAXKFN]]: it is not in the problem, and it connects the problem with the known one.
Phase 4 then found three independent checks and a new use of the result.

For a box in $n$ dimensions with edges $a_1, \dots, a_n$, the same plan, used $n - 1$ times, gives $d = \sqrt{a_1^2 + \dots + a_n^2}$.

## Explanations

### L1 human

Think of a shoe box and the longest straight stick that fits inside, from one bottom corner to the opposite top corner.
First find the diagonal of the bottom with the rule for right triangles.
For a box of $3$ by $4$, the bottom diagonal is $5$.
The stick, the bottom diagonal and the height $12$ then form another right triangle.
So the stick has length $13$, since $5^2 + 12^2 = 169 = 13^2$.

### L2 human

We use the result of phase 4 on a new problem: the distance from $P = (1, 2, 3)$ to $Q = (4, 6, 15)$.
The segment $PQ$ is the diagonal of a box whose edges are parallel to the axes.
The edges have lengths $|4 - 1| = 3$, $|6 - 2| = 4$ and $|15 - 3| = 12$, so
$$PQ = \sqrt{9 + 16 + 144} = 13.$$
A solved problem has become a method for a whole family of problems, which is what phase 4 is for.
Watch out: in phase 3 the right angle at $C$ needs its reason, because a drawing in perspective can make the angle $ACG$ look acute or obtuse.
