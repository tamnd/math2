---
tag: G42Y4TPD4N
kind: concept
name: Sequence alignment
msc: [92D20, 68W32]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence_alignment
same_as:
  wikidata: Q827246
  wikipedia: Sequence alignment
---

## Summary

A sequence alignment arranges two or more [[strings|1P6EP01HZF]], such as DNA or protein sequences, in rows.
Gap symbols are inserted so that corresponding letters stand in the same column.
Columns with equal letters suggest positions that descend from a common ancestor, and gaps suggest insertions or deletions.
Alignments are scored, and finding an alignment of best score is the basic task of sequence comparison in bioinformatics.
Global alignment matches whole sequences, local alignment matches the most similar pieces.

## Explanations

### L1 human

Write two DNA words one above the other and slide letters around so that as many as possible line up.
Where a letter has no partner, put a dash in the other row.
For example, $ACGT$ and $AGT$ align as $ACGT$ over $A{-}GT$: three columns match, and one column says that $C$ was inserted in the first word or deleted from the second.
The fewer the mismatches and dashes, the more related the sequences look.
