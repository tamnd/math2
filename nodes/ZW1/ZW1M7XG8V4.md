---
tag: ZW1M7XG8V4
kind: concept
name: Kleene star
msc: [68Q45, 68R15]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene_star
same_as:
  wikidata: Q849775
  wikipedia: Kleene star
---

## Summary

The Kleene star $L^*$ of a [[formal language|5MFZ4VNY6D]] $L$ is the set of all concatenations of finitely many strings of $L$.
It includes the empty string, the concatenation of no strings.
Applied to an alphabet $\Sigma$, it gives the set $\Sigma^*$ of all [[strings|1P6EP01HZF]].
It is one of the three operations, with union and concatenation, that build the regular expressions.
It is the basic way to express repetition in formal languages.

## Explanations

### L1 human

The star means "repeat as many times as you like, possibly zero times".
If $L$ contains the strings $ab$ and $c$, then $L^*$ contains $\varepsilon$, $ab$, $c$, $abc$, $cab$, $abab$, and so on.
Each member is a sequence of blocks, and each block is taken from $L$.
Writing $a^*$ for the star of $\set{a}$ gives all strings of $a$s, including the empty one.
