---
tag: YRRS4BWA6Z
kind: concept
name: DeGroot learning
msc: [91D30, 91D15, 60J20]
sources:
  - url: https://en.wikipedia.org/wiki/DeGroot_learning
same_as:
  wikidata: Q5243912
  wikipedia: DeGroot learning
---

## Summary

DeGroot learning is a model of opinion formation in a group.
Each member repeatedly replaces their opinion by a weighted average of the opinions of the people they listen to.
Morris DeGroot proposed it in 1974 as a model of reaching a consensus.
The weights form a stochastic matrix, so the dynamics is linear and is governed by the same theory as a [[Markov chain|0G48PYM96Q]].
Under mild conditions on the network the opinions converge to a consensus, which is a weighted average of the initial opinions.

## Explanations

### L1 human

Three friends each guess the temperature tomorrow.
Every evening each of them listens to the others and moves their guess to an average of what they heard, with more weight on the people they trust.
After many evenings the guesses agree.
The final common guess is a mix of the first guesses, and the people who are trusted most have the biggest say in it.
