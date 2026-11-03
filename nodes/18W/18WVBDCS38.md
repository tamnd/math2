---
tag: 18WVBDCS38
kind: concept
name: Regular language
msc: [68Q45]
specializes: [5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_language
same_as:
  wikidata: Q752532
  wikipedia: Regular language
---

## Summary

A regular language is a [[formal language|5MFZ4VNY6D]] that some [[deterministic finite automaton|W65B6BKZRY]] accepts.
By [[Kleene's theorem|JRB4QD04AN]], these are also the languages described by [[regular expressions|4DMYF2PR4Q]].
Regular languages form the lowest level of the [[Chomsky hierarchy|V7HSWG6R5F]] and have very good [[closure properties|446KZ8HJ5F]] and decision procedures.
They are recognized with a fixed amount of memory, whatever the length of the input.

## Explanations

### L1 human

A language is regular when a machine with finitely many states can decide, letter by letter, whether a word belongs to it.
The words with an even number of $a$'s form a regular language, since the machine only needs to remember a parity.
The words $a^n b^n$, with equally many $a$'s and $b$'s, do not form a regular language, since the machine would have to remember an unbounded count.
The [[pumping lemma|CBR9WAGZGZ]] and the [[Myhill–Nerode theorem|96BRMR4P3N]] are the usual tools to prove that a language is not regular.
