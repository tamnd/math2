---
tag: Z2NXKDK06G
kind: concept
name: Subformula property
msc: ["03F05", "03B05"]
topics: [R10RMQCJQX]
audience: grad
uses: [W72CA3R9MP, PZX9J3VEMT, NCDZ969V7X, AYRZ98Y0NW]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: Structural proof theory
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Analytic proof
---

## Summary

A derivation has the subformula property when it never mentions a formula that is not a piece of what it proves.
For example, a cut-free derivation of $\Rightarrow p \vee \neg p$ could only contain $p$, $\neg p$ and $p \vee \neg p$, and that short list is why intuitionistic LJ has no such derivation.

The *subformulas* of a formula $A$ are $A$ itself and the subformulas of its immediate parts.
The parts are $B$ and $C$ for $B \wedge C$, $B \vee C$ and $B \to C$; they are $B$ for $\neg B$; and they are $B[t/x]$, for every term $t$, for $\forall x\, B$ and $\exists x\, B$.
A class of derivations has the *subformula property* when every formula in a derivation of the class is a subformula of a formula in its conclusion.
In a [[sequent calculus|W72CA3R9MP]] the conclusion is the end sequent, and in natural deduction it is the end formula together with the open assumptions.
Cut-free sequent derivations and normal natural deduction derivations have the property.

## Motivation

A proof may pass through lemmas that look unrelated to the theorem.
That freedom makes proofs short, but it makes the search for a proof unbounded, since any formula at all might be the right lemma.
If every formula of a derivation comes from the conclusion, the search for a derivation of a given sequent runs over a fixed, finite stock of formulas, at least in propositional logic.
The [[cut-elimination theorem|AYRZ98Y0NW]] says that in pure logic nothing is lost by keeping to such derivations.

The property is the main tool for showing that something is not provable.
To show that LJ does not prove excluded middle, we list the few possible last steps of a cut-free derivation and rule each one out.
The same method proves the disjunction property of intuitionistic logic, decides propositional logics, and underlies tableau and resolution methods in automated reasoning.

## Notation

The extended sense of subformula, with all instances $B[t/x]$ of quantified formulas, is Gentzen's.
In propositional logic the subformulas of $A$ are just the nodes of its formula tree.
Derivations with the property are also called *analytic*.
For natural deduction the property is usually stated for normal derivations and with respect to the conclusion and the open assumptions together.

## Remarks

### Why LJ cannot prove excluded middle

We show that LJ does not derive $\Rightarrow p \vee \neg p$, for a propositional variable $p$.
By cut elimination it is enough to rule out a cut-free derivation, and by the property its only formulas are $p$, $\neg p$ and $p \vee \neg p$.
The antecedent of the end sequent is empty, so the last step is not a left rule or a left structural rule.
LJ allows one formula on the right, so the last step is not a contraction or exchange on the right either.
A weakening would come from the empty sequent $\Rightarrow$, which has no cut-free derivation.
So the last step is ${\vee}$R, from $\Rightarrow p$ or from $\Rightarrow \neg p$.
The first is false when $p$ is false, the second is false when $p$ is true, and LJ is sound, so neither is derivable.

In LK the argument breaks at one point: the succedent may hold two formulas.
There the last step can be a contraction from $\Rightarrow p \vee \neg p, p \vee \neg p$, and a derivation exists.

### What counts as a subformula

In first-order logic the instances matter.
The cut-free derivation of $\forall x\, P(x) \Rightarrow \exists x\, P(x)$ passes through $P(y) \Rightarrow P(y)$, and $P(y)$ counts as a subformula of $\forall x\, P(x)$; [[the quantifier example|87MDKS926K]] checks each step.
In propositional logic the list is short and finite.
The cut-free derivation of Peirce's law $((p \to q) \to p) \to p$ in [[the Peirce example|WFK9VE30Y0]] uses only $p$, $q$, $p \to q$, $(p \to q) \to p$ and the law itself, which are exactly its subformulas.

### Where the property comes from

Every rule of LK except cut has the property for a single step: each formula of a premise is a subformula of a formula of the conclusion.
By induction on the derivation, every cut-free derivation has the property.
Cut is the exception, because its cut formula may vanish.
By cut elimination, every sequent derivable in LK or LJ has a derivation with the property.
In Kleene's [[G3 calculi|KP5KA51FC4]] every derivation has it, since they have no cut, and each premise formula is a context formula of the conclusion or a part of its principal formula.
In natural deduction the [[normalization theorem|W33WAE1XTC]] plays the role of cut elimination.

