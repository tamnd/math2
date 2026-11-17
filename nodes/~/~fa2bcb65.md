---
tag: ~fa2bcb65
kind: concept
name: Two-column proof
aliases: [two-column-proof, statements-and-reasons]
msc: ["00A35", "97E50", "97G40"]
topics: [STSM6PR7TX]
audience: school
uses: [0B94TKFQJX, ~7e59ebb2, 0NTF6DMVAP, KRZD96GSVC]
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

A two-column proof is a [[proof|0B94TKFQJX]] written as a table with two columns.
The left column, headed "Statements", lists the steps, one assertion in each row.
The right column, headed "Reasons", gives for each statement its justification.
A reason is "given" (a hypothesis), a definition, a postulate, an earlier theorem, or a rule applied to rows with stated numbers.
The first rows state the given facts, and the last row states the fact to be proved.
The format matters because school geometry in the United States often teaches proof with it.
It also makes the demand "one reason for each step" visible.

## Motivation

Students who write their first proofs often write true facts without reasons, or reasons without the facts that they support.
The two-column format separates the two parts of each step.
A row with an empty "Reasons" cell is a visible gap, and a teacher can check each row on its own.
The format grew out of school geometry, where proofs are short chains of facts about a figure.
There each fact follows from a postulate or an earlier theorem of [[Euclidean geometry|KRZD96GSVC]].

## Notation

1. A two-column proof starts with two lines: "Given:" with the hypotheses, and "Prove:" with the conclusion. A labelled figure usually comes with them.
2. The rows are numbered, and a reason can cite earlier rows by number, as in "SAS (1, 3, 4)".
3. School books use short names for reasons, for example "def. of midpoint" and "reflexive property". Other names are "SAS" for side-angle-side and "CPCTC" for "corresponding parts of congruent triangles are congruent".
4. In a table the headings are "Statements" and "Reasons". Some books write "Steps" and "Justifications".

## Remarks

### When it applies

The format fits short direct arguments in which each step uses one or two earlier facts.
School geometry is the main case, with statements about equal segments, equal angles and [[congruent triangles|093EDENVA1]].
School algebra also uses it to solve an equation step by step, with the properties of equality as reasons.
The format is awkward for a long proof, for a proof with several cases, and for a proof by contradiction.
The reason is that a flat table has no place for an assumption that is later dropped.

### The steps

1. Write the "Given" and the "Prove" lines, and draw a labelled figure.
2. Fill the first rows with the given facts. Each such row has the reason "given".
3. Add one row for each new fact. The reason must be a definition, a postulate, a theorem, or a rule applied to earlier rows.
4. Cite the earlier rows by number when the reason combines them.
5. End with the row that states the "Prove" line exactly.
6. Check each reason: it must be true, and it must apply to the rows that it cites.

### Paragraph proofs and flow-chart proofs

A paragraph proof gives the same steps in sentences, with the reason inside each sentence.
An example is "Since $AB = AC$ is given and $AD = AD$, the triangles are congruent by SAS."
A paragraph proof is the form that mathematicians use, and the page [[writing proofs|~7e59ebb2]] treats it.
A flow-chart proof writes each statement in a box and its reason under the box.
An arrow goes from each box to the boxes that use it.
A flow chart shows which steps depend on which, so it shows parallel lines of argument that a table puts one after another.
The three formats can contain the same steps and the same reasons.

### Examples

1. [[A two-column proof that vertical angles are equal|~0cb91f79]]: five rows, with "angles on a straight line" as the main reason.
2. [[A two-column proof of the isosceles triangle theorem|~58d380cc]]: the bisector of the top angle and side-angle-side congruence give equal base angles.
3. A proof in school algebra of "if $3x + 5 = 11$, then $x = 2$". The rows are $3x + 5 = 11$ (given) and $3x = 6$ (subtract $5$ from both sides of row 1). The last row is $x = 2$ (divide both sides of row 2 by $3$).
4. A proof that the angles of a triangle add up to $180^\circ$. It draws the line through one vertex parallel to the opposite side, then uses alternate angles and a straight angle. The rows follow the proof of the [[angle sum of a triangle|05MDKQBEAF]].

### Non-examples

