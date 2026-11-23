---
tag: AC6XQ4KRNT
kind: concept
name: Barbara
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [MZBNX2T6Q6, S4BTTGFR6J, 1TD6HRM5NG, KSJ9W29KXQ, 0BJR9QR08E, 0GHS47PDAQ, 7MT8CPCEM4]
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

Barbara is the syllogism that chains two "all" statements: if every $S$ is an $M$ and every $M$ is a $P$, then every $S$ is a $P$.
It is the oldest named rule of logic, and it is the transitivity of inclusion written in words.

For example: all rectangles are parallelograms, all squares are rectangles, so all squares are parallelograms.
In sets, the premises say $\text{squares} \subseteq \text{rectangles}$ and $\text{rectangles} \subseteq \text{parallelograms}$, and the conclusion follows.

In exact terms, Barbara is the categorical syllogism of mood AAA in the first figure, written AAA-1:
$$\text{all } M \text{ are } P, \quad \text{all } S \text{ are } M, \quad \text{therefore all } S \text{ are } P.$$
All three propositions are universal affirmatives, the A propositions of [[Aristotelian syllogistic|MZBNX2T6Q6]].
Barbara is valid: every choice of classes that makes both premises true makes the conclusion true.

## Motivation

Barbara is the pattern behind every chain of "all" statements, and mathematics uses it constantly without naming it.
Each time a proof says "every group of prime order is cyclic, and every cyclic group is abelian, so every group of prime order is abelian", it uses Barbara.
Aristotle took the four moods of the first figure as perfect, meaning that their validity is evident without proof.
He then proved the other valid moods by reducing them to these four, and Barbara is the first of them.
In modern logic Barbara becomes a short derivation in predicate logic, and that derivation is a first example of the proofs studied in [[rules of inference|QPD3X471Q1]].

## Notation

The three [[terms|KSJ9W29KXQ]] are the minor term $S$, the middle term $M$ and the major term $P$.

| Line | Sentence | Set form | Predicate logic |
|---|---|---|---|
| major premise | all $M$ are $P$ | $M \subseteq P$ | $\forall x\,(M(x) \to P(x))$ |
| minor premise | all $S$ are $M$ | $S \subseteq M$ | $\forall x\,(S(x) \to M(x))$ |
| conclusion | all $S$ are $P$ | $S \subseteq P$ | $\forall x\,(S(x) \to P(x))$ |

The name is a medieval memory aid: its three vowels a, a, a give the [[mood|1TD6HRM5NG]] AAA, and the label AAA-1 adds the [[figure|S4BTTGFR6J]].

## Remarks

### Why it is valid

Let $x$ be any element of $S$.
By the minor premise $x \in M$, and by the major premise $x \in P$.
So every element of $S$ lies in $P$, which is the conclusion.
The argument never needs an element to exist, so Barbara is valid in the traditional and in the modern reading.
In predicate logic it is the [[universal|0GHS47PDAQ]] form of the [[hypothetical syllogism|7MT8CPCEM4]]: from $A \to B$ and $B \to C$ infer $A \to C$, for every object at once.

### Two worked instances

[[Barbara for squares, rectangles and parallelograms|RKJG1VXH8E]] checks the mood and the figure and proves validity in three ways: with sets, with predicate logic and with a Venn diagram.
[[A chain of divisibility facts by Barbara|ZSEGKSZK6Y]] uses Barbara twice in a row to show that every multiple of $12$ has a digit sum divisible by $3$.
Its first step is
$$\text{multiples of } 12 \subseteq \text{multiples of } 6 \subseteq \text{multiples of } 3.$$

### Near misses

Move the middle term and the form breaks.
"All $P$ are $M$, all $S$ are $M$, so all $S$ are $P$" (AAA-2) is the [[fallacy of the undistributed middle|F8BP8S0RYG]].
"All $M$ are $P$, all $M$ are $S$, so all $S$ are $P$" (AAA-3) is invalid as well: the multiples of $4$ are even and are integers, but not every integer is even.
Weaken the conclusion to "some $S$ is $P$" and you get Barbari (AAI-1), which is valid only when $S$ is not empty.

### Barbara among the moods

Barbara is the only valid syllogism whose conclusion is an A proposition.
The reason is short.
An A conclusion needs two affirmative and two universal premises, so both premises are A.
The minor term is distributed in the conclusion, so it must be the subject of the minor premise, "all $S$ are $M$".
The middle term must then be distributed in the major premise, so that premise is "all $M$ are $P$".
In the medieval names, the moods that begin with B, such as Baroco and Bocardo, are reduced to Barbara; those two need a proof by contradiction.

### Watch out

Barbara proves $S \subseteq P$ and says nothing about $P \subseteq S$.
"All squares are parallelograms" is true, and "all parallelograms are squares" is false.
Reversing a premise is the most common error: "all $P$ are $M$" in place of "all $M$ are $P$" gives the undistributed middle.
And Barbara with a false premise is still valid, but it proves nothing: "all primes are odd, all primes greater than $10$ are primes, so all primes greater than $10$ are odd" has a true conclusion and a false major premise.

### History

Aristotle's *Prior Analytics* treats the moods of the first figure, Barbara among them, as perfect syllogisms.
The name comes from the medieval Latin names of the moods, in which the vowels give the mood.

### Try it

Write the proof of "every square matrix with a zero row is singular" as Barbara, with the middle term "square matrices with determinant $0$".
All matrices with determinant $0$ are singular, all square matrices with a zero row have determinant $0$, so all square matrices with a zero row are singular.

Is "all rhombuses are parallelograms, all squares are parallelograms, so all squares are rhombuses" Barbara?
No: the middle term is the predicate of both premises, so the form is AAA-2, which is invalid, although its conclusion happens to be true.

## Explanations

### L1 human

Barbara is the rule "if every $S$ is an $M$, and every $M$ is a $P$, then every $S$ is a $P$".
Draw a circle for $S$ inside a circle for $M$, and the circle for $M$ inside a circle for $P$.
Then the circle for $S$ is inside the circle for $P$.
For example, every cat is a mammal and every mammal is an animal, so every cat is an animal.
The three letters "a" in the name stand for the three "all" sentences.

### L2 human

We derive Barbara in predicate logic.
The premises are $\forall x\,(M(x) \to P(x))$ and $\forall x\,(S(x) \to M(x))$.

1. Take an arbitrary object $a$ and assume $S(a)$.
2. The minor premise, instantiated at $a$, gives $S(a) \to M(a)$, so $M(a)$ by modus ponens.
3. The major premise, instantiated at $a$, gives $M(a) \to P(a)$, so $P(a)$ by modus ponens.
4. Discharging the assumption gives $S(a) \to P(a)$.
5. The object $a$ was arbitrary, so we may generalize: $\forall x\,(S(x) \to P(x))$.

The derivation uses no assumption that anything exists, which is why Barbara survives in the modern reading.
The trap is step 5: we may generalize only because $a$ appears in no premise.

### L3 human

Inclusion of classes is a preorder, and Barbara is its transitivity.
In the language of category theory, a preorder is a category with at most one arrow between two objects, and Barbara is the composition of two arrows.
The same pattern holds for every transitive relation, such as $a < b$ and $b < c$ giving $a < c$, but syllogistic itself has only inclusion and its relatives.
Modern logic generalizes Barbara to the rule of the [[hypothetical syllogism|7MT8CPCEM4]] under a quantifier, and to the cut rule of sequent calculi, which chains a proof of $M$ from $S$ with a proof of $P$ from $M$.
