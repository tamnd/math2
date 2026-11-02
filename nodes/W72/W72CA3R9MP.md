---
tag: W72CA3R9MP
kind: concept
name: Sequent calculus
msc: ["03F05", "03F03"]
uses: [N4EDJNMTEF]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
same_as:
  wikidata: Q1771121
  wikipedia: Sequent calculus
---

## Summary

A sequent calculus is a proof system whose lines are sequents $\Gamma \vdash \Delta$.
Such a sequent is read as "if all formulas of $\Gamma$ hold, then some formula of $\Delta$ holds".
Gentzen introduced the systems LK for classical logic and LJ for intuitionistic logic in 1934.
Each connective has rules that introduce it on the left and on the right.
This symmetry makes the calculus the main tool of structural [[proof theory|N4EDJNMTEF]].

## Explanations

### L1 human

A sequent is a pair of lists of formulas, written $\Gamma \vdash \Delta$.
It says that the assumptions on the left together force at least one of the claims on the right.
Proofs are trees of sequents that grow downward, from axioms $A \vdash A$ to the sequent one wants.
For example, from $A \vdash A$ the rule for "and" on the left gives $A \wedge B \vdash A$.
Every rule only adds structure, except one rule, the cut, which removes a formula.
