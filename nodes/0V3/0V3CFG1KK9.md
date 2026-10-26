---
tag: 0V3CFG1KK9
kind: definition
name: Semigroup
msc: [20M10]
defines: 0XMEM406JM
uses: [0580ZJSA3Q, 0NNQ4KFEX7]
sources:
  - url: https://en.wikipedia.org/wiki/Semigroup
    locator: Definition
---

## Definition

A semigroup is a pair $(S, \ast)$, where $S$ is a set and $\ast$ is a [[binary operation|0M418FE7BB]] on $S$ that is [[associative|0K8F7PVDMX]].
Thus $(a \ast b) \ast c = a \ast (b \ast c)$ for all $a, b, c \in S$.

## Remarks

The positive integers with addition form a semigroup that has no identity element.
Each [[monoid|0N6R902FG1]] and each [[group|G5S1M9]] is a semigroup.
Some authors allow the empty set as a semigroup, and others do not.

## Explanations

### L1 human

A semigroup is the simplest structure with an associative operation.
You can combine elements and the grouping does not matter, but maybe nothing acts as "do nothing" and no step can be undone.
An example is the set of nonempty words over an alphabet, with the operation that writes one word after the other.
