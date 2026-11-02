---
tag: BFBNQ36QS8
kind: concept
name: Cartesian closed category
msc: [18D15]
sources:
  - url: https://en.wikipedia.org/wiki/Cartesian_closed_category
same_as:
  wikidata: Q1725874
  wikipedia: Cartesian closed category
---

## Summary

A Cartesian closed category is a [[category|A2DE66937D]] with finite [[products|S5744QZV4N]] in which every pair of objects has an [[exponential object|RHWD8DY41R]].
In it, morphisms $X \times Y \to Z$ match morphisms $X \to Z^Y$, as in currying of functions.
Sets, small categories, presheaf categories and every [[topos|6837RS7N82]] are Cartesian closed.
Cartesian closed categories are the models of the simply typed [[lambda calculus|BD756KR8FM]].

## Explanations

### L1 human

In the world of sets you can form pairs, and you can form the set of all functions between two sets.
A Cartesian closed category is any category where both of these constructions make sense and fit together as they do for sets.
The key rule is that a function of two inputs is the same as a function of one input that returns a function.
The category of all small categories is an example: the functors between two categories form a category again.
