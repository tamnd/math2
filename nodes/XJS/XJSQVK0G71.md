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

In logic and philosophy, the notion that the introduction and elimination rules for a logical connective should be in balance, ensuring that the connective does not introduce more than it can eliminate, and vice versa.
In [[natural deduction|PAQ4ZX2TX1]], the usual test has two parts.
The rules are *locally sound* when an introduction followed at once by an elimination of the same formula can be removed by a reduction.
They are *locally complete* when every proof of a formula can be expanded into eliminations followed by an introduction of that formula.
Harmony is the central condition of [[proof-theoretic semantics|K97KZB5R7N]] for rules that define a connective.

## Motivation

If the meaning of a [[connective|QS0XVAN9BG]] is given by its rules, then its rules cannot be arbitrary.
Prior's connective [[tonk|QSVQ1KPNBX]] has an introduction rule of disjunction and an elimination rule of conjunction, and it makes every formula derivable from every formula.
Harmony excludes such connectives.
It asks that the elimination rules give back exactly what the introduction rules require, no more and no less.

## Notation

An introduction rule of $\circ$ is written $\circ$I and an elimination rule $\circ$E.
A *detour* or *maximal formula* is an occurrence of a formula that is the conclusion of an introduction and the major premise of an elimination.
Local soundness is shown by a *reduction*, written $D \rightsquigarrow D'$, and local completeness by an *expansion*.
Some authors use the word harmony for local soundness alone, and stability for the two conditions together.

## Remarks

### Examples

- The rules $\wedge$I, $\wedge$E$_1$ and $\wedge$E$_2$ for conjunction are in harmony, see [[this example|53ERPXVZ3S]].
- The rules ${\to}$I and ${\to}$E for implication are in harmony, and the reduction is the detour reduction of the [[normalization theorem|W33WAE1XTC]], see [[this example|QWWR80Y2XT]].
- The rules for disjunction are in harmony: a proof of $A \vee B$ by $\vee$I from a proof of $A$, followed by $\vee$E, reduces to the first minor derivation of the $\vee$E step, with that proof of $A$ put in place of the assumption $A$.
- The rule $\bot$E, with no introduction rule for $\bot$, is in harmony in a trivial way, since there is no detour on $\bot$.

### Non-examples

- The rules of tonk are not in harmony: there is no reduction of tonk-I followed by tonk-E, see [[this non-example|JVV2QRX0H2]].
- Conjunction with $\wedge$I and only $\wedge$E$_1$ is locally sound but not locally complete: from a proof of $A \wedge B$ it cannot recover $B$.
- Conjunction with an extra elimination rule that infers $C$ from $A \wedge B$, for any $C$, is not locally sound.

### Basic properties

- If all connectives of a natural deduction system are locally sound, every detour has a reduction, and normalization arguments can start.
- If a system extended by a new connective still normalizes, and its normal derivations have the subformula property, then it is a [[conservative extension|N238J43XNE]] of the old system.
- With local completeness for every connective, each derivation of $A$ from the assumption $A$ can be expanded until all its maximal parts end in atomic formulas.
- Under the [[Curry-Howard correspondence|A77FER1Q5H]], the reductions are beta reductions and the expansions are eta expansions.

### History

Gentzen wrote that the introduction rules are, as it were, the definitions of the connectives.
Prawitz formulated the inversion principle, which gives the elimination rules from the introduction rules.
Prior introduced tonk in 1960, and Belnap replied in 1962 with the requirement that a new connective give a conservative extension.
Michael Dummett coined the name harmony, and he discussed it in *The Logical Basis of Metaphysics* of 1991.

### Common errors

- Checking only local soundness. Rules that are too weak pass this test, and local completeness detects them.
- Thinking that harmony depends on the truth tables. It is a condition on the rules only.
- Expecting the classical rule of double negation elimination to be in harmony with the intuitionistic rules for negation. It is not, under the usual definitions.

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
General-elimination rules, in the style of $\vee$E, give a uniform way to derive elimination rules from introduction rules.
For classical logic, harmony can be recovered with multiple conclusions or with bilateral systems that have rules for assertion and denial.
In [[proof-theoretic semantics|K97KZB5R7N]], harmony is the condition that makes introduction rules work as definitions.
