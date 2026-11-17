---
tag: 9BA5AWWYD9
kind: example
name: The identity element of a group is unique
msc: ["00A35", "20A05"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [5P955TVSS2]
uses: [5P955TVSS2, G5S1M9, 07WYQPB8E3, 0D9NDGE9KP]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_element
    locator: Properties
---

## Example

Let $G$ be a [[group|G5S1M9]] with operation $\cdot$.
A group axiom says that there is an element $e$ with $eg = ge = g$ for each $g \in G$.
Books then speak of "the [[identity element|07WYQPB8E3]] of $G$" and write $e_G$ or $1$.
This [[definite description|5P955TVSS2]] is legal only after two proofs.

1. Existence. The group axioms state that at least one such element exists.
2. Uniqueness. Let $e$ and $e'$ both be identity elements.
3. Since $e'$ is an identity, $e e' = e$. Here $e'$ acts on the right of $e$.
4. Since $e$ is an identity, $e e' = e'$. Here $e$ acts on the left of $e'$.
5. So $e = e e' = e'$.
6. So $G$ has exactly one identity element, and the name "the identity" refers to one object.

## Remarks

1. The proof uses no associativity and no inverses. It works in each set with a binary operation, see [[uniqueness of identity and inverses|0D9NDGE9KP]].
2. The proof needs a two-sided identity. A left identity and a right identity are equal by the same argument, but two left identities need not be equal. In the operation $x \cdot y = y$ on a set with two elements, each element is a left identity.
3. In a [[group isomorphism|08MG7H8JW5]] $\varphi$, uniqueness gives $\varphi(e_G) = e_H$: the element $\varphi(e_G)$ acts as an identity on $\varphi(G) = H$.

## Explanations

### L1 human

In ordinary addition, $0$ does nothing: $5 + 0 = 5$.
A group always has an element that does nothing, like $0$ does for addition.
We may call it "the" element that does nothing, because there cannot be two of them.
If two elements both did nothing, combining them would give the first one and also the second one.
So they are the same element.

### L2 human

We use uniqueness to find the identity of a group of matrices.

1. Let $G$ be the set of invertible $2 \times 2$ real matrices, with matrix multiplication.
2. The identity matrix $I$ satisfies $AI = IA = A$ for each $A \in G$.
3. By uniqueness, $I$ is the identity of $G$, and no other matrix in $G$ is an identity.

The typical use: to find the identity, guess an element and check the defining equations.
Uniqueness then says that the guess is the identity.
A trap is to check only one equation, such as $AI = A$, in a structure where only a one-sided identity is known.
