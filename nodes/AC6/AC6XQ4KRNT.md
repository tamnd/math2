---
tag: AC6XQ4KRNT
kind: concept
name: Barbara
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [~566128b7, S4BTTGFR6J, 1TD6HRM5NG, KSJ9W29KXQ, 0BJR9QR08E, 0GHS47PDAQ, 7MT8CPCEM4]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section B
    note: adopted
    mention: wikipedia://en/76765067#IU2G
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
inventory: [3NW0EMK79W]
---

## Summary

Barbara is the categorical syllogism of mood AAA in the first figure, written AAA-1.
Its form is: all $M$ are $P$, all $S$ are $M$, therefore all $S$ are $P$.
All three propositions are universal affirmatives, the A propositions of [[syllogistic|~566128b7]].
Barbara is valid: whenever both premises are true, the conclusion is true.
In the language of sets it says that $S \subseteq M$ and $M \subseteq P$ give $S \subseteq P$.

## Motivation

Barbara is the pattern behind every chain of "all" statements.
Mathematics uses it all the time, often without naming it: every square is a rectangle, every rectangle is a parallelogram, so every square is a parallelogram.
Aristotle took the moods of the first figure as perfect, meaning that their validity is evident without proof.
The other valid moods are proved by reducing them to these four, and Barbara is the first of them.

## Notation

The three [[terms|KSJ9W29KXQ]] are the minor term $S$, the middle term $M$ and the major term $P$.

| Line | Sentence | Set form | Predicate logic |
|---|---|---|---|
| major premise | all $M$ are $P$ | $M \subseteq P$ | $\forall x\,(M(x) \to P(x))$ |
| minor premise | all $S$ are $M$ | $S \subseteq M$ | $\forall x\,(S(x) \to M(x))$ |
| conclusion | all $S$ are $P$ | $S \subseteq P$ | $\forall x\,(S(x) \to P(x))$ |

The name is a medieval memory aid: its three vowels a, a, a give the [[mood|1TD6HRM5NG]] AAA.
The label AAA-1 gives the mood and the [[figure|S4BTTGFR6J]].

## Remarks

### Examples

- [[Barbara for squares, rectangles and parallelograms|~943d5024]]: the syllogism is checked to be AAA-1 and proved valid in three ways.
- [[A chain of divisibility facts by Barbara|~84f820f1]]: two uses of Barbara in a row prove that every multiple of $12$ has a digit sum divisible by $3$.

### Non-examples

- [[The fallacy of the undistributed middle|~a7484779]]: "all $P$ are $M$, all $S$ are $M$, so all $S$ are $P$" has the mood AAA but the second figure. It is invalid.
- "All $M$ are $P$, all $M$ are $S$, so all $S$ are $P$" (AAA-3) is invalid. The multiples of $4$ are even and are integers, but not every integer is even.

### Basic properties

- Barbara is valid in the traditional reading and in the modern reading, because its proof uses no assumption that a term is non-empty.
- Barbara is the transitivity of the [[subset|0BJR9QR08E]] relation: $S \subseteq M \subseteq P$ gives $S \subseteq P$.
- In predicate logic, Barbara is the [[universal|0GHS47PDAQ]] form of the [[hypothetical syllogism|7MT8CPCEM4]]: from $A \to B$ and $B \to C$ infer $A \to C$, for every object at once.
- The mood names that begin with B, such as Baroco, Bocardo and Bamalip, reduce to Barbara.
- Baroco and Bocardo reduce to Barbara by reduction to contradiction.
- Weakening the conclusion to "some $S$ is $P$" gives Barbari (AAI-1), which is valid only when $S$ is not empty.
- Barbara is the only valid syllogism whose conclusion is an A proposition. In each other valid mood the conclusion is E, I or O.

### History

Aristotle's Prior Analytics treats the moods of the first figure, Barbara among them, as perfect syllogisms.
The name Barbara comes from the medieval Latin names of the moods, in which the vowels give the mood.

### Common errors

- Reversing a premise: "all $P$ are $M$" in place of "all $M$ are $P$" gives the undistributed middle, which is invalid.
- Reversing the conclusion: Barbara proves $S \subseteq P$ and says nothing about $P \subseteq S$.
- Confusing validity with truth: Barbara with a false premise is still valid, but it does not prove its conclusion.

## Explanations

### L1 human

Barbara is the rule "if every $S$ is an $M$, and every $M$ is a $P$, then every $S$ is a $P$".
Draw a circle for $S$ inside a circle for $M$, and the circle for $M$ inside a circle for $P$.
Then the circle for $S$ is inside the circle for $P$.
For example, every cat is a mammal and every mammal is an animal, so every cat is an animal.
The three letters "a" in the name stand for the three "all" sentences.

### L2 human

We prove that Barbara is the only valid mood with an A conclusion.

1. An A conclusion "all $S$ are $P$" distributes its subject $S$.
2. By the rules of the syllogism, a valid syllogism with a universal conclusion needs two universal premises, and with an affirmative conclusion it needs two affirmative premises. So both premises are A.
3. The minor term $S$ is distributed in the conclusion, so it must be distributed in the minor premise. In an A proposition only the subject is distributed, so the minor premise is "all $S$ are $M$".
4. The middle term must be distributed at least once. It is not distributed in "all $S$ are $M$", so the major premise must have $M$ as subject: "all $M$ are $P$".
5. These premises are those of Barbara.

The typical use of this argument is to see how the rules of distribution pin down a mood.
The trap is to forget step 4: "all $P$ are $M$" is also an A proposition, but it leaves $M$ undistributed.

### L3 human

In predicate logic, Barbara is the derivation of $\forall x\,(S(x) \to P(x))$ from $\forall x\,(M(x) \to P(x))$ and $\forall x\,(S(x) \to M(x))$.
Instantiate both premises at a fresh variable $a$, chain the two implications, and generalize over $a$.
The derivation needs no existence assumption, unlike the derivation of Barbari.
In category-theoretic terms, inclusion of classes is a preorder, and Barbara is the composition of two arrows in it.
The same pattern holds for any transitive relation, for example $a < b$ and $b < c$ give $a < c$, but syllogistic itself has only the relation of inclusion.
