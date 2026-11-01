---
tag: HNK1Y62G7V
kind: concept
name: Filtration
msc: [60G05, 60G07]
sources:
  - url: https://en.wikipedia.org/wiki/Filtration_(probability_theory)
same_as:
  wikidata: Q55647796
  wikipedia: Filtration (probability theory)
---

## Summary

A filtration is an increasing family $(\mathcal{F}_t)_{t \in T}$ of sub-$\sigma$-algebras of the $\sigma$-algebra of a probability space, indexed by time.
The $\sigma$-algebra $\mathcal{F}_t$ models the information available at time $t$, and information is never lost as time goes on.
Filtrations are the setting for [[adapted processes|YRNFE016FF]], [[stopping times|WND87FBAKC]] and [[martingales|0D0GBNDKDH]].

## Explanations

### L1 human

Imagine watching a game of chance round by round.
After each round you know more than before: all earlier results and the new one.
A filtration records this growing knowledge: at each time it lists the events whose occurrence you can already decide.
For repeated coin tosses, the information at time $n$ consists of the events that depend only on the first $n$ tosses.
