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

Material implication joins two propositions into the proposition that the first does not hold without the second.
Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The material implication from $p$ to $q$ is the proposition $p \to q$, read "if $p$, then $q$".
It is false when $p$ is true and $q$ is false, and true in the three other rows:

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
The formula is read "if $p$, then $q$", "$p$ implies $q$", "$p$ only if $q$", "$q$ if $p$", "$p$ is sufficient for $q$" and "$q$ is necessary for $p$".

## Remarks

The value of $p \to q$ depends only on the values of $p$ and $q$, so material implication is a binary [[logical connective|QS0XVAN9BG]].
In each of the four rows, $p \to q$ has the same value as $\neg p \lor q$.

Two rows give shortcuts.
When $p$ is false, $p \to q$ is true whatever $q$ is, which is [[vacuous truth|0V4QXPGJQK]].
When $q$ is true, $p \to q$ is true whatever $p$ is.
The [[converse|09A3N7ZN5G]] $q \to p$ has a different table: it is false in the row $p$ F, $q$ T.
The concept page [[material implication|0NMG7W7Q11]] gives the examples, the non-examples and the laws.

## Explanations

### L1 human

"If it rains, then the street is wet" is broken only on a day with rain and a dry street.
On a day without rain, the sentence is not broken, whatever the street looks like.
So of the four possible days, only one makes the sentence false.
The table lists the four days in the order rain and wet, rain and dry, no rain and wet, no rain and dry.

### L2 human

Find the value of "if $5 < 3$, then $5$ is even".

1. The antecedent "$5 < 3$" is false.
2. The consequent "$5$ is even" is false.
3. The row FF of the table gives T, so the implication is true.

The table is used in this way to evaluate one implication inside a longer formula, one connective at a time.
Watch out: the answer does not mean that $5 < 3$ "leads to" an even $5$ in any sense of meaning.
The value T comes only from the false antecedent.
