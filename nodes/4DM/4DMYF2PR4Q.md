---
tag: 4DMYF2PR4Q
kind: concept
name: Regular expression
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_expression
same_as:
  wikidata: Q185612
  wikipedia: Regular expression
---

## Summary

A regular expression is a finite formula that describes a [[formal language|5MFZ4VNY6D]], built from single letters with union, concatenation and the [[Kleene star|ZW1M7XG8V4]].
By [[Kleene's theorem|JRB4QD04AN]], the languages described in this way are exactly the [[regular languages|18WVBDCS38]].
Regular expressions give a compact text notation for patterns, and they are used in text editors, search tools and the lexical analysis of programming languages.
Practical pattern languages often add features, such as back-references, that go beyond regular languages.

## Explanations

### L1 human

A regular expression is a short pattern that matches a set of words.
The expression $a + b$ matches $a$ or $b$, the expression $ab$ matches $a$ followed by $b$, and $a^*$ matches any number of $a$'s, including none.
Combining these, $(a + b)^* a$ matches every word over $\set{a, b}$ that ends with $a$.
A finite pattern can thus describe an infinite set of words.
