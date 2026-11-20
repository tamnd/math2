---
tag: DS5YPGT8GA
kind: definition
name: Product fuzzy logic
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
defines: YTHRDT9PDR
uses: [FQZ04D0HH3, BHGCVPAJW0, 7R2JBNNMT5]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms; 5. Other notable fuzzy logics
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: Propositional fuzzy logics
  - book: isbn:9780792352389
---

## Definition

*Product fuzzy logic* $\Pi$ is the Hilbert calculus in the language of [[BL|FQZ04D0HH3]] whose axioms are those of BL and the cancellation axiom
$$\neg \varphi \lor ((\varphi \to \varphi \otimes \psi) \to \psi),$$
with modus ponens as the only rule.

A *product algebra* is a BL-algebra in which the cancellation axiom is valid.

The *standard product algebra* $[0, 1]_\Pi$ is the standard BL-algebra of the product [[t-norm|BHGCVPAJW0]] $x \cdot y$.
Its operations are $\min$, $\max$, $x \cdot y$, the residuum, $0$ and $1$, where by [[the residua statement|7R2JBNNMT5]]:
$$x \Rightarrow_\Pi y = \begin{cases} 1 & x \le y, \\ y / x & x > y. \end{cases}$$
The negation is $\neg x = x \Rightarrow_\Pi 0$, equal to $1$ if $x = 0$ and to $0$ if $x > 0$.

## Notation

SEP writes the cancellation axiom with $\&$ for $\otimes$.
The letter $\Pi$ names both the logic and the t-norm; $[0, 1]_\Pi$ is the standard algebra.

## Remarks

1. SEP states that this calculus axiomatizes the logic of the product t-norm.
2. Wikipedia describes product logic as BL plus an axiom for cancellativity of conjunction, with product algebras as models.
3. In $[0, 1]_\Pi$ the axiom has value $1$: for $x = 0$ the disjunct $\neg x$ is $1$, and for $x > 0$ the second disjunct is $1$; see [[the example|B6G1P9DBF9]].
4. The weak connectives are $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$, by divisibility and the BL definition of $\lor$.

## Explanations

### L1 human

Product logic is BL with one extra axiom.
The axiom says: unless $\varphi$ is fully false, conjunction with $\varphi$ loses no information about $\psi$.

### L2 human

To evaluate a formula, read $\otimes$ as multiplication and $\to$ as the residuum above.
Check cases on whether the antecedent is at most the consequent.
A trap: $\neg$ is not $1 - x$ here; it sends every positive value to $0$.

### L3 human

Product algebras are a subvariety of BL-algebras, defined by one extra identity.
SEP's statement in remark 1 is a standard completeness theorem: the theorems of $\Pi$ are the formulas valid in $[0, 1]_\Pi$.
