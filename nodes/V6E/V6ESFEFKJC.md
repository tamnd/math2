---
tag: V6ESFEFKJC
kind: concept
name: Proof without words
aliases: [graphical-proof, proofs-without-words, visual-proof, wordless-proof]
msc: ["00A35", "97E50"]
topics: [1BTHSHST4M]
audience: school
uses: [0B94TKFQJX]
sources:
  - wikipedia: en:18045517@r1330717914
    locator: Proof without words
    note: adopted
    mention: wikipedia://en/18045517
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Proof_without_words
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Staircase_paradox
    locator: Explanation
same_as:
  wikidata: Q3402800
  wikipedia: Proof without words
inventory: [38RD4477HG]
---

## Summary

A proof without words is a picture, or a short sequence of pictures, that shows why a mathematical statement is true with little or no text.
The picture usually shows one case of a general statement, and it counts as an argument only when the reader can see that the same construction works in every case.
The reader must supply the words: what each part of the picture stands for, and why each visible fact holds.
Proofs without words matter because they show the idea of a [[proof|0B94TKFQJX]] at a glance, and because they raise the question whether a picture can be a proof.

## Motivation

The identity $1 + 3 + 5 + \cdots + (2n - 1) = n^2$ has a short proof by [[mathematical induction|0ASJVEFA9J]], as [[this example|QSWRESJAZ4]] shows.
The induction proof checks the identity, but it does not say why squares appear.
A square of $n \times n$ dots, cut into $n$ L-shaped layers of $1, 3, 5, \ldots$ dots, shows the reason at once.
Many identities about sums, areas and inequalities have such a picture.
The picture is easy to remember and easy to teach, so mathematicians collect and publish such pictures.
This leads to two questions: how to read a picture as an argument, and when a picture is enough.

## Remarks

### Examples

