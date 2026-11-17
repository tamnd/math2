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

1. Let $AB$ be the given segment.
2. Draw the [[circle|060W5CBZP6]] with center $A$ through $B$, and the circle with center $B$ through $A$.
3. Let $C$ be a point where the two circles meet.
4. Since $C$ is on the first circle, $AC = AB$. Since $C$ is on the second circle, $BC = BA$.
5. So $AC = AB = BC$, and the triangle $ABC$ is equilateral. Which was to be done.

The proposition asks for an object, and the last step produces it, so the end mark is `Q.E.F.`, not `Q.E.D.`.

## Remarks

Proposition 4 of Book I states that two triangles with two equal sides and an equal included angle are congruent.
It is a theorem, not a construction, so it ends with the phrase "which was to be shown", the source of `Q.E.D.`.
Step 3 has a gap: no postulate of Euclid says that the two circles meet.
Later axiom systems for geometry add a continuity axiom that closes this gap.
The gap shows again that an end mark does not make a proof complete.

## Explanations

### L1 human

Euclid shows how to draw a triangle with three equal sides on a given segment.
He draws two circles and joins the point where they cross to the ends of the segment.
At the end he writes "which was to be done", because he made something.
At the end of a proof that something is true, he writes "which was to be shown".

### L2 human

To choose between `Q.E.D.` and `Q.E.F.`, read the task in the statement.

1. If the statement says "show that" or "prove that", the result is a theorem, and the end mark is `Q.E.D.`.
2. If the statement says "construct" or "find", the result is a construction, and the end mark is `Q.E.F.`.
3. Proposition I.1 says "construct", so it ends with `Q.E.F.`.

The typical use of `Q.E.F.` today is rare, and most modern texts end constructions and proofs with the same square.
A trap: a construction also needs a proof that the object has the required property, as step 4 gives here.
