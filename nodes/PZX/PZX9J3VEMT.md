---
tag: PZX9J3VEMT
kind: definition
name: Sequent calculus
msc: ["03F05", "03F03"]
defines: W72CA3R9MP
uses: [086QKPF0A6, 0M28ASWG8T, 0H5GKDTB01, 0ZNX6DQ3EJ, 0XR7A7RSXB, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
---

## Definition

Fix a language of [[predicate logic|086QKPF0A6]].
A *sequent* is an expression $\Gamma \vdash \Delta$, where $\Gamma$ and $\Delta$ are finite lists of formulas.
The *sequent calculus* LK has the following parts.

1. Axioms: $A \vdash A$ for each formula $A$.
2. Structural rules: weakening, contraction and exchange on each side, and the cut rule. The cut rule infers $\Gamma, \Pi \vdash \Delta, \Lambda$ from $\Gamma \vdash \Delta, A$ and $A, \Pi \vdash \Lambda$.
3. Logical rules: for each connective and quantifier, rules that introduce it on the left and on the right.

The logical rules for [[conjunction|0M28ASWG8T]], [[disjunction|0H5GKDTB01]], [[implication|0ZNX6DQ3EJ]], [[negation|0XR7A7RSXB]] and the quantifiers are these.

- $\wedge$R: from $\Gamma \vdash \Delta, A$ and $\Gamma \vdash \Delta, B$ infer $\Gamma \vdash \Delta, A \wedge B$.
- $\wedge$L: from $A, \Gamma \vdash \Delta$ infer $A \wedge B, \Gamma \vdash \Delta$ and $B \wedge A, \Gamma \vdash \Delta$.
- $\vee$L: from $A, \Gamma \vdash \Delta$ and $B, \Gamma \vdash \Delta$ infer $A \vee B, \Gamma \vdash \Delta$.
- $\vee$R: from $\Gamma \vdash \Delta, A$ infer $\Gamma \vdash \Delta, A \vee B$ and $\Gamma \vdash \Delta, B \vee A$.
- $\to$R: from $A, \Gamma \vdash \Delta, B$ infer $\Gamma \vdash \Delta, A \to B$.
- $\to$L: from $\Gamma \vdash \Delta, A$ and $B, \Pi \vdash \Lambda$ infer $A \to B, \Gamma, \Pi \vdash \Delta, \Lambda$.
- $\neg$R: from $A, \Gamma \vdash \Delta$ infer $\Gamma \vdash \Delta, \neg A$.
- $\neg$L: from $\Gamma \vdash \Delta, A$ infer $\neg A, \Gamma \vdash \Delta$.
- $\forall$R: from $\Gamma \vdash \Delta, A(y)$ infer $\Gamma \vdash \Delta, \forall x\, A(x)$, where the variable $y$ is not free in $\Gamma, \Delta, \forall x\, A(x)$.
- $\forall$L: from $A(t), \Gamma \vdash \Delta$ infer $\forall x\, A(x), \Gamma \vdash \Delta$, where $t$ is a term.
- $\exists$L: from $A(y), \Gamma \vdash \Delta$ infer $\exists x\, A(x), \Gamma \vdash \Delta$, where $y$ is not free in $\Gamma, \Delta, \exists x\, A(x)$.
- $\exists$R: from $\Gamma \vdash \Delta, A(t)$ infer $\Gamma \vdash \Delta, \exists x\, A(x)$, where $t$ is a term.

A *derivation* is a finite tree of sequents.
Each leaf is an axiom, and each other node follows from its children by a rule.
The calculus LJ for intuitionistic logic is LK with the restriction that each right side has at most one formula.

## Remarks

Example: the [[law of excluded middle|0RYYK8PG4S]] has an LK derivation.
Start from $A \vdash A$ and get $\vdash A, \neg A$ by $\neg$R.
Then $\vee$R twice gives $\vdash A \vee \neg A, A \vee \neg A$, and contraction gives $\vdash A \vee \neg A$.
Non-example: this is not an LJ derivation, because $\vdash A, \neg A$ has two formulas on the right.
In fact $\vdash A \vee \neg A$ has no LJ derivation at all.
A sequent $A_1, \dots, A_m \vdash B_1, \dots, B_n$ means the same as the formula $(A_1 \wedge \dots \wedge A_m) \to (B_1 \vee \dots \vee B_n)$.
Some books use multisets or sets in place of lists, and then drop the exchange rule.
