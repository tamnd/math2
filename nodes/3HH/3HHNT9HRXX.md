---
tag: 3HHNT9HRXX
kind: example
name: A two-column proof of the isosceles triangle theorem
msc: ["00A35", "97G40", "51M04"]
topics: [STSM6PR7TX]
audience: school
instance_of: [P8PCGFASP8]
uses: [P8PCGFASP8, 056VS31A0J, 5NEJPXA6N4, 093EDENVA1]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Two-column proof
  - url: https://en.wikipedia.org/wiki/Isosceles_triangle
    locator: lead section
---

## Example

We prove the [[isosceles triangle theorem|056VS31A0J]] in the [[two-column format|P8PCGFASP8]].

Given: a triangle $ABC$ with $AB = AC$.

Prove: $\angle ABC = \angle ACB$.

| # | Statements | Reasons |
|---|---|---|
| 1 | $AB = AC$ | given |
| 2 | the bisector of $\angle BAC$ meets the side $BC$ at a point $D$ | every angle has a bisector, and a ray inside $\angle BAC$ meets $BC$ |
| 3 | $\angle BAD = \angle CAD$ | definition of an angle bisector (2) |
| 4 | $AD = AD$ | a segment is equal to itself (reflexive property) |
| 5 | triangle $ABD$ is congruent to triangle $ACD$, with $A \mapsto A$, $B \mapsto C$, $D \mapsto D$ | side-angle-side (1, 3, 4) |
| 6 | $\angle ABD = \angle ACD$ | corresponding parts of congruent triangles are equal (5) |
| 7 | $\angle ABC = \angle ACB$ | $D$ lies on the segment $BC$ (2), so $\angle ABD = \angle ABC$ and $\angle ACD = \angle ACB$; then row 6 |

Row 2 brings in a new point $D$, and its reason says why such a point exists, so the row is not an assumption.
Row 5 applies side-angle-side from the [[congruence criteria for triangles|5NEJPXA6N4]].
The two sides are $AB$ and $AD$ in one triangle and $AC$ and $AD$ in the other, and the angles between them are $\angle BAD$ and $\angle CAD$, which rows 1, 3 and 4 give in the right order.
Row 6 uses the definition of [[congruent triangles|093EDENVA1]]: under the correspondence of row 5, the angle at $B$ matches the angle at $C$.
Row 7 only renames the angles, since the ray $BD$ is the ray $BC$ and the ray $CD$ is the ray $CB$.

## Remarks

The proof introduces an auxiliary object, the bisector $AD$.
The row that introduces it needs a reason for its existence, like a "let" in a paragraph proof that claims an object exists.

The congruence in row 5 gives more than the theorem.
It gives $BD = CD$, so $D$ is the midpoint of $BC$, and it gives $\angle ADB = \angle ADC$.
These two angles add up to $180^\circ$, so each is $90^\circ$, and $AD$ is perpendicular to $BC$.

Without the hypothesis $AB = AC$, row 5 fails.
For $A = (1, 3)$, $B = (0, 0)$ and $C = (4, 0)$ we get $AB = \sqrt{10}$ and $AC = \sqrt{18}$, and the base angles differ, since $\tan \angle ABC = 3$ and $\tan \angle ACB = 1$.

Euclid's proof in Book I, Proposition 5 of the Elements does not use an angle bisector.
The proof by the bisector is shorter, but it needs the existence of the bisector first.

## Explanations

### L1 human

A triangle with two equal sides is called isosceles.
The theorem says that the two angles at the bottom of such a triangle are equal.
The proof cuts the top angle in half with a line.
This line splits the triangle into two halves that fit on top of each other exactly.
So the two bottom angles, one in each half, are equal, and the table lists each of these facts with its reason.

### L2 human

We test the rows on the triangle $A = (0, 4)$, $B = (-3, 0)$ and $C = (3, 0)$.
Row 1 holds, since $AB = \sqrt{3^2 + 4^2} = 5$ and $AC = 5$.
By the symmetry $x \mapsto -x$, the bisector of the angle at $A$ is the line $x = 0$, so row 2 gives $D = (0, 0)$.
The triangles $ABD$ and $ACD$ both have sides $5$, $4$ and $3$, so rows 4 and 5 hold.
Finally $\tan \angle ABC = \frac{4}{3} = \tan \angle ACB$, so the base angles are equal, as rows 6 and 7 say.

The bisector is there to make two triangles that share a side, so that a congruence criterion applies.
Watch out: with the midpoint $D$ of $BC$ instead of the bisector, the claim $\angle BAD = \angle CAD$ cannot come "from the figure".
The correct criterion is then side-side-side, with $AB = AC$, $BD = CD$ and $AD = AD$.
