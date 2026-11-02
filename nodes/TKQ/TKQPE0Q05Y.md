---
tag: TKQPE0Q05Y
kind: concept
name: Elastic net
msc: [62J07, 62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Elastic_net_regularization
same_as:
  wikidata: Q5353562
  wikipedia: Elastic net regularization
---

## Summary

The elastic net fits a linear model by penalised least squares.
Its penalty combines the $\ell^1$ penalty of the [[lasso|KZ226116HW]] and the squared $\ell^2$ penalty of [[ridge regression|3KZW2930V2]].
It keeps the variable selection of the lasso, since some coefficients are set exactly to zero.
The ridge part makes the problem strictly convex.
It also lets groups of strongly correlated regressors enter the model together, where the lasso tends to pick one of them.
It was proposed by Hui Zou and Trevor Hastie.

## Explanations

### L1 human

The lasso likes to keep one regressor out of a group of near copies and drop the rest.
Ridge regression keeps them all but never drops anything.
The elastic net mixes the two penalties with two tuning parameters, so it can drop useless regressors while sharing the weight among correlated useful ones.
If the ridge parameter is zero, it is the lasso; if the lasso parameter is zero, it is ridge regression.
