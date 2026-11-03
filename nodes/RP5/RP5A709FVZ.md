---
tag: RP5A709FVZ
kind: concept
name: Bitonic sorter
msc: [68P10, 68Q06, 68W10]
specializes: [G854V12EC7]
sources:
  - url: https://en.wikipedia.org/wiki/Bitonic_sorter
same_as:
  wikidata: Q4918918
  wikipedia: Bitonic sorter
---

## Summary

A bitonic sorter is a [[sorting network|G854V12EC7]] for $n = 2^k$ inputs, due to Kenneth Batcher, built from networks that sort bitonic sequences.
A bitonic sequence first rises and then falls, up to a cyclic shift.
A single layer of comparators, the half-cleaner, splits a bitonic sequence into two bitonic halves.
Every entry of the first half is then at most every entry of the second.
The sorter has depth $k(k+1)/2$ and uses $n k (k+1)/4$ comparators, and its regular structure suits parallel hardware and GPUs.

## Explanations

### L1 human

Think of a sequence shaped like a hill: it goes up and then comes down.
Compare each entry of the first half with the entry in the same place in the second half, and swap so the smaller one is in front.
Now the small values are all in the front half and the large values in the back half, and each half is again a hill.
Repeating this on each half sorts the hill.
To sort an arbitrary list, sort the first half upwards and the second half downwards, which makes a hill, and then sort the hill.
For $4$ inputs this uses $6$ comparators in $3$ rounds.
