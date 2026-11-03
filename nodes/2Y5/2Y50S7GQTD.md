---
tag: 2Y50S7GQTD
kind: concept
name: Randomized algorithm
msc: [68W20, 68Q87]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Randomized_algorithm
same_as:
  wikidata: Q583461
  wikipedia: Randomized algorithm
---

## Summary

A randomized algorithm is an [[algorithm|9DMSG5HAQX]] that may make random choices, such as coin flips, while it runs.
Its running time or its output is then a [[random variable|0PNRKMRC55]], and one studies its expected running time or its probability of error.
A Las Vegas algorithm always answers correctly but has a random running time.
A Monte Carlo algorithm has a bounded running time but may err with small probability.
Randomness often gives simpler or faster algorithms than the best known deterministic ones.
It leads to complexity classes such as [[BPP|PTD7E1PKV4]], [[RP|TPDMV6ZXN3]] and [[ZPP|QJZ5ZY0HJ8]].

## Explanations

### L1 human

Sometimes flipping coins helps to compute.
Randomized [[quicksort|Q9B393M2AV]] picks its pivot at random, and then on every input it sorts $n$ items with $O(n \log n)$ comparisons on average.
To test whether two polynomials are the same, one can plug in a random number and compare the values.
If the polynomials differ, they agree at only a few points, so a random point will almost surely expose the difference.
Repeating such a test several times makes the chance of error as small as one likes.
