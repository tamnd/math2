---
tag: MZBNX2T6Q6
kind: concept
name: Aristotelian syllogistic
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [KSJ9W29KXQ, 0ZGC7ZESYN, 0QHEWQD30B, 0GHS47PDAQ, 0MSRQHCNN9, 0KCT6DPXJK]
sources:
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Term_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Categorical_proposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Prior_Analytics
    locator: lead section
---

## Summary

Aristotelian syllogistic is the first formal logic: it decides whether an argument about classes is correct by looking only at its shape, never at its subject matter.
Its arguments have two premises and a conclusion, each saying "all", "no", "some" or "some are not" about two classes.

Here is the standard example.
All mammals are animals, all dogs are mammals, so all dogs are animals.
Replace "dogs" by $S$, "mammals" by $M$ and "animals" by $P$, and you get the form "all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$", called [[Barbara|AC6XQ4KRNT]].
Every argument of this form with true premises has a true conclusion, whatever the classes are.
Now compare: all unicorns have one horn, all unicorns are horses, so some horses have one horn.
This form, called [[Darapti|ARGGZ9N2SV]], was valid for Aristotle, but in modern logic both premises are true (there are no unicorns to break them) and the conclusion is false.

In exact terms, a categorical proposition joins a subject term $S$ to a predicate term $P$ in one of four ways:
$$\text{A: all } S \text{ are } P, \quad \text{E: no } S \text{ is } P, \quad \text{I: some } S \text{ is } P, \quad \text{O: some } S \text{ is not } P.$$
A categorical syllogism has two categorical premises and a categorical conclusion built from exactly three [[terms|KSJ9W29KXQ]].
The conclusion joins the minor term $S$ (its subject) to the major term $P$ (its predicate), and the middle term $M$ occurs once in each premise and not in the conclusion.
The syllogism is valid when every choice of classes for the three terms that makes both premises true also makes the conclusion true.

## Motivation

Many arguments in mathematics have the shape of Barbara.
All squares are rectangles, and all rectangles are parallelograms, so all squares are parallelograms.
The argument is correct because of the words "all" and "are" and the places of the three terms, and not because of anything about squares.
Aristotle saw this and replaced the terms by letters.
That step turned the study of correct reasoning into the study of forms, and every later formal system continues it, from abstract [[formal systems|439M8B4DY2]] to the proof systems of first-order logic.

The second motive is to catch the invalid forms.
"All squares are parallelograms, and all rectangles are parallelograms, so all rectangles are squares" looks much like Barbara, but its conclusion is false.
Syllogistic gives exact tests that separate the valid forms from the invalid ones.
The Darapti example adds a third lesson: validity can depend on a hidden assumption, here that the classes are not empty.
The [[square of opposition|VYNBSVZ2TH]] and the list of [[syllogistic moods|1TD6HRM5NG]] study that assumption in detail.

## Notation

The letters A, E, I, O come from the Latin *affirmo* (I affirm) and *nego* (I deny): A and I affirm, E and O deny.
Many books write the propositions as $SaP$, $SeP$, $SiP$ and $SoP$.
The table gives the quantity, the quality and the modern reading in [[predicate logic|086QKPF0A6]], where $S$ and $P$ are one-place [[predicates|0QHEWQD30B]].

| Letter | Sentence | Quantity | Quality | Predicate logic |
|---|---|---|---|---|
| A | All $S$ are $P$ | universal | affirmative | $\forall x\,(S(x) \to P(x))$ |
| E | No $S$ is $P$ | universal | negative | $\forall x\,(S(x) \to \neg P(x))$ |
| I | Some $S$ is $P$ | particular | affirmative | $\exists x\,(S(x) \land P(x))$ |
| O | Some $S$ is not $P$ | particular | negative | $\exists x\,(S(x) \land \neg P(x))$ |

The formulas use the [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]].
The traditional order of a syllogism is major premise (the one with $P$), minor premise (the one with $S$), conclusion.
The three letters in this order are the mood, and the position of the middle term is the [[figure|S4BTTGFR6J]], so Barbara is AAA-1.

## Remarks

### Four forms worked through

Barbara (AAA-1) is valid because inclusion is transitive: the premises say $M \subseteq P$ and $S \subseteq M$, so $S \subseteq P$.
Celarent (EAE-1) reads: no rational number is a square root of $2$, all integers are rational, so no integer is a square root of $2$.
It is valid because a set inside $M$ cannot meet a set that is disjoint from $M$.

Darii (AII-1) reads: all multiples of $4$ are even, some squares are multiples of $4$, so some squares are even.
The second premise has a witness, the square $16$, and the first premise carries it into the conclusion: $16$ is even.
The [[reduction of Camestres to Celarent|TKW0RRHV88]] shows a valid form of the second figure turned into one of the first.
[[Darapti|ARGGZ9N2SV]] (AAI-3) is valid exactly when the middle term is not empty, as the unicorns showed.

### Arguments that are not valid syllogisms

The [[undistributed middle|F8BP8S0RYG]] has the shape of a syllogism: "all squares are parallelograms, all rectangles are parallelograms, so all rectangles are squares".
The rectangle with sides $1$ and $2$ makes both premises true and the conclusion false, so the form is invalid.
[[An argument with four terms|S174DQ9N4T]] is not a syllogism at all, because no term links the two premises.
"Every square is a rectangle, so every side of a square is a side of a rectangle" is valid in predicate logic, but it is not a syllogism either.
The phrase "is a side of" is a relation between two objects, and syllogistic can only say that one class lies inside, meets or misses another.

