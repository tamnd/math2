---
tag: 8TV1YW8EXC
kind: concept
name: Markov chain mixing time
msc: [60J10, 60J22]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_chain_mixing_time
same_as:
  wikidata: Q6771322
  wikipedia: Markov chain mixing time
---

## Summary

The mixing time of a finite [[Markov chain|0G48PYM96Q]] is the number of steps it needs to come close to its [[stationary distribution|0KRH5157WP]].
This must hold whatever the starting state.
Closeness is measured in total variation distance, usually with threshold $1/4$.
Mixing times measure the cost of Markov chain Monte Carlo and of card shuffling.
Their study is a large part of modern Markov chain theory.

## Explanations

### L1 human

Shuffle a deck of cards again and again: how many shuffles until the order is close to random?
The mixing time answers this kind of question for any chain.
It is the first time at which, from the worst starting state, no event has a probability more than $1/4$ away from its probability under the equilibrium law.
For a chain that jumps to a uniformly random state at each step, one step is enough, so the mixing time is $1$.
