---
tag: HGJVM49PA4
kind: concept
name: Double-negation translation
msc: ["03F25", "03F55", "03B20"]
topics: [8XY7JYZKFW]
audience: grad
uses: [Q11N8X99FK, 0XR7A7RSXB, 6KT3BJZ7D1, 0QFT7Z76N5, CK8ZQRN183, QEZR7PZ2DD]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Propositional logic
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: First-order logic
  - url: https://en.wikipedia.org/wiki/Glivenko%27s_theorem
    locator: lead section
  - book: isbn:9781447145578
same_as:
  wikidata: Q5299605
  wikipedia: Double-negation translation
---

## Summary

A double-negation translation is a map $A \mapsto A^*$ from the formulas of a first-order language to formulas of the same language with two properties.
First, $A^*$ is equivalent to $A$ in classical logic.
Second, for every set of formulas $\Gamma$, $\Gamma \vdash A$ in classical logic if and only if $\Gamma^* \vdash A^*$ in [[intuitionistic logic|Q11N8X99FK]].
The translation inserts double [[negations|0XR7A7RSXB]] $\neg \neg$ at chosen places, and $\neg B$ is read as $B \to \bot$.
The three standard translations are those of Kolmogorov, of Gödel and Gentzen, and of Kuroda; the [[definition|QEZR7PZ2DD]] gives their clauses.
The idea matters because it embeds classical logic into intuitionistic logic, so that classical [[Peano arithmetic|0QFT7Z76N5]] is consistent if intuitionistic [[Heyting arithmetic|CK8ZQRN183]] is consistent.

## Motivation

Intuitionistic logic drops the law of excluded middle $A \vee \neg A$.
At first sight, classical reasoning then looks stronger and less safe than intuitionistic reasoning.
But intuitionistic logic proves $\neg \neg (A \vee \neg A)$ for every formula $A$.
So a classical theorem often has an intuitionistic proof once it is weakened by double negations at the right places.
The weakened formula says "a counterexample is impossible", and this negative content is what a classical proof establishes.
A double-negation translation makes this precise for all formulas at once.
In arithmetic it shows that a contradiction from the classical axioms would give a contradiction from the intuitionistic axioms.

## Notation

We write $A^N$ for the Gödel-Gentzen translation, $A^K$ for the Kolmogorov translation and $A^{Ku}$ for the Kuroda translation.
Many books call the Gödel-Gentzen translation the negative translation, and some write $A^g$ or $A^\circ$ for it.
For a set $\Gamma$ we write $\Gamma^N = \set{B^N : B \in \Gamma}$.
We write $\vdash_c$ for derivability in classical [[natural deduction|6KT3BJZ7D1]] NK and $\vdash_i$ for derivability in intuitionistic natural deduction NJ.

## Remarks

### Examples

