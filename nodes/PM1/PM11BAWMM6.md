---
tag: PM11BAWMM6
kind: concept
name: Knuth–Morris–Pratt algorithm
msc: [68W32, 68R15, 68W40]
specializes: [TQ3YZDGCHM]
sources:
  - url: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
same_as:
  wikidata: Q45285
  wikipedia: Knuth–Morris–Pratt algorithm
---

## Summary

The Knuth–Morris–Pratt algorithm is a [[string-searching algorithm|TQ3YZDGCHM]] that runs in linear time.
It finds all occurrences of a pattern of length $m$ in a text of length $n$ in time $O(n + m)$.
It first computes, for each prefix of the pattern, the longest proper prefix that is also a suffix of it.
After a mismatch, this table tells how far the pattern can shift without missing an occurrence.
So the scan of the text never moves backwards.

## Explanations

### L1 human

When a partial match fails, the naive method throws away what it has learned and starts again one place to the right.
KMP remembers it: if the part already matched ends with a piece that is also the start of the pattern, the search can continue from there.
For the pattern "abab", after matching "aba" and then failing, the final "a" is already the start of a new possible match.
The table of such overlaps depends only on the pattern, so it is built once in advance.
With it, the text is scanned from left to right without ever moving backwards.
