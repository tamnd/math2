---
tag: 1TD6HRM5NG
kind: concept
name: Syllogistic moods
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [MZBNX2T6Q6, S4BTTGFR6J, KSJ9W29KXQ, 0KCT6DPXJK]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#SZR8
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/List_of_valid_argument_forms
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Venn_diagram
    locator: lead section
inventory: [VSCWWD952V]
---

## Summary

The mood of a syllogism is the three-letter word that records whether each of its three sentences is an "all", "no", "some" or "some are not" sentence.
Mood and figure together give a finite list of forms, so the validity of a syllogism becomes a lookup in a table.

"All mammals are animals, all cats are mammals, so all cats are animals" has three "all" sentences, so its mood is AAA, and the valid form with these letters in the first figure is called Barbara.
"No rational number is a square root of $2$, every integer is rational, so no integer is a square root of $2$" has mood EAE, and in the first figure it is called Celarent.

In exact terms, the mood of a categorical syllogism is the list of the kinds of its propositions, as letters from A, E, I, O, in the order major premise, minor premise, conclusion.
There are $4^3 = 64$ moods, and with the four [[figures|S4BTTGFR6J]] they give $256$ forms.
Exactly $24$ forms are valid in the traditional reading, in which every term names a non-empty class.
Exactly $15$ are valid in the modern reading, and the other $9$ need one particular term to be non-empty.

## Motivation

A [[categorical syllogism|MZBNX2T6Q6]] is fixed by two pieces of data: the kinds of its three propositions and the places of its middle term.
Once the terms are replaced by letters, only finitely many forms remain, so you can decide every form once and for all.
The list of valid moods was the working tool of logic for many centuries.
A student who knew the names could test an argument by finding its figure and mood and looking for the name.
Today the same list is a small, complete example of a decision procedure, and each entry can be checked with a [[Venn diagram|0KCT6DPXJK]].

## Notation

The three letters come in the order major premise, minor premise, conclusion, and the figure is added as a number: AAA-1, EAE-2, IAI-3.
In the table, the moods in the middle column are valid in the modern reading, and the moods in the last column are valid only if the term in brackets is non-empty.

| Figure | Valid in the modern reading | Valid with existential import |
|---|---|---|
| 1 | Barbara AAA, Celarent EAE, Darii AII, Ferio EIO | Barbari AAI ($S$), Celaront EAO ($S$) |
| 2 | Cesare EAE, Camestres AEE, Festino EIO, Baroco AOO | Cesaro EAO ($S$), Camestros AEO ($S$) |
| 3 | Disamis IAI, Datisi AII, Bocardo OAO, Ferison EIO | Darapti AAI ($M$), Felapton EAO ($M$) |
| 4 | Calemes AEE, Dimatis IAI, Fresison EIO | Bamalip AAI ($P$), Calemos AEO ($S$), Fesapo EAO ($M$) |

The counts are $4 + 4 + 4 + 3 = 15$ and $2 + 2 + 2 + 3 = 9$, so $24$ in all.
Some books use older names in the fourth figure: Bramantip for Bamalip, Camenes for Calemes and Dimaris for Dimatis.

The letters of a name encode a proof by reduction to the first figure.
The first letter B, C, D or F names the target: Barbara, Celarent, Darii or Ferio.
An s after a vowel says to convert that proposition simply, as "no $S$ is $P$" to "no $P$ is $S$".
A p says to convert it by limitation, as "all $S$ are $P$" to "some $P$ is $S$", which needs existential import.
An m says to exchange the premises, and the c in Baroco and Bocardo says that the proof goes by contradiction.

## Remarks

### Moods at work

[[Barbara|AC6XQ4KRNT]], AAA-1, reads "all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$", and it is valid in both readings.
[[Darapti|ARGGZ9N2SV]], AAI-3, reads "all $M$ are $P$, all $M$ are $S$, so some $S$ are $P$"; it is valid in the traditional reading and fails in the modern one when $M$ is empty.
[[Dimatis|CBM4330BRB]], IAI-4, reads "some $P$ are $M$, all $M$ are $S$, so some $S$ are $P$"; it is valid in both readings and reduces to Darii.
The [[undistributed middle|F8BP8S0RYG]] is AAA-2 and invalid, while the same letters in the first figure give Barbara, so validity depends on the figure as well as the mood.

### What has no mood

[[Modus ponens|E72YM7QK6X]], as in "if $12$ is divisible by $4$ then $12$ is even; $12$ is divisible by $4$; so $12$ is even", has no mood.
Its premises are a conditional and a sentence about one object, not categorical propositions.
"All squares are rectangles, so some rectangles are squares" has one premise; it is an immediate inference, not a syllogism.
A word such as AAAA is not a mood, because a mood has one letter for each premise and one for the conclusion.

### The rules behind the table

