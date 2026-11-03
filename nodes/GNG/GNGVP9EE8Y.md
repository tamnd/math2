---
tag: GNGVP9EE8Y
kind: concept
name: Merge sort
msc: [68P10, 68W40]
specializes: [MGKDQAM7K3, G9NFJ55KCX]
sources:
  - url: https://en.wikipedia.org/wiki/Merge_sort
same_as:
  wikidata: Q189057
  wikipedia: Merge sort
---

## Summary

Merge sort is a [[divide-and-conquer|G9NFJ55KCX]] [[sorting algorithm|MGKDQAM7K3]].
It splits the list into two halves, sorts each half recursively, and merges the two sorted halves into one sorted list.
It uses $O(n \log n)$ comparisons in the worst case, which is optimal for comparison sorts up to a constant factor, and it is stable.
Mathlib formalizes it as `List.mergeSort`.

## Explanations

### L1 human

Merging two sorted piles is easy: look at the top card of each pile and take the smaller, again and again.
Merge sort uses this trick recursively.
To sort $(5, 2, 4, 1)$, sort $(5, 2)$ into $(2, 5)$ and $(4, 1)$ into $(1, 4)$, then merge them into $(1, 2, 4, 5)$.
Since the list is halved at each level, there are about $\log_2 n$ levels, each costing about $n$ steps.
