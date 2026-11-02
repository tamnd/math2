---
tag: F02PJ2ZK9X
kind: concept
name: Sperner property
msc: [06A07, 05D05]
sources:
  - url: https://en.wikipedia.org/wiki/Sperner_property_of_a_partially_ordered_set
same_as:
  wikidata: Q7576398
  wikipedia: Sperner property of a partially ordered set
---

## Summary

A finite [[graded poset|1C7TKGTB2F]] has the Sperner property when no [[antichain|03HF498P1J]] is larger than its largest rank level.
Each rank level is an antichain, so the property says that the [[width|RA5SQ908G1]] of the poset equals the size of a largest level.
[[Sperner's theorem|0J87V9K1GE]] is the statement that the lattice of subsets of a finite set has this property.

## Explanations

### L1 human

Sort the elements of a graded poset into levels by rank.
Elements on one level are never comparable, so each level is an antichain.
The poset is Sperner when you cannot beat the biggest level by picking incomparable elements from several levels at once.
For the subsets of $\set{1, 2, 3, 4}$, the biggest level has the $6$ two-element subsets, and no family of $7$ subsets avoids all inclusions.
