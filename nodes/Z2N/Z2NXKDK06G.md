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

The *subformulas* of a formula $A$ are $A$ itself and the subformulas of its immediate parts: $B$ and $C$ for $B \wedge C$, $B \vee C$ and $B \to C$, $B$ for $\neg B$, and $B[t/x]$ for $\forall x\, B$ and $\exists x\, B$, for every term $t$.
A class of derivations has the *subformula property* when every formula in a derivation of the class is a subformula of a formula in its conclusion.
For sequents, the conclusion is the end sequent, and in natural deduction it is the end formula together with the open assumptions.
Cut-free sequent derivations and normal natural deduction derivations have the property, and this makes them analytic: they contain no detours through unrelated formulas.

## Motivation

A proof of a theorem may pass through lemmas whose statements have nothing to do with the theorem.
That freedom makes proofs short, but it also makes the search for a proof unbounded.
If every formula of a derivation comes from the conclusion, then the derivations of a given sequent can be searched in a finite space of formulas.
The [[cut-elimination theorem|AYRZ98Y0NW]] shows that in pure logic we lose nothing by keeping to such derivations.

## Notation

The extended sense of subformula, with instances $B[t/x]$ of quantified formulas, is Gentzen's.
In the propositional case, the subformulas of $A$ are its parts in the usual sense of the formula tree.
Some authors call a derivation with this property *analytic*.
For natural deduction, the property is usually stated for normal derivations and with respect to the conclusion and the open assumptions.

## Remarks

### Examples

- A cut-free LK derivation of Peirce's law $((p \to q) \to p) \to p$ uses only the formulas $p$, $q$, $p \to q$, $(p \to q) \to p$ and the end formula, see [[this example|WFK9VE30Y0]].
- The cut-free derivation of $\forall x\, P(x) \Rightarrow \exists x\, P(x)$ through $P(y) \Rightarrow P(y)$ uses the instance $P(y)$, a subformula in the extended sense, see [[this example|87MDKS926K]].
- Every derivation in Kleene's [[contraction-free calculi|KP5KA51FC4]] G3 has the property, since none of its rules removes a formula except as part of a principal formula.
- A normal derivation in the implicational fragment of [[natural deduction|PAQ4ZX2TX1]] has the property, by the [[normalization theorem|W33WAE1XTC]].

### Non-examples

- A derivation with a cut on a formula that is not a subformula of the end sequent fails the property. The cut formula is the failing formula.
- Every derivation of $p \to p$ in the Hilbert system with the axiom schemes K and S and modus ponens fails the property, see [[this non-example|D9V052EY7J]].
- A natural deduction derivation that introduces $A \wedge B$ and then eliminates it again fails the property when $A \wedge B$ is not a subformula of the conclusion or the assumptions.

### Basic properties

- Every rule of LK except cut has the property for one step: each formula of a premise is a subformula of a formula of the conclusion. So every cut-free derivation has the property.
- By cut elimination, every sequent derivable in LK or LJ has a derivation with the property.
- Classical propositional logic is decidable: a backward search in a cut-free calculus with sets of formulas visits only finitely many sequents of subformulas. The [[inversion lemma|EXMS77F2XN]] makes this search deterministic.
- Intuitionistic propositional logic is decidable. A cut-free search in LJ needs a bound on repeated formulas, and Dyckhoff's calculus LJT gives a terminating search, see [[contraction-free sequent calculi|KP5KA51FC4]].
- The empty sequent has no derivation with the property, since it has no subformulas and every rule except cut has a nonempty conclusion. This gives the consistency of LK.

### History

Gentzen proved the property for cut-free derivations of LK and LJ, as a consequence of his Hauptsatz, published in 1934 and 1935.
He used it to give a decision procedure for intuitionistic propositional logic.
Prawitz proved it for normal natural deduction derivations in his book *Natural Deduction* of 1965.

### Common errors

- Forgetting the instances $B[t/x]$ in first-order logic: $P(y)$ counts as a subformula of $\forall x\, P(x)$.
- Thinking that the property holds for all derivations: it holds for cut-free or normal ones.
- Thinking that the property alone gives decidability of first-order logic: the terms $t$ in the instances are unbounded, and first-order validity is undecidable.

## Explanations

### L1 human

A formula is built from smaller pieces, like a sentence from words.
A proof has the subformula property when it only uses pieces of what it proves.
For example, a proof of "if $p$ and $q$ then $p$" that only talks about $p$, $q$ and "$p$ and $q$" has the property.
Such a proof never brings in an outside idea.
That makes these proofs easier to find, since there are fewer things to try.

### L2 human

We show that LJ does not derive $\Rightarrow p \vee \neg p$, for a propositional variable $p$.

1. By cut elimination, it is enough to show that there is no cut-free LJ derivation.
2. The antecedent is empty, so the last step is not a left rule. It is not a contraction or an exchange on the right, because LJ allows only one formula there.
3. A weakening would come from the empty sequent $\Rightarrow$, which has no cut-free derivation.
4. So the last step is ${\vee}$R, from $\Rightarrow p$ or from $\Rightarrow \neg p$.
5. $\Rightarrow p$ is false when $p$ is false, and $\Rightarrow \neg p$ is false when $p$ is true. So neither is derivable, since LJ is sound.

The typical use is this kind of argument: the subformula property limits the possible last steps, and we check each one.
A trap is to apply it to a calculus where cut has not been eliminated.

### L3 human

The subformula property is the syntactic side of conservativity: a derivation of a sequent with connectives from a set $K$ uses only rules for connectives in $K$.
So each fragment of LK or LJ is conservative over the smaller fragments, and the meaning of a connective depends only on its own rules, as [[proof-theoretic semantics|K97KZB5R7N]] requires.
Its failure for modus ponens is why Hilbert systems are poor for proof search, and why resolution and tableaux, which are analytic, are used in [[automated theorem proving|A51M1KK9DJ]].
For deep inference and display calculi, weaker forms of the property are studied, since their rules can act inside formulas.
