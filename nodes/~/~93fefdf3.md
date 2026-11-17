---
tag: ~93fefdf3
kind: example
name: A four-point geometry
msc: ["00A35", "51A05"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [~fde3e74a]
uses: [~fde3e74a, CSXT0BG2CM, MCDZP31ZF3, MVCH6N9SNW, VM8TQ70CVJ, QKCAEG2Y0E]
sources:
  - url: https://en.wikipedia.org/wiki/Axiomatic_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Finite_geometry
    locator: lead section
---

## Example

We study a small [[axiom system|~fde3e74a]] of [[incidence geometry|CSXT0BG2CM]].
The primitive terms are "point", "line" and the relation "the point $P$ lies on the line $L$".
The axioms are these three statements.

- A1. There are exactly four points.
- A2. For each two distinct points, there is exactly one line on which both points lie.
- A3. On each line there lie exactly two points.

We prove a theorem from the axioms, and then we check consistency and independence with [[models|MVCH6N9SNW]].

Theorem: there are exactly $6$ lines.

1. To each line $L$ we assign the set of points that lie on $L$. By A3, this set has exactly two points.
2. Two different lines get different sets. If $L \neq L'$ both had the set $\{P, Q\}$, then $P$ and $Q$ would lie on two lines, and A2 forbids this.
3. Each set $\{P, Q\}$ of two distinct points is assigned to some line. By A2, some line $L$ contains $P$ and $Q$. By A3, $L$ contains no other point, so its set is $\{P, Q\}$.
4. By steps 1 to 3, the lines correspond one to one to the sets of two points.
5. By A1 there are four points, and the number of sets of two points from four points is $\binom{4}{2} = \frac{4 \cdot 3}{2} = 6$.
6. So there are exactly $6$ lines.

Consistency: the axioms have a model.

7. Take the points $1, 2, 3, 4$ and the six lines $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{2,3\}$, $\{2,4\}$, $\{3,4\}$. A point lies on a line when it is an element of it.
8. A1 holds, because there are four points.
9. A2 holds, because two distinct points $i$ and $j$ lie on the line $\{i, j\}$ and on no other line of the list.
10. A3 holds, because each line of the list has two elements.
11. Thus the system is [[consistent|VM8TQ70CVJ]]: a statement and its negation cannot both follow from A1 to A3, since both would be true in this model.

Independence: no axiom follows from the other two.

12. A1 is independent of A2 and A3. Take the points $1, 2, 3$ and the lines $\{1,2\}$, $\{1,3\}$, $\{2,3\}$. A2 and A3 hold by the checks of steps 9 and 10, but there are three points, so A1 fails.
13. A3 is independent of A1 and A2. Take the points $1, 2, 3, 4$ and one line $\{1, 2, 3, 4\}$. A1 holds. A2 holds, because two distinct points lie on the one line and there is no other line. A3 fails, because the line has four points.
14. A2 is independent of A1 and A3. Take the points $1, 2, 3, 4$ and no lines at all. A1 holds. A3 holds, because there is no line for which it could fail. A2 fails, because the points $1$ and $2$ lie on no line.
15. In each of steps 12 to 14, two axioms are true and the third is false in a model. If the third axiom followed from the other two, it would be true in the model. So it does not follow, and it is [[independent|QKCAEG2Y0E]].

## Remarks

The model of step 7 is the complete graph on four vertices, read as a geometry: vertices are points and edges are lines.
The theorem of step 6 is true in every model of A1 to A3, and in this model it counts the $6$ edges of the complete graph.
If A1 says "exactly $n$ points" for some $n \geq 2$, the same proof gives exactly $\binom{n}{2} = n(n-1)/2$ lines.
Step 14 shows a point that students often miss: a statement of the form "each line has a property" is true when there are no lines.
This small system is a [[finite geometry|MCDZP31ZF3]], and the same method of models shows the independence of the [[parallel postulate|2PC3XY0PYZ]] in plane geometry.

## Explanations

### L1 human

Imagine four towns, and roads between them.
The rules say: there are four towns, each two towns have exactly one road between them, and each road joins exactly two towns.
From the rules alone we can count the roads: each road matches one pair of towns, and four towns make six pairs.
To show that the rules do not contradict each other, we draw a picture that obeys them: four dots with all six connecting segments.
To show that a rule is really needed, we draw a picture that obeys the other two rules and breaks this one.

### L2 human

We test a fourth candidate axiom against the system.

- A4. Each two distinct lines share a point.

1. Let $P$, $Q$, $R$ and $S$ be the four points, which exist by A1.
2. By steps 2 and 3 of the theorem, there is a line $L$ whose points are $P$ and $Q$, and a line $L'$ whose points are $R$ and $S$.
3. The lines $L$ and $L'$ are distinct, and they share no point.
4. So "some two distinct lines share no point" is a theorem of A1 to A3.
5. Hence the system A1 to A4 is inconsistent, and it has no model.

The typical use of the theorem and the models together is this: a proof shows what holds in every model, and a model shows what does not follow.
A trap is to think that a model in which a statement is true proves the statement.
One model shows only that the statement is consistent with the axioms; a proof must work in every model.
