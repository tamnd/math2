---
tag: 53YA8BDBTQ
kind: concept
name: Gold code
msc: [94A55, 94A05, 11T71]
sources:
  - url: https://en.wikipedia.org/wiki/Gold_code
same_as:
  wikidata: Q2635984
  wikipedia: Gold code
---

## Summary

A Gold code is a family of $2^n + 1$ binary sequences of period $2^n - 1$, built by adding shifts of two suitably chosen [[maximum length sequences|H32KMWJ90G]].
Any two sequences of the family have small cross-correlation at every shift, taking only three values.
This lets many users share a channel at once, each with its own sequence, as in code-division multiple access and satellite navigation.
Robert Gold introduced these families in 1967.
See the [[definition|QPBYBTD3NF]].

## Explanations

### L1 human

When many transmitters share the same radio band, each can be given its own long pattern of $+1$s and $-1$s.
A receiver listening for one pattern multiplies the incoming signal by it and adds up; the other patterns should then nearly cancel out.
For this to work, any two patterns, even shifted against each other, must look very different.
Gold found a simple recipe: take two special m-sequences and add one to every shift of the other, bit by bit.
For period $7$ this gives $9$ sequences whose pairwise correlations are always $-1$, $-5$ or $3$.
