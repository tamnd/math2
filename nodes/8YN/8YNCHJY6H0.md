---
tag: 8YNCHJY6H0
kind: example
name: Euclid's first construction ends with Q.E.F.
msc: ["00A35", "51M15"]
topics: [Z2WNQ1DNTX]
audience: school
instance_of: [ET9J6R9T5C]
uses: [060W5CBZP6, 0DAECMZVRT, 83WHDAV68J, ET9J6R9T5C]
sources:
  - url: https://en.wikipedia.org/wiki/Q.E.D.
    locator: Difference from Q.E.F.
---

## Example

Proposition 1 of Book I of [[Euclid's Elements|83WHDAV68J]] is a [[construction|0DAECMZVRT]]: on a given segment, construct an equilateral triangle.
Euclid ends it with the Greek phrase that the Latin `Q.E.F.`, *quod erat faciendum*, "which was to be done", translates.
We follow the construction and check why its [[end mark|ET9J6R9T5C]] is `Q.E.F.`.

1. Let $AB$ be the given segment.
2. Draw the [[circle|060W5CBZP6]] with center $A$ through $B$, and the circle with center $B$ through $A$.
3. Let $C$ be a point where the two circles meet.
4. Since $C$ is on the first circle, $AC = AB$.
   Since $C$ is on the second circle, $BC = BA$.
5. So $AC = AB = BC$, and the triangle $ABC$ is equilateral.
   Which was to be done.

Check with coordinates: for $A = (0, 0)$ and $B = (2, 0)$ the circles meet at $C = (1, \sqrt{3})$, and
$$AC = \sqrt{1 + 3} = 2, \qquad BC = \sqrt{1 + 3} = 2, \qquad AB = 2.$$

The proposition asks for an object, and the last step produces it, so the end mark is `Q.E.F.` and not `Q.E.D.`.

## Remarks

Proposition 4 of Book I states that two triangles with two equal sides and an equal included angle are congruent.
It is a theorem, not a construction, so it ends with "which was to be shown", the source of `Q.E.D.`.

Step 3 has a gap: no postulate of Euclid says that the two circles meet.
Later axiom systems for geometry add a continuity axiom that closes this gap.
So the end mark did not make the argument complete, and this is the main lesson about every end mark.

Step 4 is a small proof inside the construction.
A construction must also show that the object has the required property, so `Q.E.F.` closes both the making and the checking.

## Explanations

### L1 human

Euclid shows how to draw a triangle with three equal sides on a given segment.
He draws two circles and joins the point where they cross to the ends of the segment.
At the end he writes "which was to be done", because he made something.
At the end of a proof that something is true, he writes "which was to be shown".

### L2 human

To choose between `Q.E.D.` and `Q.E.F.`, read the task in the statement.
If the statement says "show that" or "prove that", the result is a theorem, and the end mark is `Q.E.D.`.
If the statement says "construct" or "find", the result is a construction, and the end mark is `Q.E.F.`.
Proposition I.1 says "construct", so it ends with `Q.E.F.`, while Proposition I.4 says that two triangles are congruent, so it ends with `Q.E.D.`.
Modern texts seldom keep the distinction and end constructions and proofs with the same square.
