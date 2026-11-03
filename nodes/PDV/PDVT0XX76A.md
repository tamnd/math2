---
tag: PDVT0XX76A
kind: concept
name: Needleman–Wunsch algorithm
msc: [92D20, 68W32, 90C39]
sources:
  - url: https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm
same_as:
  wikidata: Q583546
  wikipedia: Needleman–Wunsch algorithm
---

## Summary

The Needleman–Wunsch algorithm finds an optimal global [[sequence alignment|G42Y4TPD4N]] of two sequences.
It is a [[dynamic programming|R3FXF08WBH]] method.
Its table entry $(i, j)$ is the best score for aligning the first $i$ letters of one sequence with the first $j$ letters of the other.
For sequences of lengths $m$ and $n$ it runs in time proportional to $mn$, while the number of alignments grows exponentially.
It was one of the first applications of dynamic programming in biology.

## Explanations

### L1 human

An alignment of two words ends in one of three ways.
The last letters are paired, or the last letter of one word faces a gap, or the last letter of the other word faces a gap.
In each case, what remains is an alignment of shorter words.
So the best score for the full words comes from the best scores for slightly shorter words.
The algorithm fills a grid with these best scores, row by row, and then walks back through the grid to read off the best alignment.
