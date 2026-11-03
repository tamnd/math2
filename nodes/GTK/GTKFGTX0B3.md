---
tag: GTKFGTX0B3
kind: concept
name: Trembling hand perfect equilibrium
msc: [91A11, 91A10]
specializes: [745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Trembling_hand_perfect_equilibrium
same_as:
  wikidata: Q1039525
  wikipedia: Trembling hand perfect equilibrium
---

## Summary

A trembling hand perfect equilibrium is a [[Nash equilibrium|745WYP9YJ0]] that survives small mistakes.
Each player's strategy must stay a best response when the other players play every strategy with a tiny positive probability.
Reinhard Selten introduced it to rule out equilibria that rest on weakly dominated strategies.
Every finite game has at least one such equilibrium.

## Explanations

### L1 human

Imagine that every player has a slightly shaky hand.
Now and then, by accident, a player presses the wrong button.
An equilibrium is trembling hand perfect if each player's plan is still a good plan when the others make such rare mistakes.
For example, if two players both get $1$ when both say "yes" and $0$ otherwise, then "both say no" is a Nash equilibrium.
It is not trembling hand perfect: if the other player might say "yes" by mistake, saying "yes" is strictly better than saying "no".
