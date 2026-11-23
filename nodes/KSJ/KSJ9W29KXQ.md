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

The terms of a syllogism are the three classes it talks about, and each has a fixed job: two of them meet in the conclusion, and the third links them in the premises and then drops out.
Whether a syllogism is valid depends only on where the three terms stand and on which of them the sentences speak about in full.

Take "all multiples of $4$ are even, some squares are multiples of $4$, so some squares are even".
The conclusion is about squares, so "squares" is the minor term.
It says they are even, so "even numbers" is the major term.
"Multiples of $4$" appears in both premises and not in the conclusion, so it is the middle term.

In exact terms, a term of syllogistic is a word or phrase that names a class of things.
A categorical proposition joins a subject term and a predicate term.
A categorical syllogism has exactly three terms: the major term is the predicate of the conclusion, the minor term is its subject, and the middle term occurs in both premises and not in the conclusion.
The premise that contains the major term is the major premise, and the premise that contains the minor term is the minor premise.
A term is distributed in a proposition when the proposition says something about every member of the class that the term names.

## Motivation

The argument "all rectangles are parallelograms, all squares are rectangles, so all squares are parallelograms" gets its force from the class of rectangles.
That class links the two premises and then disappears.
To describe such arguments in general, we need names for the three roles, and these are the minor, middle and major terms.
Distribution then explains why some arrangements of the terms give valid arguments and others do not.
It turns the test of validity into a few checks that you can do by eye, before you draw a [[Venn diagram|0KCT6DPXJK]].
The roles of the terms define the [[figures|S4BTTGFR6J]] and the [[moods|1TD6HRM5NG]] of [[Aristotelian syllogistic|MZBNX2T6Q6]].

## Notation

The minor, middle and major terms are written $S$, $M$ and $P$, from "subject", "middle" and "predicate".
Distribution in the four categorical propositions follows one rule: universal propositions distribute their subject, and negative propositions distribute their predicate.

| Proposition | Subject distributed | Predicate distributed |
|---|---|---|
| A: all $S$ are $P$ | yes | no |
| E: no $S$ is $P$ | yes | yes |
| I: some $S$ is $P$ | no | no |
| O: some $S$ is not $P$ | no | yes |

## Remarks

### Reading distribution

"No triangle is a square" distributes both terms.
It excludes every triangle from the squares, and also every square from the triangles.
"Some primes are not odd" distributes its predicate: it says that a certain prime lies outside the whole class of odd numbers.
"All squares are rectangles" does not distribute its predicate, because it says nothing about the rectangles that are not squares.
Simple conversion keeps the distribution of both terms in E and I, and this is why E and I convert and A and O do not.

### The two rules about terms

A valid syllogism distributes its middle term in at least one premise.
Otherwise the two premises can speak about different parts of the middle class, as in the [[undistributed middle|F8BP8S0RYG]]: squares and rectangles are both parallelograms, but different ones.
A term that is distributed in the conclusion of a valid syllogism is distributed in its premise.
Breaking this rule is called the illicit major or the illicit minor.
For example, take "all multiples of $4$ are even, no number of the form $4k + 2$ is a multiple of $4$, so no number of the form $4k + 2$ is even".
The E conclusion speaks about every even number, but the A premise "all multiples of $4$ are even" does not.
The conclusion is false, since $2 = 4 \cdot 0 + 2$ is even, so the form is invalid by an illicit major.

### What is not a term

"Is a side of" is not a term.
It names a relation between two objects, not a class, so it cannot be the subject or the predicate of a categorical proposition.
In "all squares are rhombuses, all rectangles are parallelograms, so all squares are parallelograms" no term is a middle term: the argument has [[four terms|S174DQ9N4T]], and no term occurs in both premises.

### Watch out

The major term is defined by the conclusion, not by the order in the text.
In "some squares are even, because all multiples of $4$ are even and some squares are multiples of $4$", the major premise comes first only after we rearrange.
A word with two meanings is two terms.
In "every square is a rectangle, $9$ is a square, so $9$ is a rectangle", "square" means a figure once and a number once.
And "some" does not distribute the subject: "some primes are odd" says nothing about every prime.

### History

Aristotle introduced the major, the minor and the middle term in the *Prior Analytics*.
The doctrine of distribution comes from medieval logic, and it became the basis of the textbook rules of validity.

### Try it

Which terms are distributed in "no rational number is a square root of $2$"?
Both, because it is an E proposition: it excludes every rational number and every square root of $2$.

Find the middle term of "no integer is a square root of $2$, since no rational number is one and every integer is rational".
It is "rational numbers", the only term in both premises; it is distributed in the E premise, so the first rule holds.

## Explanations

### L1 human

A syllogism talks about three groups of things.
Two groups appear in the conclusion, and the third group links them in the premises.
In "all cats are mammals, all mammals are animals, so all cats are animals", the groups are cats, mammals and animals.
The linking group "mammals" is the middle term, and it does not appear in the conclusion.
"Cats" is the minor term, because the conclusion is about cats, and "animals" is the major term.

### L2 human

We find the terms of "some squares are even, because all multiples of $4$ are even and some squares are multiples of $4$", and we check the distribution rules.

1. The conclusion is "some squares are even numbers", so "squares" is the minor term and "even numbers" is the major term.
2. The middle term is "multiples of $4$", the only term that occurs in both premises.
3. The major premise is "all multiples of $4$ are even", because it contains the major term, and the minor premise is "some squares are multiples of $4$".
4. The major premise is an A proposition, so it distributes its subject, the middle term.
5. The conclusion is an I proposition, so it distributes no term, and the second rule has nothing to check.

This check of the distribution rules is the usual first step before a full test of validity.
The trap is the order in the text: here the major premise came second in the sentence, and the roles still come from the conclusion.
