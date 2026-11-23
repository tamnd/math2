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

Gentzen's sequent calculus LK derives sequents $\Gamma \Rightarrow \Delta$ from axioms $A \Rightarrow A$ by structural rules, a cut rule, and a left and a right rule for each logical symbol.

Fix a first-order language of [[predicate logic|086QKPF0A6]].
A *sequent* is an expression $\Gamma \Rightarrow \Delta$, where the antecedent $\Gamma$ and the succedent $\Delta$ are finite sequences of formulas, possibly empty.
In the rules below, $A$ and $B$ are formulas, $\Gamma, \Delta, \Pi, \Lambda$ are finite sequences, and a comma joins sequences.

The *axioms* are all sequents $A \Rightarrow A$.

The *structural rules* are weakening (W), contraction (C) and exchange (X) on each side, and cut:
$$\dfrac{\Gamma \Rightarrow \Delta}{A, \Gamma \Rightarrow \Delta}\,\mathrm{WL} \qquad \dfrac{\Gamma \Rightarrow \Delta}{\Gamma \Rightarrow \Delta, A}\,\mathrm{WR} \qquad \dfrac{A, A, \Gamma \Rightarrow \Delta}{A, \Gamma \Rightarrow \Delta}\,\mathrm{CL} \qquad \dfrac{\Gamma \Rightarrow \Delta, A, A}{\Gamma \Rightarrow \Delta, A}\,\mathrm{CR}$$
$$\dfrac{\Gamma, A, B, \Pi \Rightarrow \Delta}{\Gamma, B, A, \Pi \Rightarrow \Delta}\,\mathrm{XL} \qquad \dfrac{\Gamma \Rightarrow \Delta, A, B, \Lambda}{\Gamma \Rightarrow \Delta, B, A, \Lambda}\,\mathrm{XR} \qquad \dfrac{\Gamma \Rightarrow \Delta, A \qquad A, \Pi \Rightarrow \Lambda}{\Gamma, \Pi \Rightarrow \Delta, \Lambda}\,\mathrm{Cut}$$
In the cut rule, $A$ is the *cut formula*.

The *propositional rules* for [[conjunction|0M28ASWG8T]], [[disjunction|0H5GKDTB01]], [[implication|0ZNX6DQ3EJ]] and [[negation|0XR7A7RSXB]] are the following, where each rule for $\wedge$L and $\vee$R has a second form with $A$ and $B$ swapped in the compound formula:
$$\dfrac{A, \Gamma \Rightarrow \Delta}{A \wedge B, \Gamma \Rightarrow \Delta}\,{\wedge}\mathrm{L} \qquad \dfrac{\Gamma \Rightarrow \Delta, A \qquad \Gamma \Rightarrow \Delta, B}{\Gamma \Rightarrow \Delta, A \wedge B}\,{\wedge}\mathrm{R}$$
$$\dfrac{A, \Gamma \Rightarrow \Delta \qquad B, \Gamma \Rightarrow \Delta}{A \vee B, \Gamma \Rightarrow \Delta}\,{\vee}\mathrm{L} \qquad \dfrac{\Gamma \Rightarrow \Delta, A}{\Gamma \Rightarrow \Delta, A \vee B}\,{\vee}\mathrm{R}$$
$$\dfrac{\Gamma \Rightarrow \Delta, A \qquad B, \Pi \Rightarrow \Lambda}{A \to B, \Gamma, \Pi \Rightarrow \Delta, \Lambda}\,{\to}\mathrm{L} \qquad \dfrac{A, \Gamma \Rightarrow \Delta, B}{\Gamma \Rightarrow \Delta, A \to B}\,{\to}\mathrm{R}$$
$$\dfrac{\Gamma \Rightarrow \Delta, A}{\neg A, \Gamma \Rightarrow \Delta}\,{\neg}\mathrm{L} \qquad \dfrac{A, \Gamma \Rightarrow \Delta}{\Gamma \Rightarrow \Delta, \neg A}\,{\neg}\mathrm{R}$$

The *quantifier rules* use the [[substitution|NCDZ969V7X]] $A[t/x]$, where the term $t$ or the variable $y$ is substitutable for $x$ in $A$:
$$\dfrac{A[t/x], \Gamma \Rightarrow \Delta}{\forall x\, A, \Gamma \Rightarrow \Delta}\,{\forall}\mathrm{L} \qquad \dfrac{\Gamma \Rightarrow \Delta, A[y/x]}{\Gamma \Rightarrow \Delta, \forall x\, A}\,{\forall}\mathrm{R} \qquad \dfrac{A[y/x], \Gamma \Rightarrow \Delta}{\exists x\, A, \Gamma \Rightarrow \Delta}\,{\exists}\mathrm{L} \qquad \dfrac{\Gamma \Rightarrow \Delta, A[t/x]}{\Gamma \Rightarrow \Delta, \exists x\, A}\,{\exists}\mathrm{R}$$
In ${\forall}$L and ${\exists}$R the term $t$ is arbitrary.
In ${\forall}$R and ${\exists}$L the variable $y$ is the *eigenvariable* of the step, and it must satisfy the *eigenvariable condition*: $y$ is not free in $\Gamma$, in $\Delta$, or in the quantified formula $\forall x\, A$ or $\exists x\, A$.

