---
tag: P8PCGFASP8
kind: concept
name: Two-column proof
aliases: [two-column-proof, statements-and-reasons]
msc: ["00A35", "97E50", "97G40"]
topics: [STSM6PR7TX]
audience: school
uses: [0B94TKFQJX, 8JQHJK94RZ, 0NTF6DMVAP, KRZD96GSVC]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Two-column proof
  - doi: 10.1023/A:1020264906740
    locator: pages 283-312
  - url: https://en.wikipedia.org/wiki/Flowchart
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: Notation
---

## Summary

A two-column proof writes each step of a [[proof|0B94TKFQJX]] as a row of a table: the statement on the left, and its reason on the right.
Here is the school fact that vertical angles are equal, first as a table and then as a paragraph.

Two lines meet at $E$, with $A$ and $B$ on one line and $C$ and $D$ on the other, and $E$ between each pair.
The goal is $\angle AEC = \angle BED$.

| # | Statements | Reasons |
|---|---|---|
| 1 | $E$ lies between $A$ and $B$, and between $C$ and $D$ | given |
| 2 | $\angle AEC + \angle CEB = 180^\circ$ | angles on a straight line (1) |
| 3 | $\angle CEB + \angle BED = 180^\circ$ | angles on a straight line (1) |
| 4 | $\angle AEC + \angle CEB = \angle CEB + \angle BED$ | rows 2 and 3 |
| 5 | $\angle AEC = \angle BED$ | subtract $\angle CEB$ from both sides of row 4 |

The same argument as a paragraph reads as follows.

> Since $A$, $E$ and $B$ lie on a line, $\angle AEC + \angle CEB = 180^\circ$.
> In the same way, $C$, $E$ and $D$ lie on a line, so $\angle CEB + \angle BED = 180^\circ$.
> Both angles $\angle AEC$ and $\angle BED$ are therefore $180^\circ - \angle CEB$, and so they are equal.
> $\square$

The two forms hold the same steps and the same reasons.
The table puts every reason in its own cell, so a missing reason shows as an empty cell, while the paragraph puts the reasons inside sentences and is the form used in books and papers.

## Motivation

Students who write their first proofs often write true facts without reasons, or reasons without the facts they support.
The two-column format separates the two parts of each step, and a teacher can check each row on its own.
The format grew up in school geometry, where proofs are short chains of facts about a figure, and each fact follows from a postulate or an earlier theorem of [[Euclidean geometry|KRZD96GSVC]].

## Notation

A two-column proof starts with a "Given" line for the hypotheses and a "Prove" line for the conclusion, usually next to a labeled figure.
The rows are numbered, and a reason cites earlier rows by number, as in "SAS (1, 3, 4)".
School books use short names for common reasons, such as "def. of midpoint", "reflexive property", "SAS" for side-angle-side, and "CPCTC" for "corresponding parts of congruent triangles are congruent".
Some books head the columns "Steps" and "Justifications" instead of "Statements" and "Reasons".

## Remarks

### Writing one

Start with the "Given" and "Prove" lines and a labeled figure.
The first rows repeat the given facts, each with the reason "given".
Each later row states one new fact, and its reason is a definition, a postulate, a theorem, or a rule applied to rows named by number.
The last row states the "Prove" line exactly.
Then read the reasons once more and ask of each one whether it is true and whether it applies to the rows it cites.

The format fits short direct arguments in which each step uses one or two earlier facts.
Statements about equal segments, equal angles and [[congruent triangles|093EDENVA1]] are the main case, and school algebra uses the same table to solve an equation, with the properties of equality as reasons.

### Worked tables

[[The vertical angles table|RS4X3VQRRR]] is the table above, with a check of each row and a numerical test.
[[The isosceles triangle theorem|3HHNT9HRXX]] needs an auxiliary object, the bisector of the top angle.
The row that introduces it must give a reason why the bisector exists, just as a "let" in a paragraph proof needs one when it claims existence.

[[A table with "from the diagram" as a reason|PP4787SRH9]] shows the most common failure.
Every statement in it is true, but one reason is a look at the figure, and the table never uses the hypothesis $AB = AC$.
So the same table would "prove" the claim for every triangle, and the claim is false for some.

### Paragraphs and flow charts

A paragraph proof gives the same steps in sentences, with each reason inside its sentence, as [[writing proofs|8JQHJK94RZ]] describes.
A flow-chart proof writes each statement in a box, with its reason under the box, and draws an arrow from each box to the boxes that use it.
In the vertical angles proof, the boxes for rows 2 and 3 sit side by side, both pointing into row 4.
A flow chart shows which steps depend on which, while a table lists independent steps one after another.

