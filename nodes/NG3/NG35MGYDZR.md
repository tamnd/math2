---
tag: NG35MGYDZR
kind: concept
name: Stopped process
msc: [60G40, 60G05]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Stopped_process
same_as:
  wikidata: Q7619859
  wikipedia: Stopped process
---

## Summary

The stopped process $X^\tau$ of a [[stochastic process|0QH5ENKZM1]] $X$ at a [[stopping time|WND87FBAKC]] $\tau$ follows $X$ up to time $\tau$.
After time $\tau$ it stays frozen at the value $X_\tau$.
Stopping preserves the [[martingale|0D0GBNDKDH]] property, which is the heart of the [[optional stopping theorem|DC9HZT2HVJ]].
It is also the basic operation of localisation, used to define [[local martingales|XC2YPC2BSW]] and stochastic integrals.

## Explanations

### L1 human

Picture a gambler's fortune changing over time, and a rule telling the gambler when to leave the table.
After leaving, the fortune no longer changes.
The stopped process is this frozen record: equal to the fortune until the gambler leaves, and constant afterwards.
For a random walk stopped when it first reaches $5$ or $-5$, the stopped walk stays between $-5$ and $5$ for ever.
