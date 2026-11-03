---
tag: TQ3YZDGCHM
kind: concept
name: String-searching algorithm
msc: [68W32, 68R15, 68W40]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/String-searching_algorithm
same_as:
  wikidata: Q374040
  wikipedia: String-searching algorithm
---

## Summary

A string-searching algorithm, or string-matching algorithm, finds the places where a short [[string|1P6EP01HZF]], the pattern, occurs inside a longer string, the text.
The obvious method compares the pattern at every position and needs time $O(nm)$ for a text of length $n$ and a pattern of length $m$.
Cleverer methods, such as the [[Knuth–Morris–Pratt algorithm|PM11BAWMM6]], reach time $O(n + m)$ by reusing what earlier comparisons revealed.
These algorithms underlie text editors, search tools and the analysis of DNA sequences.

## Explanations

### L1 human

Searching for a word in a document is string searching.
The simplest way is to lay the word against the text at the first letter, compare letter by letter, then slide one place to the right and repeat.
In the text "abracadabra", the pattern "abra" occurs at positions $1$ and $8$.
Good algorithms avoid re-reading letters of the text again and again, so long texts can be searched quickly.
