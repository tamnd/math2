---
tag: W6KG32T7AJ
kind: concept
name: Edit distance
msc: [68W32, 68R15, 68P30]
sources:
  - url: https://en.wikipedia.org/wiki/Edit_distance
same_as:
  wikidata: Q5338467
  wikipedia: Edit distance
---

## Summary

The edit distance between two [[strings|1P6EP01HZF]] is the least number of elementary edits needed to turn one into the other.
In its most common form, the Levenshtein distance, the allowed edits are inserting, deleting or substituting one symbol.
It is a [[metric|0VKD1TP7F3]] on the set of strings, and it can be computed by [[dynamic programming|R3FXF08WBH]].
It is used in spelling correction and in comparing biological sequences.
Restricting the edits gives other distances, such as the [[Hamming distance|EP5HNGSXFA]], which allows only substitutions.

## Explanations

### L1 human

How far apart are the words "abc" and "acd"?
Delete the "b" to get "ac", then add a "d" at the end to get "acd": two edits.
One edit cannot do it, because the words differ in two places and have the same length.
So their edit distance is $2$.
Words with a small edit distance are likely typing mistakes of one another.
