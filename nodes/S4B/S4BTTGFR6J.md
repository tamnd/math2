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

The figure of a categorical syllogism is the arrangement of the middle term $M$ in its two premises, when the syllogism is written in standard order.
Standard order puts the major premise first, then the minor premise, then the conclusion.
The major premise contains the major term $P$, the predicate of the conclusion, and the minor premise contains the minor term $S$, the subject of the conclusion.
We write each proposition as the pair (subject, predicate), so the conclusion is $(S, P)$.
There are four figures.
In the first figure, $M$ is the subject of the major premise and the predicate of the minor premise.
In the second figure, $M$ is the predicate of both premises, and in the third figure, $M$ is the subject of both premises.
In the fourth figure, $M$ is the predicate of the major premise and the subject of the minor premise.
The figure together with the [[mood|1TD6HRM5NG]] fixes the form of the syllogism completely.
Figures matter because validity depends on them: the same three letters can give a valid form in one figure and an invalid form in another.

## Motivation

The words "all", "no", "some" and "not" do not determine an argument alone.
"All $M$ are $P$, all $S$ are $M$, so all $S$ are $P$" is valid, but "all $P$ are $M$, all $S$ are $M$, so all $S$ are $P$" is not.
Both have three A propositions; they differ only in the place of the middle term.
To list the valid [[syllogisms|MZBNX2T6Q6]], one must therefore sort them by this place as well as by the kinds of propositions.
The figures are this sorting.

## Notation

In the scheme below each premise is written as the pair (subject, predicate), the major premise first and the minor premise second.
The conclusion is always $(S, P)$.

| Figure | Major premise | Minor premise | Place of $M$ |
|---|---|---|---|
| 1 | $(M, P)$ | $(S, M)$ | subject, then predicate |
| 2 | $(P, M)$ | $(S, M)$ | predicate in both |
| 3 | $(M, P)$ | $(M, S)$ | subject in both |
| 4 | $(P, M)$ | $(M, S)$ | predicate, then subject |

A syllogism is named by its mood and its figure, for example AAA-1 for Barbara and AEE-2 for Camestres.
Some authors list the minor premise first; then the scheme of the first and the fourth figure is read in the other order, so the convention must be checked in each book.

## Remarks

### Examples

- First figure: [[Barbara|AC6XQ4KRNT]], "all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$". The middle term is the subject of the major premise and the predicate of the minor premise.
- Second figure: Camestres, "all $P$ are $M$, no $S$ is $M$, so no $S$ is $P$"; see [[the reduction of Camestres to Celarent|TKW0RRHV88]]. With $P$ the squares, $M$ the rectangles and $S$ the triangles, it says that no triangle is a square.
- Third figure: Disamis, "some $M$ are $P$, all $M$ are $S$, so some $S$ are $P$". With $M$ the primes, $P$ the odd numbers and $S$ the integers greater than $1$, it says that some integers greater than $1$ are odd.
- Third figure with existential import: [[Darapti|ARGGZ9N2SV]], "all $M$ are $P$, all $M$ are $S$, so some $S$ are $P$", valid only when $M$ is not empty.
- Fourth figure: [[Dimatis|CBM4330BRB]], "some $P$ are $M$, all $M$ are $S$, so some $S$ are $P$".

### Non-examples

- [[An argument with four terms|S174DQ9N4T]] has no figure. No term occurs in both premises, so there is no middle term whose place could be read.
- A chain such as "all squares are rhombuses, all rhombuses are parallelograms, all parallelograms are quadrilaterals, so all squares are quadrilaterals" has three premises. It has no figure, because a figure is defined for exactly two premises; it splits into two syllogisms of the first figure.
- "All squares are rectangles, so some rectangles are squares" is an inference from one premise, a conversion. It has no middle term and no figure.

### Basic properties

