---
tag: VYNBSVZ2TH
kind: concept
name: Square of opposition
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [MZBNX2T6Q6, 0ZGC7ZESYN, 029JBBF693, 0ECVK59Y03]
sources:
  - url: https://en.wikipedia.org/wiki/Square_of_opposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Categorical_proposition
    locator: lead section
---

## Summary

The square of opposition is a picture of how the four sentences "all", "no", "some" and "some are not" about the same two classes constrain one another's truth.
Its main lesson is which sentence is the negation of which, and its fine print is the assumption that the subject class is not empty.

Draw it for swans and white things:
$$\begin{array}{ccc} \text{A: all swans are white} & \text{contraries} & \text{E: no swan is white} \\ \text{subaltern} \downarrow & \text{contradictories (diagonals)} & \downarrow \text{subaltern} \\ \text{I: some swan is white} & \text{subcontraries} & \text{O: some swan is not white} \end{array}$$
Black swans exist, so A is false and O, across the diagonal, is true.
White swans exist too, so E is false and I is true.
The two top sentences are both false here, which is allowed: they can never both be true.

In exact terms, take the four categorical propositions with subject $S$ and predicate $P$: A "all $S$ are $P$", E "no $S$ is $P$", I "some $S$ is $P$", O "some $S$ is not $P$".
Two propositions are contradictories when exactly one of them is true in every case, contraries when they cannot both be true, and subcontraries when they cannot both be false.
A proposition $q$ is a subaltern of $p$ when $p$ implies $q$.
In the traditional square, A and O, and E and I, are contradictories; A and E are contraries; I and O are subcontraries; and I and O are the subalterns of A and E.
In the modern square only the two pairs of contradictories remain, because the modern reading gives A and E no existential import.

## Motivation

Mathematicians negate statements all the time, and the square tells you how.
The [[negation|029JBBF693]] of "every continuous function on $[0, 1]$ is bounded" is "some continuous function on $[0, 1]$ is not bounded", the corner across the diagonal.
It is not "no continuous function on $[0, 1]$ is bounded", which is only the contrary.
To refute "all primes are odd" you need one even prime, and $2$ is enough; you do not need to show that no prime is odd.

The square also records the weaker relations, and they show where the traditional and the modern readings of [[Aristotelian syllogistic|MZBNX2T6Q6]] part.
That difference, existential import, decides which of the $24$ traditional [[syllogistic moods|1TD6HRM5NG]] survive in modern logic.
The same square, with $\Box$ and $\Diamond$ in place of "all" and "some", returns in modal logic.

## Notation

The table lists the relations and how they change when $S$ may be [[empty|0ECVK59Y03]].

| Pair | Relation | Traditional square | Modern square |
|---|---|---|---|
| A and O | contradictories | exactly one is true | exactly one is true |
| E and I | contradictories | exactly one is true | exactly one is true |
| A and E | [[contraries|JEPK6Q555H]] | not both true | both true when $S$ is empty |
| I and O | [[subcontraries|EHGHN4HNPD]] | not both false | both false when $S$ is empty |
| A to I, E to O | [[subalternation|FKRJAQ07GS]] | the universal implies the particular | fails when $S$ is empty |

The universal proposition is the superaltern and the particular one is the subaltern.
In set language, A says $S \subseteq P$, E says $S \cap P = \varnothing$, I says $S \cap P \neq \varnothing$, and O says $S \not\subseteq P$.
Some books draw the modern square with only the diagonals.

## Remarks

### Filling in a square

Take $S$ the multiples of $6$ and $P$ the even numbers.
A, "all multiples of $6$ are even", is true, because $6k = 2 \cdot 3k$.
So O is false, across the diagonal.
I, "some multiple of $6$ is even", is true, with witness $6$, as subalternation from A requires.
So E is false, across the other diagonal.

The [[square for primes and odd numbers|1Y82P4EFR1]] shows the mixed case: A and E both false, I and O both true, with witnesses $2$ and $3$.
The [[square with an empty subject term|JEW1GKR244]] shows the opposite extreme: with $S$ the even primes greater than $2$, A and E are both true and I and O both false.

### Why the relations hold

