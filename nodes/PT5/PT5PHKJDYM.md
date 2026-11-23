---
tag: PT5PHKJDYM
kind: concept
name: Monoidal t-norm based logic
aliases: [mtl, monoidal-t-norm-logic]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
uses: [VR6D8JXX1W]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: "2. MTL: A fundamental fuzzy logic; 7. Algebraic semantics"
  - url: https://en.wikipedia.org/wiki/Monoidal_t-norm_logic
    locator: lead; Axioms; Semantics
  - url: https://en.wikipedia.org/wiki/T-norm_fuzzy_logics
    locator: History
---

## Summary

The nilpotent minimum is the t-norm that returns $\min(x, y)$ when $x + y > 1$ and $0$ otherwise.
It gives $0.4 * 0.6 = 0$, since $0.4 + 0.6$ is not above $1$, but $0.4 * 0.61 = 0.4$.
It jumps, so it is not continuous, yet it is left-continuous and has a residuum.

*Monoidal t-norm based logic* MTL is the propositional logic of all left-continuous [[t-norms|VR6D8JXX1W]], the nilpotent minimum among them.
A formula is provable in MTL exactly when it has value $1$ under every evaluation, for every left-continuous t-norm and its residuum.
Esteva and Godo introduced MTL in 2001, with a Hilbert calculus and modus ponens; see [[the definition|TGQ8T276MG]].
[[BL|3AQ5GHTXA4]] is MTL plus divisibility.

## Motivation

A t-norm has a residuum exactly when it is left-continuous, by [[the left-continuity statement|D1R4D2HEPP]].
So left-continuous t-norms are the widest class for which the residuated semantics of fuzzy logic works.
BL covers only the continuous ones, and it leaves out t-norms such as the nilpotent minimum.
MTL is the logic of the whole class, so it is the weakest logic whose conjunction is a t-norm and whose implication is its residuum.

## Notation

SEP writes strong conjunction as $\&$, Wikipedia writes $\otimes$, and this sub-area writes $\odot$ for the Łukasiewicz case.
In MTL the weak conjunction $\land$ is a primitive connective, because without divisibility it is not definable from $\otimes$ and $\to$.
The standard MTL-algebra of a left-continuous t-norm $*$ is written $[0, 1]_*$.

## Remarks

### Models of MTL

The [[nilpotent minimum|ZJX7P6TVG9]] gives a standard MTL-algebra that is not a BL-algebra.
The [[three basic t-norms|E1M4RTRAVS]] give standard BL-algebras, and every BL-algebra is an MTL-algebra.
Every Boolean algebra and every linearly ordered Heyting algebra is an MTL-algebra, with $\otimes = \land$.
[[Prelinearity|D0ZADJFPQE]] is valid for every left-continuous t-norm, so the axiom MTL6 is sound for the standard semantics.

### What is not a model

The [[drastic t-norm|VK2A62AQ0F]] has no residuum, so it gives no MTL-algebra.
A Heyting algebra that refutes prelinearity is not an MTL-algebra, and [[the fork|6S7TSV01WB]] gives one.

### Weak and strong conjunction

The formula $A \otimes B \to A \land B$ is valid, and its converse is not.
Check: with the product at $A = B = \tfrac12$, the converse is $\tfrac12 \Rightarrow \tfrac14 = \tfrac12$.
In BL one may define $A \land B$ as $A \otimes (A \to B)$, but in MTL this fails.
For the nilpotent minimum at $A = 0.4$, $B = 0.3$ the definition gives $0.4 * 0.6 = 0$, not $0.3$.

### Completeness

MTL is complete for all MTL-algebras and for all MTL-chains, since every MTL-algebra is a subdirect product of chains.
It is also strongly complete for the standard semantics: $\Gamma \models_{\mathrm{MTL}} \varphi$ iff $\Gamma \vdash_{\mathrm{MTL}} \varphi$, for every set $\Gamma$ of premises.
Jenei and Montagna proved standard completeness of MTL in 2002, starting from completeness for MTL-chains.
The validity problem of MTL is decidable.

### Extensions

BL, Łukasiewicz, Gödel and product logic are all axiomatic extensions of MTL.
The logic of the nilpotent minimum is another, and it is not an extension of BL.

### Watch out

Do not call MTL the logic of all t-norms, since only left-continuous t-norms have the residuum that interprets $\to$.
Do not assume that each MTL-algebra is a chain either.
The product $[0, 1]_* \times [0, 1]_*$ is an MTL-algebra, and $(1, 0)$ and $(0, 1)$ are incomparable in it.

### History

Esteva and Godo introduced MTL and MTL-algebras in 2001, as a weakening of Hájek's BL of 1998.
Jenei and Montagna proved standard completeness in 2002.
Cintula in 2005 and Chvalovský in 2012 showed that the axioms MTL2 and MTL3 are derivable from the rest.

## Explanations

### L1 human

MTL is the most general of the main fuzzy logics.
It allows every "and" on degrees of truth that has a matching "if then".
Its laws hold in each of these fuzzy logics.

### L2 human

To refute a formula in MTL, find one left-continuous t-norm and one evaluation where its value is below $1$.
The nilpotent minimum is a good first test, since it is not continuous.
Watch out: $\land$ and $\otimes$ are different connectives, and $\land$ must be read as $\min$, not as the t-norm.

### L3 human

MTL-algebras are the prelinear, commutative, bounded, integral [[residuated lattices|E337A6WVH3]].
They form a variety, and the subdirect decomposition into chains gives completeness for chains.
Standard completeness reduces validity in all MTL-chains to validity in the chains $[0, 1]_*$.
Běhounek and Cintula took completeness with respect to chains as the basis of a general definition of fuzzy logic.
