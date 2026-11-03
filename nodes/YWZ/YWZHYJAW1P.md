---
tag: YWZHYJAW1P
kind: concept
name: Vickrey–Clarke–Groves mechanism
msc: [91B03, 91B26]
sources:
  - url: https://en.wikipedia.org/wiki/Vickrey%E2%80%93Clarke%E2%80%93Groves_mechanism
same_as:
  wikidata: Q25304551
  wikipedia: Vickrey–Clarke–Groves mechanism
---

## Summary

The Vickrey–Clarke–Groves mechanism, or VCG mechanism, chooses the outcome that maximises the total reported value of all agents.
It charges each agent the harm her presence causes to the others.
Truthful reporting is a dominant strategy for every agent, so the mechanism achieves the efficient outcome in dominant strategies.
It generalises the [[Vickrey auction|75GR8RZSFP]] to any finite set of outcomes, and it is named after William Vickrey, Edward Clarke and Theodore Groves.
It is a central example in [[mechanism design|DTXJQKEHDP]], though it can have low revenue and need not balance its budget.

## Explanations

### L1 human

Everyone reports how much they value each possible outcome, and the outcome with the largest total value is chosen.
Each person then pays the amount by which her presence lowers the total value of everyone else.
Because of this payment, each person's gain lines up with the total gain, so lying cannot help.
With one object for sale, this is exactly the second-price auction: the winner pays the value that the second-highest bidder would have had.
