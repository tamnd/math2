---
tag: G6WP8B6NGD
kind: concept
name: Omega-regular language
msc: [68Q45, 03D05]
sources:
  - url: https://en.wikipedia.org/wiki/Omega-regular_language
same_as:
  wikidata: Q309558
  wikipedia: Omega-regular language
---

## Summary

An omega-regular language is a set of infinite words built from [[regular languages|18WVBDCS38]] of finite words by concatenation, infinite repetition and finite unions.
These languages are exactly the ones recognized by [[Büchi automata|92DM43HQZT]].
They play for infinite words the role that regular languages play for finite words, and they are closed under union, intersection and complement.
Omega-regular languages describe the behaviours of non-terminating systems, which is why they are central in verification.

## Explanations

### L1 human

Some systems, such as operating systems or traffic lights, are meant to run forever, so their behaviour is an infinite sequence of events.
An omega-regular language describes a set of such sequences with a finite pattern: first some finite prefix, then a block repeated forever.
For example, $(a + b)^* b^\omega$ describes the infinite words over $\set{a, b}$ that contain only finitely many $a$'s.
The infinite repetition $V^\omega$ plays the role that the Kleene star plays for finite words.
