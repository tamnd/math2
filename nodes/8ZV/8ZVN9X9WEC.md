---
tag: 8ZVN9X9WEC
kind: concept
name: Decision tree model
msc: [68Q17, 68Q25, 68Q04]
specializes: [YFHEG4GYHW]
sources:
  - url: https://en.wikipedia.org/wiki/Decision_tree_model
same_as:
  wikidata: Q5249246
  wikipedia: Decision tree model
---

## Summary

The decision tree model measures the cost of a computation by the number of queries it makes to the input, and ignores all other work.
An algorithm is a [[rooted tree|0Y0JGC2K9T]].
Each inner node asks one question about the input, the answer chooses the branch, and each leaf gives the output.
The cost is the depth of the tree, the number of questions in the worst case.
The model gives simple lower bounds, such as the bound $\log_2(n!)$ on the number of comparisons needed to sort $n$ items.

## Explanations

### L1 human

Think of the game of twenty questions.
Each question has a yes or no answer, and the next question may depend on the earlier answers.
A decision tree writes down the whole strategy as a branching diagram.
For example, to compute the OR of two bits, first ask for the first bit; if it is $1$, answer $1$, otherwise answer with the second bit.
The worst case uses two questions, and one cannot do better.
