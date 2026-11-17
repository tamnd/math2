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

In [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]], the objects are sets, and the only primitive relation is membership $x \in y$.
Neither "set" nor "$\in$" has a definition.
We show how other notions are defined from these [[primitive notions|QMQEJKFEYZ]], and how the axioms give them their properties.

1. Subset is defined: $x \subseteq y$ means $\forall z\,(z \in x \Rightarrow z \in y)$, see [[subset|0BJR9QR08E]]. The definiens uses only $\in$ and logic.
2. Equality is governed by the [[axiom of extensionality|0TB16T2C97]]: if $x$ and $y$ have the same elements, then $x = y$.
3. Some set $x$ satisfies $\forall z\,(z \notin x)$. Some presentations take this as an axiom, and others derive it from the axioms of infinity and separation.
4. It is unique by extensionality: two sets with no elements have the same elements.
5. So "the [[empty set|0ECVK59Y03]]" is a legal definition, written $\varnothing$.
6. The natural numbers are then defined: $0 = \varnothing$, $1 = \{\varnothing\}$, $2 = \{\varnothing, \{\varnothing\}\}$, and so on.

## Remarks

1. The axioms never say what a set "is". They state which sets exist and when two sets are equal.
2. The naive description "a set is any collection of objects" leads to [[Russell's paradox|0HESMMSYEG]]. The axioms of ZF replace this description and allow only certain collections as sets.
3. Some set theories, such as von Neumann-Bernays-Gödel set theory, add "class" as a second primitive notion.
4. The step from $\in$ to the natural numbers shows that a single primitive relation can support most of mathematics.

## Explanations

### L1 human

Set theory starts with two ideas that it does not explain: a "set", and one thing being "in" a set.
It then gives rules, such as "two sets with the same members are the same set".
From these ideas and rules, mathematicians build numbers, functions and almost everything else.
Even the number $0$ is built as the set with nothing in it.

### L2 human

We prove from extensionality that $\{a, a\} = \{a\}$.

1. By definition, $z \in \{a, a\}$ exactly when $z = a$ or $z = a$, that is, exactly when $z = a$.
2. By definition, $z \in \{a\}$ exactly when $z = a$.
3. So the two sets have the same elements.
4. By the axiom of extensionality, $\{a, a\} = \{a\}$.

The typical use: to prove that two sets are equal, show that each element of one is an element of the other.
A trap is to argue from a picture of a set as a list, where $\{a, a\}$ would have two entries.
