---
tag: MJ5S28Y5WV
kind: example
name: A four-point geometry
msc: ["00A35", "51A05"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [GD2JBXJV5Z]
uses: [GD2JBXJV5Z, CSXT0BG2CM, MCDZP31ZF3, MVCH6N9SNW, VM8TQ70CVJ, QKCAEG2Y0E]
sources:
  - url: https://en.wikipedia.org/wiki/Axiomatic_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Finite_geometry
    locator: lead section
---

## Example

A tiny [[axiom system|GD2JBXJV5Z]] of [[incidence geometry|CSXT0BG2CM]] shows every part of the method in one place: a theorem, a proof of consistency and proofs of independence.
The primitive terms are "point", "line" and the relation "the point $P$ lies on the line $L$".
There are three axioms.

- A1: there are exactly four points.
- A2: for each two distinct points, there is exactly one line on which both lie.
- A3: on each line there lie exactly two points.

Theorem: there are exactly $6$ lines.

1. To each line $L$ we attach the set of points that lie on $L$.
   By A3 this set has exactly two points.
2. Different lines get different sets.
   If $L \neq L'$ both had the set $\{P, Q\}$, then $P$ and $Q$ would lie on two lines, and A2 forbids this.
3. Every set $\{P, Q\}$ of two distinct points is the set of some line.
   By A2 some line $L$ contains $P$ and $Q$, and by A3 it contains no other point.
4. So lines correspond one to one to pairs of points, and by A1 the number of pairs is
   $$\binom{4}{2} = \frac{4 \cdot 3}{2} = 6.$$

Consistency: the axioms have a [[model|MVCH6N9SNW]].

5. Take the points $1, 2, 3, 4$ and the six lines $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{2,3\}$, $\{2,4\}$, $\{3,4\}$, where a point lies on a line when it is an element of it.
6. A1 holds, since there are four points.
   A2 holds, since distinct points $i$ and $j$ lie on the line $\{i, j\}$ and on no other line of the list.
   A3 holds, since each line of the list has two elements.
7. So the system is [[consistent|VM8TQ70CVJ]].
   If the axioms proved both a statement and its negation, both would be true in this model, which is impossible.

Independence: no axiom follows from the other two.

8. A1 is independent.
   Take the points $1, 2, 3$ and the lines $\{1,2\}$, $\{1,3\}$, $\{2,3\}$.
   A2 and A3 hold by the checks of step 6, but there are only three points.
9. A3 is independent.
   Take the points $1, 2, 3, 4$ and the single line $\{1, 2, 3, 4\}$.
   A1 holds, and A2 holds because any two points lie on the one line and there is no other line, but the line has four points.
10. A2 is independent.
    Take the points $1, 2, 3, 4$ and no lines at all.
    A1 holds, and A3 holds because there is no line on which it could fail, but the points $1$ and $2$ lie on no common line.
11. In each of steps 8 to 10, two axioms are true and the third is false in a model.
    If the third followed from the other two, it would be true there too.
    So it is [[independent|QKCAEG2Y0E]] of them.

## Remarks

The model of step 5 is the complete graph on four vertices, read as a geometry: vertices are points and edges are lines.
The theorem counts its $6$ edges, and it is true in every model of A1 to A3, not only in this one.
If A1 says "exactly $n$ points" for some $n \geq 2$, the same proof gives exactly $\binom{n}{2} = n(n-1)/2$ lines.

Step 10 shows a point that students often miss.
A statement of the form "each line has a property" is true when there are no lines at all, so A3 holds in the empty model.
This small system is a [[finite geometry|MCDZP31ZF3]], and the same method of models shows that the [[parallel postulate|2PC3XY0PYZ]] is independent of the other axioms of plane geometry.

## Explanations

### L1 human

Imagine four towns and some roads.
The rules say: there are four towns, each two towns have exactly one road between them, and each road joins exactly two towns.
From the rules alone we can count the roads, because each road matches one pair of towns and four towns make six pairs.
To show that the rules do not contradict each other, we draw a picture that obeys them: four dots with all six connecting segments.
To show that a rule is really needed, we draw a picture that obeys the other two rules and breaks this one.

### L2 human

Here is a typical test: can we add a fourth axiom, A4, saying that each two distinct lines share a point?

1. Let $P$, $Q$, $R$ and $S$ be the four points given by A1.
2. By steps 2 and 3 of the theorem, there is a line $L$ whose points are $P$ and $Q$, and a line $L'$ whose points are $R$ and $S$.
3. These lines are distinct, because their sets of points differ, and they share no point.
4. So "some two distinct lines share no point" is a theorem of A1 to A3, and A1 to A4 together prove a statement and its negation.

The system A1 to A4 is therefore inconsistent, and it has no model.
A proof tells you what holds in every model, and a model tells you what does not follow.
Watch out: a single model in which a statement is true does not prove the statement.
It shows only that the statement is consistent with the axioms, and a proof must work in every model.
