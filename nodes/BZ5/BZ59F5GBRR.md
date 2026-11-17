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

A contraction-free sequent calculus is a sequent calculus without a contraction rule, whose rules make contraction admissible.
The main examples are the calculi G3cp and G3ip of the [[definition|KP5KA51FC4]], and Dyckhoff's calculus LJT for intuitionistic propositional logic.
They use multisets, atomic axioms with built-in weakening, and rules that copy a principal formula into a premise where it may be needed again.
In LJT every premise is smaller than its conclusion, so backward proof search terminates.

## Motivation

In Gentzen's [[LK and LJ|PZX9J3VEMT]], contraction can be applied at any point of a backward search, so the search space is infinite.
Removing contraction as a rule, while keeping it admissible, makes the search space easier to control.
For classical propositional logic, G3cp gives a terminating search in which every rule is invertible.
For intuitionistic propositional logic, the left implication rule of G3ip must keep its principal formula, and LJT shows how to avoid this loop.

## Notation

The names G3cp and G3ip follow Kleene's systems G3 and the book of Troelstra and Schwichtenberg.
LJT is Dyckhoff's name, and Troelstra and Schwichtenberg call it G4ip.
We write $\vdash_n S$ for derivability with height at most $n$.
Rules are named L${\circ}$ and R${\circ}$ for the connective $\circ$, and LJT adds rules such as L${\wedge}{\to}$ named by the shape of the principal formula.

## Remarks

### Examples

- G3cp derives [[Peirce's law|GMSZ75D5WE]] with one application of each rule and no contraction, see [[this example|MSPDTQHDYB]].
- LJT derives $\neg \neg (p \vee \neg p)$ with a search in which each step reduces the weight, see [[this example|VCM68VE14Y]].
- G3ip is contraction-free: its rule L${\to}$ keeps $A \to B$ in the left premise, and contraction is height-preserving admissible.
- The first-order calculus G3c keeps the principal formula in the premises of L${\forall}$ and R${\exists}$, G3i keeps it in L${\forall}$, and contraction is admissible in both.

### Non-examples

- Cut-free LK without its contraction rules is not contraction-free in this sense: it derives $\Rightarrow p \vee \neg p, p \vee \neg p$ but not $\Rightarrow p \vee \neg p$, see [[this non-example|MNEF21BD71]].
- Gentzen's LJ has contraction as a rule, and the rule is needed: without CL, cut-free LJ does not derive $\Rightarrow \neg \neg (p \vee \neg p)$.
- Linear logic has no contraction, but contraction is not admissible there, so it is a substructural logic and not a contraction-free calculus for classical or intuitionistic logic.

### Basic properties

- In G3cp and G3ip, weakening and contraction are height-preserving admissible.
- Cut is admissible in G3cp, G3ip and LJT.
- Every rule of G3cp is height-preserving invertible, by the [[inversion lemma|EXMS77F2XN]].
- G3cp and G3ip have the [[subformula property|Z2NXKDK06G]]. In LJT, every formula of a derivation is a subformula of the end sequent or is built by $\to$ from such subformulas.
- In LJT, with weights $w(p) = w(\bot) = 1$, $w(A \wedge B) = w(A) + w(B) + 2$ and $w(A \vee B) = w(A \to B) = w(A) + w(B) + 1$, every premise is smaller than its conclusion in the multiset ordering.

### History

Kleene introduced the calculi G3 in his *Introduction to Metamathematics* of 1952.
Roy Dyckhoff introduced LJT in the paper *Contraction-free sequent calculi for intuitionistic logic* in the Journal of Symbolic Logic in 1992.
Related calculi were given by Vorob'ev and by Hudelmaier.

### Common errors

- Confusing "contraction-free" with "no contraction is needed". Contraction is admissible because the rules already duplicate the formulas that need it.
- Dropping $A \to B$ from the left premise of L${\to}$ in G3ip. The resulting calculus does not derive $\neg \neg (p \vee \neg p)$.
- Applying L0${\to}$ of LJT when $p$ is not in the antecedent. The rule needs the atom $p$ itself.

## Explanations

### L1 human

When a proof uses an assumption twice, a formal system must allow the assumption to be copied.
Gentzen did this with an explicit copying rule, which makes it hard for a computer to search for proofs.
Contraction-free calculi build the copying into the other rules, only where it is needed.
For intuitionistic logic, Dyckhoff's calculus avoids it altogether, so a search for a proof always stops.

### L2 human

We show that the weight decreases for L${\to}{\to}$ of LJT.

1. The principal formula $(C \to D) \to B$ has weight $w(C) + w(D) + w(B) + 2$.
2. The left premise replaces it by $D \to B$ and $C \to D$, of weights $w(D) + w(B) + 1$ and $w(C) + w(D) + 1$, and drops $E$.
3. Both are smaller, since every weight is at least $1$.
4. The right premise replaces it by $B$, which is smaller.

The typical use of the weights is a termination proof for backward search.
A trap is the weight of $\wedge$: with $w(A \wedge B) = w(A) + w(B) + 1$, the rule L${\wedge}{\to}$ would not decrease the weight.

### L3 human

The calculi G3 make the structural rules admissible instead of primitive, so derivations are determined by their logical rules.
LJT shows that intuitionistic propositional logic has a terminating cut-free calculus without loop checking.
Contraction-free calculi are a starting point for terminating calculi for intermediate and modal logics.
