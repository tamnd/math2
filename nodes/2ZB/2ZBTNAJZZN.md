---
tag: 2ZBTNAJZZN
kind: example
name: Every square is a rectangle is not "for all x, x is a square and x is a rectangle"
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: WGZX7GV3PP
    note: the proposed formula uses a conjunction where the sentence needs an implication, so it has a different truth value
uses: [WGZX7GV3PP, 0GHS47PDAQ, 025YZN3VJW, 0NMG7W7Q11]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_form
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Example

Let the domain be the set of all quadrilaterals in the plane.
Let $S(x)$ be "$x$ is a square" and $R(x)$ be "$x$ is a rectangle".
Consider the proposed translation of "every square is a rectangle":
$$\Psi \;=\; \forall x \, \bigl( S(x) \land R(x) \bigr).$$
We show that $\Psi$ is not a correct translation, because its truth value differs from that of the sentence.

1. The sentence is true, because a square has four right angles, and a quadrilateral with four right angles is a rectangle.
2. Let $t$ be a trapezoid with exactly two parallel sides.
   Then $S(t)$ is false, so $S(t) \land R(t)$ is false by the truth table of [[conjunction|025YZN3VJW]].
3. One false instance makes a universal statement false, so $\Psi$ is false, with the counterexample $t$.
4. The sentence and $\Psi$ have different truth values, so $\Psi$ is not a translation of the sentence.
5. The correct translation is $\forall x \, (S(x) \to R(x))$.
   For the trapezoid $t$, the [[implication|0NMG7W7Q11]] $S(t) \to R(t)$ is true, because its antecedent is false, and for a square $x$, both $S(x)$ and $R(x)$ are true.

## Remarks

The formula $\Psi$ says "every quadrilateral is a square and a rectangle", which is a different and false claim.
The error comes from translating the word "is" in "a square is a rectangle" by $\land$.
The method of [[translating statements into logical form|WGZX7GV3PP]] pairs a universal quantifier with $\to$.
If the domain were the set of squares only, then $\Psi$ and the sentence would both be true, and the error would not show.
So a test of a translation should use a domain with objects that lack the first property.

## Explanations

### L1 human

"Every square is a rectangle" is a claim about squares only.
It does not say anything about triangles or other shapes.
"Everything is a square and a rectangle" is a claim about every shape.
A circle or a trapezoid makes the second claim false.
So the two sentences do not mean the same thing.

### L2 human

To check a translation of "every $A$ is $B$", test the formula on an object that is not an $A$.
For such an object the sentence makes no claim, so the formula must be true for it.
With $\land$, the instance $A(x) \land B(x)$ is false for this object, so the formula fails.
With $\to$, the instance $A(x) \to B(x)$ is true for this object, as required.
The same test catches "every prime greater than $2$ is odd" written as $\forall n \, (P(n) \land n > 2 \land O(n))$: the number $4$ makes it false.
Watch out: on objects that are $A$s and also $B$s, the formulas with $\land$ and with $\to$ agree, so testing only those objects proves nothing.
