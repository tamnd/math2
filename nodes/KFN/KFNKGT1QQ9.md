---
tag: KFNKGT1QQ9
kind: concept
name: NTU method
msc: [80A19, 80A20]
sources:
  - url: https://en.wikipedia.org/wiki/NTU_method
same_as:
  wikidata: Q905855
  wikipedia: NTU method
---

## Summary

The NTU method, or effectiveness–NTU method, computes the heat rate of a [[heat exchanger|97ASA870TV]] when only the inlet temperatures are known.
It uses the effectiveness, the ratio of the actual heat rate to the largest possible one.
It also uses the number of transfer units $\mathrm{NTU} = UA / C_{\min}$, a dimensionless size of the exchanger.
For each flow arrangement the effectiveness is an explicit function of $\mathrm{NTU}$ and the ratio of heat capacity rates.
It avoids the trial and error that the [[log mean temperature difference|62ESNKESQV]] method needs when outlet temperatures are unknown.

## Explanations

### L1 human

Imagine you know how hot the two fluids are when they enter an exchanger, and how big the exchanger is.
You want to know how much heat it will move.
The NTU method first computes the most heat any exchanger could move between these streams.
Then a formula, depending on the size and the layout, tells what fraction of that maximum this exchanger achieves.
For example, a counterflow exchanger with $\mathrm{NTU} = 2$ and equal heat capacity rates achieves two thirds of the maximum.
