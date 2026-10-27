---
tag: 0ASJVEFA9J
kind: concept
name: Mathematical induction
aliases: [principle-of-mathematical-induction, proof-by-induction]
msc: [03F30]
topics: [G9JFJGY4TQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
same_as:
  wikidata: Q178377
  wikipedia: Mathematical induction
---

## Summary

Mathematical induction is a method to prove that a property $P(n)$ holds for every [[natural number|0MWKJ44V5A]] $n$.
A proof by induction has two steps.
The base case proves $P(0)$.
The induction step proves, for an arbitrary natural number $n$, that $P(n)$ implies $P(n + 1)$.
Then $P(n)$ holds for every natural number $n$.

## Remarks

The method is valid because of the induction axiom of the [[Peano axioms|0QFT7Z76N5]].
In the induction step, the assumption $P(n)$ is the induction hypothesis.
Common variants are [[induction from an arbitrary base case|0GF6AJEBZ0]] and [[strong induction|0KMVFSHFGZ]].

## Explanations

### L1 human

Think of a line of dominoes that never ends.
If the first domino falls, and each falling domino knocks over the next one, then every domino falls.
The base case is the first domino, and the induction step is the rule that each domino knocks over the next one.
