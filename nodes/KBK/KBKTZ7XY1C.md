---
tag: KBKTZ7XY1C
kind: concept
name: Weighted automaton
msc: [68Q45, 16Y60]
sources:
  - url: https://en.wikipedia.org/wiki/Weighted_automaton
same_as:
  wikidata: Q109535851
  wikipedia: Weighted automaton
---

## Summary

A weighted automaton is a finite automaton whose transitions carry weights taken from a [[semiring|D31S3GR51T]].
Instead of accepting or rejecting a word, it assigns the word a weight.
This weight is the sum, over all runs on the word, of the product of the weights along the run.
So it computes a formal power series in noncommuting variables, a function from words to the semiring.
Over the Boolean semiring it is just a [[nondeterministic finite automaton|SFMYM96C1B]]; other semirings give counting, probabilities or costs.

## Explanations

### L1 human

Give every arrow of an automaton a number.
A path through the automaton has a value, the product of its numbers, and a word gets the sum of the values of all its accepting paths.
With weights $1$ in the natural numbers, the weight of a word is the number of accepting paths it has.
With costs in the tropical semiring, where "sum" means minimum and "product" means ordinary addition, the weight of a word is the cost of its cheapest path.
