---
tag: BZ59F5GBRR
kind: concept
name: Contraction-free sequent calculus
msc: ["03F05", "03B20"]
topics: [R10RMQCJQX]
audience: grad
uses: [KP5KA51FC4, PZX9J3VEMT, W72CA3R9MP]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Structural rules
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Cut-elimination in the sequent calculus
---

## Summary

A contraction-free sequent calculus has no rule that merges two copies of a formula, yet it loses nothing, because its logical rules keep a copy wherever a later step needs one.
So contraction is an [[admissible|C5K35H0R4Y]] rule there, not a primitive one, and a derivation consists of logical steps only.
Exactly: a sequent calculus is contraction-free when contraction is not among its rules and, for every formula $A$,
$$\vdash A, A, \Gamma \Rightarrow \Delta \text{ implies } \vdash A, \Gamma \Rightarrow \Delta, \qquad \vdash \Gamma \Rightarrow \Delta, A, A \text{ implies } \vdash \Gamma \Rightarrow \Delta, A.$$
The standard examples are Kleene's calculi G3cp and G3ip and Dyckhoff's LJT, all given in the [[definition|KP5KA51FC4]].
In G3cp and G3ip contraction is even height-preserving admissible: the shorter sequent has a derivation that is no higher.

## Motivation

Take the intuitionistic sequent $N \Rightarrow \bot$ with $N = (p \vee \neg p) \to \bot$.
Any proof must use $N$ twice: once to refute $p \vee \neg p$ after choosing $\neg p$, and once more inside the proof of $\neg p$.
In Gentzen's [[LJ|PZX9J3VEMT]] the second use needs an explicit contraction on $N$.
In G3ip the left implication rule keeps $N$ in its left premise, so the copy is already there.

A computer that searches for proofs backwards suffers from an explicit contraction rule.
The rule can be applied to any formula at any moment, so the search tree has no bound.
Contraction-free calculi tie the copying to the logical rules, which makes classical propositional search terminate at once and leads, through LJT, to a terminating search for intuitionistic logic.
The [[inversion lemma|EXMS77F2XN]] and the [[cut-elimination theorem|AYRZ98Y0NW]] are both proved most cleanly for these calculi.

## Notation

The names G3cp and G3ip follow Kleene's system G3 and the book of Troelstra and Schwichtenberg, where c, i and p mean classical, intuitionistic and propositional.
Dyckhoff called his calculus LJT, and Troelstra and Schwichtenberg call it G4ip.
We write $\vdash_n S$ when the sequent $S$ has a derivation of height at most $n$.
Rules are named L${\circ}$ and R${\circ}$ after the connective, and LJT adds rules such as L${\wedge}{\to}$, named after the shape of the antecedent of an implication.

## Remarks

### Contraction at work in G3ip

Here is the G3ip derivation of $N \Rightarrow \bot$, read from the bottom up.
Recall that $\neg p$ is $p \to \bot$, and that L${\to}$ in G3ip goes from $A \to B, \Gamma \Rightarrow A$ and $B, \Gamma \Rightarrow C$ to $A \to B, \Gamma \Rightarrow C$.

1. L${\to}$ on $N$ needs $N \Rightarrow p \vee \neg p$ and $\bot \Rightarrow \bot$, and the second is an axiom.
2. R${\vee}$ reduces $N \Rightarrow p \vee \neg p$ to $N \Rightarrow \neg p$, and R${\to}$ reduces that to $p, N \Rightarrow \bot$.
3. L${\to}$ on $N$ again needs $N, p \Rightarrow p \vee \neg p$ and $\bot, p \Rightarrow \bot$.
4. R${\vee}$ reduces the first to the axiom $N, p \Rightarrow p$, and the second is an axiom.

Step 3 uses $N$ a second time, and it is available only because step 1 kept it in the left premise.
No contraction rule appears, and none is needed.

### Why contraction is admissible

The proof of admissibility is an induction on the height $n$ of a derivation of $A, A, \Gamma \Rightarrow \Delta$, for all formulas at once.
If neither copy of $A$ is principal in the last rule, apply the induction hypothesis to the premises and repeat the rule.
If one copy is principal, invert the rule on the other copy with the [[inversion lemma|EXMS77F2XN]], which does not raise the height, then contract and repeat the rule.

For L${\wedge}$, a derivation of $A \wedge B, A \wedge B, \Gamma \Rightarrow \Delta$ of height $n$ ends with a premise $A, B, A \wedge B, \Gamma \Rightarrow \Delta$ of height $n - 1$.
Inversion gives $A, B, A, B, \Gamma \Rightarrow \Delta$ of height at most $n - 1$.
The induction hypothesis contracts $A$ and $B$, and L${\wedge}$ gives $A \wedge B, \Gamma \Rightarrow \Delta$ of height at most $n$.

For L${\to}$ in G3ip, inversion works only for the right premise, and the repeated principal formula covers the left one.
The left premise $A \to B, A \to B, \Gamma \Rightarrow A$ contracts by the induction hypothesis, since its height is smaller.

### More worked derivations

