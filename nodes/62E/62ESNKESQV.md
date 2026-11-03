---
tag: 62ESNKESQV
kind: concept
name: Log mean temperature difference
msc: [80A19, 80A20]
sources:
  - url: https://en.wikipedia.org/wiki/Logarithmic_mean_temperature_difference
same_as:
  wikidata: Q3272672
  wikipedia: Logarithmic mean temperature difference
---

## Summary

The log mean temperature difference is the logarithmic mean of the temperature differences between the two streams at the two ends of a [[heat exchanger|97ASA870TV]].
For parallel flow and counterflow with constant overall [[heat transfer coefficient|J821AD6YTE]] $U$, the heat rate is exactly $q = U A \, \Delta T_{\mathrm{lm}}$.
So it is the right average temperature difference for sizing an exchanger.
The arithmetic mean of the end differences is larger, unless the two end differences are equal.

## Explanations

### L1 human

Along a heat exchanger, the gap in temperature between the hot and the cold fluid changes.
To know how much heat flows, you need a kind of average gap.
The temperature gap changes exponentially along the exchanger, and the average of such a profile is the logarithmic mean.
If the gaps at the two ends are $40$ and $10$ degrees, the log mean is about $21.6$ degrees, less than the plain average of $25$.
