---
tag: 72PG6XCQ7D
kind: concept
name: Ternary discriminator
msc: [08B05, 08A40]
sources:
  - book: isbn:9780387905785
---

## Summary

The ternary discriminator on a set $A$ is the operation $t(x, y, z)$ that returns $z$ when $x = y$ and returns $x$ otherwise.
It tests whether two elements are equal and chooses its output accordingly.
Algebras in which this operation is a term operation are called quasi-primal when they are finite.
Classes of algebras sharing a term for it generate [[discriminator varieties|MC9MX40Z7S]], which have a very clear structure theory.

## Explanations

### L1 human

The discriminator is an "if equal, then this, else that" operation.
It looks at its first two arguments: if they are the same, it outputs the third, and if they differ, it outputs the first.
On $\set{0, 1, 2}$, for example, $t(1, 1, 2) = 2$ and $t(1, 0, 2) = 1$.
Many logical and algebraic structures can express this test with their own operations, and this has strong consequences.
