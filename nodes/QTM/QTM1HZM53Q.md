---
tag: QTM1HZM53Q
kind: concept
name: Survival function
msc: [62N05, 62N01, "60E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Survival_function
same_as:
  wikidata: Q2915096
  wikipedia: Survival function
---

## Summary

The survival function of a lifetime $T$ gives, for each time $t$, the probability that the event has not yet happened at time $t$.
It equals one minus the [[cumulative distribution function|0H8H7ZTHW2]] of $T$.
It is the main quantity estimated in [[survival analysis|443ZWDX88P]], and it determines the distribution of $T$.
In reliability engineering it is called the reliability function.

## Explanations

### L1 human

If $T$ is the lifetime of a light bulb, $S(1000)$ is the chance that the bulb still works after $1000$ hours.
The curve $S$ starts at $1$, because every bulb works at the start, and goes down as time passes.
It never goes up again: a broken bulb stays broken.
For a lifetime with constant risk of failure, the curve is the decaying exponential $e^{-\lambda t}$.
