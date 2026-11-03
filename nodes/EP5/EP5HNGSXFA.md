---
tag: EP5HNGSXFA
kind: concept
name: Hamming distance
msc: [94B05, 68R15, 68P30]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_distance
same_as:
  wikidata: Q272172
  wikipedia: Hamming distance
---

## Summary

The Hamming distance between two [[strings|1P6EP01HZF]] of the same length is the number of positions at which they differ.
It is a [[metric|0VKD1TP7F3]] on the set of strings of a given length.
It is the basic distance of coding theory.
How many errors a code can detect and correct depends on how far apart its codewords are in this distance.
It is also the graph distance in the hypercube graph on $\set{0, 1}^n$.

## Explanations

### L1 human

Write two words of the same length one above the other and count the columns where the letters differ.
For $10110$ and $11100$ the second and fourth columns differ, so the Hamming distance is $2$.
It counts how many single symbol errors turn one word into the other.
If any two allowed codewords differ in at least $3$ places, then one error can always be corrected, since the damaged word is still closest to the original.
