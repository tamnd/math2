---
tag: A5YGEC10HD
kind: example
name: A group has exactly one identity element
msc: ["97E40", "20A05"]
topics: [WMY13MXY3W]
audience: ug1
instance_of: [ACSC75R7R5]
uses: [ACSC75R7R5, G5S1M9, 07WYQPB8E3, GDBV09GFYB]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_element
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Example

Let $G$ be a [[group|G5S1M9]] with its operation written as a product.
An [[identity element|07WYQPB8E3]] of $G$ is an element $e$ with $eg = g$ and $ge = g$ for every $g \in G$.
We prove the [[existence and uniqueness statement|ACSC75R7R5]] "$G$ has exactly one identity element", in its two parts.

1. Existence: the group axioms state that $G$ has an identity element.
   So there is at least one.
2. Uniqueness: let $e$ and $e'$ be identity elements of $G$.
   We show $e = e'$.
3. Since $e'$ is an identity, $e e' = e$, by the rule $g e' = g$ with $g = e$.
4. Since $e$ is an identity, $e e' = e'$, by the rule $e g = g$ with $g = e'$.
5. Steps 3 and 4 give $e = e e' = e'$.
   So any two identity elements are equal.
6. Steps 1 and 5 together give exactly one identity element.
   This is the theorem on the [[uniqueness of the identity element|GDBV09GFYB]].

## Remarks

Uniqueness justifies the phrase "the identity of $G$" and the symbol $e$ or $1$ for it.
The existence part comes from the axioms, so all the work is in uniqueness.

The uniqueness proof uses neither associativity nor inverses.
So it works in any set with a binary operation, a magma, and a magma has at most one two-sided identity.
A magma may have no identity at all.
The positive integers under addition have none, because $e + 1 = 1$ forces $e = 0$, which is not positive.
So in this wider setting the statement is only "at most one", and existence must come from somewhere else.

One-sided identities behave differently.
On a set with at least two elements, the operation $x \cdot y = y$ makes every element a left identity, so left identities need not be unique.
The proof above uses a left identity and a right identity, and it shows that the two coincide.

## Explanations

### L1 human

In ordinary addition, the number $0$ changes nothing: $5 + 0 = 5$ and $0 + 7 = 7$.
Suppose a number $z$ also changes nothing when it is added to any number.
Adding $z$ to $0$ changes nothing, so $0 + z = 0$.
Adding $0$ to $z$ changes nothing, so $0 + z = z$.
So $z = 0$, and $0$ is the only number with this property.

### L2 human

Use the same two-part pattern to show that each element $g$ of a group has exactly one inverse.

1. Existence: the group axioms give an element $h$ with $gh = e$ and $hg = e$.
2. Uniqueness: let $h$ and $h'$ both be inverses of $g$.
3. Then $h = he = h(gh') = (hg)h' = eh' = h'$, by associativity in the middle step.
4. So any two inverses are equal, and the inverse $g^{-1}$ is unique.

The pattern justifies a notation such as $g^{-1}$ or $e$ for "the" object.
Watch out: here uniqueness needs associativity, unlike the identity.
Without associativity, an element can have two different inverses.
