---
tag: 3AQ5GHTXA4
kind: concept
name: Hájek's basic logic BL
aliases: [basic-fuzzy-logic, bl-logic, hajek-basic-logic]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
uses: [VR6D8JXX1W, PT5PHKJDYM]
sources:
  - url: https://en.wikipedia.org/wiki/BL_(logic)
    locator: lead; Axioms; Semantics
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 5. Other notable fuzzy logics
  - url: https://en.wikipedia.org/wiki/T-norm_fuzzy_logics
    locator: Motivation; History
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: Propositional fuzzy logics
  - book: isbn:9780792352389
---

## Summary

Take $x = 0.7$ and $y = 0.4$, and compute $x * (x \Rightarrow y)$ for the three basic t-norms.
Łukasiewicz gives $0.7 \odot 0.7 = 0.4$, the product gives $0.7 \cdot \tfrac47 = 0.4$, and the minimum gives $\min(0.7, 0.4) = 0.4$.
All three return $\min(x, y)$, and this law, called divisibility, holds for every continuous [[t-norm|VR6D8JXX1W]].

*Basic fuzzy logic* BL is the propositional logic of all continuous t-norms.
A formula is provable in BL exactly when it takes value $1$ under every evaluation in $[0, 1]$, for every continuous t-norm and its residuum.
Hájek introduced BL in his 1998 monograph, with eight axiom schemes and modus ponens; see [[the definition|FQZ04D0HH3]].
BL is [[MTL|PT5PHKJDYM]] plus divisibility, and Łukasiewicz, Gödel and product logic each add one more axiom to BL.

## Motivation

Each continuous t-norm gives a logic, whose tautologies are the formulas with value $1$ under all evaluations.
These logics differ: $\neg \neg A \to A$ holds for Łukasiewicz and fails for the minimum.
BL collects the formulas that all of them share.

By the Mostert-Shields theorem of 1957, every continuous t-norm is an ordinal sum of Łukasiewicz and product copies, with the minimum outside the copies.
So BL is the common core of the three basic fuzzy logics and of every way of gluing them together.
It answers the question of what one can prove about a fuzzy "and" knowing only that it is continuous.

## Notation

The primitive connectives are strong conjunction $\otimes$, implication $\to$ and the constant $\bot$.
This sub-area writes $\odot$ for strong conjunction in the Łukasiewicz case, Wikipedia writes $\otimes$, and SEP writes $\&$.
Weak conjunction is defined by $A \land B := A \otimes (A \to B)$, and negation by $\neg A := A \to \bot$.
Weak disjunction is defined by $A \lor B := ((A \to B) \to B) \land ((B \to A) \to A)$.
In a standard algebra, $\land$ and $\lor$ become $\min$ and $\max$.

## Remarks

### Models of BL

The standard algebras of the three basic t-norms are BL-algebras, because each satisfies divisibility; see [[the divisibility example|E1M4RTRAVS]].
The [[ordinal sum of Łukasiewicz and product|Z6H5WJYJ4H]] is a continuous t-norm, so it gives one more standard BL-algebra, which is neither Łukasiewicz, Gödel nor product.
Every Boolean algebra is a BL-algebra, with $x \otimes y = x \land y$ and $x \to y = \neg x \lor y$.
The standard BL-algebras are fixed by their strong conjunction, which can be any continuous t-norm.

### What is not a model

The [[nilpotent minimum|ZJX7P6TVG9]] is left-continuous but not continuous, and it fails divisibility, so it gives an MTL-algebra that is not a BL-algebra.
The Heyting algebra of a branching Kripke frame fails prelinearity, as [[the fork|6S7TSV01WB]] shows, so it is not a model of BL.
The drastic t-norm gives no algebra at all, since it has no residuum; see [[the drastic non-example|VK2A62AQ0F]].

### What BL proves and what it does not

[[Prelinearity|D0ZADJFPQE]] holds for every left-continuous t-norm, so the axiom BL6 is valid in every standard BL-algebra.
The law of excluded middle $A \lor \neg A$ is not provable.
Check: in Gödel logic at $A = \tfrac12$, we get $\neg A = 0$ and $\max(\tfrac12, 0) = \tfrac12$.
The formula $A \to A \otimes A$ is not provable either.
Check: for the product at $A = \tfrac12$, we get $\tfrac12 \Rightarrow \tfrac14 = \tfrac14 / \tfrac12 = \tfrac12$.

### The three extensions

Łukasiewicz logic is BL plus double negation $\neg \neg A \to A$.
Gödel logic is BL plus idempotence $A \to A \otimes A$.
[[Product logic|YTHRDT9PDR]] is BL plus the axiom $\neg A \lor ((A \to A \otimes B) \to B)$.
Each extension is complete for its own standard algebra, so BL is strictly weaker than each of them.

### Completeness

BL is sound and complete for all BL-algebras and for all linearly ordered BL-algebras.
It is also complete for the standard BL-algebras on $[0, 1]$, a result called standard completeness.
Cignoli, Esteva, Godo and Torrens proved it in 2000.
So the semantic description in the Summary is a theorem, not a definition.

### Watch out

Do not read $\land$ as the strong conjunction.
In BL, $\land$ is the minimum and $\otimes$ is the t-norm, and they agree only in Gödel logic.
Do not take BL to be the logic of one t-norm either.
A formula valid for one t-norm, such as $\neg \neg A \to A$ for Łukasiewicz, need not be in BL, since it has value $\tfrac12$ at $A = \tfrac12$ in Gödel logic.

### History

Hájek introduced BL in his 1998 monograph *Metamathematics of Fuzzy Logic*, which also treated the three basic t-norm logics in propositional and first-order form.
Cintula in 2005 and Chvalovský in 2012 showed that two of the original axioms, BL2 and BL3, are derivable from the rest.
Cignoli, Esteva, Godo and Torrens proved standard completeness in 2000.
Esteva and Godo introduced the weaker logic MTL in 2001, by dropping divisibility.

### Try it

Compute $x * (x \Rightarrow y)$ at $x = 0.6$, $y = 0.3$ for the nilpotent minimum, where $x \Rightarrow y = \max(1 - x, y)$ when $x > y$.
You get $0.6 * 0.4$, and since $0.6 + 0.4 = 1$ is not above $1$, the value is $0$.
That is not $\min(0.6, 0.3) = 0.3$, so divisibility fails.

## Explanations

### L1 human

There are many ways to compute "and" on degrees of truth, and each way gives a fuzzy logic.
BL collects the laws that hold for every continuous way.
It is a common base, and each of the three main fuzzy logics adds one law to it.

### L2 human

To show that a formula is not provable in BL, find one continuous t-norm and one input where its value is below $1$.
For example, $\neg \neg A \to A$ at $A = \tfrac12$ for the minimum has value $1 \Rightarrow \tfrac12 = \tfrac12$.
To show that a formula is provable, derive it from the axioms, or check it for every continuous t-norm, which standard completeness allows.
Watch out: one failing t-norm refutes a formula, but to confirm it you must cover all continuous t-norms, including ordinal sums.

### L3 human

BL-algebras are the MTL-algebras that satisfy divisibility $x \land y = x \otimes (x \Rightarrow y)$.
They form a variety, and every BL-algebra is a subdirect product of BL-chains, by prelinearity.
Standard completeness reduces validity in all BL-chains to validity in the chains on $[0, 1]$ given by continuous t-norms.
The general algebraic setting is that of [[residuated lattices|E337A6WVH3]].