The diagonals hold in both readings.
"All $S$ are $P$" fails exactly when some element of $S$ is not in $P$, which is O; the pair E and I is the same with $P$ replaced by its complement.

The other relations need $S \neq \varnothing$.
If A and E were both true, then $S \subseteq P$ and $S \cap P = \varnothing$, so $S = \varnothing$.
If I and O were both false, then $S \cap P = \varnothing$ and $S \subseteq P$, so again $S = \varnothing$.
If A is true and $s \in S$, then $s \in S \cap P$, so I is true; E to O is the same with the complement of $P$.
When $S$ is empty, the modern reading makes A and E true and I and O false, and all three relations fail.
So existential import is the only source of the difference between the two squares.

### What is not on the square

A [[statement and its converse|AC40F9453Y]], "all $S$ are $P$" and "all $P$ are $S$", have different subjects and are not two corners of one square.
All four combinations of their truth values occur, so no relation of the square holds between them.
"$x > 2$" and "$x < 2$" cannot both be true, so they behave like contraries, but they are not categorical propositions about two terms.

### Watch out

The contrary is not the negation.
The negation of "all students passed" is "some student did not pass", not "no student passed".
Contraries can both be false: "all primes are odd" and "no prime is odd" are both false.
Subalternation needs a non-empty subject.
"Every even prime greater than $2$ is a multiple of $4$" is true in the modern reading, but "some even prime greater than $2$ is a multiple of $4$" is false.

### History

Aristotle described contradictory and contrary pairs of propositions in *On Interpretation*.
The square as a diagram comes from ancient commentators on Aristotle, and it became a standard figure in medieval logic.
The modern reading, in which "all $S$ are $P$" is $\forall x\,(S(x) \to P(x))$ and says nothing about existence, came with the logic of the nineteenth century.

### Try it

Give the negation of "no group of order $4$ is cyclic".
It is the I corner, "some group of order $4$ is cyclic", which is true: $\mathbb{Z}/4\mathbb{Z}$ is one.

A is true and $S$ is not empty: what can you say about the other three corners?
O is false by the diagonal, I is true by subalternation, and E is false by the other diagonal.

## Explanations

### L1 human

Take the four sentences "all cats are black", "no cat is black", "some cat is black" and "some cat is not black".
Put the two "all" or "no" sentences on top, and the two "some" sentences below.
The sentences on a diagonal are exact opposites: one is true and the other is false, always.
The two on top cannot both be true, but for real cats they are both false.
The two below cannot both be false, as long as there are cats at all.

### L2 human

We use the square to refute a claim correctly.

1. The claim is "all primes are odd", the A corner.
2. Its negation is the corner across the diagonal, O: "some prime is not odd".
3. To refute the claim we need one prime that is not odd, and $2$ is one.
4. The E corner "no prime is odd" is the contrary of the claim, and it is false as well, because of $3$.

To negate a universal claim, move along the diagonal to a particular claim of the opposite quality.
The trap is to aim at the contrary: refuting "all primes are odd" does not require showing that no prime is odd.

### L3 human

The modern square is the square of a quantifier and its dual: the diagonals are the laws $\neg \forall x\, \varphi \leftrightarrow \exists x\, \neg \varphi$ and $\neg \exists x\, \psi \leftrightarrow \forall x\, \neg \psi$.
In [[modal logic|C3RZY20ETK]], $\Box p$, $\Box \neg p$, $\Diamond p$ and $\Diamond \neg p$ form a square of the same shape.
On a Kripke frame all the traditional relations hold for every formula exactly when $\Box p \to \Diamond p$ is valid on the frame, that is, when every world sees some world; that axiom plays the role of existential import.

Each relation is a condition on the pairs of truth values two propositions may take: contradictories exclude $(T, T)$ and $(F, F)$, contraries exclude $(T, T)$, subcontraries exclude $(F, F)$, and subalternation excludes $(T, F)$.
In a [[Boolean algebra|0XADJKM699]] of propositions, $a$ and $b$ are contradictories when $b = \neg a$, contraries when $a \land b = 0$, subcontraries when $a \lor b = 1$, and $b$ is a subaltern of $a$ when $a \leq b$.
