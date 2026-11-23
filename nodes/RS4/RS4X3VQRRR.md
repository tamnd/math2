---
tag: RS4X3VQRRR
kind: example
name: A two-column proof that vertical angles are equal
msc: ["00A35", "97G40", "51M04"]
topics: [STSM6PR7TX]
audience: school
instance_of: [P8PCGFASP8]
uses: [P8PCGFASP8, 0GJAJC6TNZ, 0MP9BCF6DP]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Two-column proof
---

## Example

Two [[lines|0MP9BCF6DP]] meet at a point $E$.
The points $A$ and $B$ lie on the first line, on opposite sides of $E$, and the points $C$ and $D$ lie on the second line, on opposite sides of $E$.
The [[angles|0GJAJC6TNZ]] $\angle AEC$ and $\angle BED$ are called vertical angles, because their sides are opposite rays.

Given: the lines $AB$ and $CD$ meet at $E$, with $E$ between $A$ and $B$ and between $C$ and $D$.

Prove: $\angle AEC = \angle BED$.

| # | Statements | Reasons |
|---|---|---|
| 1 | $E$ lies between $A$ and $B$, and between $C$ and $D$ | given |
| 2 | $\angle AEC + \angle CEB = 180^\circ$ | angles on a straight line: $EA$ and $EB$ are opposite rays (1) |
| 3 | $\angle CEB + \angle BED = 180^\circ$ | angles on a straight line: $EC$ and $ED$ are opposite rays (1) |
| 4 | $\angle AEC + \angle CEB = \angle CEB + \angle BED$ | rows 2 and 3 have the same right side |
| 5 | $\angle AEC = \angle BED$ | subtract $\angle CEB$ from both sides of row 4 |

We check each row.
Row 1 repeats the given facts, and every later row depends on it.
In row 2 the ray $EC$ splits the straight angle $\angle AEB$ into $\angle AEC$ and $\angle CEB$, and a straight angle measures $180^\circ$.
Row 3 is the same fact for the straight angle $\angle CED$, split by the ray $EB$.
Row 4 holds because two quantities equal to $180^\circ$ are equal to each other, and row 5 subtracts the same number from both sides.
Row 5 is the "Prove" line, so the [[two-column proof|P8PCGFASP8]] is complete.

A numerical check: if $\angle AEC = 40^\circ$, then row 2 gives $\angle CEB = 140^\circ$, and row 3 gives $\angle BED = 180^\circ - 140^\circ = 40^\circ$.

## Remarks

The table shows the basic shape of the format: the givens come first, each row has one fact and one reason, and the goal is the last row.

As a paragraph proof the argument takes two sentences.

> The angles $\angle AEC$ and $\angle BED$ are both supplementary to $\angle CEB$, because each pair lies along a straight line.
> So they are equal.

As a flow chart, the boxes for rows 2 and 3 sit side by side, with arrows into the box for row 4.
The flow chart shows what the table hides: rows 2 and 3 do not depend on each other.

## Explanations

### L1 human

When two straight roads cross, they make four corners.
The corners opposite each other have the same size.
The proof uses one fact: two angles that together make a straight line add up to $180^\circ$.
For example, if one corner is $40^\circ$, the corner next to it is $140^\circ$, and the opposite corner is again $180^\circ - 140^\circ = 40^\circ$.
The table writes each of these facts in a row, with its reason next to it.

### L2 human

We write the table for the other pair of vertical angles, $\angle CEB$ and $\angle AED$.
This time the common angle is $\angle AEC$.

| # | Statements | Reasons |
|---|---|---|
| 1 | $E$ lies between $A$ and $B$, and between $C$ and $D$ | given |
| 2 | $\angle CEB + \angle AEC = 180^\circ$ | $EA$ and $EB$ are opposite rays (1) |
| 3 | $\angle AEC + \angle AED = 180^\circ$ | $EC$ and $ED$ are opposite rays (1) |
| 4 | $\angle CEB + \angle AEC = \angle AEC + \angle AED$ | rows 2 and 3 |
| 5 | $\angle CEB = \angle AED$ | subtract $\angle AEC$ from both sides of row 4 |

The pattern proves that two angles are equal because they have the same supplement.
Watch out: writing row 5 right after row 1 with the reason "vertical angles are equal" cites the theorem being proved, so the proof would be circular.
