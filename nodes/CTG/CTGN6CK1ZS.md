---
tag: CTGN6CK1ZS
kind: concept
name: Detailed balance
msc: [60J10, 82C05]
sources:
  - url: https://en.wikipedia.org/wiki/Detailed_balance
same_as:
  wikidata: Q1201087
  wikipedia: Detailed balance
---

## Summary

Detailed balance is a property of a distribution $\pi$ and a [[Markov chain|0G48PYM96Q]].
It says that, in equilibrium, the probability flow from each state $i$ to each state $j$ equals the flow from $j$ back to $i$.
Detailed balance implies that $\pi$ is a [[stationary distribution|0KRH5157WP]], and a chain with such a $\pi$ is called reversible.
It is the usual design principle of Markov chain Monte Carlo algorithms.

## Explanations

### L1 human

Picture many walkers spread over the states according to $\pi$, all moving at once by the rules of the chain.
Stationarity only asks that the total number in each state stay the same.
Detailed balance asks more: for every pair of states, as many walkers go from $i$ to $j$ as from $j$ to $i$.
A film of the chain in equilibrium then looks the same when played backwards.
A random walk on a graph that moves to a uniformly chosen neighbour has this property, with $\pi$ proportional to the degrees.