1. [[A two-column proof with "from the diagram" as a reason|~6bdd522a]]. One reason is not a definition, a postulate or a theorem. So the table is not a two-column proof, even if every statement is true.
2. A paragraph proof is a proof, but it is not a two-column proof: its steps are sentences, not rows of a table.
3. A structured proof in the sense of Lamport is not a two-column proof. It has levels of steps, and each step has its own sub-proof, as the page [[structured and hierarchical proofs|~a051973d]] explains. A two-column proof is one flat list.

### Arguments for and against the format

For the format:

1. Each step must have a reason, and a missing reason is visible.
2. The format separates what is claimed from why it holds.
3. A teacher can check and grade each row on its own.

Against the format:

1. Students can learn to fill the table without a plan, and the plan of the proof does not appear in it.
2. The format is far from the proofs in books and papers, which are written in paragraphs.
3. Cases, assumptions that are later dropped, and claims inside a proof have no natural place in a flat table.
4. Simple arguments become long, because each small fact needs its own row.

A course can use the format for the first proofs and then move to paragraph proofs.

### Basic properties

1. Each row follows from the rows above it and from the facts named in its reason. So a correct two-column proof is a [[direct proof|0NTF6DMVAP]] of the implication from the "Given" to the "Prove".
2. Each two-column proof can be rewritten as a paragraph proof with one sentence for each row, and back.
3. The citations of earlier rows define a graph of dependencies. This graph is the flow-chart proof of the same argument.
4. An indirect proof needs an extra row such as "assume that $\angle A \ne \angle B$", with the reason "assumption for an indirect proof". Its final row contradicts a given fact.

### History

Two-column proofs appear in American school geometry in the early twentieth century, and a printed example from 1913 survives.
In 2002 Patricio Herbst traced how the format became a custom of American school geometry in that period.
Today the format is still a common exercise in elementary geometry classes in the United States.

### Common errors

1. A reason restates the statement, as in "$AB = CD$ because the segments are equal". A reason must be a definition, a postulate, a theorem or a given fact.
2. A reason is "from the figure" or "it looks equal". A figure can suggest a fact, but it does not prove it.
3. A row cites the "Prove" statement or a later row. Then the argument is circular.
4. A student lists the "Prove" statement among the given facts at the start.

## Explanations

### L1 human

A two-column proof is a table with "Statements" on the left and "Reasons" on the right.
Each row says one fact and why it is true.
For example, row 1 can say "$AB = AC$" with the reason "given".
Row 2 can say "$AD = AD$" with the reason "a segment is equal to itself".
The last row is the fact that the problem asked us to prove.
The table is a checklist: if every reason is correct, the proof is correct.

### L2 human

We prove "if $M$ is the midpoint of the segment $AB$ and $AB = 10$, then $AM = 5$".

| # | Statements | Reasons |
|---|---|---|
| 1 | $M$ is the midpoint of $AB$, and $AB = 10$ | given |
| 2 | $AM = MB$ | definition of [[midpoint|0S706JBZBG]] (1) |
| 3 | $AM + MB = AB$ | $M$ lies on the segment $AB$ (1), segment addition |
| 4 | $AM + AM = 10$ | substitution of rows 1 and 2 into row 3 |
| 5 | $AM = 5$ | divide both sides of row 4 by $2$ |

1. Row 2 uses only the definition of the midpoint.
2. Row 3 uses that $M$ lies between $A$ and $B$, which is also part of the definition.
3. Row 4 replaces $MB$ by $AM$ and $AB$ by $10$.
4. Row 5 solves the equation $2 \cdot AM = 10$.

The typical use of the format is in a first geometry course, to learn that each fact in a proof needs a reason.
A trap is to give the reason "definition of midpoint" in row 3 as well, without saying that $M$ lies on the segment.
The equation $AM + MB = AB$ fails for a point $M$ off the segment.

### L3 human

The two-column format is close to the line-numbered formats of [[natural deduction|6KT3BJZ7D1]].
In the Suppes-Lemmon notation each line has a number, a formula, a rule and the numbers of the lines that the rule uses.
This is a two-column proof with more columns.
Fitch notation adds indentation for assumptions, and this is exactly what a school two-column proof lacks.
A structured proof in the sense of Leslie Lamport is a different format.
It is a tree of steps, each step with its own sub-proof, while a two-column proof is a flat list.
The page [[structured and hierarchical proofs|~a051973d]] describes this format.
The flow-chart form shows the dependencies as a directed acyclic graph, and a proof assistant stores a proof as such a graph of terms.
In mathematics education the format is a topic of debate, and the page [[teaching reasoning and proof|VHGA6J4NZK]] treats the research on it.
