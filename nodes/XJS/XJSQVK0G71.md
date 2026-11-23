---
tag: XJSQVK0G71
kind: concept
name: Harmony
msc: ["03F03", "03A05"]
topics: [R10RMQCJQX]
audience: grad
uses: [PAQ4ZX2TX1, QS0XVAN9BG]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section H
    note: adopted
    mention: wikipedia://en/76765067#2JXB
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Logical_harmony
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Proof-theoretic_semantics
    locator: Philosophical motivation
inventory: [FXKS4B0HTC]
---

## Summary

Prove $A$ and prove $B$, combine them by ${\wedge}$I into $A \wedge B$, and take $A$ back out by ${\wedge}$E$_1$: the detour gave nothing that the proof of $A$ did not already give.
Harmony is the requirement that the introduction and elimination rules of a connective balance in this way, so that the eliminations take out no more and no less than the introductions put in.
In [[natural deduction|PAQ4ZX2TX1]] the usual test has two parts.
The rules are *locally sound* when an introduction followed at once by an elimination of the same formula can be removed by a reduction.
They are *locally complete* when every proof of a formula can be expanded into eliminations followed by an introduction of that formula.
Harmony is the central condition of [[proof-theoretic semantics|K97KZB5R7N]] for rules that define a connective.

## Motivation

If the meaning of a [[connective|QS0XVAN9BG]] is given by its rules, then its rules cannot be arbitrary.
Prior's connective [[tonk|QSVQ1KPNBX]] has an introduction rule of disjunction and an elimination rule of conjunction, and it makes every formula derivable from every formula.
Harmony excludes such connectives.
It asks that the elimination rules give back exactly what the introduction rules require.

## Notation

An introduction rule of $\circ$ is written $\circ$I and an elimination rule $\circ$E.
A *detour* or *maximal formula* is an occurrence of a formula that is the conclusion of an introduction and the major premise of an elimination.
Local soundness is shown by a *reduction*, written $D \rightsquigarrow D'$, and local completeness by an *expansion*.
Some authors use the word harmony for local soundness alone, and stability for the two conditions together.

## Remarks

### The test on conjunction

For $\wedge$ the reduction and the expansion are short.
A detour ${\wedge}$I then ${\wedge}$E$_1$, built from derivations $D_1$ of $A$ and $D_2$ of $B$, reduces to $D_1$, and the detour with ${\wedge}$E$_2$ reduces to $D_2$.
For the expansion, take any derivation $D$ of $A \wedge B$, apply ${\wedge}$E$_1$ and ${\wedge}$E$_2$ to two copies of it, and recombine by ${\wedge}$I.
$$\dfrac{\dfrac{A \wedge B}{A}\,{\wedge}\mathrm{E}_1 \qquad \dfrac{A \wedge B}{B}\,{\wedge}\mathrm{E}_2}{A \wedge B}\,{\wedge}\mathrm{I}$$
The full check is in [[the conjunction example|53ERPXVZ3S]], and implication works the same way, with the detour reduction of the [[normalization theorem|W33WAE1XTC]], see [[the implication example|QWWR80Y2XT]].

### Disjunction and falsum

The rules for disjunction are in harmony.
A proof of $A \vee B$ by ${\vee}$I from a proof of $A$, followed by ${\vee}$E, reduces to the first minor derivation of the ${\vee}$E step, with that proof of $A$ put in place of the assumption $A$.
The rule ${\bot}$E, with no introduction rule for $\bot$, is in harmony in a trivial way, since there is no detour on $\bot$.

### Failures in both directions

The rules of tonk are not locally sound: there is no reduction of tonk-I followed by tonk-E, see [[the tonk example|JVV2QRX0H2]].
Conjunction with an extra elimination rule that infers any $C$ from $A \wedge B$ is not locally sound either, since the detour gives $C$ and the subproofs give only $A$ and $B$.
In the other direction, conjunction with ${\wedge}$I and only ${\wedge}$E$_1$ is locally sound but not locally complete, because from a proof of $A \wedge B$ it cannot recover $B$.

### What harmony gives

If all connectives of a natural deduction system are locally sound, every detour has a reduction, and a normalization proof has the steps it needs.
If a system extended by a new connective still normalizes, and its normal derivations have the subformula property, then it is a [[conservative extension|N238J43XNE]] of the old system.
Local completeness lets us expand an assumption $A$ into a derivation of $A$ from $A$ that breaks $A$ down to atoms and builds it back, the natural deduction form of atomic axioms.
Under the [[Curry-Howard correspondence|A77FER1Q5H]], the reductions are beta reductions and the expansions are eta expansions.

### Watch out

Checking only local soundness is not enough, since rules that are too weak pass it, and local completeness detects them.
Harmony is a condition on the rules only, and it does not refer to truth tables.
Local soundness also does not prove normalization: it gives a reduction for each detour, and showing that reductions end is a separate task.
The classical rule of double negation elimination is not in harmony with the intuitionistic rules for negation under the usual definitions.

### History

Gentzen wrote in 1934 and 1935 that the introduction rules are, as it were, the definitions of the connectives.
Prawitz formulated the inversion principle in *Natural Deduction* of 1965, which gives the elimination rules from the introduction rules.
Prior introduced tonk in 1960, and Belnap replied in 1962 with the requirement that a new connective give a conservative extension.
Michael Dummett introduced the name harmony in *Frege: Philosophy of Language* of 1973, and he discussed it at length in *The Logical Basis of Metaphysics* of 1991.

### Try it

Exercise 1: give the expansion for implication.
Answer: from a derivation $D$ of $A \to B$, apply ${\to}$E to $D$ and a new assumption $[A]^u$ to get $B$, then ${\to}$I discharging $u$ gives $A \to B$ again.

Exercise 2: is a rule that infers $A$ from $A \vee B$ in harmony with the usual ${\vee}$I rules?
Answer: no, since a canonical proof of $A \vee B$ may come from a proof of $B$, and then the detour gives $A$ with no proof of $A$ to reduce to.

## Explanations

### L1 human

A connective is in harmony when what we can conclude from a statement matches what we needed to prove it.
For "and", we need both parts to prove "$A$ and $B$", and from it we may conclude either part.
Nothing is lost and nothing is gained.

### L2 human

To test harmony for a connective, write down a proof that introduces it and then eliminates it at once.

1. Check that the conclusion can be obtained without the detour, from the subproofs used by the introduction.
2. Then take any proof of the compound formula, apply the eliminations, and rebuild the formula with the introduction.

The typical use is to accept or reject a proposed rule set.
A trap: an elimination rule can be weaker than allowed and still pass step 1, so step 2 is needed.

### L3 human

Harmony is the natural deduction form of the principal case of cut elimination.
General-elimination rules, in the style of ${\vee}$E, give a uniform way to derive elimination rules from introduction rules.
For classical logic, harmony can be recovered with multiple conclusions or with bilateral systems that have rules for assertion and denial.
In [[proof-theoretic semantics|K97KZB5R7N]], harmony is the condition that makes introduction rules work as definitions.
