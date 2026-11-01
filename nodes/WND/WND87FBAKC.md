---
tag: WND87FBAKC
kind: concept
name: Stopping time
msc: [60G40, 60G05]
sources:
  - url: https://en.wikipedia.org/wiki/Stopping_time
same_as:
  wikidata: Q1288707
  wikipedia: Stopping time
---

## Summary

A stopping time is a random time $\tau$ with the following property.
At each time $t$, one can decide whether $\tau$ has already happened using only the information available at time $t$.
First hitting times of sets by adapted processes are the main examples.
Stopping times are central in martingale theory, through the [[optional stopping theorem|DC9HZT2HVJ]], and in the strong Markov property and optimal stopping.

## Explanations

### L1 human

A stopping time is a rule for when to stop that never needs to look into the future.
"Stop the first time the coin shows heads" is such a rule: when it happens, you know it.
"Stop at the last head before the hundredth toss" is not, because you cannot know that a head is the last one until later.
For a random walk started at $0$, the first time it reaches $5$ is a stopping time.
