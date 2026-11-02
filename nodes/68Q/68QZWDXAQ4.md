---
tag: 68QZWDXAQ4
kind: example
name: Skolem's paradox
msc: [03C62, "03E30", 03A05]
illustrates: [484M0TZ1S7]
uses: [0HE5WDQ9FJ, 01TQB88H4C, 0W7FBYS1F1, 0WTEMGYV2C, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem's_paradox
same_as:
  wikidata: Q1096353
  wikipedia: Skolem's paradox
---

## Example

Assume that [[ZFC|0HE5WDQ9FJ]], written in first-order logic, is consistent.
Its signature has one binary relation symbol $\in$, so it is countable.
By the [[Löwenheim–Skolem theorem|484M0TZ1S7]], ZFC has a [[countable|01TQB88H4C]] [[model|MVCH6N9SNW]] $M$.
By [[Cantor's theorem|0WTEMGYV2C]], ZFC proves that the power set of $\omega$ is [[uncountable|0W7FBYS1F1]].
So $M$ contains an element $p$ that $M$ believes is uncountable: no element of $M$ is a bijection between $\omega^M$ and $p$.
But $M$ is countable, so the set of elements of $p$ in $M$ is countable when seen from outside.
There is no contradiction.
A bijection between $\omega^M$ and the members of $p$ exists outside $M$, but it is not an element of $M$.

## Remarks

The example shows that "uncountable" is not an absolute notion: it depends on which functions the model contains.
The same reasoning shows that no countable first-order theory with an infinite model can pin down the size of its models.
Thoralf Skolem pointed out this situation in the 1920s.

## Explanations

### L1 human

Set theory proves that some sets are uncountable, yet it has a model with only countably many objects.
This sounds impossible, but it is not.
Inside the small model, the counting functions that would list an uncountable set are simply missing.
From outside, one can list the set, but the model cannot see this list.
