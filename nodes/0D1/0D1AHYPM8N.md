---
tag: 0D1AHYPM8N
kind: definition
name: Tautology
msc: [03B05]
defines: 05006AJ7DZ
uses: [09K9MWD2QQ, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Tautology_(logic)
    locator: lead section
---

## Definition

Let $\varphi$ be a formula of [[propositional logic|09K9MWD2QQ]] with the propositional variables $p_1, \dots, p_n$.
The formula $\varphi$ is a tautology when $\varphi$ is true for each of the $2^n$ assignments of truth values to $p_1, \dots, p_n$.

## Remarks

Examples are $p \lor \neg p$ and $p \to p$.
A formula that is false for each assignment is a contradiction.
A [[truth table|05RSK4Q657]] decides in a finite number of steps whether a formula is a tautology.

## Explanations

### L1 human

A tautology is true only because of its form.
The sentence "it rains or it does not rain" is true whatever the weather.
Its form $p \lor \neg p$ is a tautology.
