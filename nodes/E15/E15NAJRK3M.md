---
tag: E15NAJRK3M
kind: concept
name: Lead–lag compensator
msc: [93B51, 93C80]
sources:
  - url: https://en.wikipedia.org/wiki/Lead%E2%80%93lag_compensator
same_as:
  wikidata: Q6508813
  wikipedia: Lead–lag compensator
---

## Summary

A lead–lag compensator is a simple controller made of first-order factors $(s + z)/(s + p)$ that reshape the frequency response of a feedback loop.
A lead factor adds positive phase near the crossover frequency, which improves stability margins and speeds up the response.
A lag factor raises the gain at low frequencies relative to high ones, which reduces steady-state errors.
Lead–lag design is a classical method of loop shaping with [[Bode plots|EMVW7N54FE]].

## Explanations

### L1 human

A feedback loop can oscillate if the signal comes back too late, that is, with too much phase lag.
A lead compensator pushes the signal a little earlier in phase over a band of frequencies, which calms the oscillation.
A lag compensator does the opposite job: it boosts slow signals, so that small persistent errors get corrected.
For example, $(s + 1)/(s + 3)$ adds up to $30$ degrees of phase, the most at the frequency $\sqrt{3}$.
