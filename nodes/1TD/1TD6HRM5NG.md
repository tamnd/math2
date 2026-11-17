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

The mood of a categorical syllogism is the list of the kinds of its three propositions, written as three letters from A, E, I, O in the order major premise, minor premise, conclusion.
For example, a syllogism whose premises and conclusion are all universal affirmative has the mood AAA.
There are $4^3 = 64$ moods, and with the four [[figures|S4BTTGFR6J]] they give $64 \cdot 4 = 256$ syllogistic forms.
Exactly $24$ of these forms are valid in the traditional reading, in which every term names a non-empty class.
Exactly $15$ of them are valid in the modern reading, and the other $9$ need the extra assumption that one particular term is not empty.
The valid forms carry medieval Latin names, such as Barbara and Celarent, whose vowels give the mood and whose consonants describe the reduction to the first figure.
The moods matter because they turn the question "is this argument valid" into a lookup in a finite table, and the table can be checked with [[Venn diagrams|0KCT6DPXJK]].

## Motivation

A [[categorical syllogism|MZBNX2T6Q6]] is fixed by two pieces of data: the kinds of its three propositions and the places of its middle term.
Once the terms are replaced by letters, only finitely many forms remain.
So one can list all forms once and decide for each of them whether it is valid.
The list of valid moods was the working tool of logic for many centuries.
A student who knew the names could test an argument by finding its figure and mood and looking for the name.

## Notation

The three letters are written in the order major premise, minor premise, conclusion, and the figure is added as a number: AAA-1, EAE-2, IAI-3.
In the table below the moods in the first column of each figure are valid in the modern reading.
The moods in the second column are valid only if the term in brackets is not empty.

| Figure | Valid in the modern reading | Valid with existential import |
|---|---|---|
| 1 | Barbara AAA, Celarent EAE, Darii AII, Ferio EIO | Barbari AAI ($S$), Celaront EAO ($S$) |
| 2 | Cesare EAE, Camestres AEE, Festino EIO, Baroco AOO | Cesaro EAO ($S$), Camestros AEO ($S$) |
| 3 | Disamis IAI, Datisi AII, Bocardo OAO, Ferison EIO | Darapti AAI ($M$), Felapton EAO ($M$) |
| 4 | Calemes AEE, Dimatis IAI, Fresison EIO | Bamalip AAI ($P$), Calemos AEO ($S$), Fesapo EAO ($M$) |

The counts are $4 + 4 + 4 + 3 = 15$ and $2 + 2 + 2 + 3 = 9$, so $24$ in total.
Some books use older names for the fourth figure: Bramantip for Bamalip, Camenes for Calemes and Dimaris for Dimatis.

The letters of a name encode a proof by reduction to the first figure.
The first letter B, C, D or F says that the mood reduces to Barbara, Celarent, Darii or Ferio.
The letter s after a vowel says that this proposition is converted simply ("no $S$ is $P$" to "no $P$ is $S$", or "some $S$ is $P$" to "some $P$ is $S$").
The letter p says that it is converted by limitation ("all $S$ are $P$" to "some $P$ is $S$"), which needs existential import.
The letter m says that the premises are exchanged, and the letter c in Baroco and Bocardo says that the proof goes by contradiction.

## Remarks

### Examples

- [[Barbara|AC6XQ4KRNT]], AAA-1: all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$. It is valid in both readings.
- [[Darapti and existential import|ARGGZ9N2SV]], AAI-3: all $M$ are $P$, all $M$ are $S$, so some $S$ are $P$. It is valid in the traditional reading and fails in the modern reading when $M$ is empty.
- [[Dimatis|CBM4330BRB]], IAI-4: some $P$ are $M$, all $M$ are $S$, so some $S$ are $P$. It is valid in both readings, and it reduces to Darii.
- The [[undistributed middle|F8BP8S0RYG]], AAA-2, is a mood that is not valid. The same letters AAA give Barbara in the first figure, so validity depends on the figure as well as on the mood.

### Non-examples

- [[Modus ponens is not a categorical syllogism|E72YM7QK6X]]: "if $n$ is divisible by $4$ then $n$ is even; $12$ is divisible by $4$; so $12$ is even" has no mood. Its premises are a conditional and a singular sentence, not categorical propositions.
- The list AAAA does not describe a syllogism. A mood has exactly three letters, one for each of the two premises and the conclusion.
- "All squares are rectangles, so some rectangles are squares" is a single A premise with an I conclusion. It is an immediate inference, not a syllogism, and it has no mood.

### Basic properties

