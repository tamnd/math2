---
tag: HVF403PQ4H
kind: concept
name: Initial algebra semantics
msc: [08A70, 68Q55, 08B20]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_algebra
---

## Summary

Initial algebra semantics gives meaning to syntax through the universal property of an initial algebra.
The terms of a signature form the [[term algebra|3YYKGWJJND]], which is an [[initial algebra|R76EC56V9R]]: it has exactly one [[homomorphism|KBXSZC6BV1]] to every algebra of the signature.
Choosing a semantic algebra then fixes the meaning of every term, and the meaning is compositional because the map is a homomorphism.
The same idea, with equations added, gives the standard meaning of an algebraic specification and of an [[abstract data type|86144NHH59]].

## Explanations

### L1 human

A program or a formula is built from small pieces by fixed rules.
To give it a meaning, it is enough to say what each basic symbol means and how each rule combines meanings.
The meaning of the whole then follows by working up from the pieces, and there is only one way to do it.
For example, the term $s(s(0)) + s(0)$ in the symbols $0$, $s$, $+$ gets the value $3$ once $0$ means zero, $s$ means "add one" and $+$ means addition.
Initial algebra semantics is the precise form of this recipe.
