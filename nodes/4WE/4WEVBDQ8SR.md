---
tag: 4WEVBDQ8SR
kind: concept
name: Approximation algorithm
msc: [68W25, 90C27, 68Q25]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_algorithm
same_as:
  wikidata: Q621751
  wikipedia: Approximation algorithm
---

## Summary

An approximation algorithm is an efficient [[algorithm|9DMSG5HAQX]] for an optimization problem.
It returns a solution whose cost is provably within a fixed factor of the optimum.
It is the main way to deal with [[NP-hard|MHA48AWBXN]] optimization problems, where an exact optimum is unlikely to be found in polynomial time.
The factor is the approximation ratio.
Results on [[hardness of approximation|X97H4RM1XR]] show that for many problems some ratios cannot be reached unless P equals NP.

## Explanations

### L1 human

Sometimes finding the very best answer is hopelessly slow, but a fairly good answer comes quickly.
An approximation algorithm gives a guarantee such as "my answer costs at most twice the best possible".
Suppose guards at crossroads must watch every road of a network, using as few guards as possible.
Pick any road with no guard at either end, put guards at both of its ends, and repeat.
Each road picked needs at least one guard in any solution, so this uses at most twice the minimum number of guards.
The guarantee holds for every input, not just on average.