- Every valid mood has at least one universal premise and at least one affirmative premise. A brute-force check of the $256$ forms confirms this, and the rules of distribution explain it.
- The valid moods are exactly the forms that satisfy four rules: the middle term is distributed at least once; a term distributed in the conclusion is distributed in its premise; not both premises are negative; the conclusion is negative exactly when one premise is negative.
- In the modern reading one further rule holds: two universal premises never give a particular conclusion. This rule removes exactly the $9$ moods of the second column.
- Five of the $9$ conditional moods are weakened moods: Barbari, Celaront, Cesaro, Camestros and Calemos conclude the subaltern of the conclusion of Barbara, Celarent, Cesare, Camestres and Calemes. They need $S$ to be non-empty.
- The other four conditional moods, Darapti, Felapton, Bamalip and Fesapo, are not weakened moods. They have no universal counterpart, and they need $M$ or $P$ to be non-empty.

### History

Aristotle proved $14$ valid moods in his three figures: four in the first figure, four in the second and six in the third.
The weakened moods and the moods of the fourth figure were added in later ancient and medieval logic.
The Latin names and the verse that begins "Barbara, Celarent, Darii, Ferio" come from medieval logic textbooks.
In the nineteenth century, logicians in the tradition of Boole read universal propositions without existential import, and diagrams of the kind used by John Venn made the check of each mood mechanical.

### Common errors

- Taking the mood alone as enough to decide validity. AAA-1 is valid and AAA-2 is invalid.
- Reading the letters in the order in which the premises stand in the text. The first letter belongs to the major premise, the premise that contains the predicate of the conclusion.
- Accepting Darapti or Barbari without checking that the needed term is non-empty. With an empty term the premises can be true and the conclusion false.

## Explanations

### L1 human

Each sentence in a syllogism is of one of four kinds: "all", "no", "some" or "some are not".
The kinds are named by the letters A, E, I and O.
A syllogism has three sentences, so its mood is a word of three letters, such as AAA or EIO.
Medieval students learned the good moods by names in which the vowels are the letters: Barbara is AAA, Celarent is EAE, Darii is AII.
For example, "all mammals are animals, all cats are mammals, so all cats are animals" is Barbara.
There are $256$ patterns in total, and only $24$ of them are good, so a list of names was a practical tool.

### L2 human

We check two moods with a Venn diagram of three circles $S$, $M$ and $P$.
The circles cut the rectangle into $8$ regions; we name each region by the circles that contain it, such as $SM\bar P$ for "in $S$ and $M$, not in $P$".
A universal premise says that some regions are empty, and we shade them.
A particular premise says that some region is not empty, and we put a cross in it, or on a boundary line when two regions are possible.

First, Celarent (EAE-1): no $M$ is $P$, all $S$ are $M$, so no $S$ is $P$.

1. "No $M$ is $P$" shades $SMP$ and $\bar S M P$.
2. "All $S$ are $M$" shades $S\bar M P$ and $S \bar M \bar P$.
3. The conclusion "no $S$ is $P$" needs $SMP$ and $S \bar M P$ to be empty.
4. $SMP$ is shaded by step 1, and $S\bar M P$ is shaded by step 2. So the diagram already shows the conclusion, and the mood is valid.

Second, Festino (EIO-2): no $P$ is $M$, some $S$ is $M$, so some $S$ is not $P$.

5. "No $P$ is $M$" shades $SMP$ and $\bar S M P$.
6. "Some $S$ is $M$" puts a cross in $SM\bar P$ or $SMP$. The region $SMP$ is shaded, so the cross goes into $S M \bar P$.
7. The conclusion "some $S$ is not $P$" needs a cross in $S M \bar P$ or $S \bar M \bar P$. Step 6 put one in $SM\bar P$, so the mood is valid.

The typical use is to draw the universal premises first, because they can force the place of a cross.
The trap is a cross on a line: if a particular premise leaves two regions possible, the cross stays on the line, and a conclusion that needs it in one region does not follow.

### L3 human

The list of valid moods is the output of a finite search, and it is a model for later decision procedures.
A form of [[monadic predicate logic|SERN6CRVWW]] in three predicates is valid exactly when it holds in all $2^8 = 256$ ways to choose which of the $8$ regions are non-empty.
Running this search over the $256$ forms gives the $15$ modern valid forms, and restricting it to models where $S$, $M$ and $P$ are non-empty gives the $24$ traditional ones.
The difference of $9$ forms is exactly the effect of existential import, as on the [[square of opposition|VYNBSVZ2TH]].

The names are also a small proof system.
Each name is a derivation of the mood from the four axioms Barbara, Celarent, Darii and Ferio, using conversion, exchange of premises and reduction to contradiction as rules.
In this sense the mnemonic verse is an early example of a list of derived rules of inference, a theme that returns in [[rules of inference|QPD3X471Q1]] and in [[natural deduction|6KT3BJZ7D1]].
