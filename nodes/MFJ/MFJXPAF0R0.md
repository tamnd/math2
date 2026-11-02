---
tag: MFJXPAF0R0
kind: concept
name: Gödel numbering
msc: [03F40]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel_numbering
same_as:
  wikidata: Q1451046
  wikipedia: Gödel numbering
---

## Summary

A Gödel numbering assigns to each symbol, formula or proof of a formal language a natural number, its code, in an effective and injective way.
It lets statements about formulas and proofs become statements about numbers.
Gödel introduced it to prove his incompleteness theorems, where a theory of arithmetic talks about its own provability through codes.

## Explanations

### L1 human

Give each symbol a number, for example $1$ for "$0$", $2$ for "$=$", and so on.
A formula is a list of symbols, so it becomes a list of numbers.
A list of numbers can be packed into one number, for example as a product of prime powers.
Then "this formula is provable" becomes a property of a number, which arithmetic can talk about.
Any computer that stores text as bits does the same thing: each file is, in the end, one large number.
