---
tag: W0VD6EAHDA
kind: definition
name: Nonassociative ring
msc: [17A01]
defines: YP5TQ6WFVN
uses: [071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Non-associative_algebra
---

## Definition

A *nonassociative ring* is an [[abelian group|071DDFVG4J]] $(A, +)$ with a binary operation $A \times A \to A$, $(a, b) \mapsto ab$, such that
$$a(b + c) = ab + ac \quad \text{and} \quad (a + b)c = ac + bc$$
for all $a, b, c \in A$.
No associativity and no unit element are required.

## Remarks

The two distributive laws say that the multiplication is biadditive.
An associative ring is a nonassociative ring whose product is associative; the word "nonassociative" means "not necessarily associative".
Some authors, and the Lean library Mathlib (`NonAssocRing`), also require a two-sided unit element.
Example: $\R^3$ with the cross product $\times$.
The product is bilinear, hence biadditive, but $(e_1 \times e_1) \times e_2 = 0 \ne -e_2 = e_1 \times (e_1 \times e_2)$, so it is not associative.
Non-example: $\Z$ with the product $a * b = a - b$.
Distributivity fails: $1 * (1 + 1) = -1$, while $1 * 1 + 1 * 1 = 0$.
