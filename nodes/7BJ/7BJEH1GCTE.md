---
tag: 7BJEH1GCTE
kind: concept
name: Darboux function
msc: [26A15, 26A24]
sources:
  - url: https://en.wikipedia.org/wiki/Darboux%27s_theorem_(analysis)
    locator: Darboux function
---

## Summary

A Darboux function is a real function on an interval that has the intermediate value property.
It never skips a value between two of its values.
Every [[continuous function|0P27W9RW0G]] on an interval is a Darboux function by the [[intermediate value theorem|00KAFBR32E]].
By [[Darboux's theorem|0Q5A47J48D]], every derivative is a Darboux function too, even when it is not continuous.
So the class of Darboux functions is much larger than the class of continuous functions.

## Explanations

### L1 human

Imagine driving along a road whose height is given by the function.
A Darboux function cannot get from height $0$ to height $1$ without passing every height in between.
Continuous functions behave like this, but so do some wild functions.
For example, $\sin(1/x)$ with value $0$ at $0$ wiggles infinitely often near $0$ and is not continuous there, yet it skips no values.