The $24$ traditional moods are exactly the forms that obey four rules.
The middle term is distributed at least once.
A term distributed in the conclusion is distributed in its premise.
The premises are not both negative.
The conclusion is negative exactly when one premise is negative.
The modern reading adds a fifth rule, that two universal premises never give a particular conclusion, and this rule removes exactly the $9$ moods of the last column.

Five of those $9$ are weakened moods.
Barbari, Celaront, Cesaro, Camestros and Calemos conclude the subaltern of the conclusion of Barbara, Celarent, Cesare, Camestres and Calemes, and they need $S$ to be non-empty.
Darapti, Felapton, Bamalip and Fesapo are not weakened, because the corresponding universal moods are invalid, and they need $M$ or $P$ to be non-empty.

### Watch out

The mood alone does not decide validity: AAA-1 is valid and AAA-2 is not.
The first letter belongs to the major premise, the premise containing the predicate of the conclusion, which need not come first in the text.
Before you accept Darapti or Barbari, check that the needed term is non-empty; with an empty term the premises can be true and the conclusion false.

### History

Aristotle proved $14$ valid moods in his three figures: four in the first, four in the second and six in the third.
The weakened moods and the moods of the fourth figure were added in later ancient and medieval logic.
The Latin names and the verse that begins "Barbara, Celarent, Darii, Ferio" come from medieval logic textbooks.

### Try it

Name the figure and mood of "no even number is odd, some primes are odd, so some primes are not even", and decide whether it is valid.
$S$ is the primes, $P$ the even numbers and $M$ the odd numbers; the premises are $(P, M)$ and $(S, M)$, so the form is EIO-2, Festino, which is valid in both readings.

Which term must be non-empty for Felapton, "no $M$ is $P$, all $M$ are $S$, so some $S$ is not $P$"?
The middle term: if $M$ is empty, both premises are true in the modern reading, and the conclusion is false when, for example, $S$ is empty.

## Explanations

### L1 human

Each sentence in a syllogism is one of four kinds: "all", "no", "some" or "some are not".
The kinds are named by the letters A, E, I and O.
A syllogism has three sentences, so its mood is a word of three letters, such as AAA or EIO.
Medieval students learned the good moods by names whose vowels are the letters: Barbara is AAA, Celarent is EAE, Darii is AII.
There are $256$ patterns in all and only $24$ of them are good, so a list of names was a practical tool.

### L2 human

We check two moods with a Venn diagram of three circles $S$, $M$ and $P$.
The circles cut the rectangle into $8$ regions, named by the circles that contain them, such as $SM\bar P$ for "in $S$ and $M$, not in $P$".
A universal premise says that some regions are empty, and we shade them.
A particular premise says that some region is not empty, and we put a cross in it, or on a boundary line when two regions are possible.

First, Celarent (EAE-1): no $M$ is $P$, all $S$ are $M$, so no $S$ is $P$.

1. "No $M$ is $P$" shades $SMP$ and $\bar S M P$.
2. "All $S$ are $M$" shades $S\bar M P$ and $S \bar M \bar P$.
3. The conclusion "no $S$ is $P$" needs $SMP$ and $S \bar M P$ to be empty.
4. Both are shaded, so the diagram already shows the conclusion, and the mood is valid.

Second, Festino (EIO-2): no $P$ is $M$, some $S$ is $M$, so some $S$ is not $P$.

5. "No $P$ is $M$" shades $SMP$ and $\bar S M P$.
6. "Some $S$ is $M$" puts a cross in $SM\bar P$ or $SMP$, and $SMP$ is shaded, so the cross goes into $S M \bar P$.
7. The conclusion "some $S$ is not $P$" needs a cross in $S M \bar P$ or $S \bar M \bar P$, and step 6 put one in $SM\bar P$, so the mood is valid.

Draw the universal premises first, because they can force the place of a cross.
The trap is a cross on a line: if a particular premise leaves two regions possible, the cross stays on the line, and a conclusion that needs it in one region does not follow.

### L3 human

The list of valid moods is the output of a finite search.
Whether a sentence of [[monadic predicate logic|SERN6CRVWW]] in three predicates is true in a model depends only on which of the $8$ regions are non-empty, so it is enough to check each of the $2^8 = 256$ choices of non-empty regions.
That this number equals the number of forms is a coincidence.
Running the search over all forms gives the $15$ modern valid forms, and keeping only the choices in which $S$, $M$ and $P$ are all non-empty gives the $24$ traditional ones.
The difference of $9$ forms is exactly the effect of existential import, as on the [[square of opposition|VYNBSVZ2TH]].

The names are also a small proof system.
Each name is a derivation of its mood from Barbara, Celarent, Darii and Ferio, with conversion, exchange of premises and reduction to contradiction as rules.
In this sense the mnemonic verse is an early list of derived rules of inference, a theme that returns in [[rules of inference|QPD3X471Q1]] and in [[natural deduction|6KT3BJZ7D1]].