### How to test a form

There are $4^3 \cdot 4 = 256$ forms: four letters for each of the three propositions and four figures.
In the traditional reading $24$ are valid, and in the modern reading $15$; the list is in [[syllogistic moods|1TD6HRM5NG]].
A [[Venn diagram|0KCT6DPXJK]] with three circles tests any form mechanically.
The traditional rules test it by counting.
The middle term is distributed at least once, a term distributed in the conclusion is distributed in its premise, not both premises are negative, and the conclusion is negative exactly when one premise is.
Distribution is explained in [[syllogistic terms|KSJ9W29KXQ]].

Aristotle tested forms in a third way, by reduction.
He accepted the four forms of the first figure, Barbara, Celarent, Darii and Ferio, as evident, and derived the others from them.
The tools are conversion ("no $S$ is $P$" to "no $P$ is $S$", and the same for I), exchange of the premises, and [[proof by contradiction|0J0XBKG64S]].
Conversion fails for A: "all squares are rectangles" is true and "all rectangles are squares" is false.

### Existential import

In the traditional reading, "all $S$ are $P$" implies "some $S$ is $P$", because every term is taken to name a non-empty class.
In the modern reading it does not: when no $S$ exists, both A and E are true and both I and O are false.
The two readings differ by exactly this assumption.
Every form valid in the modern reading stays valid in the traditional one, and the $9$ extra traditional forms become valid in the modern reading once we add the premise that a certain term is not empty.
In [[monadic predicate logic|SERN6CRVWW]], a syllogism is valid in the modern reading exactly when its translation by the table is a valid argument.

### Watch out

Do not judge a form by the truth of its conclusion.
"All squares are rhombuses, all squares are rectangles, so all rectangles are rhombuses" has true premises and a false conclusion, so its form (AAA-3) is invalid.
An instance of the same form with a true conclusion proves nothing.

Do not forget existential import.
"Every even prime greater than $2$ is divisible by $4$" is true in the modern reading, because there is no such prime.
"Some even prime greater than $2$ is divisible by $4$" is false, so the step from A to I needs the subject to be non-empty.

### History

Aristotle developed syllogistic in the *Prior Analytics* in the fourth century BC.
He used letters for terms, worked with three figures, and called the valid moods of the first figure perfect, because their validity needs no proof.
He reduced the other valid moods of his figures to them.
Medieval logicians gave the valid moods Latin names whose letters encode the reduction, and syllogistic stayed the core of logic teaching until the nineteenth century.
Modern logic treats it as a small part of predicate logic.

### Try it

Is "no prime greater than $2$ is even, all multiples of $4$ are even, so no multiple of $4$ is a prime greater than $2$" valid?
Yes: with $P$ the primes greater than $2$, $M$ the even numbers and $S$ the multiples of $4$, it is EAE in the second figure, Cesare, which is valid.

Is "some primes are odd, some odd numbers are squares, so some primes are squares" valid?
No: the middle term "odd numbers" is never distributed, and indeed no prime is a square.

## Explanations

### L1 human

A syllogism is a short argument with two starting sentences and one final sentence.
Each sentence says "all", "no", "some" or "some are not" about two groups.
For example: all cats are mammals, all mammals are animals, so all cats are animals.
The group "mammals" links the two starting sentences and then disappears.
Draw the cats as a circle inside the circle of mammals, and the mammals inside the circle of animals: the cat circle lies inside the animal circle.
The same picture works for any three groups in the same pattern, so we can replace the groups by letters and study only the pattern.

### L2 human

We prove Baroco (AOO-2) by reduction to Barbara.
Its major premise is "all $P$ are $M$", its minor premise is "some $S$ is not $M$", and its conclusion is "some $S$ is not $P$".
An instance: all squares are rhombuses, some rectangles are not rhombuses, so some rectangles are not squares.

1. Suppose that the premises are true and the conclusion is false.
2. The conclusion is an O proposition, so its negation, the A proposition "all $S$ are $P$", is true.
3. Barbara with major premise "all $P$ are $M$" and minor premise "all $S$ are $P$" gives "all $S$ are $M$".
4. "All $S$ are $M$" contradicts the minor premise "some $S$ is not $M$".
5. So the supposition of step 1 is false, and the conclusion follows from the premises.

The reduction lets us accept only the four forms of the first figure and prove the rest.
The trap is step 2: the negation of "some $S$ is not $P$" is "all $S$ are $P$", not "no $S$ is $P$".

### L3 human

In modern terms, syllogistic is a fragment of monadic predicate logic with three unary predicates and formulas of four shapes.
Validity in it is decidable: a countermodel, when one exists, needs at most one element in each of the $2^3 = 8$ regions of the Venn diagram of $S$, $M$ and $P$.
So a finite search settles all $256$ forms, and the counts $15$ and $24$ come out of it.

Two modern reconstructions of Aristotle's own system exist.
Łukasiewicz read it as an axiomatic theory, with the moods as true conditional sentences.
Corcoran and Smiley read it as a natural deduction system in which the moods are rules and the reductions are derivations.
The second view puts syllogistic beside [[natural deduction|6KT3BJZ7D1]].
Syllogistic cannot express relations, and this is a main reason why the logic of Frege and Peirce replaced it; Peirce's [[existential graphs|D3ZS6WHPM1]] are a diagram logic that reaches full first-order logic.
