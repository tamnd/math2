---
tag: K3AMMSY8DD
kind: concept
name: Statistical model
msc: [62A01]
sources:
  - url: https://en.wikipedia.org/wiki/Statistical_model
same_as:
  wikidata: Q3284399
  wikipedia: Statistical model
---

## Summary

A statistical model is a set of probability distributions that are candidates for the law of the observed data.
It fixes what is assumed about the data before any inference is made.
Every method of [[statistical inference|JZ2S01BHJJ]] starts from a model, and its guarantees hold only under the laws in that model.

## Explanations

### L1 human

You do not know exactly how your data were produced, but you know some things.
A statistical model lists all the laws that you still regard as possible.
For example, toss a coin $10$ times.
A natural model says that the number of heads is binomial with $10$ trials and some success chance $p$ between $0$ and $1$.
The data then help you decide which $p$ is plausible.
