---
tag: Q3FQAD1BXG
kind: concept
name: Graphical model
msc: [62H22]
sources:
  - url: https://en.wikipedia.org/wiki/Graphical_model
same_as:
  wikidata: Q1143367
  wikipedia: Graphical model
---

## Summary

A probabilistic graphical model is a family of joint distributions of random variables whose [[conditional independences|0THJ7416DX]] are read off a [[graph|00C0BR7D7H]].
The vertices are the variables, and missing edges mean conditional independence.
Directed acyclic graphs give [[Bayesian networks|21JT983G60]], and undirected graphs give [[Markov random fields|6W69H3A3G5]].
The graph makes large models easier to describe, to fit and to compute with.

## Explanations

### L1 human

A joint distribution of many variables is too large to write down directly.
A graphical model draws one dot for each variable and joins two dots when the variables influence each other directly.
Variables that are not joined interact only through the others.
For example, the weather affects whether the grass is wet both directly and through the sprinkler, and the graph shows exactly these routes.
