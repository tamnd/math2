---
tag: JCSAC9Y1CV
kind: concept
name: Idempotent semiring
msc: ["16Y60", "06F05"]
specializes: [D31S3GR51T]
sources:
  - url: https://en.wikipedia.org/wiki/Semiring
---

## Summary

An idempotent semiring, also called a dioid, is a [[semiring|D31S3GR51T]] in which $a + a = a$ for every element $a$.
In such a semiring the addition defines a natural partial order, with $a \le b$ when $a + b = b$, and addition becomes the join of this order.
The Boolean semiring, the tropical semirings and the semiring of formal languages are examples.
Idempotent semirings are the algebra of shortest paths, of tropical geometry and of [[Kleene algebras|BK4DDS24XC]].

## Explanations

### L1 human

In ordinary arithmetic, $1 + 1 = 2$.
In an idempotent semiring, adding something to itself changes nothing, like taking the larger of a number and itself.
A good example uses "maximum" as addition and ordinary addition as multiplication: the "sum" of $3$ and $3$ is $3$.
Because of this, the addition behaves like choosing the best of several options, which is why these semirings fit optimisation problems.
