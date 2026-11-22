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
A group axiom says that some element $e$ satisfies $e g = g e = g$ for every $g \in G$.
Books then speak of "the [[identity element|07WYQPB8E3]] of $G$" and write $e_G$ or $1$.
This [[definite description|5P955TVSS2]] is legal only after two proofs.

1. Existence.
   The group axioms state that at least one identity element exists.
2. Uniqueness.
   Let $e$ and $e'$ both be identity elements of $G$.
3. Use that $e'$ is an identity, with $g = e$ on its left:
   $$e e' = e.$$
4. Use that $e$ is an identity, with $g = e'$ on its right:
   $$e e' = e'.$$
5. The two lines have the same left side, so $e = e e' = e'$.
6. So $G$ has exactly one identity element, and "the identity" names one object.

Check with $(\mathbb{Z}, +)$: if $e + n = n$ for every integer $n$, then $n = 0$ gives $e + 0 = 0$, so $e = 0$.

## Remarks

The proof uses neither associativity nor inverses.
It works in every set with a binary operation, as [[uniqueness of identity and inverses|0D9NDGE9KP]] records.

The proof needs both sides, though.
Step 3 uses $e'$ as a right identity and step 4 uses $e$ as a left identity, so a left identity and a right identity are always equal.
Two left identities need not be equal.
On the set $\{p, q\}$, define $x \cdot y = y$.
Then $p \cdot y = y$ and $q \cdot y = y$ for every $y$, so both $p$ and $q$ are left identities, and "the left identity" would name nothing definite.
This operation has no right identity, since $y \cdot r = r$ differs from $y$ whenever $y \ne r$.

Uniqueness also has consequences.
If $\varphi \colon G \to H$ is a [[group isomorphism|08MG7H8JW5]], then $\varphi(e_G)$ acts as an identity on every element $\varphi(g)$ of $H$, so $\varphi(e_G) = e_H$ by uniqueness.

## Explanations

### L1 human

In ordinary addition, $0$ does nothing: $5 + 0 = 5$.
Every group has an element that does nothing, as $0$ does for addition.
We may call it "the" element that does nothing, because there cannot be two of them.
If two elements both did nothing, combining them would give the first one and also the second one.
So they are the same element.

### L2 human

Uniqueness turns the search for an identity into a check.
Let $G$ be the group of invertible $2 \times 2$ real matrices under multiplication, and guess the identity matrix $I$.
For every $A \in G$ we compute
$$A I = I A = A,$$
so $I$ is an identity element.
By uniqueness, $I$ is the identity of $G$, and no other matrix in $G$ has this property.

The typical use is exactly this: guess an element, check the defining equations, and let uniqueness finish.
Watch out: you must check both equations $A I = A$ and $I A = A$.
The example $x \cdot y = y$ above shows that one side alone does not force uniqueness.
