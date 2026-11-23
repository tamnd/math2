---
tag: 06GYGS41JK
kind: definition
name: Logical equivalence
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 0JMR2HM2N2
uses: [0ZGC7ZESYN, 05RSK4Q657, 0V6GAWTBYW, 0D1AHYPM8N]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_equivalence
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
  - book: isbn:9780122384523
    locator: Section 1.2
inventory: [EHDGX0E9G8]
---

## Definition

Logical equivalence is the relation between two formulas that take the same truth value in every possible case.

Let $\varphi$ and $\psi$ be formulas of [[propositional logic|09K9MWD2QQ]], and let $p_1, \ldots, p_n$ be the propositional variables that occur in $\varphi$ or in $\psi$.
A valuation is an assignment of a truth value, T or F, to each of $p_1, \ldots, p_n$.
The formulas $\varphi$ and $\psi$ are logically equivalent when, under each of the $2^n$ valuations, $\varphi$ and $\psi$ have the same truth value.

## Notation

We write $\varphi \equiv \psi$, and $\varphi \not\equiv \psi$ when the formulas are not logically equivalent.
Other books write $\varphi \Leftrightarrow \psi$.
The symbol $\equiv$ is not a connective: $\varphi \equiv \psi$ is a statement about the two formulas, not a new formula.
The connective that forms a new formula is the [[biconditional|0S6GMNJ62Y]] $\leftrightarrow$.

## Remarks

The definition quantifies over all valuations, and that is its whole content.
Two formulas that agree under one valuation, or under most of them, are not yet equivalent.
So a test by [[truth table|05RSK4Q657]] must compare the two columns in every row.

The valuations range over the variables of both formulas together.
This matters when a variable occurs on one side only: $p \lor \neg p$ and $q \lor \neg q$ are equivalent, because both are true in all four rows for $p$ and $q$.

An equivalent form of the definition uses one formula instead of two.
The biconditional $\varphi \leftrightarrow \psi$ is true under a valuation exactly when $\varphi$ and $\psi$ have the same value there.
So $\varphi \equiv \psi$ holds exactly when $\varphi \leftrightarrow \psi$ is a [[tautology|0D1AHYPM8N]].

For a small example, $p \to q$ and $\neg p \lor q$ are equivalent: both are false in the row $p$ T, $q$ F and true in the other three rows.
For a case that fails, $p \to q$ and $q \to p$ are not equivalent, because in the row $p$ T, $q$ F the first is false and the second is true.
For formulas of first-order logic, "valuation" becomes "structure together with an assignment of values to the free variables".
The concept page [[logical equivalence|0JMR2HM2N2]] has the standard equivalences and the rules for using them.

## Explanations

### L1 human

Two formulas are logically equivalent when they are true in the same cases and false in the same cases.
"Not (it is cold and it rains)" and "it is not cold or it does not rain" are both false only when it is cold and it rains.
So the two are equivalent, and one can replace the other.

### L2 human

To test $p \to q \equiv \neg p \lor q$, compute both values in each of the four rows.

1. Row TT: $p \to q$ is T, and $\neg p \lor q$ is $\mathrm{F} \lor \mathrm{T}$, which is T.
2. Row TF: $p \to q$ is F, and $\neg p \lor q$ is $\mathrm{F} \lor \mathrm{F}$, which is F.
3. Row FT: $p \to q$ is T, and $\neg p \lor q$ is $\mathrm{T} \lor \mathrm{T}$, which is T.
4. Row FF: $p \to q$ is T, and $\neg p \lor q$ is $\mathrm{T} \lor \mathrm{F}$, which is T.

The values agree in all four rows, so the formulas are equivalent.
Watch out: one row with different values proves $\varphi \not\equiv \psi$, but agreement needs every row.