### Decision procedures

Classical propositional logic is decidable by backward search in a cut-free calculus with sets of formulas.
Each sequent in the search is a pair of sets of subformulas of the goal, so there are finitely many, and the search ends.
The [[inversion lemma|EXMS77F2XN]] makes the search deterministic, since every rule of G3cp can be applied in any order.

Intuitionistic propositional logic is decidable too, but backward search in LJ can loop on a formula that is used again and again.
Gentzen bounded the number of repeated copies; Dyckhoff's calculus LJT gives a search that ends without such a bound, as described for [[contraction-free sequent calculi|KP5KA51FC4]].
In first-order logic the property does not give decidability, because the terms $t$ in the instances $B[t/x]$ are unbounded.

### Where the property fails

A derivation with a cut on a formula that is not a subformula of the end sequent fails the property, and the cut formula is the failing formula.
In the Hilbert system with the axiom schemes K and S and modus ponens, every derivation of $p \to p$ fails it, as [[the Hilbert derivation|D9V052EY7J]] shows: the last modus ponens needs a premise $A \to (p \to p)$.
In natural deduction, introducing $A \wedge B$ and at once eliminating it fails the property when $A \wedge B$ is not a subformula of the conclusion or the assumptions.

### Watch out

The first slip is to forget instances in first-order logic: $P(y)$ is a subformula of $\forall x\, P(x)$, though it is not a piece of the string.
The second slip is to apply the property to an arbitrary derivation: it holds for cut-free or normal ones, and a derivation with cuts can contain anything.
The third slip is to conclude that first-order logic is decidable, which it is not.

### History

Gentzen proved the property for cut-free derivations in LK and LJ, as a consequence of his Hauptsatz, in his paper of 1934 and 1935.
He used it there to give a decision procedure for intuitionistic propositional logic.
Prawitz proved the property for normal derivations of natural deduction in his book *Natural Deduction* of 1965.

### Try it

First, list the subformulas of $\neg (p \wedge q)$.
They are $\neg (p \wedge q)$, $p \wedge q$, $p$ and $q$.

Second, use the property to show that LJ does not derive $\Rightarrow p$.
A cut-free derivation could only contain $p$, so its last step would be a weakening from $\Rightarrow$, which is not derivable.

## Explanations

### L1 human

A formula is built from smaller pieces, the way a sentence is built from words.
A proof has the subformula property when it only uses pieces of what it proves.
For example, a proof of "if $p$ and $q$, then $p$" that only talks about $p$, $q$ and "$p$ and $q$" has the property.
Such a proof never brings in an outside idea.
That makes these proofs easier to find, because there are only a few things to try at each step.

### L2 human

We decide whether LJ derives $\Rightarrow (p \to q) \vee (q \to p)$, for distinct variables $p$ and $q$.
By the property, a cut-free derivation contains only this formula, $p \to q$, $q \to p$, $p$ and $q$.
As for excluded middle, the empty antecedent and the single formula on the right leave one possible last step, ${\vee}$R.
So we need $\Rightarrow p \to q$ or $\Rightarrow q \to p$.
The last step for $\Rightarrow p \to q$ is ${\to}$R from $p \Rightarrow q$, since a weakening would need the empty sequent.
The sequent $p \Rightarrow q$ is false when $p$ is true and $q$ is false, so LJ does not derive it, and in the same way it does not derive $q \Rightarrow p$.
So LJ does not derive the formula, while LK does, using two formulas on the right.
The typical use is exactly this: the property shrinks the possible last steps to a short list, and each item is checked by hand.
Watch out: the case analysis only works for cut-free derivations, so cut elimination must come first.

### L3 human

The subformula property is the syntactic side of conservativity.
A cut-free derivation of a sequent whose connectives lie in a set $K$ uses only rules for connectives in $K$.
So each fragment of LK or LJ is conservative over smaller fragments, and the meaning of a connective depends only on its own rules, as [[proof-theoretic semantics|K97KZB5R7N]] asks.
The failure of the property for modus ponens is why Hilbert systems are poor for proof search, and why analytic methods such as tableaux and resolution are used in [[automated theorem proving|A51M1KK9DJ]].
For deep inference and display calculi, whose rules act inside formulas or on structures, weaker forms of the property are studied.
