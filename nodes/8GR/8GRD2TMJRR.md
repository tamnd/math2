---
tag: 8GRD2TMJRR
kind: concept
name: Bonferroni correction
msc: [62J15]
sources:
  - url: https://en.wikipedia.org/wiki/Bonferroni_correction
same_as:
  wikidata: Q385989
  wikipedia: Bonferroni correction
---

## Summary

The Bonferroni correction is the simplest way to test many hypotheses at once: test each of $m$ hypotheses at level $\alpha/m$.
By [[Boole's inequality|0EGSEE9J9R]], the [[family-wise error rate|GQCY1N8JZT]] is then at most $\alpha$.
It needs no assumption on the dependence between the tests, but it loses power when $m$ is large.

## Explanations

### L1 human

If you look at many results, some will look surprising just by chance.
The Bonferroni correction makes each single test stricter by dividing the threshold by the number of tests.
With $20$ tests and an overall level of $5\%$, each p-value must be below $0.0025$ to count.
Then the chance of even one false alarm in the whole family is at most $5\%$.
