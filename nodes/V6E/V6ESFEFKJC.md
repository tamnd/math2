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

Look at this square of numbers, in which each cell carries the number of the L-shaped layer that it belongs to:
$$\begin{array}{cccc} 1 & 2 & 3 & 4 \\ 2 & 2 & 3 & 4 \\ 3 & 3 & 3 & 4 \\ 4 & 4 & 4 & 4 \end{array}$$
Count the cells of each label: there is one $1$, three $2$s, five $3$s and seven $4$s, and together they fill a $4 \times 4$ square.
So $1 + 3 + 5 + 7 = 16 = 4^2$, and you can see that the next layer around a $4 \times 4$ square would add $9$ cells and make a $5 \times 5$ square.

A proof without words is a picture of this kind: a figure, or a short sequence of figures, that shows why a statement is true with little or no text.
The statement behind the square above is exact:
$$1 + 3 + 5 + \dots + (2n - 1) = n^2 \quad \text{for every integer } n \ge 1.$$
The picture shows only the case $n = 4$.
It does not show the general $n$, and it does not show that layer $k$ always has $2k - 1$ cells; a reader who wants a [[proof|0B94TKFQJX]] must supply that rule, by a counting argument or by [[induction|0ASJVEFA9J]].
That gap between what the eye sees and what the statement claims is the whole subject of the idea.

## Motivation

The identity for odd numbers has a short [[proof by induction|QSWRESJAZ4]].
That proof checks the identity, but it does not tell you why squares appear.
The layered square does: each odd number is the border that turns one square into the next.
Many identities about sums, areas and inequalities have such a picture, and mathematicians collect them because they are easy to remember and to teach.

A picture also raises a real question about [[rigor|E1PE9R8DBB]].
If a reader can check a figure in a few seconds, is that a proof, or only a strong hint?
The answer depends on whether the reader can state the rule that makes the figure work for every case, and on whether every fact that the eye reads off is true.
The same question returns, in another form, for proofs that no human can see in full, such as [[computer-assisted proofs|MC18C7BMFT]].

## Notation

There is no special notation.
The names "visual proof", "proof by picture" and "wordless proof" mean the same thing.
The phrase "proof without words" is also the title of a regular feature in *Mathematics Magazine* and in *The College Mathematics Journal*, and of a series of collections by Roger Nelsen.
Most such pictures do carry a line of text: the identity that they show.

## Remarks

### Reading the square as a proof

To turn the layered square into a proof for every $n$, give each cell of an $n \times n$ square the position $(i, j)$, and put it in layer $\max(i, j)$.
Each cell is in exactly one layer, so the layers fill the square with no overlap.
Layer $k$ holds the $k$ cells of row $k$ up to the diagonal and the $k - 1$ cells of column $k$ above it, so it has $2k - 1$ cells.
Counting the $n^2$ cells by layers gives the identity.
The full check, with the case $n = 3$ worked cell by cell, is in [[the sum of the first n odd numbers as a picture|EE2Y5SNFME]].

So the picture becomes a proof once you can say the rule "layer $k$ has $2k - 1$ cells" and give its reason.
Most pictures of sums work this way: they count one set of cells in two ways, which is [[double counting|0F8YBHF2W3]], or they match two sets, which is a [[bijective proof|SS07J9ZAQ7]].

### Three more pictures

Two copies of a staircase of $1 + 2 + \dots + n$ cells, one turned by $180$ degrees, fit together into an $n \times (n + 1)$ rectangle.
So twice the [[triangular number|WHN4CBYZXD]] $T_n$ is $n(n + 1)$, and $T_n = \frac{n(n+1)}{2}$.
For $n = 4$ this gives $1 + 2 + 3 + 4 = 10 = \frac{4 \cdot 5}{2}$.

[[The rearrangement picture|T6WDA860PA]] puts four copies of a right triangle with legs $a$ and $b$ inside a square of side $a + b$ in two ways.
The uncovered area is $c^2$ in the first way and $a^2 + b^2$ in the second, which gives the [[Pythagorean theorem|0VP3A1290K]].

