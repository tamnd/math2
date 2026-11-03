---
tag: T00W8RQT8E
kind: concept
name: Time complexity
msc: [68Q25, 68Q15, 68W40]
sources:
  - url: https://en.wikipedia.org/wiki/Time_complexity
same_as:
  wikidata: Q2393193
  wikipedia: Time complexity
---

## Summary

The time complexity of an algorithm is the number of elementary steps it takes, as a function of the length of its input.
Usually one takes the worst case over all inputs of a given length.
It is stated up to constant factors with [[big O notation|0TGV80E6A4]], such as $O(n)$, $O(n \log n)$ or $O(2^n)$.
The time complexity of a problem is that of the fastest algorithm solving it, and it defines classes such as $\mathrm{DTIME}(f(n))$ and [[P|GVT2NKN37K]].
Time is the main resource studied in computational complexity theory.

## Explanations

### L1 human

Time complexity says how the running time of a program grows when the input gets larger.
Counting exact seconds depends on the computer, so one counts basic steps and ignores constant factors.
Looking through a list of $n$ items one by one takes about $n$ steps, written $O(n)$.
Comparing every pair of items takes about $n^2$ steps, which becomes much slower for large $n$.