- Each figure has exactly $4^3 = 64$ moods, and the four figures give the $256$ forms of [[syllogistic moods|1TD6HRM5NG]].
- In the traditional reading each figure has exactly $6$ valid moods, $24$ in total. In the modern reading the figures have $4$, $4$, $4$ and $3$ valid moods, $15$ in total.
- Special rules of the traditional reading: in the first figure the major premise is universal and the minor premise is affirmative. In the second figure the major premise is universal and exactly one premise is negative.
- In the third figure the minor premise is affirmative and the conclusion is particular. So the third figure never proves a universal conclusion.
- The first figure is the only figure that proves conclusions of all four kinds A, E, I and O, with Barbara, Celarent, Darii and Ferio.
- The second figure proves only negative conclusions. Its moods are the natural tool to show that two classes are disjoint, as in Camestres.
- If the premises of a fourth-figure syllogism are exchanged, the result has the scheme of the first figure with $S$ and $P$ swapped. The conclusion $(S, P)$ then names the two outer terms in the reverse order of a first-figure conclusion.

### History

Aristotle recognised three figures in the *Prior Analytics*, and he ordered them as the first, second and third figure used today.
The valid moods of the fourth figure were known in antiquity, but they were treated as indirect moods of the first figure, in which the conclusion has the major term as subject.
The fourth figure as a separate figure is traditionally attributed to Galen, the physician and philosopher of the second century AD.
Historians doubt this attribution.
Medieval and later logic textbooks taught all four figures.

### Common errors

- Reading the figure before putting the syllogism in standard order. The major premise is the premise that contains the predicate of the conclusion, wherever it stands in the text.
- Confusing the figure with the mood. The mood is the list of letters A, E, I, O, and the figure is the place of the middle term.
- Taking a valid mood from one figure into another. AAA is valid in the first figure and invalid in the second, the third and the fourth.

## Explanations

### L1 human

A syllogism has two starting sentences and a conclusion, and one word group, the middle term, appears in both starting sentences.
The figure says where that middle group stands in the two sentences: at the front or at the back.
In "all mammals are animals, all cats are mammals", the word "mammals" is at the front of the first sentence and at the back of the second; this is the first figure.
In "all squares are rectangles, no triangle is a rectangle", the word "rectangles" is at the back both times; this is the second figure.
There are four possible arrangements, so there are four figures.

### L2 human

We find the figure of the argument "no integer is a square root of $2$, because no rational number is a square root of $2$ and every integer is a rational number".

1. The conclusion is "no integer is a square root of $2$". So $S$ is "integers" and $P$ is "square roots of $2$".
2. The middle term is the term that occurs in both premises and not in the conclusion: $M$ is "rational numbers".
3. The major premise is the premise with $P$: "no rational number is a square root of $2$", which is $(M, P)$.
4. The minor premise is the premise with $S$: "every integer is a rational number", which is $(S, M)$.
5. The scheme $(M, P)$, $(S, M)$ is the first figure.
6. The letters are E, A, E, so the form is EAE-1, which is Celarent, a valid mood.

The typical use of the figure is this lookup: find $S$, $P$ and $M$, write the scheme, and read the figure and the mood.
The trap is step 3: in the text the minor premise came last, but the order in the text does not matter.

### L3 human

The four figures are the four ways to place one shared variable in two binary relations, each relation being one of the four categorical relations between classes.
Since E and I are symmetric relations and A and O are not, conversion moves an E or I premise from one figure to another, and this is the engine of the reduction to the first figure.
In the language of relations, the first figure is the composition of relations: Barbara is the transitivity of inclusion $S \subseteq M \subseteq P$.
Darii and Ferio take a witness of the I premise and push it through an inclusion or a disjointness.

The fourth figure is the first figure read backwards.
If we write the minor premise first, a fourth-figure syllogism reads $(M, S)$, $(P, M)$, which is a first-figure chain from $P$ through $M$ to $S$, but with the conclusion $(S, P)$ instead of the direct conclusion $(P, S)$.
This is the reason why ancient logicians could treat its moods as indirect moods of the first figure.
In modern [[monadic predicate logic|SERN6CRVWW]] the figure has no special status; each figure is just a different pattern of variables, and the validity of each pattern is decided by a finite search over the eight regions of a [[Venn diagram|0KCT6DPXJK]].