[[Nicomachus's theorem as a picture|1WR6FN0NTE]] cuts a square of side $1 + 2 + \dots + n$ into L-shaped layers of area $1^3, 2^3, \dots, n^3$.
For $n = 4$ the square has side $10$ and area $100 = 1 + 8 + 27 + 64$.

### When a picture misleads

[[The staircase picture|5WP0CV0866]] draws zigzag paths of length $2$ that come closer and closer to the diagonal of a unit square.
Every drawn staircase is correct, but the eye adds a limit and concludes that the diagonal has length $2$, which would make $\sqrt{2} = 2$.
The failing step is the limit: length does not pass to the limit of curves that only approach each other.

A protractor drawing of one triangle with angles that add up to $180$ degrees fails in a different way.
It shows one case, and a measurement is only approximate, so it checks neither the general statement nor the exact value.
A picture of $1 + 3 + 5 + 7 = 16$ with no rule for the next layer fails a third way: it is a correct check of the case $n = 4$ and nothing more.

### Is a picture a proof?

There are three common positions.
On the first, a picture is never a proof, because it leaves out the logical steps; it suggests a proof and helps you remember one.
On the second, some pictures are proofs in their own right.
The philosopher James Robert Brown defended this view in "Proofs and pictures" (1997), and Janet Folina replied against it.
On the third, the answer depends on the reader, in the same way as rigor does.
A reader who can state the general rule of the picture and give a reason for each visible fact has a proof, and a reader who only sees a pattern has a [[conjecture|WMEMMHZ3BH]].

All three positions agree on one point: each fact that the eye reads from a figure is a mathematical claim, and it needs a reason.
"These two regions have the same area" needs congruence, and "this corner is a right angle" needs a computation.
The pages on [[formal and informal proofs|8VZ77R4R8S]] and on the [[acceptance of proofs|MJ3EHQJJHX]] continue the question.

### History

Arguments with figures are as old as Greek geometry, and every proposition of [[Euclid's Elements|83WHDAV68J]] comes with one.
Nicomachus of Gerasa, who lived about 60 to 120 CE, described in his *Introduction to Arithmetic* the grouping of odd numbers behind [[Nicomachus's theorem|23WBA59VWP]].
Roger Nelsen gathered many modern pictures in the collections *Proofs without Words* I to III.
The question of what a diagram may prove got a precise form in 2009, when Jeremy Avigad, Edward Dean and John Mumma gave a formal system, called E, for the use of diagrams in the *Elements*.

### Watch out

The first trap is to take a picture of one case for a proof of all cases.
The figure for $n = 4$ shows $1 + 3 + 5 + 7 = 16$, and the general claim needs the rule for layer $k$.
The second trap is to trust the eye about lengths and angles.
A figure drawn slightly wrong can hide a gap or an overlap, as the dissection puzzles in [[fallacies and errors in proofs|T6QQ749DM5]] show.
The third trap is to pass to a limit inside a picture, as the staircase does.
Before you accept a limit, check that the quantity you measure behaves well under it.

### Try it

First, draw the staircase picture for $n = 5$ and read off $T_5$.
Two staircases of $15$ cells fill a $5 \times 6$ rectangle of $30$ cells, so $T_5 = 15$.

Second, in the layered $n \times n$ square, why does layer $k$ have $2k - 1$ cells and not $2k$?
Row $k$ and column $k$ share the corner cell $(k, k)$, so adding $k$ and $k$ counts that cell twice.

Third, which statement does the layered square for $n = 6$ check?
It checks $1 + 3 + 5 + 7 + 9 + 11 = 36$, one case of the identity and not the identity itself.

## Explanations

### L1 human

Put one coin on a table.
Put $3$ coins around it to make a $2 \times 2$ square, then $5$ more along two sides to make a $3 \times 3$ square.
Each time you add the next odd number of coins, you get the next square.
So $1 + 3 + 5 + 7$ is the number of coins in a $4 \times 4$ square, which is $16$.
The picture tells you why the rule works: each odd number is the border that grows one square into the next.
It does not by itself tell you that the border always has the next odd number of coins, and that is the one thing you must check in words.

### L2 human

We read the staircase picture for the [[triangular numbers|WHN4CBYZXD]] as a proof of $T_n = \frac{n(n + 1)}{2}$ for every $n \ge 1$.
Draw a staircase in which row $i$ has $i$ cells, for $i = 1, \dots, n$, all starting at the left edge, so the staircase has $T_n$ cells.
Turn a second copy by $180$ degrees and place it on the right; its row $i$ has $n + 1 - i$ cells.
Row $i$ of the combined figure therefore has
$$i + (n + 1 - i) = n + 1$$
cells, so the two copies fill an $n \times (n + 1)$ rectangle with no gap and no overlap.
Counting the rectangle two ways gives
$$2 T_n = n(n + 1).$$
Check: for $n = 4$, $1 + 2 + 3 + 4 = 10$ and $\frac{4 \cdot 5}{2} = 10$.

The step that the eye does is "the rows fit", and the formula $i + (n + 1 - i) = n + 1$ is that step written for every $n$.
This is the typical use of a picture: it gives the idea, and one line of algebra turns the idea into a proof.
The trap is to skip that line because the figure looks like a rectangle.

### L3 human

Proofs without words belong to the study of diagrammatic reasoning.
Euclid read facts such as "this point lies between those two" from his figures, and [[Hilbert's axioms|KM1FB8XZ2R]] added axioms of order so that these readings became stated principles.
The system E of Avigad, Dean and Mumma goes the other way: it lists exactly which inferences a diagram allows, so that a diagram can be part of a precise proof.

Many pictures of sums are [[combinatorial proofs|SS07J9ZAQ7]] in disguise, and many pictures of areas rest on facts of Euclidean geometry that fail in [[non-Euclidean geometry|SPCYMFN5V2]].
The [[tiling of a deficient board by L-trominoes|EXRJ0JF2Q3]] shows a third kind: a single figure that draws the step of an induction.
The question of what a picture proves is a special case of the questions of [[rigor|E1PE9R8DBB]] and of [[acceptance|MJ3EHQJJHX]], and it returns for proofs that nobody can see in full, such as [[long proofs|RM0S65BHWH]].
