---
tag: KKVCHFGA14
kind: concept
name: Expected shortfall
msc: [91G70, 62P05]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_shortfall
same_as:
  wikidata: Q5420856
  wikipedia: Expected shortfall
---

## Summary

The expected shortfall of a loss at level $\alpha$ is the average of the [[value at risk|C063APG9NT]] over all levels from $\alpha$ to $1$.
For continuous loss distributions it is the expected loss given that the loss exceeds its value at risk.
Unlike value at risk, it looks at the size of the losses in the tail, and it is a [[coherent risk measure|YR1E91KSFA]].
It is also called conditional value at risk (CVaR), average value at risk or tail value at risk.

## Explanations

### L1 human

Value at risk tells where the worst $1\%$ of outcomes begins; expected shortfall tells how bad those outcomes are on average.
Take the $1\%$ worst days, average their losses, and you have the $99\%$ expected shortfall.
For example, let a loss be $0$ with probability $0.98$, $10$ with probability $0.01$ and $1000$ with probability $0.01$.
Then the $99\%$ VaR is $10$, while the $99\%$ expected shortfall is $1000$.
So expected shortfall notices a rare disaster that VaR can miss.
