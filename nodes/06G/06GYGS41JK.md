---
tag: 06GYGS41JK
kind: definition
name: Logical equivalence
msc: [03B05]
defines: 0JMR2HM2N2
uses: [05RSK4Q657, 0V6GAWTBYW, 0D1AHYPM8N]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_equivalence
    locator: lead section
---

## Definition

Let $\varphi$ and $\psi$ be formulas of [[propositional logic|09K9MWD2QQ]].
The formulas $\varphi$ and $\psi$ are logically equivalent when they have the same truth value for each assignment of truth values to their variables.
This is written $\varphi \equiv \psi$.

## Remarks

The formulas $\varphi$ and $\psi$ are logically equivalent exactly when $\varphi \leftrightarrow \psi$ is a [[tautology|0D1AHYPM8N]].
For example, $p \to q \equiv \neg p \lor q$.
[[De Morgan's laws|09PKJKA6J0]] give two more examples.

## Explanations

### L1 human

Logically equivalent formulas say the same thing in different words.
You can check an equivalence with a [[truth table|05RSK4Q657]]: the two columns must agree in every row.
Then you can replace one formula by the other in a proof.
