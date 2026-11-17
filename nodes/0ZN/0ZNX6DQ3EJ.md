---
tag: 0ZNX6DQ3EJ
kind: definition
name: Material implication
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 0NMG7W7Q11
uses: [0ZGC7ZESYN]
sources:
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Definition

Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The material implication from $p$ to $q$ is the proposition $p \to q$ whose truth value is given by the table below.
It is false when $p$ is true and $q$ is false, and it is true in the three other rows.

| $p$ | $q$ | $p \to q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

The proposition $p$ is the antecedent of $p \to q$, and the proposition $q$ is the consequent.

## Notation

The formula $p \to q$ is also written $p \supset q$ and $p \Rightarrow q$.
Many books write $\Rightarrow$ only in the metalanguage, between statements, and keep $\to$ for the connective inside formulas.
In tables, the truth values T and F are also written $1$ and $0$.
The formula $p \to q$ is read "if $p$, then $q$", "$p$ implies $q$", "$p$ only if $q$", "$q$ if $p$", "$p$ is sufficient for $q$" and "$q$ is necessary for $p$".

## Remarks

The value of $p \to q$ depends only on the values of $p$ and $q$, so material implication is a binary [[logical connective|QS0XVAN9BG]].
The formula $p \to q$ has the same truth value as $\neg p \lor q$ in each of the four rows.
When $p$ is false, $p \to q$ is true whatever $q$ is: this is [[vacuous truth|0V4QXPGJQK]].
When $q$ is true, $p \to q$ is true whatever $p$ is.
The [[converse|0RVYE75E2M]] $q \to p$ has a different truth table: it is false in the row $p = \mathsf{F}$, $q = \mathsf{T}$.
The concept page [[material implication|0NMG7W7Q11]] gives the examples, the non-examples and the properties.

## Explanations

### L1 human

"If it rains, then the street is wet" is broken only on a day with rain and a dry street.
On a day without rain, the sentence is not broken, whatever the street looks like.
So of the four possible days, only one makes the sentence false.
The table above lists the four days in the order rain and wet, rain and dry, no rain and wet, no rain and dry.

### L2 human

We find the value of "if $5 < 3$, then $5$ is even".

1. The antecedent $p$ is "$5 < 3$". It is false.
2. The consequent $q$ is "$5$ is even". It is false.
3. The row $p = \mathsf{F}$, $q = \mathsf{F}$ of the table gives $\mathsf{T}$.
4. So the implication is true.

The typical use of the table is to evaluate one implication inside a longer formula, one connective at a time.
A trap: the answer in step 4 does not mean that $5 < 3$ "leads to" an even $5$ in any sense of meaning.
The value $\mathsf{T}$ comes only from the false antecedent.
