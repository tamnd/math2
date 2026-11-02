---
tag: AYRZ98Y0NW
kind: statement
role: theorem
name: Cut-elimination theorem
msc: ["03F05"]
uses: [PZX9J3VEMT, W72CA3R9MP, N4EDJNMTEF]
about: [W72CA3R9MP]
sources:
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
same_as:
  wikidata: Q376166
  wikipedia: Cut-elimination theorem
---

## Statement

Let $\Gamma \vdash \Delta$ be a sequent of first-order logic.
If $\Gamma \vdash \Delta$ has a derivation in the [[sequent calculus|PZX9J3VEMT]] LK, then it has a derivation in LK that does not use the cut rule.
The same holds for the intuitionistic calculus LJ.

## Remarks

Gentzen proved the theorem in 1934, and called it the *Hauptsatz*.
The proof is a double induction.
The outer induction is on the complexity of the cut formula, and the inner one is on the heights of the derivations above the cut.
Each step pushes a topmost cut upward or replaces it by cuts on smaller formulas.
The cost is large: removing cuts can make a derivation super-exponentially longer.

In a cut-free derivation, every formula is a subformula of a formula in the final sequent, up to the substitution of terms for variables.
This *subformula property* gives quick consequences.
For example, the empty sequent $\vdash$ has no cut-free derivation, since no rule other than cut can produce it.
So LK is consistent.

## Explanations

### L1 human

The cut rule lets a proof use a lemma: prove $A$, then use $A$ to prove the goal.
The theorem says that lemmas are never needed in pure logic.
Every proof can be rewritten so that it only builds up the formulas of the conclusion, step by step.
The price is that the new proof can be enormously longer.

### L2 human

Cut elimination is the central result of structural [[proof theory|N4EDJNMTEF]].
It gives the subformula property, the consistency of pure logic, and Craig interpolation and Herbrand's theorem by short arguments.
For arithmetic, cuts cannot be fully removed in the presence of induction.
Gentzen's consistency proof for Peano arithmetic instead removes cuts partly, with a transfinite induction up to the ordinal $\varepsilon_0$ to show that the process ends.
Through the Curry–Howard correspondence, the removal of cuts is related to the evaluation of programs.
