---
tag: RY3XCJEN2F
kind: concept
name: Smith–Waterman algorithm
msc: [92D20, 68W32, 90C39]
sources:
  - url: https://en.wikipedia.org/wiki/Smith–Waterman_algorithm
same_as:
  wikidata: Q1683352
  wikipedia: Smith–Waterman algorithm
---

## Summary

The Smith–Waterman algorithm finds an optimal local [[sequence alignment|G42Y4TPD4N]] of two sequences: the pair of substrings that align with the highest score.
It is a [[dynamic programming|R3FXF08WBH]] method like the [[Needleman–Wunsch algorithm|PDVT0XX76A]], with one change: a table entry is never allowed to fall below zero.
It is used to find similar regions, such as a shared protein domain, inside sequences that are otherwise unrelated.

## Explanations

### L1 human

Two long proteins may share one short similar piece and be unrelated elsewhere.
Aligning them end to end would bury that piece among bad matches.
Smith–Waterman fills the same kind of score grid as global alignment, but whenever a running score turns negative it starts over from zero.
The highest number in the grid marks the end of the best matching pair of pieces, and walking back until a zero gives the pieces themselves.
