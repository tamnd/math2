---
tag: RHWD8DY41R
kind: concept
name: Exponential object
msc: [18D15]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_object
same_as:
  wikidata: Q4391173
  wikipedia: Exponential object
---

## Summary

An exponential object $Z^Y$ in a category with [[products|S5744QZV4N]] is an object of morphisms from $Y$ to $Z$, together with an evaluation morphism.
It is defined by a [[universal property|EN4DD2FAJH]] that expresses currying: maps $X \times Y \to Z$ match maps $X \to Z^Y$.
Exponential objects are the defining feature of [[Cartesian closed categories|BFBNQ36QS8]].
They give the semantics of function types in [[lambda calculus|BD756KR8FM]].

## Explanations

### L1 human

A function of two variables $g(x, y)$ can be seen as a function of $x$ whose values are functions of $y$.
This trick is called currying.
For sets, the exponential $Z^Y$ is the set of all functions from $Y$ to $Z$.
For example, if $Y$ has $2$ elements and $Z$ has $3$, then $Z^Y$ has $3^2 = 9$ elements.
An exponential object is the same idea in any category with products.
