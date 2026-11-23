---
tag: S4BTTGFR6J
kind: concept
name: Syllogistic figures
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [MZBNX2T6Q6, KSJ9W29KXQ]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#5IWO
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Term_logic
    locator: lead section
inventory: [FSEAFB6ZAV]
---

## Summary

The figure of a syllogism records where the middle term stands in the two premises, as subject or as predicate, and there are four possible arrangements.
It matters because the same three kinds of sentence can make a valid argument in one figure and an invalid one in another.

Compare two arguments built from three "all" sentences.
"All rectangles are parallelograms, all squares are rectangles, so all squares are parallelograms" is valid; the middle term "rectangles" is the subject of the first premise and the predicate of the second.
"All squares are parallelograms, all rectangles are parallelograms, so all rectangles are squares" is invalid; the middle term "parallelograms" is the predicate of both premises.

In exact terms, the major term $P$ is the predicate of the conclusion and the minor term $S$ is its subject.
Standard order lists the major premise (the one containing $P$), then the minor premise (the one containing $S$), then the conclusion $(S, P)$.
Write each proposition as the pair (subject, predicate).
The figure is the first, second, third or fourth according as the premises are $(M, P), (S, M)$, or $(P, M), (S, M)$, or $(M, P), (M, S)$, or $(P, M), (M, S)$, where $M$ is the middle term.
The figure together with the [[mood|1TD6HRM5NG]] fixes the form of the syllogism.

## Motivation

The words "all", "no", "some" and "not" alone do not decide whether an argument is valid.
The two arguments in the summary have the same letters, AAA, and differ only in the place of the middle term.
To list the valid [[syllogisms|MZBNX2T6Q6]], you sort them by the kinds of their three propositions and by this place, and the figures are the second half of the sorting.
The figures also organize the proofs: Aristotle proved the moods of the other figures by turning them into first-figure moods.

## Notation

Each premise is written as the pair (subject, predicate), the major premise first; the conclusion is always $(S, P)$.

| Figure | Major premise | Minor premise | Place of $M$ |
|---|---|---|---|
| 1 | $(M, P)$ | $(S, M)$ | subject, then predicate |
| 2 | $(P, M)$ | $(S, M)$ | predicate in both |
| 3 | $(M, P)$ | $(M, S)$ | subject in both |
| 4 | $(P, M)$ | $(M, S)$ | predicate, then subject |

A syllogism is named by mood and figure, for example AAA-1 for Barbara and AEE-2 for Camestres.
Some authors list the minor premise first, which swaps the descriptions of the first and fourth figures, so check the convention of each book.

## Remarks

### One example in each figure

In the first figure, [[Barbara|AC6XQ4KRNT]] reads "all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$".
In the second figure, Camestres reads "all $P$ are $M$, no $S$ is $M$, so no $S$ is $P$".
With $P$ the squares, $M$ the rectangles and $S$ the triangles, it proves that no triangle is a square, and [[its reduction to Celarent|TKW0RRHV88]] shows how it is proved.
In the third figure, Disamis reads "some $M$ are $P$, all $M$ are $S$, so some $S$ are $P$".
With $M$ the primes, $P$ the odd numbers and $S$ the integers greater than $1$, it proves that some integers greater than $1$ are odd.
Also in the third figure, [[Darapti|ARGGZ9N2SV]] reads "all $M$ are $P$, all $M$ are $S$, so some $S$ are $P$", and it is valid only when $M$ is not empty.
In the fourth figure, [[Dimatis|CBM4330BRB]] reads "some $P$ are $M$, all $M$ are $S$, so some $S$ are $P$".

### Arguments with no figure

[[An argument with four terms|S174DQ9N4T]] has no figure, because no term occurs in both premises and there is no middle term to place.
A chain such as "all squares are rhombuses, all rhombuses are parallelograms, all parallelograms are quadrilaterals, so all squares are quadrilaterals" has three premises, and a figure is defined only for two.
The chain splits into two first-figure syllogisms.
"All squares are rectangles, so some rectangles are squares" is a conversion from one premise; it has no middle term and no figure.

### What each figure can prove

