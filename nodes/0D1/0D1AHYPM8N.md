---
tag: 0D1AHYPM8N
kind: definition
name: Tautology
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 05006AJ7DZ
uses: [09K9MWD2QQ, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Tautology_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 1.2
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Definition

The sentence "if I passed both tests, then I passed the math test" has the form $(p \land q) \to p$, and it is true in all four rows of its table, whatever the results were.
Formulas like this one are the tautologies.

Let $\varphi$ be a formula of [[propositional logic|09K9MWD2QQ]] with the propositional variables $p_1, \dots, p_n$.
The formula $\varphi$ is a tautology when $\varphi$ is true for each of the $2^n$ assignments of truth values to $p_1, \dots, p_n$.
It is a contradiction when $\varphi$ is false for each of these assignments.
It is a contingency when it is neither a tautology nor a contradiction, that is, when it is true for some assignment and false for another.

## Notation

The metalanguage writes $\models \varphi$ for "$\varphi$ is a tautology".
Some books say "valid formula" for tautology and "unsatisfiable formula" for contradiction.
Truth values are written T and F, or $1$ and $0$.

## Remarks

### Small examples

Examples of tautologies are $p \lor \neg p$, $p \to p$ and $(p \land q) \to p$.
The formula $p \land \neg p$ is a contradiction, and $p \to q$ is a contingency.

### Which variables count

The value of $\varphi$ under an assignment depends only on the values of the variables that occur in $\varphi$.
So the definition does not depend on which further variables are listed.
The constant $\top$ counts as a tautology and $\bot$ as a contradiction, each with $n = 0$ variables and a single row.

### A finite test

A [[truth table|05RSK4Q657]] lists the $2^n$ assignments, so it decides in a finite number of steps which of the three cases holds.

## Explanations

### L1 human

A tautology is true only because of its form.
The sentence "it rains or it does not rain" is true whatever the weather.
Its form $p \lor \neg p$ is a tautology.
The sentence "it rains and it does not rain" is false whatever the weather, so its form is a contradiction.

### L2 human

To show that $(p \land q) \to p$ is a tautology, we check its $4$ rows.

1. The implication can be false only in a row where $p \land q$ is T and $p$ is F.
2. If $p \land q$ is T, then $p$ is T.
3. So no row makes the formula false, and its column is T, T, T, T.

To prove a tautology, it is enough to show that no assignment makes it false.
Watch out: one true row, or many, does not make a tautology, since every row must be true.
