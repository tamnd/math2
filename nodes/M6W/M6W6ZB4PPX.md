---
tag: M6W6ZB4PPX
kind: concept
name: Dependent type
msc: [03B38, 68N15, 03F55]
uses: [Q48KGV33AH, A77FER1Q5H]
sources:
  - url: https://en.wikipedia.org/wiki/Dependent_type
same_as:
  wikidata: Q997433
  wikipedia: Dependent type
---

## Summary

A dependent type is a type that depends on a value.
An example is the type of lists of length exactly $n$, which changes with the number $n$.
Dependent types give two new type formers.
In a dependent function type $\Pi$, the result type depends on the argument.
In a dependent pair type $\Sigma$, the type of the second component depends on the first.
Under the [[Curry–Howard correspondence|A77FER1Q5H]], $\Pi$ types are universal statements and $\Sigma$ types are existential statements.
They are the basis of [[type theories|Q48KGV33AH]] used as foundations, and of proof assistants such as Agda, Coq and Lean.

## Explanations

### L1 human

In an ordinary language a function might take a number $n$ and return a list.
With dependent types its type can say more: it returns a list of length exactly $n$.
So the type of the output is not fixed in advance; it is computed from the input.
This lets types state precise properties, such as "this index is smaller than the length of the array", and the type checker then verifies them.