In G3cp, [[Peirce's law|MSPDTQHDYB]] has a derivation of height $3$ with one R${\to}$, one L${\to}$ and one more R${\to}$.
LK needs a weakening and a contraction for the same law, and G3cp hides both, in the atomic axiom and in the shared context of L${\to}$.

In LJT, the sequent $\Rightarrow \neg \neg (p \vee \neg p)$ has a [[five-rule derivation|VCM68VE14Y]] in which no formula is used twice.
The rule L${\vee}{\to}$ splits $(p \vee \neg p) \to \bot$ into $p \to \bot$ and $\neg p \to \bot$, and each piece is used once.

### What it is not

Deleting the contraction rules from LK does not give a contraction-free calculus.
[[Cut-free LK without contraction|MNEF21BD71]] derives $\Rightarrow p \vee \neg p, p \vee \neg p$ but not $\Rightarrow p \vee \neg p$, so contraction is not admissible and the calculus is incomplete.

Gentzen's LJ is not contraction-free either, since contraction is one of its rules.
Without CL, cut-free LJ cannot derive the sequent $N \Rightarrow \bot$ above: its last step must use $N$, and the premise $\Rightarrow p \vee \neg p$ is not derivable.

[[Linear logic|2P2184B6HE]] has no contraction rule, and contraction is not admissible there.
It is a substructural logic with a different set of theorems, not a contraction-free calculus for classical or intuitionistic logic.

### Termination and the weight of LJT

G3ip search can loop, because L${\to}$ keeps its principal formula.
Dyckhoff's LJT replaces L${\to}$ by four rules that split $A \to B$ by the shape of $A$.
Give each formula a weight by the rules below:
$$w(p) = w(\bot) = 1, \qquad w(A \wedge B) = w(A) + w(B) + 2, \qquad w(A \vee B) = w(A \to B) = w(A) + w(B) + 1.$$
Then in every LJT rule each premise is smaller than its conclusion, in the multiset ordering of weights.
So every branch of a backward search is finite, with no loop check.

The price is a weaker subformula property.
G3cp and G3ip have the full [[subformula property|Z2NXKDK06G]], while LJT can create new implications such as $C \to (D \to B)$ from $(C \wedge D) \to B$, built from subformulas of the end sequent.

### Watch out

The most common slip is to read "contraction-free" as "contraction is never needed".
Contraction is needed in the logic, as $N \Rightarrow \bot$ shows; it is only made unnecessary as a rule.

A second slip is to drop $A \to B$ from the left premise of L${\to}$ in G3ip to make search terminate.
The resulting calculus is incomplete: it cannot derive $N \Rightarrow \bot$, because step 3 above has no $N$ left to use.

A third slip concerns LJT: the rule L0${\to}$, from $p, B, \Gamma \Rightarrow E$ to $p, p \to B, \Gamma \Rightarrow E$, needs the atom $p$ itself in the antecedent, not just some formula.

### Try it

First, in G3cp derive $p \wedge q, p \wedge q \Rightarrow p$ and then $p \wedge q \Rightarrow p$, and compare the heights.
Both take one L${\wedge}$ above an axiom, so both have height $1$, as height-preserving contraction predicts.

Second, compute the weights of $(p \wedge q) \to r$ and $p \to (q \to r)$ in LJT.
They are $1 + 1 + 2 + 1 + 1 = 6$ and $1 + (1 + 1 + 1) + 1 = 5$, so L${\wedge}{\to}$ lowers the weight.

### History

Kleene introduced the G3 systems in his *Introduction to Metamathematics* of 1952.
Roy Dyckhoff published LJT in the Journal of Symbolic Logic in 1992, in the paper *Contraction-free sequent calculi for intuitionistic logic*.
Related calculi were found independently by Vorob'ev and by Hudelmaier.

## Explanations

### L1 human

When a proof uses an assumption twice, a formal system must let you keep the assumption after the first use.
Gentzen did this with a separate copying rule.
A computer searching for a proof can apply such a rule forever, so it may never stop.
Contraction-free calculi keep the copy inside the rules that need it.
In the derivation of $N \Rightarrow \bot$, the assumption $N$ is used twice, and the copy comes from the rule that used it first.

### L2 human

Check that the LJT rule L${\to}{\to}$ lowers the weight.
It goes from $D \to B, \Gamma \Rightarrow C \to D$ and $B, \Gamma \Rightarrow E$ to $(C \to D) \to B, \Gamma \Rightarrow E$.
The principal formula has weight
$$w((C \to D) \to B) = w(C) + w(D) + w(B) + 2.$$
The left premise replaces it and $E$ by $D \to B$ and $C \to D$, of weights $w(D) + w(B) + 1$ and $w(C) + w(D) + 1$.
Both are smaller, since every weight is at least $1$, and the right premise replaces it by $B$, which is smaller too.
This is the typical use of a weight: a termination proof for backward search.
The trap is the weight of $\wedge$: with $w(A \wedge B) = w(A) + w(B) + 1$, the rule L${\wedge}{\to}$ would keep the weight equal.

### L3 human

The G3 calculi make all structural rules admissible, so a derivation is determined by its logical rules, and induction on height becomes the main tool of structural proof theory.
The same design extends to first-order logic: G3c keeps the principal formula in L${\forall}$ and R${\exists}$, and G3i keeps it in L${\forall}$ and L${\to}$.
LJT gives a decision procedure for intuitionistic propositional logic, which is [[PSPACE|T9NTRY93ZT]]-complete.
Terminating contraction-free calculi have since been built for intermediate and modal logics, and the [[hypersequent calculus|73J7F0FN4A]] and [[labeled sequent calculus|F46GV42XCE]] reuse the same admissibility arguments.
