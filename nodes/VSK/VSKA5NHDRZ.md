---
tag: VSKA5NHDRZ
kind: example
name: The phrase "the identity element of a group" is not ambiguous
msc: ["97E40", "20A05"]
topics: [WMY13MXY3W]
audience: ug1
not_instance_of:
  - target: 8BZPKYF912
    note: each group has exactly one identity element, so the article "the" picks out one object
uses: [8BZPKYF912, ACSC75R7R5, A5YGEC10HD, PD2R4XT79Q, 0F7FQS6XY6]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_element
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Definite_description
    locator: lead section
---

## Example

The article "the" in a phrase such as "the $x$ with property $P$" assumes that exactly one $x$ has $P$.
When this fails, the phrase is a case of [[ambiguity in mathematical language|8BZPKYF912]].
We show that "the identity element of a group $G$" is not such a case.

1. The phrase is a [[definite description|PD2R4XT79Q]]: "the element $e$ of $G$ with $eg = ge = g$ for all $g \in G$".
2. A definite description names one object exactly when one object fits it.
   So we need an [[existence and uniqueness statement|ACSC75R7R5]].
3. Existence: the group axioms give an identity element.
4. Uniqueness: if $e$ and $e'$ are identity elements, then $e = ee' = e'$, as in [[a group has exactly one identity element|A5YGEC10HD]].
5. So exactly one element fits, and "the identity element of $G$" names one object.
   The phrase is not ambiguous.

## Remarks

A contrast shows what can go wrong.
The phrase "the square root of $4$" fits two numbers, $2$ and $-2$, so on its own it does not name one number.
Mathematics removes the ambiguity by a convention: the [[square root|0F7FQS6XY6]] $\sqrt{a}$ is the non-negative root.
With that convention, "the square root of $4$" means $2$.

The phrase "the identity element" needs no convention, because its uniqueness is a theorem.
It does depend on the group.
The identity element of $\mathbb{Z}$ under addition is $0$, and the identity element of $\mathbb{Q} \setminus \{0\}$ under multiplication is $1$.
So the phrase is unambiguous once the group and its operation are fixed.

## Explanations

### L1 human

"The tallest child in the class" is clear when one child is the tallest.
If two children have the same height, the phrase does not say which one is meant.
For addition of numbers, "the number that changes nothing" is clear, because only $0$ does that.
So "the" is safe there.

### L2 human

Decide which of three phrases with "the" names one object.

1. "The empty set."
   Two sets with no elements have the same elements, so they are equal.
   One object fits, and the phrase is safe.
2. "The solution of $x^2 = 9$."
   Both $3$ and $-3$ are solutions.
   Two objects fit, and the phrase is ambiguous.
3. "The limit of $(1/n)$."
   A convergent sequence has exactly one limit, and here it is $0$.
   One object fits, and the phrase is safe.

Before you write "the", check that exactly one object fits.
Watch out: in step 1, uniqueness comes from the axiom of extensionality, and a student may not think of that axiom as a proof.
