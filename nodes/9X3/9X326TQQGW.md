---
tag: 9X326TQQGW
kind: example
name: For the operation a ∗ b = b, each element is a left identity and no element is an identity
msc: [08A02, 20M10]
topics: [BAZT8JJ70S]
audience: school
not_instance_of:
  - target: 07WYQPB8E3
    note: each element is a left identity, but for a ≠ e, a ∗ e = e ≠ a, so no element is a right identity
uses: [0M418FE7BB, 0K8F7PVDMX]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_element
    locator: Properties
---

## Example

Let $S$ be a set with at least two elements, and define $a \ast b = b$ for all $a, b \in S$.
So the result is always the right input.
This is a [[binary operation|0M418FE7BB]] on $S$, because $b \in S$.

1. Each element is a left identity. Let $e \in S$. For each $a \in S$, $e \ast a = a$ by the definition.
2. No element is a right identity. Let $e \in S$. Since $S$ has at least two elements, there is an element $a \in S$ with $a \neq e$. Then $a \ast e = e \neq a$.
3. An [[identity element|07WYQPB8E3]] must be a right identity, so by step 2, $\ast$ has no identity element.
4. The operation is [[associative|0K8F7PVDMX]]: $(a \ast b) \ast c = c$ and $a \ast (b \ast c) = b \ast c = c$.

For $S = \{x, y\}$, the [[Cayley table|0YB2NRP0T5]] has the rows $x \ast x = x$, $x \ast y = y$ and $y \ast x = x$, $y \ast y = y$.
Both rows are the same as the header row, so both $x$ and $y$ are left identities.
No column is the same as the header column, so there is no right identity.

## Remarks

The example shows that a left identity need not be unique.
This does not contradict the uniqueness of the identity element: by the rule $e = e \ast f = f$, two left identities are equal only when one of them is also a right identity.
By step 4, $(S, \ast)$ is a [[semigroup|0XMEM406JM]], called a right zero semigroup, and it is not a [[monoid|0N6R902FG1]].
If $S$ has only one element $s$, then $s \ast s = s$, and $s$ is an identity element.
The mirror operation $a \ast b = a$ has each element as a right identity and no left identity.

## Explanations

### L1 human

The rule says: forget the left input and give the right input.
So any element on the left does nothing, and each element acts as a left identity.
But an element on the right does not do nothing: it replaces the left input.
So there is no element that does nothing on both sides.

### L2 human

To show that an element is not a right identity, find one element $a$ with $a \ast e \neq a$.
Here any $a \neq e$ works, and this needs at least two elements in $S$.
The typical use of this non-example is to show why the definition of an identity asks for both sides, and why the uniqueness proof uses one left identity and one right identity.
A trap is to read the Cayley table by rows only: each row equal to the header shows only a left identity.
