---
tag: YREXK6X3RP
kind: definition
name: Affine linear logic
msc: ["03F52", "03B47"]
topics: [98QF5J4W16]
audience: research
defines: K67C2N2QAH
uses: [H408H4WHBA, VHRXX0T5XT]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_logic
    locator: lead
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Variants
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 4. Complexity
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Definition

*Affine linear logic*, or *affine logic*, is the one-sided sequent calculus of [[linear logic|H408H4WHBA]] with one more rule, *weakening*:
$$\frac{\vdash \Gamma}{\vdash \Gamma, A}\ (W)$$
for every sequent $\Gamma$ and every formula $A$.
All other rules are those of linear logic: the axiom, cut, the rules for $\otimes$, $\mathbin{\wp}$, $\mathbin{\&}$, $\oplus$, the units, and the rules for $!$ and $?$.
A sequent is *derivable in affine logic* if it has a derivation with these rules.
The fragments are named as for linear logic: affine MLL, affine MALL, and so on.

## Notation

Linear logic has weakening only for formulas $?A$; affine logic has it for all formulas.
Contraction stays restricted to formulas $?A$.
The Wikipedia article on linear logic describes affine logic as the variant that forbids contraction but allows weakening.

## Remarks

1. With rule $W$, the rule $?W$ of linear logic is a special case.
2. Affine logic proves every sequent that linear logic proves, since it has all the rules of linear logic.
3. In affine logic, if $\vdash \Gamma$ is derivable, then so is $\vdash \Gamma, \Delta$ for every multiset $\Delta$, by repeated use of $W$.
4. The Wikipedia article states that affine logic embeds into linear logic by sending $A \rightarrow B$ to $A \multimap B \otimes \top$.

## Explanations

### L1 human

Affine logic is linear logic with one extra freedom: we may add any formula to a provable sequent.
In terms of resources, we may throw a resource away, but we may still not copy it.

### L2 human

We derive $\vdash p^{\perp}, q^{\perp}, p$, which says that $p$ follows from $p$ and $q$ together.

1. $\vdash p^{\perp}, p$ is an axiom.
2. Rule $W$ with $A = q^{\perp}$ gives $\vdash p^{\perp}, q^{\perp}, p$.

The typical use of rule $W$ is to discard a hypothesis that a proof does not need.
A trap: rule $W$ adds a formula to the conclusion; it does not remove one, so $\vdash p^{\perp}, p, q$ does not give $\vdash p$.
