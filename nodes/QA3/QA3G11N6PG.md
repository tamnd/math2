---
tag: QA3G11N6PG
kind: concept
name: Spectral risk measure
msc: [91G70, 91B05]
specializes: [YR1E91KSFA]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_risk_measure
same_as:
  wikidata: Q7575204
  wikipedia: Spectral risk measure
---

## Summary

A spectral risk measure is a weighted average of the [[quantiles|0X60VE98HN]] of a loss, with weights that do not decrease as the losses get worse.
The weight function is called the risk spectrum, and it expresses the risk aversion of the user.
Every spectral risk measure is a [[coherent risk measure|YR1E91KSFA]], and [[expected shortfall|KKVCHFGA14]] is the spectral measure with a flat weight on the tail.
The notion was introduced by Carlo Acerbi in 2002.

## Explanations

### L1 human

List all possible outcomes of a loss from the best to the worst, and give each outcome a weight.
A spectral risk measure is the weighted average of the losses, where worse outcomes never get less weight than better ones.
Equal weights give the plain expected loss.
Weight only on the worst $1\%$, spread evenly, gives the $99\%$ expected shortfall.
A user who fears disasters more can choose weights that grow steeply towards the worst outcomes.
