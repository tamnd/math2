---
tag: GQCY1N8JZT
kind: concept
name: Family-wise error rate
msc: [62J15]
sources:
  - url: https://en.wikipedia.org/wiki/Family-wise_error_rate
same_as:
  wikidata: Q5433418
  wikipedia: Family-wise error rate
---

## Summary

When several [[hypothesis tests|087P03NEND]] are done together, the family-wise error rate is the probability of at least one [[type I error|03N8C8ZR4B]] among them.
Controlling it at level $\alpha$ protects against any false rejection in the whole family.
The [[Bonferroni correction|8GRD2TMJRR]] is the simplest procedure that controls it.

## Explanations

### L1 human

If you run $20$ independent tests at level $5\%$ and all null hypotheses are true, the chance of at least one false alarm is $1 - 0.95^{20}$, about $64\%$.
The family-wise error rate is this chance of at least one false alarm.
A multiple testing procedure that controls it keeps this chance below a chosen level, such as $5\%$.
