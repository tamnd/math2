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

We prove the [[isosceles triangle theorem|056VS31A0J]] in the two-column format.

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

We check each row.

1. Row 2 introduces a new point $D$. The reason states why such a point exists, so the row is not an assumption.
2. Row 5 applies side-angle-side from the [[congruence criteria for triangles|5NEJPXA6N4]]. The two sides are $AB$ and $AD$ in the first triangle and $AC$ and $AD$ in the second. The angles between them are $\angle BAD$ and $\angle CAD$.
3. Rows 1, 3 and 4 give exactly these three equal parts, in the right order, so the criterion applies.
4. Row 6 uses the definition of [[congruent triangles|093EDENVA1]]. Under the correspondence of row 5, the angle at $B$ in triangle $ABD$ matches the angle at $C$ in triangle $ACD$.
5. Row 7 changes the names of the angles. The ray $BD$ is the ray $BC$, because $D$ lies between $B$ and $C$. In the same way the ray $CD$ is the ray $CB$.
6. Row 7 is the "Prove" statement.

## Remarks

1. The example shows a two-column proof that introduces an auxiliary object, the bisector $AD$. The row that introduces it needs a reason for its existence, like a "let" in a paragraph proof.
2. The argument also shows that $D$ is the midpoint of $BC$, because row 5 gives $BD = CD$. It also shows that $AD$ is perpendicular to $BC$, because $\angle ADB = \angle ADC$ and these two angles add up to $180^\circ$.
3. Without the hypothesis $AB = AC$, row 5 fails. For the triangle with $A = (1, 3)$, $B = (0, 0)$, $C = (4, 0)$ we get $AB = \sqrt{10}$ and $AC = \sqrt{18}$, and the base angles are different: $\tan \angle ABC = 3$ and $\tan \angle ACB = 1$.
4. A flow chart of the proof has three boxes for rows 1, 3 and 4 side by side. Arrows lead from them into the box for row 5. Row 2 points into row 3, because the bisector must exist before its angles are compared.
5. Euclid's proof of the same theorem in Book I, Proposition 5 of the Elements does not use an angle bisector. The proof by the bisector is shorter, but it needs the existence of the bisector first.

## Explanations

### L1 human

A triangle with two equal sides is called isosceles.
The theorem says that the two angles at the bottom of such a triangle are equal.
The proof cuts the top angle in half with a line.
This line splits the triangle into two halves that fit on top of each other exactly.
So the two bottom angles, one in each half, are equal.
The table lists each of these facts with its reason.

### L2 human

We test the rows on the triangle $A = (0, 4)$, $B = (-3, 0)$, $C = (3, 0)$.

1. Row 1: $AB = \sqrt{3^2 + 4^2} = 5$ and $AC = \sqrt{3^2 + 4^2} = 5$.
2. Row 2: the bisector of the angle at $A$ is the line $x = 0$, by the symmetry $x \mapsto -x$ of the triangle. It meets $BC$ at $D = (0, 0)$.
3. Row 4 and row 5: the triangles $ABD$ and $ACD$ have sides $5$, $4$, $3$, so they are congruent.
4. Rows 6 and 7: $\tan \angle ABC = \frac{4}{3}$ and $\tan \angle ACB = \frac{4}{3}$, so the base angles are equal.

The typical use of the bisector in this proof is to make two triangles that share a side, so that a congruence criterion applies.
A trap is to use the midpoint $D$ of $BC$ and to claim $\angle BAD = \angle CAD$ "from the figure".
With the midpoint, the correct criterion is side-side-side, with $AB = AC$, $BD = CD$ and $AD = AD$.
