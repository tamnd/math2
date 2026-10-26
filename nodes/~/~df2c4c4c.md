---
tag: ~df2c4c4c
kind: definition
name: Disjunctive normal form
msc: [03B05]
defines: ~caf734ec
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Definition
---

## Definition

A literal is a propositional variable $p$ or its negation $\neg p$.
A formula of propositional logic is in disjunctive normal form if it is a disjunction of one or more conjunctions of one or more literals.

## Remarks

Example: $(p \wedge \neg q) \vee (q \wedge r) \vee \neg p$ is in disjunctive normal form.
Every formula is logically equivalent to a formula in disjunctive normal form. For a formula that is not a contradiction, take one conjunction for each row of the truth table where it is true.
A consequence: the connectives $\wedge$, $\vee$ and $\neg$ are functionally complete.

## Explanations

### L1 human

A formula in disjunctive normal form is an or of ands of simple conditions.
It lists all the cases in which the formula is true.
