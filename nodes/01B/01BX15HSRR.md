---
tag: 01BX15HSRR
kind: statement
role: theorem
name: Well-ordering principle
msc: [03F30]
uses: [0Y9H52BT03, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Relationship to the well-ordering principle
same_as:
  wikidata: Q2488476
  wikipedia: Well-ordering principle
---

## Statement

Every nonempty set of natural numbers has a least element.
That is, if $A \subseteq \mathbb{N}$ and $A \neq \emptyset$, then there is an $a$ in $A$ with $a \le x$ for each $x$ in $A$.

## Remarks

The least element is unique, because the [[order|0Y9H52BT03]] on $\mathbb{N}$ is antisymmetric.
The principle follows from [[strong induction|0KMVFSHFGZ]], and conversely it implies the [[principle of mathematical induction|0ASJVEFA9J]].
The set of the integers does not have this property: the set of negative integers has no least element.

## Explanations

### L1 human

If some natural numbers have a property, then there is a smallest one with that property.
For example, among the natural numbers that are larger than $10$ and even, the smallest is $12$.
Proofs often use this: they take the smallest counterexample and show that it cannot exist.
