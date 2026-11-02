---
tag: 8EG1M1WZ9C
kind: concept
name: Minimax estimator
msc: [62C20]
sources:
  - url: https://en.wikipedia.org/wiki/Minimax_estimator
same_as:
  wikidata: Q6865379
  wikipedia: Minimax estimator
---

## Summary

A minimax estimator is an estimator whose worst-case [[risk|N26TSVRH2S]], over all values of the unknown parameter, is as small as possible.
The smallest achievable worst-case risk is the minimax risk of the problem.
The minimax principle gives a way to choose among estimators without a prior, and it is a basic benchmark in decision theory and nonparametric statistics.

## Explanations

### L1 human

Imagine that an opponent picks the true parameter after seeing which estimator is used, so as to make it look as bad as possible.
A minimax estimator is the best choice against such an opponent.
It may be a little worse than others for typical parameters, but it guards against the worst case.
For a coin tossed $n$ times, the minimax estimator of the heads probability under squared error is $(X + \sqrt{n}/2)/(n + \sqrt{n})$, not the plain proportion $X/n$.
