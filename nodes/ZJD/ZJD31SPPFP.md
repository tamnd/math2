---
tag: ZJD31SPPFP
kind: concept
name: Quasigroup
msc: [20N05]
specializes: [9689SFPVE9]
sources:
  - url: https://en.wikipedia.org/wiki/Quasigroup
same_as:
  wikidata: Q1503423
  wikipedia: Quasigroup
---

## Summary

A quasigroup is a set with a [[binary operation|0M418FE7BB]] in which one can always divide on both sides.
For all $a, b$ the equations $a x = b$ and $y a = b$ have exactly one solution each.
The operation need not be associative and need not have an identity element.
A quasigroup with an identity element is a loop, and an associative quasigroup that is nonempty is a [[group|G5S1M9]].
The multiplication tables of finite quasigroups are exactly the [[Latin squares|CDVRMVED2V]].

## Explanations

### L1 human

Write the multiplication table of a finite quasigroup as a square grid.
Unique division says that each element appears exactly once in every row and exactly once in every column, as in a Sudoku row.
Associativity is not required, so the table can be quite irregular.
A simple infinite example is the integers with subtraction: $a - x = b$ and $y - a = b$ each have exactly one integer solution.
Subtraction is not associative and has no two-sided identity, so this quasigroup is not a group.
