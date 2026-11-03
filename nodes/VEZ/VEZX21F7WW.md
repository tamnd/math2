---
tag: VEZX21F7WW
kind: concept
name: Congestion game
msc: [91A14]
sources:
  - url: https://en.wikipedia.org/wiki/Congestion_game
same_as:
  wikidata: Q5160467
  wikipedia: Congestion game
---

## Summary

In a congestion game each player picks a set of shared resources, such as roads in a network.
The cost of a resource depends only on how many players use it.
Robert Rosenthal introduced these games in 1973 and showed that they always have a pure Nash equilibrium, through a potential function.
They model traffic routing and are a basic example in algorithmic game theory.

## Explanations

### L1 human

Commuters each choose a route from home to work, and every road gets slower the more cars use it.
Each commuter's travel time is the sum of the delays on the roads she uses.
If commuters keep switching to faster routes one at a time, the switching must stop eventually.
At that point no commuter can find a faster route, which is a pure Nash equilibrium.