- [[The sum of the first n odd numbers as a picture|EE2Y5SNFME]]: an $n \times n$ square splits into L-shaped layers of $1, 3, \ldots, 2n - 1$ cells. The picture is a proof because the layer rule is the same for each $n$.
- [[The rearrangement picture for the Pythagorean theorem|T6WDA860PA]]: four copies of a right triangle fill a square of side $a + b$ in two ways. The uncovered area is $c^2$ in one way and $a^2 + b^2$ in the other.
- [[Nicomachus's theorem as a picture|1WR6FN0NTE]]: a square of side $1 + 2 + \cdots + n$ splits into layers of area $1^3, 2^3, \ldots, n^3$. Each layer can be checked with one line of algebra.
- Two copies of a staircase of $1 + 2 + \cdots + n$ cells fit together into an $n \times (n + 1)$ rectangle. So twice the [[triangular number|WHN4CBYZXD]] $T_n$ is $n(n + 1)$.
- The picture of the [[tiling of a deficient board by L-trominoes|EXRJ0JF2Q3]] shows the induction step: one tromino at the centre and four smaller boards. The picture is a proof by induction drawn in one figure.

### Non-examples

- [[The staircase picture does not prove that the square root of 2 is 2|5WP0CV0866]]: each staircase in the picture is drawn correctly, but the passage to the limit is not visible, and it is false. The condition that fails is that each step that the picture suggests must be valid.
- A drawing of one triangle with angles measured by a protractor is not a proof that the angles of every triangle add up to $180°$. The drawing shows one case, and a measurement is only approximate.
- A picture of $1 + 3 + 5 + 7 = 16$ alone, with no visible rule for the next layer, checks the case $n = 4$ only. The condition that fails is that the construction must work for each $n$.

### Basic properties

- A picture shows one case. It proves a general statement only when the construction depends on the parameter in a way that the reader can state, for example "layer $k$ has $2k - 1$ cells".
- Each visible fact in a picture is a mathematical claim. For example, "these two regions have the same area" is a claim that needs a reason, such as congruence.
- When we write out these claims, the picture becomes a written proof. The written proof often counts the same quantity in two ways, as in [[double counting|0F8YBHF2W3]].
- A picture can hide a limit. Areas and lengths of figures that approach a limit figure need not approach the area or length of the limit figure, as the [[staircase|5WP0CV0866]] shows.
- A picture uses facts of geometry, such as the area of a rectangle and the invariance of area under a rigid motion. These facts hold in Euclidean geometry and can fail in [[non-Euclidean geometry|SPCYMFN5V2]].

### When a picture is a proof

Mathematicians and philosophers give three answers.
The first answer is that a picture is not a proof, because it leaves out the logical details.
On this view the picture is a guide that suggests a proof and helps a reader to remember it.
The second answer is that some pictures are proofs.
The philosopher James Robert Brown defended this view in the article "Proofs and pictures" (1997), and the philosopher Janet Folina replied against it.
The third answer is that the question depends on the reader, in the same way as [[mathematical rigour|E1PE9R8DBB]] does.
A reader who can state the general rule of the picture and justify each visible fact has a proof, and a reader who only sees a pattern has a conjecture.
All three answers agree that a picture can be wrong, and that each visible fact needs a reason.
The pages on [[formal and informal proofs|8VZ77R4R8S]] and on the [[acceptance of proofs|MJ3EHQJJHX]] continue this question.

### History

Arguments with figures are as old as Greek geometry, and each proposition of [[Euclid's Elements|83WHDAV68J]] comes with a figure.
Nicomachus of Gerasa, who lived about 60 to 120 CE, described the pattern behind [[Nicomachus's theorem|23WBA59VWP]] in his *Introduction to Arithmetic*.
The journals *Mathematics Magazine* and *The College Mathematics Journal* publish a regular feature with the title "Proof without words".
Roger Nelsen collected many of these pictures in a series of books with the title *Proofs without Words*.

### Common errors

- To take a picture of one case as a proof of all cases. The reader must check that the construction is the same for each value of the parameter.
- To trust the eye about lengths and angles. A figure drawn slightly wrong can hide a gap or an overlap, as the topic [[fallacies and errors in proofs|T6QQ749DM5]] shows.
- To pass to a limit in a picture without checking that the quantity behaves well under the limit. Length is not preserved under such limits, as the [[staircase|5WP0CV0866]] shows.

## Explanations

### L1 human

A proof without words is a drawing that shows why a fact is true.
Take $1 + 3 + 5 = 9$.
Draw a $3 \times 3$ square of dots.
The dot in the corner is $1$, the next L-shaped band has $3$ dots, and the outer band has $5$ dots.
So the three odd numbers fill a square, and their sum is $3 \times 3 = 9$.
The same drawing works for a $4 \times 4$ square, a $5 \times 5$ square, and every larger square.
That is why the drawing shows that the first $n$ odd numbers always add up to $n \times n$.

### L2 human

We read the staircase picture for the [[triangular numbers|WHN4CBYZXD]] as a proof.
The claim is $T_n = 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ for each integer $n \ge 1$.

1. Draw a staircase of unit cells: row $i$ has $i$ cells, for $i = 1, \ldots, n$, all starting at the left edge. The staircase has $T_n$ cells.
2. Make a second copy, turn it by $180°$, and place it on the right of the first copy. Row $i$ of the second copy has $n + 1 - i$ cells.
3. Row $i$ of the combined figure has $i + (n + 1 - i) = n + 1$ cells, so the two copies fill an $n \times (n + 1)$ rectangle with no gap and no overlap.
4. The rectangle has $n(n + 1)$ cells, and it has $2 T_n$ cells by step 2.
5. So $2 T_n = n(n + 1)$, and $T_n = \frac{n(n + 1)}{2}$.
6. Check for $n = 4$: $1 + 2 + 3 + 4 = 10$ and $\frac{4 \cdot 5}{2} = 10$.

The typical use of a picture is to find the idea of a proof and to explain it.
Step 3 is the step that the eye does, and the formula $i + (n + 1 - i) = n + 1$ is its written form.
A trap is to skip step 3: the picture looks like a rectangle, but the proof needs the reason why the rows fit for each $n$.

### L3 human

Proofs without words belong to the study of diagrammatic reasoning.
Euclid's proofs read facts such as "this point lies between those two points" from the figure, and [[Hilbert's axioms|KM1FB8XZ2R]] added axioms of order to replace these readings by stated principles.
Jeremy Avigad, Edward Dean and John Mumma later gave a formal system, called E, that models the use of diagrams in the *Elements* (2009).
So a diagram can be part of a precise proof when the inferences that it allows are listed.
Many pictures for sums are [[combinatorial proofs|SS07J9ZAQ7]] in disguise: they count one set of cells in two ways.
The question of the status of pictures is a special case of the questions of [[rigour|E1PE9R8DBB]] and of [[acceptance|MJ3EHQJJHX]], and it returns for proofs that no human can see in full, such as [[computer-assisted proofs|MC18C7BMFT]].
