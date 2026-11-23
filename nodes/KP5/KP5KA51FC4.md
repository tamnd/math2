---
tag: KP5KA51FC4
kind: definition
name: Contraction-free sequent calculi
msc: ["03F05", "03B20"]
topics: [R10RMQCJQX]
audience: grad
defines: BZ59F5GBRR
uses: [PZX9J3VEMT, W72CA3R9MP, MYJ8Y050J0]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Structural rules
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Cut-elimination in the sequent calculus
---

## Definition

We define sequent calculi for propositional logic that have no structural rules, and in which weakening and contraction are admissible.
Formulas are built from propositional variables and $\bot$ by $\wedge$, $\vee$ and $\to$, and $\neg A$ abbreviates $A \to \bot$.
A sequent $\Gamma \Rightarrow \Delta$ has finite [[multisets|MYJ8Y050J0]] $\Gamma$ and $\Delta$ of formulas, and $p$ ranges over propositional variables.
A *contraction-free sequent calculus* is a sequent calculus in which contraction is not a rule and contraction is admissible.

**The classical calculus G3cp.** Its axioms are $p, \Gamma \Rightarrow \Delta, p$ and $\bot, \Gamma \Rightarrow \Delta$, and its rules are these.

- L${\wedge}$: from $A, B, \Gamma \Rightarrow \Delta$ infer $A \wedge B, \Gamma \Rightarrow \Delta$.
- R${\wedge}$: from $\Gamma \Rightarrow \Delta, A$ and $\Gamma \Rightarrow \Delta, B$ infer $\Gamma \Rightarrow \Delta, A \wedge B$.
- L${\vee}$: from $A, \Gamma \Rightarrow \Delta$ and $B, \Gamma \Rightarrow \Delta$ infer $A \vee B, \Gamma \Rightarrow \Delta$.
- R${\vee}$: from $\Gamma \Rightarrow \Delta, A, B$ infer $\Gamma \Rightarrow \Delta, A \vee B$.
- L${\to}$: from $\Gamma \Rightarrow \Delta, A$ and $B, \Gamma \Rightarrow \Delta$ infer $A \to B, \Gamma \Rightarrow \Delta$.
- R${\to}$: from $A, \Gamma \Rightarrow \Delta, B$ infer $\Gamma \Rightarrow \Delta, A \to B$.

**The intuitionistic calculus G3ip.** Every succedent is one formula $C$.
Its axioms are $p, \Gamma \Rightarrow p$ and $\bot, \Gamma \Rightarrow C$.
Its rules L${\wedge}$, R${\wedge}$, L${\vee}$ and R${\to}$ are those of G3cp with $\Delta$ removed.
Its other two rules are R${\vee}$, from $\Gamma \Rightarrow A_i$ infer $\Gamma \Rightarrow A_0 \vee A_1$ for $i = 0$ or $i = 1$, and L${\to}$, from $A \to B, \Gamma \Rightarrow A$ and $B, \Gamma \Rightarrow C$ infer $A \to B, \Gamma \Rightarrow C$.

**Dyckhoff's calculus LJT.** It is G3ip with L${\to}$ replaced by four rules, where $E$ is one formula.

1. L0${\to}$: from $p, B, \Gamma \Rightarrow E$ infer $p, p \to B, \Gamma \Rightarrow E$.
2. L${\wedge}{\to}$: from $C \to (D \to B), \Gamma \Rightarrow E$ infer $(C \wedge D) \to B, \Gamma \Rightarrow E$.
3. L${\vee}{\to}$: from $C \to B, D \to B, \Gamma \Rightarrow E$ infer $(C \vee D) \to B, \Gamma \Rightarrow E$.
4. L${\to}{\to}$: from $D \to B, \Gamma \Rightarrow C \to D$ and $B, \Gamma \Rightarrow E$ infer $(C \to D) \to B, \Gamma \Rightarrow E$.

