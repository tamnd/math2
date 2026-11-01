---
tag: ZGNBR2SPZ0
kind: concept
name: Markov chain Monte Carlo
msc: [65C05, 60J22, 65C40]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo
same_as:
  wikidata: Q1191869
  wikipedia: Markov chain Monte Carlo
---

## Summary

Markov chain Monte Carlo (MCMC) is a family of methods to sample from a probability distribution $\pi$.
They run a [[Markov chain|0G48PYM96Q]] whose [[stationary distribution|0KRH5157WP]] is $\pi$.
Averages of a function along the path of the chain then estimate the expectation of that function under $\pi$.
MCMC works even when $\pi$ is known only up to a normalising constant, which makes it a basic tool of Bayesian statistics and statistical physics.
The [[Metropolis–Hastings algorithm|MKHF449E22]] and the Gibbs sampler are the main examples.

## Explanations

### L1 human

Some distributions are too complicated to sample from directly, for example the law of all configurations of a large magnet.
MCMC instead designs a random walk on the configurations that, in the long run, visits each one with the right frequency.
One lets the walk run, records what it sees, and averages.
The price is that successive samples are dependent, so more of them are needed than with independent draws.
