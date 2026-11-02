---
tag: 28PE4GRFD7
kind: definition
name: Order type
msc: [06A05, "03E10"]
defines: FMFGTVVR4S
uses: [0316AYH1SC, 0Y74KN99A5]
sources:
  - url: https://en.wikipedia.org/wiki/Order_type
---

## Definition

Let $(A, \le_A)$ and $(B, \le_B)$ be [[totally ordered sets|0316AYH1SC]].
They have the same *order type* when there is an [[order isomorphism|0Y74KN99A5]] from $A$ onto $B$.
The *order type* of $(A, \le_A)$, written $\operatorname{type}(A)$, is the class of all totally ordered sets that have the same order type as $A$.

## Remarks

The sets $\N$ and $2\N = \set{0, 2, 4, \dots}$ with their usual orders have the same order type, $\omega$, by the isomorphism $n \mapsto 2n$.
The sets $\N$ and $\Z$ do not: $\N$ has a least element, $\Z$ has none, and an order isomorphism maps a least element to a least element.
Having the same order type is an equivalence relation on totally ordered sets.
Each well-ordered set is order isomorphic to a unique [[ordinal number|0RDJK7EQYY]], which is used to represent its order type.
Common notation: $\omega$ for $\N$, $\omega^*$ for the reverse of $\N$, $\zeta$ for $\Z$, $\eta$ for $\Q$ and $\lambda$ for $\R$.
The same definition makes sense for [[partially ordered sets|011C29Q1S1]].

## Explanations

### L1 human

Two ordered sets have the same order type when one can be relabelled into the other without changing the order.
The order type is the shape of the order.
