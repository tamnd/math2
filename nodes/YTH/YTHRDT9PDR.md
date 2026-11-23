---
tag: YTHRDT9PDR
kind: concept
name: Product fuzzy logic
aliases: [product-fuzzy-logic, product-logic]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
uses: [VR6D8JXX1W, 3AQ5GHTXA4]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms; 5. Other notable fuzzy logics; 6. Predicate logics
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: Propositional fuzzy logics
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Prominent examples; Properties of continuous t-norms
  - book: isbn:9780792352389
---

## Summary

Multiply $0.5$ by $0.7$ to get $0.35$, then divide $0.35$ by $0.5$ to get $0.7$ back.
In product logic, conjunction is multiplication and implication undoes it by division, so nothing is lost when the first factor is positive.

*Product fuzzy logic* $\Pi$ is the logic of the product [[t-norm|VR6D8JXX1W]] $x \cdot y$ and its residuum on $[0, 1]$.
It is [[BL|3AQ5GHTXA4]] plus one cancellation axiom; see [[the definition|DS5YPGT8GA]].
Its algebraic models are the product algebras.
With Łukasiewicz and Gödel logic, it is one of the three basic t-norm logics of Hájek's 1998 monograph.

## Motivation

The product is the third basic continuous t-norm, beside the minimum and the Łukasiewicz t-norm.
Every strict t-norm, that is, every continuous t-norm that is strictly increasing on $(0, 1]^2$, is isomorphic to the product.
So product logic is the logic of each strict t-norm.
In the Mostert-Shields decomposition of 1957, product copies are one of the two kinds of building block, beside Łukasiewicz copies.

## Notation

Strong conjunction is $\otimes$, read as $x \cdot y$, and SEP writes $\&$.
The residuum is $x \Rightarrow_\Pi y = 1$ if $x \le y$, and $y / x$ otherwise.
Negation is $\neg x = x \Rightarrow_\Pi 0$, which is $1$ at $x = 0$ and $0$ elsewhere.

## Remarks

### Computing in product logic

The residuum at $0.7$ and $0.4$ is $0.4 / 0.7 = \tfrac47$, as [[the values example|TGD3MEZCNH]] computes.
Divisibility holds, since $0.7 \cdot \tfrac47 = 0.4 = \min(0.7, 0.4)$; see [[the divisibility example|E1M4RTRAVS]].
[[The cancellation example|B6G1P9DBF9]] checks the defining axiom at explicit values and in general.
The two-element Boolean algebra is a product algebra, since $\{ 0, 1 \}$ is closed under the product and its residuum.

### What fails in product logic

The contraction $p \to p \otimes p$ fails.
Check: at $p = \tfrac12$ it has value $\tfrac14 / \tfrac12 = \tfrac12$.
Product and Gödel logic have the same negation, so $\neg \neg p \to p$ has value $1 \Rightarrow p = p < 1$ at every $p \in (0, 1)$ in both.
The Łukasiewicz and Gödel algebras refute cancellation, as [[the non-example|VVXQ399T3V]] shows, so they are not product algebras.
The [[nilpotent minimum|ZJX7P6TVG9]] gives no BL-algebra, so it gives no product algebra either.

### The three basic logics compared

The three basic logics are pairwise incomparable.
Gödel logic proves $p \to p \otimes p$, Łukasiewicz logic proves $\neg \neg p \to p$, and product logic proves cancellation.
Each of these is refuted in the other two logics, so none of the three contains another.

### Product and Łukasiewicz

The Łukasiewicz t-norm is isomorphic to the product cut at $c$, the operation $\max(c, x y)$ on $[c, 1]$, for any $c \in (0, 1)$.
The map $x \mapsto c^{1 - x}$ does it, since $c^{1 - x} c^{1 - y} = c^{1 - (x + y - 1)}$, and the cut at $c$ matches the cut at $0$.
So the two Archimedean building blocks are close relatives: one is the product with a floor, the other without.

### Watch out

Product logic does not have an involutive negation, since its negation takes only the values $0$ and $1$.
Do not read $\Rightarrow_\Pi$ as $y / x$ for all inputs either.
For $x \le y$ the value is $1$, and $y / x$ is not even defined at $x = 0$.

### History

Hájek's 1998 monograph presented the logics of the three basic continuous t-norms, Łukasiewicz, Gödel and product, in propositional and first-order form.
The monograph axiomatized product logic over BL, and the single cancellation axiom used here is an equivalent form, the one given in SEP.

## Explanations

### L1 human

Product logic reads "and" as multiplication of degrees of truth.
So "$p$ and $p$" is less true than $p$, unless $p$ is $0$ or $1$.
"Not $p$" is fully true only when $p$ is fully false.

### L2 human

To compute a value, multiply for $\otimes$, divide for $\to$ when the antecedent is larger, and take $\min$ and $\max$ for $\land$ and $\lor$.
In the standard algebra, the cancellation axiom says that if $x > 0$, then $x \Rightarrow_\Pi (x \cdot y) = y$.
That is, multiplication by $x$ followed by division by $x$ gives $y$ back.
Watch out: the rule fails at $x = 0$, and the disjunct $\neg \varphi$ covers that case.

### L3 human

Product algebras are the BL-algebras that satisfy the cancellation axiom.
The standard product algebra is the negative cone $(0, 1]$ of the ordered group $(\mathbb{R}_{> 0}, \cdot)$, with a new bottom $0$ added.
The general setting is that of [[residuated lattices|E337A6WVH3]].
