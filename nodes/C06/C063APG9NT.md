---
tag: C063APG9NT
kind: concept
name: Value at risk
msc: [91G70, 62P05]
sources:
  - url: https://en.wikipedia.org/wiki/Value_at_risk
same_as:
  wikidata: Q963287
  wikipedia: Value at risk
---

## Summary

The value at risk (VaR) of a portfolio at level $\alpha$ is a loss level over a given horizon.
The loss exceeds it with probability at most $1 - \alpha$.
Mathematically it is an $\alpha$-[[quantile|0X60VE98HN]] of the loss distribution.
It is the standard risk figure in banking regulation and internal risk reports.
It says nothing about how large the loss is beyond that level, and it is not a [[coherent risk measure|YR1E91KSFA]] because it can fail subadditivity.

## Explanations

### L1 human

Value at risk answers the question: "how bad can it get on all but the worst days?".
A one-day $99\%$ VaR of one million means that, on $99$ days out of $100$, the loss should stay below one million.
On the remaining day the loss may be larger, and VaR does not tell by how much.
For example, if daily losses are normal with mean $0$ and standard deviation $1$ million, the $99\%$ VaR is about $2.33$ million.
