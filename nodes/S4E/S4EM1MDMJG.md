---
tag: S4EM1MDMJG
kind: example
name: Partial orders form a universal Horn class
aliases: [partial-orders-universal-horn-class]
msc: ["03C52", "06A06"]
topics: [JYJHB4YBAH]
audience: grad
instance_of: [9A4CYWXPEA]
uses: [9A4CYWXPEA, 0QV2JS9RJ3, F4WRD396PB, 676H7EGTKJ]
sources:
  - book: isbn:9780521587136
---

## Example

Let $L = \set{\le}$ with $\le$ binary.
The class of [[partial orders|0QV2JS9RJ3]] is a [[universal Horn class|9A4CYWXPEA]], axiomatized by three strict universal Horn sentences:

$$\forall x \, (x \le x), \qquad \forall x \forall y \, (x \le y \wedge y \le x \rightarrow x = y), \qquad \forall x \forall y \forall z \, (x \le y \wedge y \le z \rightarrow x \le z).$$

We check the closure properties by hand.

1. A subset of a partial order with the restricted relation satisfies the three axioms, since each axiom speaks only about the elements it quantifies over. So the class is closed under [[substructures|676H7EGTKJ]].
2. Let $(P_i, \le_i)_{i \in I}$ be partial orders and $F$ a filter on $I$. In the [[reduced product|F4WRD396PB]], $[a] \le [b]$ holds when $\set{i : a(i) \le_i b(i)} \in F$.
3. Reflexivity: $\set{i : a(i) \le_i a(i)} = I \in F$.
4. Antisymmetry: if $[a] \le [b]$ and $[b] \le [a]$, then $\set{i : a(i) = b(i)}$ contains the intersection of two sets in $F$, so it lies in $F$ and $[a] = [b]$.
5. Transitivity: the set where $a(i) \le_i c(i)$ contains the intersection of the sets where $a(i) \le_i b(i)$ and $b(i) \le_i c(i)$.
6. The one-element order satisfies all three axioms, as part 3 of [[the characterization|VCJX55N45K]] predicts for strict axioms.

## Remarks

With $F = \set{I}$, the reduced product is the direct product with the coordinatewise order.
The class is not closed under surjective homomorphic images.
Map the disjoint union of the chains $a < b$ and $c < d$ onto $\set{x, y}$ by $a, d \mapsto x$ and $b, c \mapsto y$, and give the target the image relation.
Then $x \le y$ and $y \le x$ with $x \ne y$, so antisymmetry fails.
By [[Lyndon's theorem|8DJSRWME2X]], partial orders are therefore not axiomatized by positive sentences; antisymmetry, with $x = y$ as a conclusion, cannot be avoided.
Preorders, without antisymmetry, also form a universal Horn class.

## Explanations

### L1 human

A partial order ranks some things above others, like "is a divisor of" on whole numbers.
Its rules say: everything is below itself, two things below each other are equal, and "below" chains together.
Each rule says "if these hold, then that holds", so it survives when one compares many orders side by side, coordinate by coordinate.

### L2 human

We order pairs of whole numbers by divisibility in each coordinate and check one instance.

1. $(2, 3) \le (4, 9)$, since $2 \mid 4$ and $3 \mid 9$.
2. $(4, 9) \le (8, 9)$, since $4 \mid 8$ and $9 \mid 9$.
3. By transitivity, $(2, 3) \le (8, 9)$, and indeed $2 \mid 8$ and $3 \mid 9$.
4. The pairs $(2, 3)$ and $(3, 2)$ are incomparable, so the product is not total even when both factors are.

The method shows that any class defined by "if, then" rules among atomic facts is closed under products.
A trap is to use divisibility on all integers, where $2 \mid -2$ and $-2 \mid 2$ with $2 \ne -2$; that relation is a preorder, not a partial order.
