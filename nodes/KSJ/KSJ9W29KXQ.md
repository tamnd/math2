---
tag: KSJ9W29KXQ
kind: concept
name: Syllogistic terms
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
uses: [0ZGC7ZESYN, 0QHEWQD30B]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section S
    note: adopted
    mention: wikipedia://en/76765067#U59P
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Term_logic
    locator: lead section
inventory: [8R9V7XC3BF]
---

## Summary

A term of syllogistic is a word or phrase that names a class of things, such as "prime numbers" or "rectangles".
A categorical proposition joins two terms: its subject term and its predicate term.
A categorical syllogism has exactly three terms.
The major term is the predicate of the conclusion, the minor term is the subject of the conclusion, and the middle term occurs in both premises and not in the conclusion.
The premise that contains the major term is the major premise, and the premise that contains the minor term is the minor premise.
A term is distributed in a proposition when the proposition says something about every member of the class that the term names.
Terms matter because the validity of a syllogism depends only on where its three terms stand and on which of them are distributed.

## Motivation

The argument "all rectangles are parallelograms, all squares are rectangles, so all squares are parallelograms" is about three classes.
Its force comes from the class "rectangles", which links the two premises and then drops out.
To describe such arguments in general, one needs names for the three roles: the two classes that the conclusion joins and the class that links them.
These roles are the minor, major and middle terms.
The idea of distribution then explains why some arrangements of the terms give valid arguments and others do not.

## Notation

The minor, middle and major terms are written $S$, $M$ and $P$, from "subject", "middle" and "predicate".
Distribution in the four categorical propositions is as follows.

| Proposition | Subject distributed | Predicate distributed |
|---|---|---|
| A: all $S$ are $P$ | yes | no |
| E: no $S$ is $P$ | yes | yes |
| I: some $S$ is $P$ | no | no |
| O: some $S$ is not $P$ | no | yes |

A short rule: universal propositions distribute their subject, and negative propositions distribute their predicate.

## Remarks

### Examples

- In "all multiples of $4$ are even, some squares are multiples of $4$, so some squares are even", the minor term is "squares", the major term is "even numbers" and the middle term is "multiples of $4$".
- In "no rational number is a square root of $2$, every integer is a rational number, so no integer is a square root of $2$", the middle term is "rational numbers". It is distributed in the major premise, which is an E proposition.
- In "no triangle is a square", both terms are distributed: the sentence excludes every triangle from the class of squares and every square from the class of triangles.
- In "some primes are not odd", the predicate "odd numbers" is distributed: the sentence says that a certain prime lies outside the whole class of odd numbers.

### Non-examples

- "Is a side of" is not a term. It names a relation between two objects, not a class, so it cannot be the subject or the predicate of a categorical proposition.
- In "all squares are rectangles", the predicate "rectangles" is not distributed. The sentence says nothing about the rectangles that are not squares.
- In "all squares are rhombuses, all rectangles are parallelograms, so all squares are parallelograms", no term is a middle term. The argument has four terms, and no term occurs in both premises.

### Basic properties

- A valid syllogism distributes its middle term in at least one premise. If it does not, the two premises can speak about different parts of the middle class, as in the [[undistributed middle|F8BP8S0RYG]].
- A term that is distributed in the conclusion of a valid syllogism is distributed in its premise. Breaking this rule is the fallacy of the illicit major or of the illicit minor term.
- The place of the middle term in the two premises is the [[figure|S4BTTGFR6J]] of the syllogism.
- Simple conversion keeps the distribution of both terms for E and I, and this is why E and I convert and A and O do not.

### History

Aristotle introduced the major, the minor and the middle term in the *Prior Analytics*.
The doctrine of distribution comes from later, medieval logic, and it became the basis of the textbook rules of validity.

### Common errors

- Choosing the major term from the first premise in the text. The major term is defined by the conclusion: it is the predicate of the conclusion.
- Taking a term with two meanings as one term. Then the argument has four terms in fact, and the conclusion need not follow.
- Thinking that "some" distributes the subject. "Some primes are odd" says nothing about every prime.

## Explanations

### L1 human

A syllogism talks about three groups of things.
Two groups appear in the conclusion, and the third group links them in the two premises.
In "all cats are mammals, all mammals are animals, so all cats are animals", the groups are cats, mammals and animals.
The linking group "mammals" is the middle term, and it does not appear in the conclusion.
"Cats" is the minor term, because the conclusion is about cats, and "animals" is the major term.

### L2 human

We find the terms of the argument "some squares are even, because all multiples of $4$ are even and some squares are multiples of $4$", and we check the distribution rules.

1. The conclusion is "some squares are even numbers". Its subject "squares" is the minor term, and its predicate "even numbers" is the major term.
2. The middle term is "multiples of $4$", the only term that occurs in both premises.
3. The major premise is "all multiples of $4$ are even", because it contains the major term. The minor premise is "some squares are multiples of $4$".
4. The major premise is an A proposition, so it distributes its subject "multiples of $4$". So the middle term is distributed at least once.
5. The conclusion is an I proposition, so it distributes no term, and the rule on terms distributed in the conclusion holds.

The typical use of the terms is this check of the distribution rules before a full test of validity.
The trap is the order of the premises in the text: here the major premise came second in the sentence, and the roles still come from the conclusion.
