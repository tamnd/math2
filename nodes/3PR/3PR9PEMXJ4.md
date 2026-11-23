---
tag: 3PR9PEMXJ4
kind: definition
name: Hypersequent calculus
msc: ["03F05", "03B55"]
topics: [R10RMQCJQX]
audience: research
defines: 73J7F0FN4A
uses: [PZX9J3VEMT, Q11N8X99FK, MYJ8Y050J0, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Hypersequent
    locator: Formal definitions and propositional rules
  - url: https://en.wikipedia.org/wiki/Hypersequent
    locator: Intermediate logics
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Semantics
---

## Definition

A hypersequent calculus is a proof system whose lines are finite collections of sequents, read as disjunctions.
Fix the language of propositional [[intuitionistic logic|Q11N8X99FK]], with $\bot$, $\wedge$, $\vee$, $\to$ and $\neg A = A \to \bot$.
A *single-conclusion sequent* is an expression $\Gamma \Rightarrow \Pi$, where $\Gamma$ is a finite [[multiset|MYJ8Y050J0]] of formulas and $\Pi$ is empty or one formula.
A *hypersequent* is a finite nonempty multiset of such sequents, written $\Gamma_1 \Rightarrow \Pi_1 \mid \cdots \mid \Gamma_n \Rightarrow \Pi_n$.
The sequents $\Gamma_i \Rightarrow \Pi_i$ are its *components*, and $\mid$ is the *hypersequent bar*.
In a rule, $G$ is a hypersequent or empty, called the *side hypersequent*, and $G \mid S$ is $G$ with one more component $S$.

A *hypersequent calculus* is a set of axioms and rules whose premises and conclusions are hypersequents.
A *derivation* is a finite tree of hypersequents whose leaves are axioms and whose other nodes follow from the nodes directly above them by a rule.
The *formula interpretation* of a sequent is $I(\Gamma \Rightarrow \Pi) = \bigwedge \Gamma \to \bigvee \Pi$, where the empty conjunction is $\bot \to \bot$ and the empty disjunction is $\bot$.
The interpretation of a hypersequent is $I(S_1 \mid \cdots \mid S_n) = I(S_1) \vee \cdots \vee I(S_n)$.

### Avron's calculus for Gödel-Dummett logic

*Gödel-Dummett logic* LC is intuitionistic propositional logic with the extra axiom schema $(A \to B) \vee (B \to A)$.
Avron's calculus HLC for LC has the axioms $A \Rightarrow A$ and $\bot \Rightarrow$.
Its rules are the rules of [[LJ|PZX9J3VEMT]], each acting inside one component and copying $G$ unchanged, together with external weakening (EW) and external contraction (EC) on whole components.
Its one extra rule is the *communication rule*:
$$\dfrac{G \mid \Gamma_1, \Delta_1 \Rightarrow \Pi_1 \qquad G \mid \Gamma_2, \Delta_2 \Rightarrow \Pi_2}{G \mid \Gamma_1, \Gamma_2 \Rightarrow \Pi_1 \mid \Delta_1, \Delta_2 \Rightarrow \Pi_2} \ (\mathsf{com})$$
The calculus HLJ is HLC without the communication rule.
The Remarks list all rules.

## Notation

Many authors write $\vdash$ or $\Rightarrow$ inside components, and $\mathcal{G}$ or $H$ for the side hypersequent.
The name of Avron's calculus varies; HLC and GLC are both in use.
Some authors state the communication rule with two different side hypersequents $G$ and $H$ and the conclusion $G \mid H \mid \cdots$.
That form and the form above derive the same hypersequents, because EW turns $G$ and $H$ into $G \mid H$, and EC removes a repeated side hypersequent.
The special case $\Gamma_1 = \Delta_2 = \emptyset$ of $\mathsf{com}$ infers $G \mid \Gamma_2 \Rightarrow \Pi_1 \mid \Delta_1 \Rightarrow \Pi_2$ from $G \mid \Delta_1 \Rightarrow \Pi_1$ and $G \mid \Gamma_2 \Rightarrow \Pi_2$.
So the two components exchange their succedents, and many surveys state the rule in this form.
Hypersequents for classical and modal logics use multi-conclusion components $\Gamma \Rightarrow \Delta$ with $\Delta$ a multiset.

## Remarks

### The rules of HLC

The letters $A, B$ denote formulas, $\Gamma, \Delta$ multisets of formulas, and $\Pi$ an empty or one-formula succedent.

- External weakening (EW): from $G$ infer $G \mid \Gamma \Rightarrow \Pi$.
- External contraction (EC): from $G \mid \Gamma \Rightarrow \Pi \mid \Gamma \Rightarrow \Pi$ infer $G \mid \Gamma \Rightarrow \Pi$.
- Internal weakening (IW): from $G \mid \Gamma \Rightarrow \Pi$ infer $G \mid A, \Gamma \Rightarrow \Pi$, and from $G \mid \Gamma \Rightarrow$ infer $G \mid \Gamma \Rightarrow A$.
- Internal contraction (IC): from $G \mid A, A, \Gamma \Rightarrow \Pi$ infer $G \mid A, \Gamma \Rightarrow \Pi$.
- ${\wedge}$L: from $G \mid A, B, \Gamma \Rightarrow \Pi$ infer $G \mid A \wedge B, \Gamma \Rightarrow \Pi$.
- ${\wedge}$R: from $G \mid \Gamma \Rightarrow A$ and $G \mid \Gamma \Rightarrow B$ infer $G \mid \Gamma \Rightarrow A \wedge B$.
- ${\vee}$L: from $G \mid A, \Gamma \Rightarrow \Pi$ and $G \mid B, \Gamma \Rightarrow \Pi$ infer $G \mid A \vee B, \Gamma \Rightarrow \Pi$.
- ${\vee}$R: from $G \mid \Gamma \Rightarrow A$ infer $G \mid \Gamma \Rightarrow A \vee B$ and $G \mid \Gamma \Rightarrow B \vee A$.
- ${\to}$L: from $G \mid \Gamma \Rightarrow A$ and $G \mid B, \Delta \Rightarrow \Pi$ infer $G \mid A \to B, \Gamma, \Delta \Rightarrow \Pi$.
- ${\to}$R: from $G \mid A, \Gamma \Rightarrow B$ infer $G \mid \Gamma \Rightarrow A \to B$.
- Cut: from $G \mid \Gamma \Rightarrow A$ and $G \mid A, \Delta \Rightarrow \Pi$ infer $G \mid \Gamma, \Delta \Rightarrow \Pi$.

### Why each part is there

The components are single-conclusion sequents because LC is an intermediate logic, and a single succedent is what keeps LJ intuitionistic.
The bar is read as a disjunction, so that a hypersequent can hold although none of its components holds alone.

The side hypersequent $G$ is copied unchanged by every logical rule, so the logical rules act on one component at a time.
External weakening adds a new alternative, which is sound because a disjunction gets weaker when it gets longer.
External contraction merges two identical alternatives, and it is needed at the end of most derivations, where two components have become the same formula.

The communication rule is the only rule that moves formulas between components.
Without it the calculus is HLJ, and the [[non-example of HLJ|805SVAZ350]] shows that then a hypersequent is derivable only if one of its components is derivable in LJ.
So HLJ proves the same formulas as LJ, and does not prove $(p \to q) \vee (q \to p)$.

### A small case and a failing case

From the axioms $q \Rightarrow q$ and $p \Rightarrow p$, the communication rule with $G$ empty, $\Gamma_1 = \Delta_2 = \emptyset$, $\Delta_1 = q$ and $\Gamma_2 = p$ gives $p \Rightarrow q \mid q \Rightarrow p$.
The [[example of the prelinearity axiom|BNCS8H51B2]] continues this to the axiom of LC.

The expression $p \Rightarrow q, r$ is not a component of an HLC hypersequent, since its succedent has two formulas.
With such components and the rules of LK in each component, the calculus would derive $p \vee \neg p$, which is not a theorem of LC.

### Soundness of the communication rule

LC is sound and complete for [[Kripke semantics|NGHWZ9Y7ZV]] on rooted frames that are total orders.
We check that $\mathsf{com}$ preserves validity on such a model.
Assume that no component of $G$ holds at the root, so both premise components hold at every world.
Suppose that the first conclusion component fails at a world $u$, and the second fails at a world $v$.
Then $u$ forces $\Gamma_1, \Gamma_2$ but not $\Pi_1$, and $v$ forces $\Delta_1, \Delta_2$ but not $\Pi_2$.
If $u \le v$, then $v$ forces $\Gamma_2$ by persistence, so the second premise gives $\Pi_2$ at $v$, a contradiction.
If $v \le u$, then $u$ forces $\Delta_1$, so the first premise gives $\Pi_1$ at $u$, a contradiction.
In a total order one of the two cases holds, so one conclusion component holds at the root.

### Adequacy and cut elimination

Avron proved that HLC is adequate for LC: a hypersequent $H$ is derivable in HLC if and only if $I(H)$ is a theorem of LC.
In particular, $\Rightarrow A$ is derivable exactly when $A$ is a theorem of LC.
He also proved cut elimination: every hypersequent derivable in HLC has a derivation without cut.
We state these results and cite the proofs.

The proof of cut elimination follows the plan of Gentzen's [[cut-elimination theorem|AYRZ98Y0NW]], with an induction on the cut formula and an inner induction on the heights of the premises.
The new difficulty is external contraction, since a component that contains the cut formula may have been copied above the cut.
So the proof replaces the [[cut rule|HGVMPZ2DXA]] by a generalized cut that removes several copies at once, in the spirit of Gentzen's mix rule.
A cut-free derivation has the [[subformula property|Z2NXKDK06G]]: every formula in it is a subformula of a formula of the end hypersequent.

## Explanations

### L1 human

A hypersequent is a list of ordinary claims separated by bars, and it says that at least one of the claims holds.
The rules work on one claim at a time, except the communication rule.
The communication rule lets two claims swap some of their assumptions.
For example, from "$p$ gives $p$" and "$q$ gives $q$" it produces "$p$ gives $q$, or $q$ gives $p$".
That is exactly the extra axiom of Gödel-Dummett logic.

### L2 human

Let us derive the weak excluded middle $\neg p \vee \neg\neg p$ in HLC.
The axioms $p \Rightarrow p$ and $\bot \Rightarrow$ give $\neg p, p \Rightarrow$ by ${\to}$L.
Apply $\mathsf{com}$ to two copies of it, with $\Gamma_1 = \Gamma_2 = p$ and $\Delta_1 = \Delta_2 = \neg p$:
$$p, p \Rightarrow \; \mid \; \neg p, \neg p \Rightarrow.$$
Internal contraction twice gives $p \Rightarrow \mid \neg p \Rightarrow$.
Internal weakening by $\bot$ on the right and ${\to}$R in each component give $\Rightarrow \neg p \mid \Rightarrow \neg\neg p$.
Finally, ${\vee}$R in each component and external contraction give $\Rightarrow \neg p \vee \neg\neg p$.
The [[example of the weak excluded middle|Q50NC2F1Y1]] checks every step.
Watch out: external contraction applies only to identical components, so you must make the two components equal with ${\vee}$R first.

### L3 human

Hypersequents add one structural layer above the sequent: a disjunction of sequents at the meta level.
Rules such as $\mathsf{com}$ act on that layer, and they keep the logical rules of LJ unchanged.
Other structural rules on the bar give calculi for other intermediate logics.
The same idea extends to modal logics, for example S5 with Avron's modal splitting rule, and to fuzzy and substructural logics.
Other refinements of the sequent are [[display calculi|2Q62W689SC]], nested sequents and [[labelled sequent calculi|F46GV42XCE]].
