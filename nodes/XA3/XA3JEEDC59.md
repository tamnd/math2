---
tag: XA3JEEDC59
kind: concept
name: Insertion sort
msc: [68P10, 68W40]
specializes: [MGKDQAM7K3]
sources:
  - url: https://en.wikipedia.org/wiki/Insertion_sort
same_as:
  wikidata: Q117241
  wikipedia: Insertion sort
---

## Summary

Insertion sort is a simple [[sorting algorithm|MGKDQAM7K3]] that builds the sorted list one element at a time.
It inserts each new element into its place among the elements already sorted.
It uses $\Theta(n^2)$ comparisons in the worst case but only $n - 1$ on a sorted list.
So it is fast on short or nearly sorted lists.
It is stable and needs only a constant amount of extra memory.
Mathlib formalizes it as `List.insertionSort`.

## Explanations

### L1 human

This is how many people sort a hand of cards: pick up the cards one by one and slide each into the right spot in the hand.
To sort $(3, 1, 2)$: start with $(3)$; insert $1$ to get $(1, 3)$; insert $2$ between them to get $(1, 2, 3)$.
Each insertion may have to move past all the cards already held, which is why the worst case is slow.
