---
tag: CNGSMAB60A
kind: definition
name: Category of posets
msc: [18B35, 06A06]
defines: ZBKVRMWHMW
uses: [A2DE66937D, 011C29Q1S1, 0WFF6AZPBP, 07HF9YCWPP]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_preordered_sets
---

## Definition

The *category of posets* $\mathbf{Pos}$ is the [[category|A2DE66937D]] given by the following data.

1. Its objects are the [[partially ordered sets|011C29Q1S1]].
2. A morphism from $(P, \le_P)$ to $(Q, \le_Q)$ is a [[monotone function|0WFF6AZPBP]] $f \colon P \to Q$, that is, $x \le_P y$ implies $f(x) \le_Q f(y)$.
3. Composition is the usual [[composition of functions|07HF9YCWPP]], and the identity morphism of $P$ is the identity map of $P$.

## Remarks

The data form a category.
The identity map is monotone, and if $f$ and $g$ are monotone, then $x \le y$ gives $f(x) \le f(y)$ and then $g(f(x)) \le g(f(y))$.
Associativity and the identity laws hold because they hold for functions.
Posets with order-reversing maps do not form a category in the same way: the composite of two order-reversing maps preserves order.
A morphism of $\mathbf{Pos}$ is an isomorphism exactly when it is an [[order isomorphism|0Y74KN99A5]].
A monotone bijection need not be one: the identity from a two-element antichain to a two-element chain is a monotone bijection whose inverse is not monotone.

## Explanations

### L1 human

The category of posets is the world of ordered sets together with the maps that respect order.
