---
tag: PZX9J3VEMT
kind: definition
name: Sequent calculus
msc: ["03F05", "03F03"]
topics: [TTCRX3NFNY]
audience: grad
defines: W72CA3R9MP
uses: [086QKPF0A6, 0M28ASWG8T, 0H5GKDTB01, 0ZNX6DQ3EJ, 0XR7A7RSXB, 0RYYK8PG4S, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Inference rules
---

## Definition

Fix a first-order language of [[predicate logic|086QKPF0A6]].
A *sequent* is an expression $\Gamma \Rightarrow \Delta$, where $\Gamma$ (the antecedent) and $\Delta$ (the succedent) are finite sequences of formulas, possibly empty.
In the rules below, $A$ and $B$ are formulas, $\Gamma, \Delta, \Pi, \Lambda$ are finite sequences, and a comma joins sequences.
The calculus LK of Gentzen has the following axioms and rules.

**Axioms.** Every sequent $A \Rightarrow A$.

**Structural rules.**

- Weakening: from $\Gamma \Rightarrow \Delta$ infer $A, \Gamma \Rightarrow \Delta$ (WL) and $\Gamma \Rightarrow \Delta, A$ (WR).
- Contraction: from $A, A, \Gamma \Rightarrow \Delta$ infer $A, \Gamma \Rightarrow \Delta$ (CL); from $\Gamma \Rightarrow \Delta, A, A$ infer $\Gamma \Rightarrow \Delta, A$ (CR).
- Exchange: from $\Gamma, A, B, \Pi \Rightarrow \Delta$ infer $\Gamma, B, A, \Pi \Rightarrow \Delta$ (XL), and the same on the right (XR).
- Cut: from $\Gamma \Rightarrow \Delta, A$ and $A, \Pi \Rightarrow \Lambda$ infer $\Gamma, \Pi \Rightarrow \Delta, \Lambda$. The formula $A$ is the cut formula.

**Logical rules** for [[conjunction|0M28ASWG8T]], [[disjunction|0H5GKDTB01]], [[implication|0ZNX6DQ3EJ]] and [[negation|0XR7A7RSXB]]:

- ${\wedge}$R: from $\Gamma \Rightarrow \Delta, A$ and $\Gamma \Rightarrow \Delta, B$ infer $\Gamma \Rightarrow \Delta, A \wedge B$.
- ${\wedge}$L: from $A, \Gamma \Rightarrow \Delta$ infer $A \wedge B, \Gamma \Rightarrow \Delta$ and $B \wedge A, \Gamma \Rightarrow \Delta$.
- ${\vee}$L: from $A, \Gamma \Rightarrow \Delta$ and $B, \Gamma \Rightarrow \Delta$ infer $A \vee B, \Gamma \Rightarrow \Delta$.
- ${\vee}$R: from $\Gamma \Rightarrow \Delta, A$ infer $\Gamma \Rightarrow \Delta, A \vee B$ and $\Gamma \Rightarrow \Delta, B \vee A$.
- ${\to}$R: from $A, \Gamma \Rightarrow \Delta, B$ infer $\Gamma \Rightarrow \Delta, A \to B$.
- ${\to}$L: from $\Gamma \Rightarrow \Delta, A$ and $B, \Pi \Rightarrow \Lambda$ infer $A \to B, \Gamma, \Pi \Rightarrow \Delta, \Lambda$.
- ${\neg}$R: from $A, \Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta, \neg A$.
- ${\neg}$L: from $\Gamma \Rightarrow \Delta, A$ infer $\neg A, \Gamma \Rightarrow \Delta$.

**Quantifier rules**, where $A[t/x]$ is a [[substitution|NCDZ969V7X]] and the term $t$ or variable $y$ is substitutable for $x$ in $A$:

- ${\forall}$L: from $A[t/x], \Gamma \Rightarrow \Delta$ infer $\forall x\, A, \Gamma \Rightarrow \Delta$, for any term $t$.
- ${\forall}$R: from $\Gamma \Rightarrow \Delta, A[y/x]$ infer $\Gamma \Rightarrow \Delta, \forall x\, A$, where $y$ is not free in $\Gamma$, $\Delta$ or $\forall x\, A$.
- ${\exists}$L: from $A[y/x], \Gamma \Rightarrow \Delta$ infer $\exists x\, A, \Gamma \Rightarrow \Delta$, where $y$ is not free in $\Gamma$, $\Delta$ or $\exists x\, A$.
- ${\exists}$R: from $\Gamma \Rightarrow \Delta, A[t/x]$ infer $\Gamma \Rightarrow \Delta, \exists x\, A$, for any term $t$.

The variable $y$ of ${\forall}$R and ${\exists}$L is the *eigenvariable* of the step, and the condition on it is the *eigenvariable condition*.
A *derivation* is a finite tree of sequents in which each leaf is an axiom and each other node follows from the nodes directly above it by a rule.
The calculus LJ is LK with the restriction that every sequent in a derivation has at most one formula in its succedent.
A *sequent* $\Gamma \Rightarrow \Delta$ is *true* in a structure $\mathcal{M}$ under an assignment $s$ when some formula of $\Gamma$ is false or some formula of $\Delta$ is true there.

## Notation

Many books write $\Gamma \vdash \Delta$ or $\Gamma \longrightarrow \Delta$ for a sequent; we keep $\vdash$ for derivability.
Some books use multisets or sets in place of sequences, and then the exchange rule, or also contraction, is not needed.
Kleene's calculi G3 and their relatives build weakening and contraction into the axioms and rules, and they use the same context in both premises of a two-premise rule.
One-sided calculi write $\Rightarrow \Delta$ only, and move a formula $A$ from the left to the right as $\neg A$.

## Remarks

### Reading a sequent

The sequent $A_1, \dots, A_m \Rightarrow B_1, \dots, B_n$ is true in $\mathcal{M}$ under $s$ exactly when $(A_1 \wedge \cdots \wedge A_m) \to (B_1 \vee \cdots \vee B_n)$ is.
An empty antecedent reads as true, and an empty succedent reads as false.
So $\Rightarrow A$ says that $A$ holds, and $\Gamma \Rightarrow$ says that the formulas of $\Gamma$ cannot all hold.

### A derivation and a non-derivation

The [[law of excluded middle|0RYYK8PG4S]] has an LK derivation.

1. $A \Rightarrow A$ is an axiom.
2. ${\neg}$R gives $\Rightarrow A, \neg A$.
3. ${\vee}$R gives $\Rightarrow A, A \vee \neg A$.
4. XR gives $\Rightarrow A \vee \neg A, A$, and ${\vee}$R gives $\Rightarrow A \vee \neg A, A \vee \neg A$.
5. CR gives $\Rightarrow A \vee \neg A$.

This is not an LJ derivation, because step 2 has two formulas in the succedent.
In fact $\Rightarrow A \vee \neg A$ has no LJ derivation when $A$ is a propositional variable.

## Explanations

### L1 human

A sequent is a short claim of the form "these assumptions give one of these conclusions".
The calculus gives starting claims, such as "$A$ gives $A$", and rules that build larger claims from smaller ones.
For each logical word there is a rule for the left side, which uses it, and a rule for the right side, which proves it.
For example, from "$A$ gives $A$" the rule for "and" on the left gives "$A$ and $B$ give $A$".

### L2 human

We derive $A \wedge B \Rightarrow B \wedge A$.

1. $B \Rightarrow B$ is an axiom, and ${\wedge}$L gives $A \wedge B \Rightarrow B$.
2. $A \Rightarrow A$ is an axiom, and ${\wedge}$L gives $A \wedge B \Rightarrow A$.
3. ${\wedge}$R with the sequents of steps 1 and 2 gives $A \wedge B \Rightarrow B \wedge A$.

The typical use is backward proof search: start from the goal sequent and apply rules upward, where each rule removes one connective.
A trap is the eigenvariable condition of ${\forall}$R and ${\exists}$L: the eigenvariable must not occur free anywhere else in the conclusion sequent.

### L3 human

The rules of LK are symmetric under the exchange of left and right, with $\wedge$ and $\vee$, $\forall$ and $\exists$ swapped; this is a form of duality.
The cut rule is the only rule whose premises contain a formula that is not a subformula of the conclusion, and Gentzen's [[cut-elimination theorem|AYRZ98Y0NW]] shows that it can be removed.
The restriction of LJ to one formula on the right gives [[intuitionistic logic|Q11N8X99FK]], and dropping structural rules gives the substructural logics, such as linear logic.