### Where the format breaks down

A flat table has no place for an assumption that is later dropped.
Cases, proofs by contradiction and claims with their own proofs need such assumptions, so they fit badly.
An indirect proof in a table needs a row such as "assume that $\angle A \ne \angle B$" with the reason "assumption for an indirect proof", and the reader must remember that every later row depends on it.

[[A two-column proof is not a structured proof|GD8FT1XAQ9]] shows the problem on a proof by cases.
The rows "$n = 2k$" and "$n = 2k + 1$" stand side by side, and read as one flat list they contradict each other.
A [[structured proof|H2W8D7BMSW]] puts each case in its own sub-proof, so the case assumption and the letter $k$ end with it.

### For and against

Teachers who favor the format point out that every step must have a reason, that what is claimed stays apart from why it holds, and that each row can be graded on its own.
Critics answer that students can learn to fill the table without a plan, that the format is far from the paragraph proofs of later courses, and that small facts each take their own row, so simple arguments grow long.
Both sides have a point, and a common compromise uses the table for the first proofs and moves to paragraphs once students give reasons by habit.
Research on the question is collected under [[teaching reasoning and proof|VHGA6J4NZK]].

### Watch out

A reason that restates the statement, as in "$AB = CD$ because the segments are equal", is no reason.
A reason must be a given fact, a definition, a postulate or a theorem.

"Vertical angles are equal" is a correct reason in most later proofs, but not in the proof of that theorem, where it makes the table circular.
The same holds for any row that cites the "Prove" line or a later row.

Two-column proofs and structured proofs are different formats, even though both number their steps.
A two-column proof is one flat list, and a structured proof is a tree of steps, each with its own sub-proof.

### History

Two-column proofs appear in American school geometry books of the early twentieth century, and a printed example from 1913 is often reproduced.
Patricio Herbst traced in 2002 how the format became a custom of American school geometry in that period.
It remains a common exercise in geometry classes in the United States.

### Try it

Write a two-column proof that if $3x + 5 = 11$, then $x = 2$.
One answer has three rows: $3x + 5 = 11$ (given), $3x = 6$ (subtract $5$ from both sides of row 1), and $x = 2$ (divide both sides of row 2 by $3$).

Which hypothesis does the table never use if a row says "$\angle AMB = \angle AMC$, from the diagram" in a proof that the median of an isosceles triangle is perpendicular to the base?
It never uses $AB = AC$, which is the sign that the reason hides a gap.

## Explanations

### L1 human

A two-column proof is a table with "Statements" on the left and "Reasons" on the right.
Each row says one fact and why it is true.
For example, row 1 can say "$AB = AC$" with the reason "given", and row 2 can say "$AD = AD$" with the reason "a segment is equal to itself".
The last row is the fact that the problem asked us to prove.
If every reason is correct, the proof is correct.

### L2 human

We prove that if $M$ is the [[midpoint|0S706JBZBG]] of the segment $AB$ and $AB = 10$, then $AM = 5$.

| # | Statements | Reasons |
|---|---|---|
| 1 | $M$ is the midpoint of $AB$, and $AB = 10$ | given |
| 2 | $AM = MB$ | definition of midpoint (1) |
| 3 | $AM + MB = AB$ | $M$ lies on the segment $AB$ (1), segment addition |
| 4 | $AM + AM = 10$ | substitute rows 1 and 2 into row 3 |
| 5 | $AM = 5$ | divide both sides of row 4 by $2$ |

Row 2 uses only the equal halves in the definition of the midpoint, and row 3 uses that $M$ lies between $A$ and $B$, which is also part of the definition.
Row 4 replaces $MB$ by $AM$ and $AB$ by $10$, and row 5 solves $2 \cdot AM = 10$.
Watch out: the equation $AM + MB = AB$ fails for a point $M$ off the segment, so row 3 needs its reason.

### L3 human

The two-column format is close to the line-numbered formats of [[natural deduction|6KT3BJZ7D1]].
In the Suppes-Lemmon notation each line carries a number, a formula, a rule, and the numbers of the lines that the rule uses, which is a two-column proof with more columns.
Fitch notation adds indentation for assumptions, and indentation is exactly what the school format lacks.
A Lamport [[structured proof|H2W8D7BMSW]] goes further and makes the proof a tree, with each step proved by its own sub-proof.

The citations of earlier rows define a dependency graph, and the flow-chart proof draws that graph.
It is a directed acyclic graph, since a row may cite only rows above it.
Every correct table is a [[direct proof|0NTF6DMVAP]] of the implication from the "Given" line to the "Prove" line, and it can be rewritten as a paragraph with one sentence per row.