- [[The negative translation of the law of excluded middle|F8789WMFC6]]: $(P \vee \neg P)^N$ is $\neg (\neg \neg \neg P \wedge \neg \neg \neg \neg P)$, and NJ derives it in five steps.
- [[The three translations of one formula|28D8ACKEY0]]: for $\forall x\, (P(x) \vee \neg P(x))$ the translations of Kolmogorov, Gödel-Gentzen and Kuroda look different, but they are intuitionistically equivalent and provable.
- A $\Pi^0_2$ sentence $\forall x\, \exists y\, \varphi(x, y)$ of arithmetic, with $\varphi$ quantifier-free, has the translation $\forall x\, \neg \forall y\, \neg \varphi(x, y)$, up to equivalence in HA. This form denies a counterexample but names no witness; [[Friedman's A-translation|6CCK0TT69P]] recovers the witness.
- A formula without $\vee$ and $\exists$ in the language of arithmetic is equivalent in HA to its own translation. So [[PA is conservative over HA for such formulas|DC1X1S0DJE]].
- For a propositional formula $A$, the formula $\neg \neg A$ is already a translation: Glivenko's theorem says that $\vdash_c A$ if and only if $\vdash_i \neg \neg A$.

### Non-examples

- The identity map $A \mapsto A$. The condition that fails: $P \vee \neg P$ is classically provable, but not intuitionistically provable.
- [[Prefixing a double negation in predicate logic|ZV2MWBRN04]]: the map $A \mapsto \neg \neg A$ works for propositional logic but not for predicate logic. The condition that fails: $\neg \neg \forall x\, (P(x) \vee \neg P(x))$ is not intuitionistically provable.
- Doubly negating only the atomic formulas and keeping $\vee$. The condition that fails: $P \vee \neg P$ becomes $\neg \neg P \vee \neg \neg \neg P$, which is intuitionistically equivalent to $\neg \neg P \vee \neg P$, and this is not intuitionistically provable.

### Basic properties

- The [[Gödel-Gentzen translation theorem|WC4TDGEWZR]]: $\Gamma \vdash_c A$ if and only if $\Gamma^N \vdash_i A^N$. The same theorem gives $\mathsf{PA} \vdash A$ if and only if $\mathsf{HA} \vdash A^N$.
- Stability: $\vdash_i \neg \neg A^N \to A^N$ for every formula $A$. This is the main lemma of the [[proof|3WH3N4GY7W]].
- The formula $A^N$ has no $\vee$ and no $\exists$, and every atomic formula in it is doubly negated. Formulas of this shape are called negative.
- The three translations are intuitionistically equivalent: $\vdash_i A^K \leftrightarrow A^N$ and $\vdash_i A^N \leftrightarrow A^{Ku}$ for every formula $A$.
- Equiconsistency: $\bot^N = \bot$, so PA proves $\bot$ only if HA proves $\bot$. The converse holds because HA is a part of PA.
- The translation does not preserve existence: $(\exists x\, A)^N$ is $\neg \forall x\, \neg A^N$, and HA can prove this form without proving $\exists x\, A$.

### History

Kolmogorov gave his translation in 1925, and Glivenko proved his theorem for propositional logic in 1929.
Gödel and Gentzen found the translation $A^N$ independently in 1933, and used it to show that classical arithmetic is consistent relative to intuitionistic arithmetic.
Kuroda gave his translation in 1951.

### Common errors

- To think that $\mathsf{HA} \vdash A^N$ implies $\mathsf{HA} \vdash A$. For $A = \forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$ with Kleene's predicate $T$, HA proves $A^N$ but not $A$.
- To forget the double negation on atomic formulas in pure logic. In arithmetic it can be dropped, because HA proves $s = t \vee \neg s = t$, but in pure logic $\neg \neg P \to P$ is not provable.
- To translate $\exists x\, A$ as $\neg \neg \exists x\, A^N$ and then to drop the double negation. The result $\exists x\, A^N$ is not intuitionistically implied by the translation.

## Explanations

### L1 human

Intuitionistic logic accepts a statement only when it has a direct reason for it.
It does not accept "either it halts or it does not" without knowing which one holds.
But it does accept "it is impossible that neither holds".
A double-negation translation rewrites each classical claim in this careful form "a failure is impossible".
For example, "some number $n$ has property $P$" becomes "it is impossible that no number has property $P$".
Every classical proof then turns into an intuitionistic proof of the careful form.
So classical reasoning can never produce a contradiction unless intuitionistic reasoning also produces one.

### L2 human

We translate the sentence $A = \forall x\, \exists y\, (x < y)$ of arithmetic and look at what HA gets.

1. By the clause for $\exists$, $(\exists y\, (x < y))^N = \neg \forall y\, \neg (x < y)^N$.
2. In HA the atomic formula $x < y$ is decidable, so $(x < y)^N = \neg \neg (x < y)$ is equivalent to $x < y$.
3. By the clause for $\forall$, $A^N$ is equivalent in HA to $\forall x\, \neg \forall y\, \neg (x < y)$.
4. PA proves $A$, so the theorem gives $\mathsf{HA} \vdash A^N$.
5. Here HA also proves $A$ itself, with the witness $y = x + 1$, but the translation alone does not give this witness.

The typical use is to move a classical result into an intuitionistic setting: a proof of consistency, a realizability argument or a functional interpretation.
The [[Dialectica interpretation|HZ17ES9PDY]] of PA, for example, applies the translation first.
A trap is to apply a constructive tool directly to a classical proof without the translation; the tool then has to handle excluded middle, which it cannot do.

### L3 human

In a Heyting algebra the map $a \mapsto \neg \neg a$ is a nucleus, and its fixed points, the regular elements, form a Boolean algebra.
Glivenko's theorem is the logical form of this fact, and the negative translation is its extension to quantifiers.
In topos theory the same map gives the double-negation topology, whose sheaves form a Boolean topos.
In programming languages the negative translation corresponds to the continuation-passing-style transformation, with $\bot$ as the type of answers.
Replacing $\bot$ by an arbitrary formula gives [[Friedman's A-translation|6CCK0TT69P]], and composing the translation with the [[Dialectica interpretation|HZ17ES9PDY]] gives Gödel's interpretation of PA in [[system T|A4WR995XZP]].
