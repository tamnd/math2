---
tag: MNEY8VGP30
kind: concept
name: Global game
msc: [91A27, 91A10]
specializes: [2XQ7VWT8KJ]
sources:
  - url: https://en.wikipedia.org/wiki/Global_game
same_as:
  wikidata: Q5570845
  wikipedia: Global game
---

## Summary

A global game is a [[Bayesian game|2XQ7VWT8KJ]] in which players receive slightly noisy private signals about a payoff parameter of an underlying game.
The concept was introduced by Hans Carlsson and Eric van Damme in 1993.
Small noise can remove the multiplicity of equilibria of the underlying coordination game, so that a unique outcome is selected.
In two-player two-action coordination games, the selected outcome is the risk-dominant equilibrium.

## Explanations

### L1 human

Imagine many investors deciding whether to attack a currency, and the attack succeeds only if enough of them join.
If everyone knew the strength of the currency exactly, both "all attack" and "nobody attacks" could be equilibria.
In a global game, each investor sees the strength only with a little private noise.
Then each investor must guess what the others saw, and what they guess she saw, and so on.
This chain of reasoning pins down a single threshold: attack if your signal says the currency is weaker than a certain level.
