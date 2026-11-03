---
tag: 2C5QGNNCAE
kind: concept
name: Operad
msc: [18M60, 18M65]
sources:
  - url: https://en.wikipedia.org/wiki/Operad
same_as:
  wikidata: Q842072
  wikipedia: Operad
---

## Summary

An operad is a collection of abstract operations $P(n)$ with $n$ inputs and one output, for each $n \ge 0$.
It comes with a rule to plug operations into the inputs of other operations, an identity operation, and symmetric group actions that permute the inputs.
Operads encode types of algebraic structure: associative, commutative and Lie algebras each correspond to an operad.
An [[algebra over an operad|ES9YATDWA3]] is a structure of that type.
They were introduced in algebraic topology to describe loop spaces, with examples such as the [[little cubes operad|FWT0003QS1]] and [[E-infinity operads|T78YG90VVT]].
They also organize questions about nonassociative algebras, such as the duality between [[Lie|5JJYBJ6A8K]] and commutative algebras or between [[Leibniz|FGM1ZM3KKN]] and [[Zinbiel algebras|QQKRCAKD5V]].

## Explanations

### L1 human

Think of all the functions $X^n \to X$ on a fixed set $X$, for every number $n$ of arguments.
You can plug functions into the arguments of another function and get a new function, and you can permute the arguments.
An operad keeps only this plugging and permuting structure and forgets the set $X$.
For example, the operad of associative algebras has, in arity $n$, the $n!$ ways of multiplying $n$ letters in some order, like $x_2 x_1 x_3$.
