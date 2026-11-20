---
tag: H408H4WHBA
kind: definition
name: Linear logic
msc: ["03B47", "03F52"]
topics: [98QF5J4W16]
audience: research
defines: 2P2184B6HE
uses: [W72CA3R9MP, 09K9MWD2QQ, DAMGTSY6VV]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_logic
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Sequent calculus presentation
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Notation comparison
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.1 Sequent calculus
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1016/0304-3975(87)90045-4
    locator: pages 1-101
    note: Girard, Linear logic, Theoretical Computer Science 50 (1987)
---

## Definition

The formulas of propositional *linear logic* are built from atoms $p$ and their duals $p^{\perp}$ by the following connectives.

1. Multiplicatives: $A \otimes B$ (tensor), $A \mathbin{\wp} B$ (par), and the units $1$ and $\bot$.
2. Additives: $A \mathbin{\&} B$ (with), $A \oplus B$ (plus), and the units $\top$ and $0$.
3. Exponentials: $!A$ (of course) and $?A$ (why not).

*Linear negation* $A^{\perp}$ is defined by $(p)^{\perp} = p^{\perp}$, $(p^{\perp})^{\perp} = p$ and the De Morgan laws:
$$(A \otimes B)^{\perp} = A^{\perp} \mathbin{\wp} B^{\perp}, \quad (A \mathbin{\&} B)^{\perp} = A^{\perp} \oplus B^{\perp}, \quad 1^{\perp} = \bot, \quad \top^{\perp} = 0, \quad (!A)^{\perp} = ?A^{\perp},$$
and the same laws read from right to left.
A sequent is $\vdash \Gamma$, where $\Gamma$ is a finite multiset of formulas, and $?\Gamma$ is a multiset in which every formula has the form $?A$.
The sequents derivable by the following rules form linear logic.

1. Axiom: $\vdash A^{\perp}, A$.
   Cut: from $\vdash \Gamma, A$ and $\vdash \Delta, A^{\perp}$ infer $\vdash \Gamma, \Delta$.
2. $\otimes$: from $\vdash \Gamma, A$ and $\vdash \Delta, B$ infer $\vdash \Gamma, \Delta, A \otimes B$.
   $\mathbin{\wp}$: from $\vdash \Gamma, A, B$ infer $\vdash \Gamma, A \mathbin{\wp} B$.
3. $1$: $\vdash 1$ is an axiom.
   $\bot$: from $\vdash \Gamma$ infer $\vdash \Gamma, \bot$.
4. $\mathbin{\&}$: from $\vdash \Gamma, A$ and $\vdash \Gamma, B$ infer $\vdash \Gamma, A \mathbin{\&} B$.
   $\oplus$: from $\vdash \Gamma, A$ infer $\vdash \Gamma, A \oplus B$, and from $\vdash \Gamma, B$ infer $\vdash \Gamma, A \oplus B$.
5. $\top$: $\vdash \Gamma, \top$ is an axiom for every $\Gamma$; $0$ has no rule.
6. Dereliction $?D$: from $\vdash \Gamma, A$ infer $\vdash \Gamma, ?A$.
   Weakening $?W$: from $\vdash \Gamma$ infer $\vdash \Gamma, ?A$.
   Contraction $?C$: from $\vdash \Gamma, ?A, ?A$ infer $\vdash \Gamma, ?A$.
7. Promotion $!$: from $\vdash ?\Gamma, A$ infer $\vdash ?\Gamma, !A$.

## Notation

*Linear implication* is $A \multimap B = A^{\perp} \mathbin{\wp} B$.
The fragments are: MLL with $\otimes$, $\mathbin{\wp}$, $1$, $\bot$; MALL with the multiplicatives and additives; MELL with the multiplicatives and exponentials; and LL with all connectives.
A two-sided sequent $A_1, \dots, A_m \vdash B_1, \dots, B_n$ stands for $\vdash A_1^{\perp}, \dots, A_m^{\perp}, B_1, \dots, B_n$.
We use Girard's notation, and other authors use different symbols; see [[the concept|2P2184B6HE]] for a comparison.
Exchange is implicit, since sequents are multisets, and there is no general weakening or contraction.

## Remarks

The two conjunctions differ in how they treat the context.
The rule for $\otimes$ splits the context between the premises, and the rule for $\mathbin{\&}$ gives the whole context to both premises.

Example: $\vdash A^{\perp}, A \mathbin{\&} A$ is derivable: apply the rule for $\mathbin{\&}$ to two copies of the axiom $\vdash A^{\perp}, A$.

Non-example: $\vdash p^{\perp}, p \otimes p$ is not derivable for an atom $p$.
By cut elimination, a derivation can be taken cut-free, and then its last rule is the $\otimes$ rule, since the other formula is an atom.
That rule gives $p^{\perp}$ to one premise and nothing to the other, and $\vdash p$ is not derivable; see [[the full check|~4201f767]].
In classical [[propositional logic|09K9MWD2QQ]], $p \to p \wedge p$ is a tautology, which shows the role of contraction.

The rules are symmetric under negation: the rule for $\mathbin{\wp}$ plays the role of the left rule for $\otimes$ in a two-sided calculus.
Promotion requires that all other formulas have the form $?B$; in two-sided notation, all hypotheses must have the form $!B$.

## Explanations

### L1 human

Linear logic is a list of rules for proofs in which hypotheses are counted.
Each connective has its own rule, and the rules say how the hypotheses are shared or split.
Only formulas marked with "?" can be copied or thrown away.

### L2 human

We show that $p \otimes q \vdash p$ is not derivable for atoms $p$ and $q$, so a tensor cannot be projected.

1. In one-sided form the sequent is $\vdash p^{\perp} \mathbin{\wp} q^{\perp}, p$.
2. By cut elimination we search for a cut-free derivation.
   The formula $p$ is an atom, so the last rule is $\mathbin{\wp}$, with premise $\vdash p^{\perp}, q^{\perp}, p$.
3. This premise is not an axiom, since an axiom has exactly two formulas.
4. All three formulas are atoms or duals of atoms, so no logical rule ends in this sequent, and there are no structural rules on them.
5. So the sequent is not derivable: the hypothesis $q$ cannot be discarded.

The typical use of the one-sided calculus is to keep one rule for each connective, which halves the number of cases in proofs.
A trap: $p \mathbin{\&} q \vdash p$ is derivable, by the rule for $\oplus$ on $\vdash p^{\perp}, p$, so the two conjunctions behave differently.
