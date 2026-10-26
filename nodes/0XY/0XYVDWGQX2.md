---
tag: 0XYVDWGQX2
kind: statement
role: proposition
name: De Morgan's laws in a Boolean algebra
msc: ["06E05"]
uses: [06GKBTAA5E]
sources:
  - url: https://en.wikipedia.org/wiki/De_Morgan's_laws
    locator: Boolean algebra
---

## Statement

Let $A$ be a [[Boolean algebra|06GKBTAA5E]].
Then $\neg(a \vee b) = \neg a \wedge \neg b$ and $\neg(a \wedge b) = \neg a \vee \neg b$ for all $a, b \in A$.

## Remarks

Proof idea: in a Boolean algebra each element has a unique complement. Check that $\neg a \wedge \neg b$ satisfies the two complement equations for $a \vee b$.
In the [[power set Boolean algebra|004J7ZEFAT]], the laws become $X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B)$ and its dual.
In the [[two-element Boolean algebra|0WG43AC0EV]], they are the laws of logic for not, and, and or.

## History

The laws are named after Augustus De Morgan. His book Formal Logic of 1847 states them.

## Explanations

### L1 human

The complement of an or is the and of the complements, and the complement of an and is the or of the complements.
Not (rain or snow) means no rain and no snow.
