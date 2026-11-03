---
tag: MGKDQAM7K3
kind: concept
name: Sorting algorithm
msc: [68P10, 68W40]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Sorting_algorithm
same_as:
  wikidata: Q181593
  wikipedia: Sorting algorithm
---

## Summary

A sorting algorithm is an [[algorithm|9DMSG5HAQX]] that rearranges a finite list of elements of a [[totally ordered|0FRXBVVR03]] set into nondecreasing order.
Sorting is one of the most studied problems of computer science, because sorted data makes searching, merging and many other tasks fast.
Algorithms are compared by their number of comparisons, their memory use and whether they are stable.
Every comparison-based sorting algorithm needs about $n \log_2 n$ comparisons in the worst case, by the [[comparison sort lower bound|GJTE7GGJ7B]].

## Explanations

### L1 human

Sorting is putting things in order, like arranging cards in a hand from lowest to highest.
Given the list $(3, 1, 2)$, a sorting algorithm returns $(1, 2, 3)$.
Different methods do this differently: [[insertion sort|XA3JEEDC59]] inserts the cards one by one, while [[merge sort|GNGVP9EE8Y]] sorts two halves and then merges them.
