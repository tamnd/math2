---
tag: 6QXBY7J0M5
kind: definition
name: Axiom of regularity
msc: ["03E30"]
defines: NFQ9FVCP31
uses: [0HE5WDQ9FJ, 0SJ3RX9TXA, 0EZ758XE73, 0230ECX1Q5, 0ECVK59Y03]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_of_regularity
---

## Definition

Work in first-order logic with the relation symbol $\in$.
The *axiom of regularity*, or *axiom of foundation*, is the axiom
$$\forall x\, \bigl( x \ne \emptyset \to \exists y\, ( y \in x \wedge y \cap x = \emptyset ) \bigr).$$
In words: every nonempty [[set|0SJ3RX9TXA]] $x$ has an [[element|0EZ758XE73]] $y$ such that no element of $y$ is an element of $x$.

## Remarks

Example: let $x = \set{\emptyset, \set{\emptyset}}$.
The element $y = \emptyset$ satisfies $y \cap x = \emptyset$, because the [[empty set|0ECVK59Y03]] has no elements.
Non-example: a set $a$ with $a = \set{a}$ would violate the axiom.
The only element of $x = \set{a}$ is $a$, and $a \cap x = x \cap x = x \ne \emptyset$.
So in [[ZF|0HE5WDQ9FJ]], no set is an element of itself.
The axiom says that $\in$ is a [[well-founded relation|0230ECX1Q5]] on every set.
Over the other axioms of ZF, it is equivalent to the statement that every set lies in some level $V_\alpha$ of the cumulative hierarchy.
With the axiom of dependent choice, it is equivalent to the statement that there is no sequence $(x_n)$ with $x_{n+1} \in x_n$ for all $n$.
In Mathlib, the statement for ZFC sets is `ZFSet.regularity`.