## Notation

In each rule the displayed compound formula of the conclusion is *principal*, and $\Gamma$ and $\Delta$ form the *context*.
The *height* of a derivation is the largest number of rule steps on a branch, so an axiom has height $0$.
We write $\vdash_n \Gamma \Rightarrow \Delta$ when the sequent has a derivation of height at most $n$.
A rule is *height-preserving admissible* when its conclusion has a derivation of height at most $n$ whenever its premises do.
The names follow Kleene's system G3 and the book of Troelstra and Schwichtenberg, where c, i and p stand for classical, intuitionistic and propositional, and some authors call LJT G4ip.

## Remarks

### Reading the conditions

The axioms are atomic and carry arbitrary contexts $\Gamma$ and $\Delta$.
The contexts build in weakening, and the restriction to atoms keeps the rules the only source of connectives; the sequent $A, \Gamma \Rightarrow \Delta, A$ for compound $A$ is derivable by induction on $A$.
Multisets build in exchange but keep multiplicity, so $p, p \Rightarrow q$ and $p \Rightarrow q$ are different sequents, and the question of contraction still makes sense.

Each two-premise rule of G3cp copies the whole context into both premises.
This shared context is what replaces contraction: for example L${\to}$ sends $\Delta$ to both premises, so a formula of $\Delta$ needed on both branches is there without a copy step.
In G3ip, the left premise of L${\to}$ also repeats $A \to B$, because an intuitionistic proof may need the same implication again later.

LJT drops that repetition and splits $A \to B$ by the shape of $A$.
Each premise of an LJT rule is smaller than its conclusion in a well-founded order on sequents, and LJT derives exactly the sequents that G3ip derives.

### A small case

In G3cp, the sequent $p \wedge q \Rightarrow q \wedge p$ has this derivation, read upwards.

1. L${\wedge}$ reduces it to $p, q \Rightarrow q \wedge p$.
2. R${\wedge}$ reduces that to $p, q \Rightarrow q$ and $p, q \Rightarrow p$.
3. Both are axioms, with the extra atom in the context.

A failing case: $p \to q \Rightarrow q$ has no G3cp derivation.
L${\to}$ needs $\Rightarrow q, p$ and $q \Rightarrow q$, and the first is not an axiom and has no principal formula, so the search stops.
The sequent is false when $p$ and $q$ are both false, so no sound calculus derives it.

The [[contraction-free sequent calculus|BZ59F5GBRR]] concept explains why contraction is admissible in these calculi, and works through G3ip and LJT derivations.

## Explanations

### L1 human

These are rule systems for proofs in propositional logic in which no rule copies or deletes an assumption.
In Gentzen's original calculus, separate rules do the copying and the deleting.
Here every rule carries the whole list of assumptions up into its premises, so whatever a later step needs is still there.

### L2 human

Derive $\Rightarrow p \vee \neg p$ in G3cp, working backwards.
R${\vee}$ reduces it to $\Rightarrow p, \neg p$, that is $\Rightarrow p, p \to \bot$.
R${\to}$ reduces this to $p \Rightarrow p, \bot$, which is an axiom with $\Delta = \bot$.
The derivation has height $2$ and no structural step.
The typical use is backward search: start from the goal and apply rules upwards until only axioms remain.
A trap is to write axioms $A \Rightarrow A$ for compound $A$; the calculi allow only atomic axioms, and the general case is a lemma.

### L3 human

In G3cp every rule is invertible, so backward search never backtracks, and the [[inversion lemma|EXMS77F2XN]] makes this exact.
In G3ip the rules L${\to}$ and R${\vee}$ force choices, and LJT makes the search terminate without a loop check.
So LJT gives a decision procedure for intuitionistic propositional logic, a problem that is [[PSPACE|T9NTRY93ZT]]-complete.
The same design, with shared contexts and atomic axioms, extends to first-order logic in the calculi G3c and G3i.
