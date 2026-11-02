---
tag: BK4DDS24XC
kind: concept
name: Kleene algebra
msc: ["16Y60", "68Q70", "68Q45"]
specializes: [JCSAC9Y1CV]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene_algebra
same_as:
  wikidata: Q2634506
  wikipedia: Kleene algebra
---

## Summary

A Kleene algebra is an [[idempotent semiring|JCSAC9Y1CV]] with a star operation $a^*$ that behaves like "any number of repetitions of $a$".
The model is the algebra of formal languages, with union, concatenation and the Kleene star.
Kleene algebras give an equational theory of regular expressions, and they are used to reason about programs and automata.
Binary relations on a set, with union, composition and reflexive transitive closure, also form a Kleene algebra.

## Explanations

### L1 human

A regular expression such as $(ab)^*c$ describes strings: any number of copies of $ab$, followed by $c$.
Its building blocks are choice ($+$), sequencing (writing one thing after another) and repetition ($^*$).
A Kleene algebra keeps the laws that these three operations obey, such as $a^* = 1 + a a^*$, where $1$ is the empty string.
With these laws one can prove that two regular expressions describe the same strings without listing the strings.