A *derivation* is a finite tree of sequents in which each leaf is an axiom and each other node follows from the nodes directly above it by a rule.
The calculus LJ is LK with the restriction that every sequent in a derivation has at most one formula in its succedent.
A sequent $\Gamma \Rightarrow \Delta$ is *true* in a structure $\mathcal{M}$ under an assignment $s$ when some formula of $\Gamma$ is false or some formula of $\Delta$ is true there.

## Notation

Many books write $\Gamma \vdash \Delta$ or $\Gamma \longrightarrow \Delta$ for a sequent; we keep $\vdash$ for derivability.
Some books use multisets or sets in place of sequences, and then the exchange rule, or also contraction, is not needed.
Kleene's calculi G3 and their relatives build weakening and contraction into the axioms and rules, and they use the same context in both premises of a two-premise rule.
One-sided calculi write $\Rightarrow \Delta$ only, and move a formula $A$ from the left to the right as $\neg A$.

## Remarks

### Reading a sequent

The sequent $A_1, \dots, A_m \Rightarrow B_1, \dots, B_n$ is true in $\mathcal{M}$ under $s$ exactly when $(A_1 \wedge \dots \wedge A_m) \to (B_1 \vee \dots \vee B_n)$ is.
An empty antecedent reads as true, and an empty succedent reads as false.
So $\Rightarrow A$ says that $A$ holds, and $\Gamma \Rightarrow$ says that the formulas of $\Gamma$ cannot all hold.
With this reading each rule is sound: if its premises are true in $\mathcal{M}$ under every assignment, so is its conclusion.

### Why the eigenvariable condition

The condition makes ${\forall}$R mean "we proved $A$ for an object about which nothing else is assumed".
Without it, the axiom $P(a) \Rightarrow P(a)$ would give $P(a) \Rightarrow \forall x\, P(x)$, which is false in $\{0, 1\}$ with $P$ true of $0$ only and $a$ read as $0$.
[[A sequent derivation that breaks the eigenvariable condition|REMQ2W88WG]] works this case out.
The rule ${\exists}$L is the mirror image: from $P(a) \Rightarrow P(a)$ it would give $\exists x\, P(x) \Rightarrow P(a)$, false in the same structure with $a$ read as $1$.

The terms of ${\forall}$L and ${\exists}$R need no condition, since $\forall x\, A$ gives $A[t/x]$ for every term $t$, and $A[t/x]$ gives $\exists x\, A$.
Substitutability is still needed: $\forall x\, \exists y\, (x \neq y)$ must not give $\exists y\, (y \neq y)$ with the term $y$.

### Classical and intuitionistic

The [[law of excluded middle|0RYYK8PG4S]] has a short LK derivation.

1. $A \Rightarrow A$ is an axiom, and ${\neg}$R gives $\Rightarrow A, \neg A$.
2. ${\vee}$R in its second form gives $\Rightarrow A, A \vee \neg A$.
3. XR gives $\Rightarrow A \vee \neg A, A$, and ${\vee}$R gives $\Rightarrow A \vee \neg A, A \vee \neg A$.
4. CR gives $\Rightarrow A \vee \neg A$.

This is not an LJ derivation, because step 1 has two formulas in the succedent.
In fact $\Rightarrow A \vee \neg A$ has no LJ derivation when $A$ is a propositional variable.
The concept of the [[sequent calculus|W72CA3R9MP]] collects further derivations and the main theorems about them.

## Explanations

### L1 human

A sequent is a short claim of the form "these assumptions give one of these conclusions".
The calculus gives starting claims, such as "$A$ gives $A$", and rules that build larger claims from smaller ones.
For each logical word there is a rule for the left side, which uses it, and a rule for the right side, which proves it.
For example, from "$A$ gives $A$" the rule for "and" on the left gives "$A$ and $B$ give $A$".

### L2 human

We derive $\forall x\, P(x) \Rightarrow \forall x\, (P(x) \vee Q(x))$.

1. $P(y) \Rightarrow P(y)$ is an axiom.
2. ${\vee}$R gives $P(y) \Rightarrow P(y) \vee Q(y)$.
3. ${\forall}$L with the term $y$ gives $\forall x\, P(x) \Rightarrow P(y) \vee Q(y)$.
4. ${\forall}$R with eigenvariable $y$ gives $\forall x\, P(x) \Rightarrow \forall x\, (P(x) \vee Q(x))$.

Check step 4: $y$ is not free in $\forall x\, P(x)$ or in $\forall x\, (P(x) \vee Q(x))$, so the condition holds.
The typical use is backward proof search: start from the goal sequent and apply rules upward, where each rule removes one symbol.
Watch out: if steps 3 and 4 swap, the condition fails, because $y$ is then free in $P(y)$ on the left.

### L3 human

The rules of LK are symmetric under the exchange of left and right, with $\wedge$ and $\vee$, $\forall$ and $\exists$ swapped; this is a form of duality.
The cut rule is the only rule whose premises contain a formula that need not be a subformula of the conclusion, and Gentzen's [[cut-elimination theorem|AYRZ98Y0NW]] shows that it can be removed.
The restriction of LJ to one formula on the right gives [[intuitionistic logic|Q11N8X99FK]], and dropping structural rules gives the substructural logics, such as linear logic.
