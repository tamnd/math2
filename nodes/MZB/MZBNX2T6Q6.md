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

Aristotelian syllogistic is the logic of four kinds of sentences, the categorical propositions, each joining a subject term $S$ to a predicate term $P$.
The four kinds are A "All $S$ are $P$", E "No $S$ is $P$", I "Some $S$ is $P$" and O "Some $S$ is not $P$".
A categorical syllogism is an argument with two categorical premises and a categorical conclusion, built from exactly three [[terms|KSJ9W29KXQ]].
The conclusion joins the minor term $S$ (its subject) to the major term $P$ (its predicate), and the middle term $M$ occurs once in each premise and not in the conclusion.
The syllogism is valid when every choice of the three terms that makes both premises true also makes the conclusion true.
The theory lists the valid syllogisms, reduces them to four basic ones of the first figure, and gives rules to test any syllogism.
It matters as the first formal logic: validity depends only on the form, and the terms can be replaced by letters.

## Motivation

Many arguments in mathematics and in daily life have the same shape.
"All squares are rectangles, and all rectangles are parallelograms, so all squares are parallelograms" has the shape "All $M$ are $P$, all $S$ are $M$, so all $S$ are $P$".
"All primes greater than $2$ are odd, and $7$ is a prime greater than $2$, so $7$ is odd" uses the same pattern for a single object.
The correctness of such an argument does not depend on squares or on primes.
It depends only on the words "all", "no", "some" and "not" and on the places of the terms.
Aristotle saw this and replaced the terms by letters.
This step turned the study of correct reasoning into the study of forms, and every later formal logic continues it.

A second motive is to find the invalid forms.
"All squares are parallelograms, and all rectangles are parallelograms, so all rectangles are squares" looks similar, but its conclusion is false.
Syllogistic gives exact tests that separate the valid forms from the invalid ones.

## Notation

The letters A, E, I, O come from the Latin words *affirmo* (I affirm) and *nego* (I deny): A and I affirm, E and O deny.
Many books write the four propositions in short form as $SaP$, $SeP$, $SiP$ and $SoP$.
The table gives the quantity (universal or particular), the quality (affirmative or negative) and the reading in [[predicate logic|086QKPF0A6]].

| Letter | Sentence | Quantity | Quality | Predicate logic |
|---|---|---|---|---|
| A | All $S$ are $P$ | universal | affirmative | $\forall x\,(S(x) \to P(x))$ |
| E | No $S$ is $P$ | universal | negative | $\forall x\,(S(x) \to \neg P(x))$ |
| I | Some $S$ is $P$ | particular | affirmative | $\exists x\,(S(x) \land P(x))$ |
| O | Some $S$ is not $P$ | particular | negative | $\exists x\,(S(x) \land \neg P(x))$ |

In the last column $S$ and $P$ are one-place [[predicates|0QHEWQD30B]], and the formulas use the [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]].
The traditional order of a syllogism is: major premise (with $P$), minor premise (with $S$), conclusion.
The mood of a syllogism is the list of its three letters, and its figure is the position of the middle term; see [[syllogistic moods|1TD6HRM5NG]] and [[syllogistic figures|S4BTTGFR6J]].
So Barbara is the mood AAA in the first figure, often written AAA-1.

## Remarks

### Examples

- [[Barbara|AC6XQ4KRNT]]: all $M$ are $P$, all $S$ are $M$, so all $S$ are $P$. An instance is [[Barbara for squares, rectangles and parallelograms|RKJG1VXH8E]]. It is valid, because $S \subseteq M$ and $M \subseteq P$ give $S \subseteq P$.
- Celarent (EAE-1): no rational number is a square root of $2$, all integers are rational numbers, so no integer is a square root of $2$. It is valid, because a set inside $M$ cannot meet a set that is disjoint from $M$.
- Darii (AII-1): all multiples of $4$ are even, some squares are multiples of $4$, so some squares are even. The square $16$ is a multiple of $4$, so the middle term carries the witness $16$ into the conclusion.
- [[The reduction of Camestres to Celarent|TKW0RRHV88]] shows a second-figure syllogism turned into a first-figure one by conversion and by a change of the order of the premises.
- [[Darapti and existential import|ARGGZ9N2SV]] is a third-figure syllogism that is valid only when the middle term is not empty.

### Non-examples

- [[The fallacy of the undistributed middle|F8BP8S0RYG]]: "all squares are parallelograms, all rectangles are parallelograms, so all rectangles are squares" has the form of a categorical syllogism, but the conclusion does not follow. A rectangle of sides $1$ and $2$ makes the premises true and the conclusion false.
- [[An argument with four terms|S174DQ9N4T]] has two categorical premises and a categorical conclusion, but no term links the two premises. It is not a categorical syllogism, because it has four terms and no middle term.
- "Every square is a rectangle, so every side of a square is a side of a rectangle" is valid in predicate logic. It is not a categorical syllogism, because "is a side of" is a relation between two objects and not a property of one object.

### Basic properties

