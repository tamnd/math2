---
tag: QBA1NK6YCH
kind: concept
name: Fictitious play
msc: [91A26, 91A10]
sources:
  - url: https://en.wikipedia.org/wiki/Fictitious_play
same_as:
  wikidata: Q1411116
  wikipedia: Fictitious play
---

## Summary

Fictitious play is a learning rule for repeated play of a game, introduced by George W. Brown in 1951.
In each round, every player chooses a [[best response|QS6VCNJK60]] to the empirical frequencies of the opponents' past actions.
Julia Robinson proved in 1951 that in two-player [[zero-sum games|8PC5CFGMAD]] the empirical frequencies converge to optimal strategies.
In general games it need not converge, as Lloyd Shapley showed with a three-by-three example.

## Explanations

### L1 human

Imagine playing the same game again and again against the same opponent.
A simple habit is to keep a tally of how often the opponent chose each move, treat the tally as the opponent's mixed strategy, and best respond to it.
If both players follow this habit, the game is played by fictitious play.
In matching pennies, the players keep chasing each other, but the long-run frequencies of heads and tails both approach one half, which is the equilibrium.
