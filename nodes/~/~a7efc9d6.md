---
tag: ~a7efc9d6
kind: definition
name: Conjunctive normal form
msc: [03B05]
defines: ~dff2e486
uses: [~df2c4c4c]
sources:
  - url: https://en.wikipedia.org/wiki/Conjunctive_normal_form
    locator: Definition
---

## Definition

A formula of propositional logic is in conjunctive normal form if it is a conjunction of one or more disjunctions of one or more literals.
Each disjunction is a clause.

## Remarks

Example: $(p \vee \neg q) \wedge (q \vee r) \wedge \neg p$ is in conjunctive normal form.
Every formula is logically equivalent to a formula in conjunctive normal form. Negate the formula, put the negation in [[disjunctive normal form|~df2c4c4c]], and use the [[De Morgan laws|~5bea0bba]].
The satisfiability problem for formulas in conjunctive normal form with clauses of $3$ literals is NP-complete.

## Explanations

### L1 human

A formula in conjunctive normal form is an and of ors of simple conditions.
Each clause is a constraint, and the formula is true when all constraints hold.
