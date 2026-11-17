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
The points $A$ and $B$ lie on the first line, on opposite sides of $E$.
The points $C$ and $D$ lie on the second line, on opposite sides of $E$.
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

1. Row 1 repeats the given facts. Every later row depends on it.
2. Row 2: the ray $EC$ splits the straight angle $\angle AEB$ into $\angle AEC$ and $\angle CEB$. A straight angle measures $180^\circ$, so the two parts add up to $180^\circ$.
3. Row 3: the ray $EB$ splits the straight angle $\angle CED$ into $\angle CEB$ and $\angle BED$, in the same way.
4. Row 4: two quantities equal to $180^\circ$ are equal to each other.
5. Row 5: subtracting the same number from equal numbers gives equal numbers.
6. Row 5 is the "Prove" statement, so the proof is complete.

A numerical check: if $\angle AEC = 40^\circ$, then row 2 gives $\angle CEB = 140^\circ$, and row 3 gives $\angle BED = 180^\circ - 140^\circ = 40^\circ$.

## Remarks

1. The example shows the basic shape of a [[two-column proof|P8PCGFASP8]]. The givens come first, each row has one fact and one reason, and the goal is the last row.
2. The same table proves $\angle CEB = \angle AED$, with $\angle AEC$ as the common angle in place of $\angle CEB$.
3. As a paragraph proof the argument has two sentences. "The angles $\angle AEC$ and $\angle BED$ are both supplementary to $\angle CEB$, because each pair lies on a straight line. So they are equal."
4. As a flow chart the argument has two boxes for rows 2 and 3 side by side. Both have arrows into the box for row 4. The flow chart shows that rows 2 and 3 do not depend on each other.

## Explanations

### L1 human

When two straight roads cross, they make four corners.
The corners opposite each other have the same size.
The proof uses one fact: two angles that together make a straight line add up to $180^\circ$.
For example, if one corner is $40^\circ$, its neighbour is $140^\circ$, and the opposite corner is again $180^\circ - 140^\circ = 40^\circ$.
The table writes each of these facts in a row, with its reason next to it.

### L2 human

We write the same table for the other pair of vertical angles, $\angle CEB$ and $\angle AED$.

1. Row 1: the given facts, as before.
2. Row 2: $\angle CEB + \angle AEC = 180^\circ$, because $EA$ and $EB$ are opposite rays.
3. Row 3: $\angle AEC + \angle AED = 180^\circ$, because $EC$ and $ED$ are opposite rays.
4. Row 4: $\angle CEB + \angle AEC = \angle AEC + \angle AED$, from rows 2 and 3.
5. Row 5: $\angle CEB = \angle AED$, by subtracting $\angle AEC$.

The typical use of this pattern is to prove that two angles are equal because they have the same supplement.
A trap is to write row 5 directly after row 1 with the reason "vertical angles".
That reason is the theorem itself, so the proof would be circular.
