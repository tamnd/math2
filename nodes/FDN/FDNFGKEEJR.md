---
tag: FDNFGKEEJR
kind: concept
name: Space complexity
msc: [68Q15, 68Q04]
sources:
  - url: https://en.wikipedia.org/wiki/Space_complexity
same_as:
  wikidata: Q2098905
  wikipedia: Space complexity
---

## Summary

The space complexity of an algorithm is the amount of memory it needs, as a function of the length of its input.
In the [[Turing machine|758EYCN27B]] model it counts the work-tape cells that the machine uses.
Space is, with [[time complexity|T00W8RQT8E]], one of the two main resources of complexity theory.
Bounds on space define classes such as L, NL and PSPACE.

## Explanations

### L1 human

Think of an algorithm as a person with a notebook who reads a long input on a separate sheet.
Space complexity asks how many pages of the notebook the person needs, in the worst case, for inputs of a given length.
The input sheet itself does not count, so an algorithm can use far less space than the length of its input.
For example, to check that a word has the form $0^k 1^k$, it is enough to count the $0$s and the $1$s in binary.
This needs only about $\log_2 n$ cells for an input of length $n$.
