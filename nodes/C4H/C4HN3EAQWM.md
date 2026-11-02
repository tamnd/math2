---
tag: C4HN3EAQWM
kind: concept
name: Observability
msc: [93B07, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Observability
same_as:
  wikidata: Q1369844
  wikipedia: Observability
---

## Summary

A [[control system|ZPDTVZQN5K]] with an output is observable if the initial state can be recovered from the known input and the measured output over time.
Observability matters because in practice only some quantities can be measured, while a feedback law usually needs the full state.
For linear systems it is dual to [[controllability|A9WFM77Z4P]]: the pair $(A, C)$ is observable exactly when $(A^T, C^T)$ is controllable.

## Explanations

### L1 human

Suppose you can only see the position of a moving car, not its speed.
By watching the position for a while, you can still find the speed, since the speed is the rate of change of the position.
So this system is observable even though one quantity is hidden.
If you could only see the speed, you would never know where the car started, and the system would not be observable.