Each figure has $4^3 = 64$ moods, and the four figures give the $256$ forms of [[syllogistic moods|1TD6HRM5NG]].
In the traditional reading each figure has exactly $6$ valid moods, $24$ in all.
In the modern reading the figures have $4$, $4$, $4$ and $3$ valid moods, $15$ in all.

The first figure proves conclusions of all four kinds, with Barbara (A), Celarent (E), Darii (I) and Ferio (O), and Barbara is the only valid mood in any figure with an A conclusion.
The second figure proves only negative conclusions, so it is the figure for showing that two classes are disjoint.
The third figure proves only particular conclusions.

The traditional special rules follow from the general rules of distribution.
In the first figure the major premise is universal and the minor premise affirmative.
In the second figure the major premise is universal and one premise is negative.
In the third figure the minor premise is affirmative.

### Watch out

Put the syllogism in standard order before you read its figure.
The major premise is the one that contains the predicate of the conclusion, wherever it stands in the text.
The mood is the list of letters and the figure is the place of the middle term; they are different things.
A valid mood in one figure need not be valid in another: AAA is valid in the first figure and invalid in the other three.

### History

Aristotle recognized three figures in the *Prior Analytics*, in the order used today.
The valid moods of the fourth figure were known in antiquity, but they were counted as indirect moods of the first figure, whose conclusion has the major term as subject.
The fourth figure as a separate figure is traditionally attributed to Galen, and historians doubt the attribution.

### Try it

Find the figure and mood of "some rational numbers are integers, all integers are algebraic numbers, so some algebraic numbers are rational".
The conclusion gives $S$ the algebraic numbers and $P$ the rational numbers, and $M$ is the integers.
The major premise $(P, M)$ is "some rational numbers are integers" and the minor premise $(M, S)$ is "all integers are algebraic", so it is IAI-4, Dimatis.

Is "no prime greater than $2$ is even, all multiples of $4$ are even, so no multiple of $4$ is a prime greater than $2$" in the first figure?
No: "even" is the predicate of both premises, so it is in the second figure, and EAE-2 is Cesare.

## Explanations

### L1 human

A syllogism has two starting sentences and a conclusion, and one group, the middle term, appears in both starting sentences.
The figure says where that middle group stands: at the front or at the back of each sentence.
In "all mammals are animals, all cats are mammals", the word "mammals" is at the front of the first sentence and at the back of the second, which is the first figure.
In "all squares are rectangles, no triangle is a rectangle", the word "rectangles" is at the back both times, which is the second figure.
There are four possible arrangements, so there are four figures.

### L2 human

We find the figure of the argument "no integer is a square root of $2$, because no rational number is a square root of $2$ and every integer is a rational number".

1. The conclusion is "no integer is a square root of $2$", so $S$ is the integers and $P$ is the square roots of $2$.
2. The middle term occurs in both premises and not in the conclusion, so $M$ is the rational numbers.
3. The major premise is the one with $P$: "no rational number is a square root of $2$", which is $(M, P)$.
4. The minor premise is the one with $S$: "every integer is a rational number", which is $(S, M)$.
5. The scheme $(M, P)$, $(S, M)$ is the first figure.
6. The letters are E, A, E, so the form is EAE-1, Celarent, a valid mood.

Find $S$, $P$ and $M$, write the scheme, and read off the figure and the mood.
The trap is step 3: in the text the minor premise came last, but the order in the text does not matter.

### L3 human

The four figures are the four ways to place one shared variable in two binary relations, each one of the four categorical relations between classes.
E and I are symmetric relations and A and O are not, so converting an E or I premise moves a syllogism from one figure to another, and this drives the reduction to the first figure.
In the first figure the premises compose: Barbara is the transitivity of inclusion $S \subseteq M \subseteq P$, and Darii and Ferio push a witness of the I premise through an inclusion or a disjointness.

The fourth figure is the first figure read backwards.
Exchange its premises and it reads $(M, S)$, $(P, M)$, a first-figure chain from $P$ through $M$ to $S$, but with the conclusion $(S, P)$ in place of the direct conclusion $(P, S)$.
That is why ancient logicians could treat its moods as indirect moods of the first figure.
In [[monadic predicate logic|SERN6CRVWW]] the figures have no special status; each is a pattern of variables, and its validity is decided by a finite search over the eight regions of a [[Venn diagram|0KCT6DPXJK]].
