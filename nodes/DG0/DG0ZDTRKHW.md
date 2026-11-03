---
tag: DG0ZDTRKHW
kind: concept
name: Reed–Frost model
msc: [92D30, 60J10]
specializes: [AKP63KCK02]
sources:
  - url: https://en.wikipedia.org/wiki/Reed%E2%80%93Frost_model
same_as:
  wikidata: Q7306784
  wikipedia: Reed–Frost model
---

## Summary

The Reed–Frost model is a stochastic epidemic model in discrete time, also called a chain binomial model.
Infection passes in generations: each infectious host can infect each susceptible host independently with a fixed probability, and then is removed.
It was developed by Lowell Reed and Wade Hampton Frost in the 1920s.
It is the simplest model in which chance decides whether an outbreak takes off.

## Explanations

### L1 human

Think of a small household where one person catches a cold.
During one week, each sick person has a fixed chance of passing the cold to each healthy person, independently.
Next week the newly sick people do the same, while the people who were sick before have recovered.
For example, in a household of two with one sick person and contact probability $p = 0.4$, the other person gets sick with probability $0.4$.
The outbreak stops in the first week where nobody new gets sick.
