---
tag: K83HS1C5WG
kind: concept
name: Star-free language
msc: [68Q45, 68Q70]
specializes: [18WVBDCS38]
sources:
  - url: https://en.wikipedia.org/wiki/Star-free_language
same_as:
  wikidata: Q3217203
  wikipedia: Star-free language
---

## Summary

A star-free language is a [[regular language|18WVBDCS38]] that can be built from finite languages by union, complement and concatenation, without the [[Kleene star|ZW1M7XG8V4]].
Complement makes this class larger than it first looks: some languages usually written with a star, such as $(ab)^*$, are star-free.
By [[Schützenberger's theorem|YSXPVN8G0D]], a regular language is star-free exactly when its [[syntactic monoid|D47RMDH8MJ]] is aperiodic.
Star-free languages are also exactly the languages definable in first-order logic over words, a result of McNaughton and Papert.

## Explanations

### L1 human

Star-free languages describe patterns that need no counting modulo a number.
They can say "the word contains $aa$" or "every $a$ is followed by $b$", but they cannot say "the length is even".
For example, $\Sigma^*$ is star-free because it is the complement of the empty set, and so the words containing $aa$ form the star-free language $\Sigma^* aa \Sigma^*$.
The language $(aa)^*$ of words of even length over $\set{a}$ is regular but not star-free.