- Exactly $4^3 \cdot 4 = 256$ syllogistic forms exist: $4$ choices of letter for each of the three propositions and $4$ figures. Of these, $24$ are valid in the traditional reading and $15$ in the modern reading; the list is in [[syllogistic moods|1TD6HRM5NG]].
- Conversion: "No $S$ is $P$" and "No $P$ is $S$" say the same thing, and so do "Some $S$ is $P$" and "Some $P$ is $S$". This simple conversion fails for A and O: "All squares are rectangles" is true and "All rectangles are squares" is false.
- Reduction: each valid syllogism can be reduced to one of the four perfect moods of the first figure, Barbara, Celarent, Darii and Ferio. The tools are conversion, the exchange of the premises, and proof by [[contradiction|0J0XBKG64S]].
- Rules of validity: a syllogism in the traditional reading is valid exactly when the middle term is distributed at least once, no term is distributed in the conclusion without being distributed in its premise, not both premises are negative, and the conclusion is negative exactly when one premise is negative. Distribution is explained in [[syllogistic terms|KSJ9W29KXQ]].
- Translation: in [[monadic predicate logic|SERN6CRVWW]] with the readings of the table, a syllogism is valid in the modern reading exactly when its translation is a valid argument of predicate logic. A [[Venn diagram|0KCT6DPXJK]] with three circles gives a mechanical test.
- Existential import: in the traditional reading "All $S$ are $P$" implies "Some $S$ is $P$". In the modern reading it does not, because both A and E are true when no $S$ exists. The traditional results are the modern results under the extra premise that $S$, $M$ and $P$ are not empty.

### History

Aristotle developed syllogistic in the *Prior Analytics* in the fourth century BC.
He used letters for terms, recognised three figures, and called the four valid moods of the first figure perfect, because their validity needs no proof.
He reduced the other valid moods of his three figures to them.
Medieval logicians gave the valid moods Latin names whose letters encode the reduction, and syllogistic stayed the core of logic teaching until the nineteenth century.
Modern logic treats syllogistic as a small part of predicate logic, namely the monadic fragment without existential assumptions.

### Common errors

- Judging validity by the truth of the conclusion. "All squares are rhombuses, all squares are rectangles, so all rectangles are rhombuses" has true premises and a false conclusion, so the form is invalid; a true conclusion in another instance does not make the form valid.
- Converting an A proposition. From "all $S$ are $P$" one cannot infer "all $P$ are $S$". The fallacy of the undistributed middle often hides this step.
- Forgetting existential import. "All even primes greater than $2$ are divisible by $4$" is true in the modern reading, because there is no such prime, but "some even prime greater than $2$ is divisible by $4$" is false.

## Explanations

### L1 human

A syllogism is a short argument with two starting sentences and one final sentence.
Each sentence says "all", "no", "some" or "some are not" about two groups.
For example: all cats are mammals, all mammals are animals, so all cats are animals.
The group "mammals" links the two starting sentences and then disappears.
If we draw the cats as a circle inside the circle of mammals, and the mammals inside the circle of animals, the cat circle lies inside the animal circle.
The argument works for any three groups that fit the same pattern, for example squares, rectangles and parallelograms.
That is why we can replace the groups by letters and study only the pattern.

### L2 human

We prove Baroco (AOO-2) by reduction to Barbara.

- Major premise: all $P$ are $M$.
- Minor premise: some $S$ is not $M$.
- Conclusion: some $S$ is not $P$.

1. Suppose that the premises are true and the conclusion is false.
2. The conclusion is an O proposition. Its negation is the A proposition "all $S$ are $P$", so this A proposition is true.
3. We form Barbara from "all $P$ are $M$" (major) and "all $S$ are $P$" (minor). Here $P$ is the middle term.
4. Barbara gives "all $S$ are $M$".
5. "All $S$ are $M$" is the negation of the minor premise "some $S$ is not $M$". Both cannot be true.
6. The supposition of step 1 is false, so the conclusion follows from the premises.

A concrete instance: all squares are rhombuses, some rectangles are not rhombuses, so some rectangles are not squares.
The typical use of the reduction is to prove each valid mood from the four perfect moods, so that only four forms must be accepted without proof.
The trap is the choice of the negation in step 2.
The negation of "some $S$ is not $P$" is "all $S$ are $P$", not "no $S$ is $P$".

### L3 human

In modern terms, syllogistic is a fragment of [[monadic predicate logic|SERN6CRVWW]] with three unary predicates and formulas of four shapes.
Validity in this fragment is decidable: a countermodel, when it exists, needs at most one element for each of the $2^3 = 8$ regions of the Venn diagram of $S$, $M$ and $P$.
So the $256$ forms can be checked by a finite search, and the counts $15$ and $24$ come out of such a search.
The difference between the two counts is the existential import of the traditional reading, which predicate logic does not assume; the [[square of opposition|VYNBSVZ2TH]] shows the same difference for single propositions.

Two modern reconstructions of Aristotle's own system exist.
Łukasiewicz read syllogistic as an axiomatic theory, with the moods as true conditional sentences and Barbara and Datisi among the axioms.
Corcoran and Smiley read it as a natural deduction system in which the moods are rules of inference and the reductions are derivations.
The second view puts syllogistic beside [[natural deduction|6KT3BJZ7D1]] and makes the reduction to the first figure a normalisation of proofs.
Syllogistic cannot express relations, and this is a main reason why the logic of Frege and Peirce replaced it.
Venn diagrams test syllogisms with pictures of classes; the [[existential graphs|D3ZS6WHPM1]] of Peirce are a diagram logic that reaches full first-order logic.
