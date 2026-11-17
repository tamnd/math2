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

Let $\varphi$ and $\psi$ be formulas of [[propositional logic|09K9MWD2QQ]], and let $p_1, \ldots, p_n$ be the propositional variables that occur in $\varphi$ or in $\psi$.
A valuation is an assignment of a truth value, T or F, to each of $p_1, \ldots, p_n$.
The formulas $\varphi$ and $\psi$ are logically equivalent when, under each of the $2^n$ valuations, $\varphi$ and $\psi$ have the same truth value.

## Notation

We write $\varphi \equiv \psi$, and $\varphi \not\equiv \psi$ when the formulas are not logically equivalent.
Other books write $\varphi \Leftrightarrow \psi$.
The symbol $\equiv$ is not a connective: $\varphi \equiv \psi$ is a statement about the two formulas, not a new formula.
The connective that forms a new formula is the [[biconditional|0S6GMNJ62Y]] $\leftrightarrow$.
In proofs, the arrows $\Rightarrow$ and $\Leftrightarrow$ often stand between statements as metalanguage, while $\to$ and $\leftrightarrow$ stand inside formulas.

## Remarks

The formulas $\varphi$ and $\psi$ are logically equivalent exactly when $\varphi \leftrightarrow \psi$ is a [[tautology|0D1AHYPM8N]].
The reason is that $\varphi \leftrightarrow \psi$ is true under a valuation exactly when $\varphi$ and $\psi$ have the same truth value under it.
A [[truth table|05RSK4Q657]] with one row for each valuation tests the definition: the columns of $\varphi$ and $\psi$ must agree in every row.
A variable that occurs in only one of the two formulas still counts: $p \lor \neg p$ and $q \lor \neg q$ are equivalent, since both are true in all four rows for $p$ and $q$.
For formulas of first-order logic, "valuation" is replaced by "structure together with an assignment of values to the free variables".
The concept page [[logical equivalence|0JMR2HM2N2]] gives the examples, the non-examples and the first properties.

## Explanations

### L1 human

Two formulas are logically equivalent when they are true in the same cases and false in the same cases.
For example, "not (it is cold and it rains)" and "it is not cold or it does not rain" are both false only when it is cold and it rains.
So the two formulas are equivalent, and one can replace the other.

### L2 human

To test $p \to q \equiv \neg p \lor q$, we compute both columns.

1. Row TT: $p \to q$ is T, and $\neg p \lor q$ is $\mathrm{F} \lor \mathrm{T}$, which is T.
2. Row TF: $p \to q$ is F, and $\neg p \lor q$ is $\mathrm{F} \lor \mathrm{F}$, which is F.
3. Row FT: $p \to q$ is T, and $\neg p \lor q$ is $\mathrm{T} \lor \mathrm{T}$, which is T.
4. Row FF: $p \to q$ is T, and $\neg p \lor q$ is $\mathrm{T} \lor \mathrm{F}$, which is T.

The columns agree in all four rows, so the formulas are equivalent.
A trap is to stop after a row in which the columns agree: one row with different values is enough to show $\varphi \not\equiv \psi$, but agreement needs all rows.
