---
tag: Y2BSHY2D6M
kind: example
name: Set and membership as primitive notions of ZF
msc: ["00A35", "03E30"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [QMQEJKFEYZ]
uses: [QMQEJKFEYZ, 0HE5WDQ9FJ, 0TB16T2C97, 0ECVK59Y03, 0BJR9QR08E, 0HESMMSYEG]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_notion
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
    locator: lead section
---

## Example

In [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] the objects are sets, and the only primitive relation is membership, $x \in y$.
Neither "set" nor "$\in$" has a definition, so both are [[primitive notions|QMQEJKFEYZ]].
We follow a few definitions down to them, and we see how the axioms give the defined notions their properties.

1. [[Subset|0BJR9QR08E]] is defined from membership:
   $$x \subseteq y \quad \text{means} \quad \forall z \, (z \in x \Rightarrow z \in y).$$
   The definiens uses only $\in$ and logic.
2. Equality of sets is governed by the [[axiom of extensionality|0TB16T2C97]]: if $x$ and $y$ have the same elements, then $x = y$.
3. Some set $x$ satisfies $\forall z \, (z \notin x)$.
   Some presentations take this as an axiom, and others derive it from the existence of some set and the axiom schema of separation.
4. Such a set is unique, by extensionality: two sets with no elements have the same elements.
5. So "the [[empty set|0ECVK59Y03]]", written $\varnothing$, is a legal definition by definite description.
6. The natural numbers are then defined, in von Neumann's way, as
   $$0 = \varnothing, \qquad 1 = \{\varnothing\}, \qquad 2 = \{\varnothing, \{\varnothing\}\},$$
   and in general $n + 1 = n \cup \{n\}$.

## Remarks

The axioms never say what a set is.
They say which sets exist and when two sets are equal, and that is all a proof may use.

The naive description "a set is any collection of objects" leads to [[Russell's paradox|0HESMMSYEG]]: the collection of all sets that are not elements of themselves would be an element of itself exactly when it is not.
The axioms of ZF replace that description, and they allow only certain collections to be sets.
Other set theories choose more primitive notions.
Von Neumann-Bernays-Gödel set theory, for example, adds "class" as a second kind of object.

The step from $\in$ to the natural numbers shows how far one primitive relation can carry a theory.
Integers, rationals, real numbers, functions and spaces are all defined sets in ZF.

## Explanations

### L1 human

Set theory starts with two ideas that it does not explain: a "set", and one thing being "in" a set.
It then gives rules, such as "two sets with the same members are the same set".
From these ideas and rules, mathematicians build numbers, functions and almost everything else.
Even the number $0$ is built, as the set with nothing in it.

### L2 human

We prove from extensionality that $\{a, a\} = \{a\}$.
By the meaning of the brace notation, $z \in \{a, a\}$ holds exactly when $z = a$ or $z = a$, which is exactly when $z = a$.
In the same way, $z \in \{a\}$ holds exactly when $z = a$.
So the two sets have the same elements, and the axiom of extensionality gives $\{a, a\} = \{a\}$.
The typical use of extensionality is this: to prove that two sets are equal, show that every element of each one is an element of the other.
Watch out: a picture of a set as a list would give $\{a, a\}$ two entries, but a set has no order and no repeated members.
