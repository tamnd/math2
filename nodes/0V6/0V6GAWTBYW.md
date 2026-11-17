---
tag: 0V6GAWTBYW
kind: definition
name: Biconditional
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 0S6GMNJ62Y
uses: [0ZGC7ZESYN, 0ZNX6DQ3EJ, 0M28ASWG8T]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_biconditional
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Definition

Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The biconditional of $p$ and $q$ is the proposition $p \leftrightarrow q$ whose truth value is given by the table below.
It is true when $p$ and $q$ are both true or both false, and false otherwise.

| $p$ | $q$ | $p \leftrightarrow q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

## Notation

The formula $p \leftrightarrow q$ is also written $p \equiv q$ and $p \Leftrightarrow q$.
It is read "$p$ if and only if $q$", "$p$ iff $q$", "$p$ exactly when $q$" and "$p$ is necessary and sufficient for $q$".
Many books use $\Leftrightarrow$ and $\equiv$ only in the metalanguage, between statements, and keep $\leftrightarrow$ for the connective inside formulas.
In Lean and Mathlib the biconditional is `Iff`, written `a ↔ b`.
In tables, the truth values T and F are also written $1$ and $0$.

## Remarks

The value of $p \leftrightarrow q$ depends only on the values of $p$ and $q$, so the biconditional is a binary [[logical connective|QS0XVAN9BG]].
In each of the four rows, $p \leftrightarrow q$ has the same value as $(p \to q) \land (q \to p)$, where $\to$ is [[material implication|0ZNX6DQ3EJ]] and $\land$ is [[conjunction|0M28ASWG8T]].
For example, in the row $p = \mathsf{T}$, $q = \mathsf{F}$, the implication $p \to q$ is false, so the conjunction is false, as is $p \leftrightarrow q$.
The concept page [[biconditional|0S6GMNJ62Y]] gives the examples, the non-examples, the properties and the method of proof in two directions.

## Explanations

### L1 human

"The light is on if and only if the switch is up" says two things.
When the switch is up, the light is on.
When the light is on, the switch is up.
The sentence is true when both parts are true and when both parts are false.
It is false when one part is true and the other is false, for example a lit lamp with the switch down.

### L2 human

We find the value of "$7$ is prime if and only if $7$ is even".

1. The left side "$7$ is prime" is true, because the only positive divisors of $7$ are $1$ and $7$.
2. The right side "$7$ is even" is false, because $7 = 2 \cdot 3 + 1$.
3. The row $p = \mathsf{T}$, $q = \mathsf{F}$ of the table gives $\mathsf{F}$.
4. So the biconditional is false.

The typical use of the table is to check one biconditional inside a longer formula.
A trap: a true biconditional does not say that its two sides are true.
"$4$ is odd if and only if $9$ is even" is true, because both sides are false.
